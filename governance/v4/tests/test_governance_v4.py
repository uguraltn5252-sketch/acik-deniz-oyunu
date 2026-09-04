#!/usr/bin/env python3
"""Generic runtime, migration-audit, positive and failure-path tests."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
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
        cls.canonical_copy = read_json(
            "working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json"
        )["records"][0]

    def authorize_scenario(self, state_name: str, request: dict, mutation: dict | None = None) -> None:
        supplied = copy.deepcopy(request)
        if mutation is not None:
            copy_record = copy.deepcopy(self.canonical_copy)
            copy_record.update(mutation)
            supplied["copy_record"] = copy_record
        validator.authorize_request(
            self.scenario_states[state_name],
            self.scenario_tasks,
            self.registry,
            self.contracts,
            supplied,
            self.canonical_copy,
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
        self.assertFalse(result["cutover_performed"])
        self.assertEqual(result["loaded_task_ids"], ["GOV4-REWORK-001"])

    def test_03_separate_migration_rework_audit_passes(self) -> None:
        result = migration_audit.validate_rework(ROOT)
        self.assertEqual(result["changed_files"], 10)
        self.assertTrue(all(result["parity"].values()))

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
                "action": "PRODUCE_VISUAL",
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
        for action in ("COPY_CHECK", "QA_REVIEW"):
            request = {
                "role": "SIMULATION_QA",
                "action": action,
                "task_id": "VISUAL-EXAMPLE-001",
                "branch": "work/v2.7-visual",
                "path": "working/v2.7/visual/example/card.png",
            }
            if action == "COPY_CHECK":
                request["copy_record"] = self.canonical_copy
            self.authorize_scenario("visual_active", request)
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
        validator.authorize_request(
            self.state,
            self.tasks,
            self.registry,
            self.contracts,
            {
                "role": "PROJECT_OWNER",
                "action": "CUTOVER_DECISION",
                "task_id": "GOV4-REWORK-001",
                "branch": "migration/governance-v4",
                "path": "governance/v4/evidence/REWORK_RESULT.json",
            },
            self.canonical_copy,
        )

    def test_12_bootstrap_is_noncanonical_and_reflects_task_binding(self) -> None:
        idle = bootstrap.build_bootstrap(ROOT, "VISUAL_DESIGN")
        self.assertIn("GENERATED / NON_CANONICAL", idle)
        self.assertIn("ACTIVE_PROJECT_TASK: NONE", idle)
        self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", idle)
        migration = bootstrap.build_bootstrap(ROOT, "PROJECT_OWNER", "GOV4-REWORK-001")
        self.assertIn("TASK_BINDING: MIGRATION_CONTROL_ONLY", migration)
        self.assertIn("CURRENT_ROLE_TASK_ACTIONS: CUTOVER_DECISION", migration)

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
        self.assertEqual(len(cases), 16)
        for case in cases:
            with self.subTest(case=case["id"]):
                with self.assertRaises(validator.GovernanceViolation) as caught:
                    if case.get("type") == "LOCKED_TREE":
                        validator.validate_locked_tree(case["actual"], case["expected"])
                    else:
                        self.authorize_scenario(
                            case["state"],
                            case["request"],
                            case.get("copy_mutation"),
                        )
                self.assertEqual(caught.exception.code, case["expected_code"])

    def test_16_no_active_task_rejects_every_named_non_read_only_action_class(self) -> None:
        requests = [
            ("SIMULATION_QA", "COPY_CHECK"),
            ("SIMULATION_QA", "RULES_INTEGRITY_REVIEW"),
            ("SIMULATION_QA", "QA_REVIEW"),
            ("VISUAL_DESIGN", "PRODUCE_VISUAL"),
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
        state["permissions"]["visual_production"] = False
        request = {
            "role": "VISUAL_DESIGN",
            "action": "PRODUCE_VISUAL",
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
                self.canonical_copy,
            )
        self.assertEqual(caught.exception.code, "PERMISSION_CLOSED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
