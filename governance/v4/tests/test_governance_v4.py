#!/usr/bin/env python3
"""Generic runtime, migration-audit, positive and failure-path tests."""

from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
V4 = ROOT / "governance" / "v4"
sys.path.insert(0, str(V4))

import bootstrap  # noqa: E402
import migration_audit  # noqa: E402
import validator  # noqa: E402


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class GovernanceV4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.negative_checks = 0
        cls.state, cls.tasks, cls.contracts, cls.registry = validator.load_repository_bundle(ROOT)
        cls.scenarios = read_json("governance/v4/tests/fixtures/RUNTIME_SCENARIOS.json")
        cls.scenario_states = cls.scenarios["states"]
        cls.scenario_tasks = cls.scenarios["tasks"]
        cls.negatives = read_json("governance/v4/tests/fixtures/NEGATIVE_CASES.json")
        cls.owner_copy_document = read_json(
            "working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json"
        )
        cls.full_copy_document = read_json(
            "working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json"
        )
        cls.canonical_copies = validator.load_canonical_copy_index(ROOT, cls.contracts)

    @contextmanager
    def assert_rejected(self, code: str | None = None):
        with self.assertRaises(validator.GovernanceViolation) as caught:
            yield caught
        if code is not None:
            self.assertEqual(caught.exception.code, code)
        type(self).negative_checks += 1

    def hardening_snapshot(self) -> dict:
        completed = self.contracts["lifecycle"]["completed_hardening"]
        return json.loads(validator.git(
            ROOT, "show", f"{completed['snapshot_commit']}:{completed['state_ref']}",
        ))

    def authorize_scenario(
        self,
        state_name: str,
        request: dict,
        mutation: dict | None = None,
        permission_overrides: dict | None = None,
        authorization_overrides: dict | None = None,
    ) -> None:
        state = copy.deepcopy(self.scenario_states[state_name])
        tasks = copy.deepcopy(self.scenario_tasks)
        if authorization_overrides:
            tasks[state["active_project_task_id"]]["authorization"].update(authorization_overrides)
        if permission_overrides:
            state["permissions"].update(permission_overrides)
        supplied = copy.deepcopy(request)
        if mutation is not None:
            card_id = supplied.get("card_id")
            copy_record = copy.deepcopy(self.canonical_copies[card_id])
            copy_record.update(mutation)
            supplied["copy_record"] = copy_record
        validator.authorize_request(
            state,
            tasks,
            self.registry,
            self.contracts,
            supplied,
            self.canonical_copies,
        )

    def test_01_v3_validator_still_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "governance/validate_governance.py"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_02_generic_repository_validator_passes(self) -> None:
        result = validator.validate_repository(ROOT)
        expected = self.scenarios["repository_expectations"]
        self.assertEqual(result["active_task_id"], expected["active_task_id"])
        self.assertTrue(result["cutover_performed"])
        self.assertEqual(result["loaded_task_ids"], expected["loaded_task_ids"])

    def test_03_separate_migration_rework_audit_passes(self) -> None:
        accepted = self.state["migration_control"]["accepted_migration_commit"]
        with tempfile.TemporaryDirectory(prefix="foulwake-v4-audit-") as temporary:
            clone = Path(temporary) / "accepted-migration"
            subprocess.run(
                ["git", "clone", "--quiet", "--shared", "--no-checkout", str(ROOT), str(clone)],
                check=True,
            )
            subprocess.run(
                ["git", "checkout", "--quiet", "-b", "migration/governance-v4", accepted],
                cwd=clone,
                check=True,
            )
            result = subprocess.run(
                [sys.executable, "governance/v4/migration_audit.py", "--root", str(clone)],
                cwd=clone,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("exact rework scope: 10 files", result.stdout)
            self.assertIn("v3/v4 parity: PASS", result.stdout)

    def test_04_runtime_validator_has_no_snapshot_constants(self) -> None:
        source = (V4 / "validator.py").read_text(encoding="utf-8")
        forbidden = [
            "e891a678822c5cb1773714f2ceda33eaccee9a57",
            "5564c7fbdea297ab1b8b3fa675c83f6e788151f1",
            "migration/governance-v4",
            "ART-001",
            "V4_REWORK_COMPLETE",
            "EXPECTED_SOURCE",
            "EXPECTED_BRANCH",
            "EXPECTED_BLOCKERS",
            "EXPECTED_ROLES",
            "EXPECTED_GATES",
        ]
        for token in forbidden:
            with self.subTest(token=token):
                self.assertNotIn(token, source)

    def test_05_cutover_complete_runtime_state_passes_generic_validator(self) -> None:
        validator.validate_runtime_documents(
            self.scenario_states["cutover_complete"],
            self.scenario_tasks,
            self.contracts,
            self.registry,
        )
        self.assertTrue(
            self.scenario_states["cutover_complete"]["migration_control"]["cutover_performed"]
        )

    def test_06_new_active_task_validates_without_validator_change(self) -> None:
        validator.validate_runtime_documents(
            self.scenario_states["visual_active"],
            self.scenario_tasks,
            self.contracts,
            self.registry,
        )

    def test_07_read_only_validation_needs_no_active_task(self) -> None:
        self.authorize_scenario(
            "no_active_task",
            {"role": "SIMULATION_QA", "action": "READ_ONLY_VALIDATION"},
        )

    def test_08_new_visual_task_executor_positive_path(self) -> None:
        self.authorize_scenario(
            "visual_active",
            {
                "role": "VISUAL_DESIGN",
                "action": "PRODUCE_THUMBNAIL",
                "task_id": "VISUAL-EXAMPLE-001",
                "branch": "work/v2.7-visual",
                "path": "working/v2.7/visual/example/card.png",
            },
        )

    def test_09_explicit_reviewers_positive_paths(self) -> None:
        self.authorize_scenario(
            "visual_active",
            {
                "role": "ART_DIRECTION",
                "action": "FRAMING_DECISION",
                "task_id": "VISUAL-EXAMPLE-001",
                "producer_role": "VISUAL_DESIGN",
                "disposition": "FRAMING_PASS",
                "branch": "work/v2.7-visual",
                "path": "working/v2.7/visual/example/card.png",
            },
        )
        for action in ("QA_REVIEW",):
            request = {
                "role": "SIMULATION_QA",
                "action": action,
                "task_id": "VISUAL-EXAMPLE-001",
                "branch": "work/v2.7-visual",
                "path": "working/v2.7/visual/example/card.png",
            }
            self.authorize_scenario("visual_active", request)
        for card_id in ("SET-KP-01", "GUC-22", "GUC-23", "KAR-01"):
            self.authorize_scenario(
                "visual_active",
                {
                    "role": "SIMULATION_QA",
                    "action": "COPY_CHECK",
                    "card_id": card_id,
                    "copy_record": self.canonical_copies[card_id],
                    "task_id": "VISUAL-EXAMPLE-001",
                    "branch": "work/v2.7-visual",
                    "path": "working/v2.7/visual/example/card.png",
                },
            )
        self.authorize_scenario(
            "visual_active",
            {
                "role": "PROJECT_OWNER",
                "action": "PROJECT_OWNER_AESTHETIC_ACCEPTANCE",
                "task_id": "VISUAL-EXAMPLE-001",
                "producer_role": "VISUAL_DESIGN",
                "branch": "work/v2.7-visual",
                "path": "working/v2.7/visual/example/card.png",
            },
        )

    def test_10_new_art_direction_task_positive_path(self) -> None:
        self.authorize_scenario(
            "art_direction_active",
            {
                "role": "ART_DIRECTION",
                "action": "ART_LANGUAGE_REVIEW",
                "task_id": "ART-EXAMPLE-001",
                "branch": "work/v2.7-art-direction",
                "path": "working/v2.7/visual/art_direction/example/review.md",
            },
        )

    def test_11_owner_cutover_uses_only_exact_migration_control_exception(self) -> None:
        accepted = self.state["migration_control"]["accepted_migration_commit"]
        pre_cutover_state = json.loads(
            validator.git(
                ROOT,
                "show",
                f"{accepted}:governance/v4/runtime/STATE.json",
            )
        )
        pre_cutover_task_id = pre_cutover_state["migration_control"]["task_id"]
        pre_cutover_task = json.loads(
            validator.git(
                ROOT,
                "show",
                f"{accepted}:governance/v4/tasks/{pre_cutover_task_id}.json",
            )
        )
        validator.authorize_request(
            pre_cutover_state,
            {pre_cutover_task_id: pre_cutover_task},
            self.registry,
            self.contracts,
            {
                "role": "PROJECT_OWNER",
                "action": "CUTOVER_DECISION",
                "task_id": pre_cutover_task_id,
                "branch": "migration/governance-v4",
                "path": "governance/v4/evidence/REWORK_RESULT.json",
            },
            self.canonical_copies,
        )
        with self.assert_rejected():
            validator.authorize_request(
                self.state,
                self.tasks,
                self.registry,
                self.contracts,
                {
                    "role": "PROJECT_OWNER",
                    "action": "CUTOVER_DECISION",
                    "task_id": "GOV4-CUTOVER-001",
                    "branch": "v2.7-design",
                    "path": "governance/v4/evidence/CUTOVER_RESULT.json",
                },
                self.canonical_copies,
            )

    def test_12_bootstrap_is_noncanonical_and_reflects_task_binding(self) -> None:
        expected = self.scenarios["repository_expectations"]
        for role, authorized in expected["role_write_authorized"].items():
            rendered = bootstrap.build_bootstrap(ROOT, role)
            self.assertIn("GENERATED / NON_CANONICAL", rendered)
            self.assertIn(f"ACTIVE_PROJECT_TASK: {expected['active_task_id'] or 'NONE'}", rendered)
            self.assertIn(f"CURRENT_WRITE_AUTHORIZED: {str(authorized).upper()}", rendered)
        hardening = bootstrap.build_bootstrap(ROOT, "CHIEF_EDITOR", "GOV4-HARDENING-001")
        self.assertIn("TASK_BINDING: INACTIVE / NO AUTHORITY", hardening)
        self.assertIn("TASK_STATUS: CLOSED / HARDENING_COMPLETE", hardening)
        self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", hardening)
        self.assertIn("CURRENT_ROLE_TASK_ACTIONS: NONE", hardening)
        cutover = bootstrap.build_bootstrap(ROOT, "PROJECT_OWNER", "GOV4-CUTOVER-001")
        self.assertIn("TASK_BINDING: MIGRATION_CONTROL_ONLY", cutover)
        self.assertIn("CURRENT_ROLE_TASK_ACTIONS: NONE", cutover)

    def test_13_original_migration_result_and_task_are_unchanged(self) -> None:
        baseline = "e891a678822c5cb1773714f2ceda33eaccee9a57"
        for path in (
            "governance/v4/evidence/MIGRATION_RESULT.json",
            "governance/v4/tasks/GOV4-MIGRATION-001.json",
        ):
            with self.subTest(path=path):
                before = validator.git(ROOT, "rev-parse", f"{baseline}:{path}")
                current = validator.git(ROOT, "hash-object", path)
                self.assertEqual(current, before)

    def test_14_original_nine_negative_cases_are_retained(self) -> None:
        all_ids = {case["id"] for case in self.negatives["cases"]}
        self.assertEqual(
            set(self.negatives["preserved_original_case_ids"]),
            {f"NEG-{number:02d}-" + suffix for number, suffix in [
                (1, "WRONG-BRANCH"),
                (2, "OUT-OF-SCOPE-FILE"),
                (3, "V26-TREE-DRIFT"),
                (4, "SPECIALIST-SELF-APPROVAL"),
                (5, "EXACT-COPY-DRIFT"),
                (6, "CLOSED-TASK-REUSE"),
                (7, "BLOCKERS-OPEN-RELEASE"),
                (8, "VISUAL-FRAMING-PASS"),
                (9, "OWNER-BYPASS"),
            ]},
        )
        self.assertTrue(set(self.negatives["preserved_original_case_ids"]) <= all_ids)

    def test_15_all_original_and_added_negative_cases_are_rejected(self) -> None:
        cases = self.negatives["cases"]
        self.assertGreaterEqual(len(cases), 27)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        preserved = json.loads(validator.git(
            ROOT, "show",
            f"{self.contracts['lifecycle']['completed_hardening']['snapshot_commit']}:governance/v4/tests/fixtures/NEGATIVE_CASES.json",
        ))["cases"]
        for original in preserved:
            self.assertIn(original, cases)
        for case in cases:
            with self.subTest(case=case["id"]):
                with self.assert_rejected() as caught:
                    if case.get("type") == "LOCKED_TREE":
                        validator.validate_locked_tree(case["actual"], case["expected"])
                    elif case.get("type") == "DUPLICATE_COPY_ID":
                        full_document = copy.deepcopy(self.full_copy_document)
                        collection = case["collection"]
                        full_document[collection].append(
                            copy.deepcopy(full_document[collection][0])
                        )
                        validator.build_canonical_copy_index(
                            self.owner_copy_document,
                            full_document,
                            self.contracts["owner_controls"]["exact_copy"],
                        )
                    else:
                        self.authorize_scenario(
                            case["state"],
                            case["request"],
                            case.get("copy_mutation"),
                            case.get("permission_overrides"),
                            case.get("authorization_overrides"),
                        )
                self.assertEqual(caught.exception.code, case["expected_code"])

    def test_16_no_active_task_rejects_every_named_non_read_only_action_class(self) -> None:
        requests = [
            ("SIMULATION_QA", "COPY_CHECK"),
            ("SIMULATION_QA", "RULES_INTEGRITY_REVIEW"),
            ("SIMULATION_QA", "QA_REVIEW"),
            ("VISUAL_DESIGN", "PRODUCE_VISUAL"),
            ("VISUAL_DESIGN", "PRODUCE_THUMBNAIL"),
            ("VISUAL_DESIGN", "PRODUCE_PILOT_OR_CANDIDATE"),
            ("VISUAL_DESIGN", "PRODUCE_FULL_121"),
            ("VISUAL_DESIGN", "PRODUCE_PDF_OR_PRINT_PACKAGE"),
            ("CHIEF_EDITOR", "MANAGE_STATE"),
            ("CHIEF_EDITOR", "RESOLVE_SOURCE_CONFLICT"),
        ]
        for role, action in requests:
            with self.subTest(action=action):
                with self.assert_rejected() as caught:
                    self.authorize_scenario(
                        "no_active_task",
                        {
                            "role": role,
                            "action": action,
                            "task_id": "VISUAL-EXAMPLE-001",
                            "branch": "work/v2.7-visual",
                            "path": "working/v2.7/visual/example/card.png",
                        },
                    )
                self.assertEqual(
                    caught.exception.code,
                    "NO_ACTIVE_TASK_FOR_SPECIALIST_ACTION",
                )

    def test_17_state_permission_cannot_be_bypassed_by_task_action(self) -> None:
        state = copy.deepcopy(self.scenario_states["visual_active"])
        state["permissions"]["thumbnails"] = False
        request = {
            "role": "VISUAL_DESIGN",
            "action": "PRODUCE_THUMBNAIL",
            "task_id": "VISUAL-EXAMPLE-001",
            "branch": "work/v2.7-visual",
            "path": "working/v2.7/visual/example/card.png",
        }
        with self.assert_rejected() as caught:
            validator.authorize_request(
                state,
                self.scenario_tasks,
                self.registry,
                self.contracts,
                request,
                self.canonical_copies,
            )
        self.assertEqual(caught.exception.code, "PERMISSION_CLOSED")

    def test_18_owner_override_precedes_full_source(self) -> None:
        full_document = copy.deepcopy(self.full_copy_document)
        full_document["powers"].append({
            "id": "SET-KP-01",
            "name": "Not canonical",
            "group": "Not canonical",
            "time": "Not canonical",
            "effect": "Not canonical",
            "flavor": "Not canonical",
        })
        resolved = validator.build_canonical_copy_index(
            self.owner_copy_document,
            full_document,
            self.contracts["owner_controls"]["exact_copy"],
        )
        self.assertEqual(resolved["SET-KP-01"], self.canonical_copies["SET-KP-01"])

    def test_19_full_copy_resolver_and_owner_mapping_are_exact(self) -> None:
        self.assertEqual(len(self.canonical_copies), 51)
        decision = self.state["resolved_source_decisions"]["SRC-002"]
        self.assertEqual(
            decision["source_git_blob"],
            "38a03b71cd3232fd844db8d80d8e53662510b6a3",
        )
        for card_id, expected_name in decision["mapping"].items():
            with self.subTest(card_id=card_id):
                self.assertEqual(self.canonical_copies[card_id]["name"], expected_name)

    def test_20_four_granular_production_actions_require_direct_gates(self) -> None:
        granular = self.contracts["runtime_authorization"]["granular_production_actions"]
        self.assertEqual(
            granular,
            {
                "PRODUCE_THUMBNAIL": "thumbnails",
                "PRODUCE_PILOT_OR_CANDIDATE": "pilot_or_candidate",
                "PRODUCE_FULL_121": "full_121_production",
                "PRODUCE_PDF_OR_PRINT_PACKAGE": "pdf_or_print_package",
            },
        )
        for action in granular:
            with self.subTest(action=action):
                self.authorize_scenario(
                    "visual_active",
                    {
                        "role": "VISUAL_DESIGN",
                        "action": action,
                        "task_id": "VISUAL-EXAMPLE-001",
                        "branch": "work/v2.7-visual",
                        "path": "working/v2.7/visual/example/card.png",
                    },
                )

    def test_21_hardening_closes_idle_and_removes_only_src_002(self) -> None:
        task = read_json("governance/v4/tasks/GOV4-HARDENING-001.json")
        snapshot = self.hardening_snapshot()
        before = json.loads(
            validator.git(
                ROOT,
                "show",
                f"{task['reactivation']['source_head']}:governance/v4/runtime/STATE.json",
            )
        )
        self.assertIsNone(snapshot["active_project_task_id"])
        self.assertEqual(task["status"], "CLOSED / HARDENING_COMPLETE")
        self.assertFalse(task["authorization"]["enabled"])
        self.assertFalse(task["authorization"]["write_authorized"])
        expected_blockers = dict(before["open_blockers"])
        expected_blockers.pop("SRC-002")
        self.assertEqual(snapshot["open_blockers"], expected_blockers)
        self.assertTrue(all(value is False for value in snapshot["permissions"].values()))
        evidence = read_json(snapshot["hardening_control"]["evidence_ref"])
        self.assertEqual(snapshot["status"], evidence["result"])

    def test_22_post_hardening_active_task_passes_full_repository_validation(self) -> None:
        state = self.hardening_snapshot()
        state["active_project_task_id"] = "SIMULATION-EXAMPLE-001"
        state["permissions"]["simulation"] = True
        state["status"] = "V4_ACTIVE / NEW_EXACT_TASK"
        tasks = {**self.tasks, **self.scenario_tasks}
        validator.validate_runtime_documents(state, tasks, self.contracts, self.registry)
        with patch.object(validator, "load_repository_bundle", return_value=(state, tasks, self.contracts, self.registry)):
            result = validator.validate_repository(ROOT)
        self.assertEqual(result["active_task_id"], "SIMULATION-EXAMPLE-001")
        for action in ("RUN_SIMULATION", "QA_REVIEW", "RULES_INTEGRITY_REVIEW"):
            self.authorize_scenario("simulation_active", {
                "role": "SIMULATION_QA", "action": action,
                "task_id": "SIMULATION-EXAMPLE-001",
                "branch": "work/v2.7-simulation",
                "path": "working/v2.7/qa/example/preflight.py",
            })

    def test_23_live_blockers_may_progress_but_src_002_cannot_reopen(self) -> None:
        state = self.hardening_snapshot()
        state["open_blockers"].pop(next(iter(state["open_blockers"])))
        state["open_blockers"]["NEW-REVIEW"] = "New evidence requirement."
        state["status"] = "V4_ACTIVE / BLOCKER_PROGRESS"
        with patch.object(validator, "load_repository_bundle", return_value=(state, self.tasks, self.contracts, self.registry)):
            validator.validate_repository(ROOT)
            state["open_blockers"]["SRC-002"] = "Cannot reopen a resolved binding decision."
            with self.assert_rejected("RESOLVED_BLOCKER_STILL_OPEN"):
                validator.validate_repository(ROOT)

    def test_24_hardening_cannot_be_reused_or_reauthorized(self) -> None:
        task_id = self.state["hardening_control"]["task_id"]
        task = read_json(self.state["hardening_control"]["task_ref"])
        for key in ("enabled", "write_authorized"):
            mutated = copy.deepcopy(task)
            mutated["authorization"][key] = True
            with patch.object(validator, "load_task", return_value=mutated):
                with self.assert_rejected("HARDENING_AUTHORITY_OPEN"):
                    validator.verify_hardening_closure(ROOT, self.state, self.contracts, self.registry)
        state = copy.deepcopy(self.state)
        state["active_project_task_id"] = task_id
        task["status"] = "ACTIVE"
        task["authorization"].update(enabled=True, write_authorized=True)
        with self.assert_rejected("INACTIVE_TASK_REUSE"):
            validator.validate_runtime_documents(state, {task_id: task}, self.contracts, self.registry)

    def test_25_every_repository_output_review_requires_write_authorized(self) -> None:
        actions = {
            "STORY_EDITOR": ["PERIOD_LANGUAGE_REVIEW"],
            "ART_DIRECTION": ["ART_LANGUAGE_REVIEW", "FRAMING_DECISION", "COMPOSITION_REVIEW", "DECK_RHYTHM_REVIEW", "AESTHETIC_RECOMMENDATION"],
            "SIMULATION_QA": ["RUN_SIMULATION", "QA_REVIEW", "COPY_CHECK", "PHYSICAL_EVIDENCE_REVIEW", "RULES_INTEGRITY_REVIEW"],
        }
        for role, role_actions in actions.items():
            for action in role_actions:
                with self.subTest(role=role, action=action):
                    self.assertIn(action, self.contracts["runtime_authorization"]["write_actions"])
                    state = copy.deepcopy(self.scenario_states["simulation_active"])
                    task = copy.deepcopy(self.scenario_tasks["SIMULATION-EXAMPLE-001"])
                    task["executor_role"] = role
                    task["authorization"].update(allowed_actions=[action], role_actions={role: [action]})
                    request = {
                        "role": role, "action": action, "task_id": task["task_id"],
                        "branch": task["scope"]["branch"], "path": task["scope"]["allowed_exact_paths"][0],
                        "producer_role": "VISUAL_DESIGN", "disposition": "FRAMING_PASS",
                        "card_id": "SET-KP-01", "copy_record": self.canonical_copies["SET-KP-01"],
                    }
                    validator.authorize_request(state, {task["task_id"]: task}, self.registry, self.contracts, request, self.canonical_copies)
                    task["authorization"]["write_authorized"] = False
                    with self.assert_rejected("TASK_WRITE_CLOSED"):
                        validator.authorize_request(state, {task["task_id"]: task}, self.registry, self.contracts, request, self.canonical_copies)

    def test_26_historical_idle_bootstrap_remains_fail_closed(self) -> None:
        state = self.hardening_snapshot()
        with patch.object(bootstrap, "load_repository_bundle", return_value=(state, self.tasks, self.contracts, self.registry)):
            for role in ("CHIEF_EDITOR", "SIMULATION_QA", "VISUAL_DESIGN"):
                rendered = bootstrap.build_bootstrap(ROOT, role)
                self.assertIn("ACTIVE_PROJECT_TASK: NONE", rendered)
                self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", rendered)
        self.assertNotIn("READ_ONLY_VALIDATION", self.contracts["runtime_authorization"]["write_actions"])
        for role in self.registry["roles"]:
            validator.authorize_request(state, self.tasks, self.registry, self.contracts, {"role": role, "action": "READ_ONLY_VALIDATION"})

    def test_27_hardening_snapshot_evidence_and_mapping_remain_binding(self) -> None:
        state = copy.deepcopy(self.state)
        state["resolved_source_decisions"]["SRC-002"]["mapping"].pop("GUC-24")
        with self.assert_rejected("SOURCE_DECISION_DRIFT"):
            validator.verify_hardening_closure(ROOT, state, self.contracts, self.registry)
        contracts = copy.deepcopy(self.contracts)
        contracts["lifecycle"]["completed_hardening"]["snapshot_commit"] = "0" * 40
        with self.assert_rejected("HARDENING_SNAPSHOT_NOT_ANCESTOR"):
            validator.verify_hardening_closure(ROOT, self.state, contracts, self.registry)
        original_git = validator.git
        def drifted_evidence(root, *args, **kwargs):
            if args == ("hash-object", self.state["hardening_control"]["evidence_ref"]):
                return "0" * 40
            return original_git(root, *args, **kwargs)
        with patch.object(validator, "git", side_effect=drifted_evidence):
            with self.assert_rejected("HARDENING_SNAPSHOT_DRIFT"):
                validator.verify_hardening_closure(ROOT, self.state, self.contracts, self.registry)

    def test_28_real_git_lifecycle_and_request_integrity(self) -> None:
        """Exercise real registry/state files and commits, without mocking the loader."""
        with tempfile.TemporaryDirectory(prefix="foulwake-lifecycle-test-") as temporary:
            repo = Path(temporary) / "repo"
            subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", str(ROOT), str(repo)], check=True)
            snapshot = self.contracts["lifecycle"]["completed_hardening"]["snapshot_commit"]
            validator.git(repo, "checkout", "--quiet", "--detach", snapshot)
            for relative in ("governance/v4/contracts/CONTRACTS.json", "governance/v4/validator.py"):
                shutil.copy2(ROOT / relative, repo / relative)
            def save(relative, value):
                path = repo / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            def commit(message):
                validator.git(repo, "add", "-A")
                validator.git(repo, "-c", "user.name=Governance test", "-c", "user.email=test@example.invalid", "commit", "--quiet", "-m", message)
                return validator.git(repo, "rev-parse", "HEAD")
            baseline = commit("test only: install lifecycle validator")
            self.assertIsNone(validator.validate_repository(repo)["active_task_id"])
            task = copy.deepcopy(self.scenario_tasks["SIMULATION-EXAMPLE-001"])
            task_id = task["task_id"]
            state = self.hardening_snapshot()
            state.update(active_project_task_id=task_id, status="TEST / ACTIVE")
            state["permissions"]["simulation"] = True
            task.update(source={"branch": "v2.7-design", "commit": baseline},
                        owner_authorization={"task_id": task_id, "decision": "AUTHORIZED", "recorded_from": "TEST FIXTURE ONLY"},
                        acceptance_criteria=["Exact evidence files reviewed independently"],
                        reviewer_roles=["CHIEF_EDITOR"], runtime_permissions=copy.deepcopy(state["permissions"]))
            source_path = "working/v2.7/V27_MECHANIC_DECISIONS.json"
            task["inputs"] = [{"path": source_path, "git_blob": validator.git(repo, "rev-parse", f"{baseline}:{source_path}")}]
            task["scope"]["max_changed_files"] = 3
            task_path = f"governance/v4/tasks/{task_id}.json"
            state_path = "governance/v4/runtime/STATE.json"
            save(task_path, task)
            save(state_path, state)
            opening = {"role": "CHIEF_EDITOR", "action": "OPEN_TASK", "task_id": task_id, "baseline_commit": baseline}
            for role in ("SIMULATION_QA", "VISUAL_DESIGN"):
                with self.assert_rejected("TASK_ISSUER_ROLE"):
                    validator.authorize_repository_request(repo, {**opening, "role": role})
            validator.authorize_repository_request(repo, opening)
            delegated = copy.deepcopy(task)
            delegated["issued_by"] = "CHIEF_EDITOR"
            delegated["owner_authorization"]["delegation_id"] = self.contracts["lifecycle"]["task_issuance_delegation"]["id"]
            save(task_path, delegated)
            validator.validate_repository(repo)
            delegated["owner_authorization"]["delegation_id"] = "UNAUTHORIZED-DELEGATION"
            save(task_path, delegated)
            with self.assert_rejected("TASK_DELEGATION_MISSING"):
                validator.validate_repository(repo)
            save(task_path, task)
            for field, code in (("source", "TASK_BASELINE_MISSING"), ("acceptance_criteria", "TASK_ACCEPTANCE_MISSING"),
                                ("owner_authorization", "TASK_OWNER_AUTHORIZATION_MISSING")):
                broken = copy.deepcopy(task)
                broken.pop(field)
                save(task_path, broken)
                with self.assert_rejected(code):
                    validator.validate_repository(repo)
            save(task_path, task)
            orphan = copy.deepcopy(task)
            orphan["task_id"] = "ORPHAN-001"
            save("governance/v4/tasks/ORPHAN-001.json", orphan)
            with self.assert_rejected("TASK_REGISTRY_DRIFT"):
                validator.validate_repository(repo)
            (repo / "governance/v4/tasks/ORPHAN-001.json").unlink()
            activation = commit("test only: open exact QA task")
            validator.git(repo, "switch", "--quiet", "-c", task["scope"]["branch"])
            request = {"role": "SIMULATION_QA", "action": "RUN_SIMULATION", "task_id": task_id,
                       "branch": task["scope"]["branch"], "path": task["scope"]["allowed_exact_paths"][0]}
            validator.authorize_repository_request(repo, request)
            for role in ("CHIEF_EDITOR", "VISUAL_DESIGN", "STORY_EDITOR", "ART_DIRECTION"):
                with self.assert_rejected("TASK_ACTION_FORBIDDEN" if role == "CHIEF_EDITOR" else "ROLE_TASK_MISMATCH"):
                    validator.authorize_repository_request(repo, {**request, "role": role})
            self.assertIn("CURRENT_WRITE_AUTHORIZED: TRUE", bootstrap.build_bootstrap(repo, "SIMULATION_QA"))
            self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", bootstrap.build_bootstrap(repo, "CHIEF_EDITOR"))
            source_file = repo / self.contracts["owner_controls"]["exact_copy"]["source"]
            original = source_file.read_bytes()
            source_file.write_bytes(original + b"\n")
            with self.assert_rejected("PINNED_SOURCE_HASH_DRIFT"):
                validator.authorize_repository_request(repo, request)
            source_file.write_bytes(original)
            locked_file = next((repo / "releases/v2.6").glob("*.json"))
            original = locked_file.read_bytes()
            locked_file.write_bytes(original + b"\n")
            with self.assert_rejected("LOCKED_WORKTREE_DRIFT"):
                validator.authorize_repository_request(repo, request)
            locked_file.write_bytes(original)
            forbidden = repo / "governance/UNAUTHORIZED_TEST.md"
            forbidden.write_text("test only\n")
            with self.assert_rejected("OUT_OF_SCOPE_PATH"):
                validator.authorize_repository_request(repo, request)
            forbidden.unlink()
            output = repo / request["path"]
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(b"\x00\xff")
            with self.assert_rejected("TASK_BINARY_FORBIDDEN"):
                validator.authorize_repository_request(repo, request)
            output.write_text("# test fixture only; no simulation executed\n")
            validator.authorize_repository_request(repo, request)
            delivery = commit("test only: record dummy evidence")
            blob = validator.git(repo, "rev-parse", f"{delivery}:{request['path']}")
            task["status"] = "CLOSED"
            task["authorization"].update(enabled=False, write_authorized=False)
            task["completion"] = {"accepted_by": "CHIEF_EDITOR", "delivery_commit": delivery,
                                  "accepted_blobs": {request["path"]: blob}}
            state.update(active_project_task_id=None, status="TEST / CLOSED")
            state["permissions"]["simulation"] = False
            save(task_path, task)
            save(state_path, state)
            self.assertIsNone(validator.validate_repository(repo)["active_task_id"])
            with self.assert_rejected("NO_ACTIVE_TASK_FOR_SPECIALIST_ACTION"):
                validator.authorize_repository_request(repo, request)
            output.write_text("# modified after acceptance\n")
            with self.assert_rejected("ACCEPTED_ARTIFACT_DRIFT"):
                validator.validate_repository(repo)

    def read_only_assignment_fixture(self):
        # Routing an unassigned Story role must not depend on which role is
        # currently producing in the real repository.
        state = copy.deepcopy(self.scenario_states["simulation_active"])
        tasks = {**copy.deepcopy(self.tasks), **copy.deepcopy(self.scenario_tasks)}
        task_id = "STORY-REVIEW-EXAMPLE-001"
        path = "working/v2.7/FOULWAKE_STORY_FRAMEWORK.md"
        task = {
            "task_id": task_id, "canonical_task_authority": True,
            "project_task": False, "status": "READ_ONLY_ASSIGNED",
            "issued_by": "CHIEF_EDITOR", "executor_role": "STORY_EDITOR",
            "reviewer_roles": ["CHIEF_EDITOR"],
            "authorization": {"enabled": True, "write_authorized": False,
                              "allowed_actions": ["READ_ONLY_VALIDATION"],
                              "role_actions": {"STORY_EDITOR": ["READ_ONLY_VALIDATION"]}},
            "scope": {"branch": "work/v2.7-story", "allowed_globs": [],
                      "allowed_exact_paths": [path], "max_changed_files": 0,
                      "binary_files_allowed": False},
            "required_outputs": [], "delivery": {"channel": "VISIBLE_ROLE_CHAT_ONLY"},
            "runtime_permissions": {key: False for key in state["permissions"]},
            "owner_authorization": {"task_id": task_id, "decision": "AUTHORIZED",
                                    "delegation_id": self.contracts["lifecycle"]["task_issuance_delegation"]["id"],
                                    "recorded_from": "Isolated read-only routing test."},
            "source": {"commit": validator.git(ROOT, "rev-parse", "HEAD")},
            "inputs": [{"path": path, "git_blob": validator.git(ROOT, "rev-parse", f"HEAD:{path}")}],
        }
        tasks[task_id] = task
        state.setdefault("read_only_assignments", {})["STORY_EDITOR"] = {
            "task_id": task_id, "task_ref": f"governance/v4/tasks/{task_id}.json",
            "status": "READ_ONLY_ASSIGNED",
        }
        return state, tasks, task_id

    def test_29_read_only_assignment_routes_the_role_without_replacing_active_work(self):
        state, tasks, task_id = self.read_only_assignment_fixture()
        active_before = state["active_project_task_id"]
        permissions_before = copy.deepcopy(state["permissions"])
        validator.validate_read_only_assignments(ROOT, state, tasks, self.contracts, self.registry)
        with patch.object(bootstrap, "load_repository_bundle", return_value=(state, tasks, self.contracts, self.registry)):
            rendered = bootstrap.build_bootstrap(ROOT, "STORY_EDITOR")
            self.assertIn(f"TASK_ID: {task_id}", rendered)
            self.assertIn("TASK_BINDING: READ_ONLY_ASSIGNMENT", rendered)
            self.assertIn("CURRENT_ROLE_TASK_ACTIONS: READ_ONLY_VALIDATION", rendered)
            self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", rendered)
            self.assertIn("VISIBLE_ROLE_CHAT_ONLY", rendered)
            unrelated = bootstrap.build_bootstrap(ROOT, "VISUAL_DESIGN", task_id)
            self.assertIn("TASK_BINDING: INACTIVE / NO AUTHORITY", unrelated)
            self.assertIn("CURRENT_ROLE_TASK_ACTIONS: NONE", unrelated)
        self.assertEqual(state["active_project_task_id"], active_before)
        self.assertEqual(state["permissions"], permissions_before)

    def test_30_read_only_assignment_denies_every_story_write_action(self):
        state, tasks, task_id = self.read_only_assignment_fixture()
        request = {"role": "STORY_EDITOR", "task_id": task_id, "branch": "work/v2.7-story",
                   "path": tasks[task_id]["scope"]["allowed_exact_paths"][0],
                   "action": "READ_ONLY_VALIDATION"}
        validator.authorize_request(state, tasks, self.registry, self.contracts, request)
        for action in ("WRITE", "PRODUCE_STORY", "PRODUCE_FLAVOR", "PERIOD_LANGUAGE_REVIEW"):
            with self.subTest(action=action), self.assert_rejected():
                validator.authorize_request(state, tasks, self.registry, self.contracts,
                                            {**request, "action": action})

    def test_31_read_only_assignment_rejects_widened_authority_and_source_drift(self):
        cases = [
            (lambda task: task["authorization"].update(write_authorized=True), "READ_ONLY_ASSIGNMENT_AUTHORITY"),
            (lambda task: task["authorization"].update(allowed_actions=["PRODUCE_STORY"]), "READ_ONLY_ASSIGNMENT_AUTHORITY"),
            (lambda task: task["scope"].update(max_changed_files=1), "READ_ONLY_ASSIGNMENT_SCOPE"),
            (lambda task: task["scope"].update(branch="work/v2.7-visual"), "READ_ONLY_ASSIGNMENT_SCOPE"),
            (lambda task: task["delivery"].update(channel="REPOSITORY"), "READ_ONLY_ASSIGNMENT_SCOPE"),
            (lambda task: task["runtime_permissions"].update(simulation=True), "READ_ONLY_ASSIGNMENT_PERMISSION"),
            (lambda task: task["owner_authorization"].update(decision="UNVERIFIED"), "READ_ONLY_ASSIGNMENT_OWNER_AUTHORIZATION"),
            (lambda task: task["inputs"][0].update(git_blob="0" * 40), "READ_ONLY_ASSIGNMENT_INPUT_DRIFT"),
        ]
        for mutate, code in cases:
            state, tasks, task_id = self.read_only_assignment_fixture()
            mutate(tasks[task_id])
            with self.subTest(code=code), self.assert_rejected(code):
                validator.validate_read_only_assignments(ROOT, state, tasks, self.contracts, self.registry)


if __name__ == "__main__":
    program = unittest.main(verbosity=2, exit=False)
    print(f"Negative controls verified: {GovernanceV4Tests.negative_checks}")
    raise SystemExit(0 if program.result.wasSuccessful() else 1)
