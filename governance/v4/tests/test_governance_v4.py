#!/usr/bin/env python3
"""Generic runtime, migration-audit, positive and failure-path tests."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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

    def authorize_scenario(
        self,
        state_name: str,
        request: dict,
        mutation: dict | None = None,
        permission_overrides: dict | None = None,
    ) -> None:
        state = copy.deepcopy(self.scenario_states[state_name])
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
            self.scenario_tasks,
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
        self.assertEqual(result["active_task_id"], None)
        self.assertTrue(result["cutover_performed"])
        self.assertEqual(result["loaded_task_ids"], ["GOV4-CUTOVER-001"])

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
        with self.assertRaises(validator.GovernanceViolation):
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
        visual = bootstrap.build_bootstrap(ROOT, "VISUAL_DESIGN")
        self.assertIn("GENERATED / NON_CANONICAL", visual)
        self.assertIn("ACTIVE_PROJECT_TASK: NONE", visual)
        self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", visual)
        chief = bootstrap.build_bootstrap(ROOT, "CHIEF_EDITOR")
        self.assertIn("ACTIVE_PROJECT_TASK: NONE", chief)
        self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", chief)
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
        self.assertEqual(len(cases), 24)
        for case in cases:
            with self.subTest(case=case["id"]):
                with self.assertRaises(validator.GovernanceViolation) as caught:
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
                with self.assertRaises(validator.GovernanceViolation) as caught:
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
        with self.assertRaises(validator.GovernanceViolation) as caught:
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
        before = json.loads(
            validator.git(
                ROOT,
                "show",
                f"{task['reactivation']['source_head']}:governance/v4/runtime/STATE.json",
            )
        )
        self.assertIsNone(self.state["active_project_task_id"])
        self.assertEqual(task["status"], "CLOSED / HARDENING_COMPLETE")
        self.assertFalse(task["authorization"]["enabled"])
        self.assertFalse(task["authorization"]["write_authorized"])
        expected_blockers = dict(before["open_blockers"])
        expected_blockers.pop("SRC-002")
        self.assertEqual(self.state["open_blockers"], expected_blockers)
        self.assertTrue(all(value is False for value in self.state["permissions"].values()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
