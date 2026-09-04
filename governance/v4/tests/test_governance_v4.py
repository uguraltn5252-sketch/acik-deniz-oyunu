#!/usr/bin/env python3
"""Parity, positive-path and failure-path tests for FOULWAKE Governance v4."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[3]
V4 = ROOT / "governance" / "v4"
sys.path.insert(0, str(V4))

import bootstrap  # noqa: E402
import validator  # noqa: E402


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class GovernanceV4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.state = read_json("governance/v4/runtime/STATE.json")
        cls.task = read_json("governance/v4/tasks/GOV4-MIGRATION-001.json")
        cls.contracts = read_json("governance/v4/contracts/CONTRACTS.json")
        cls.registry = read_json("governance/v4/roles/REGISTRY.json")
        cls.history = read_json("governance/v4/history/evidence/INDEX.json")
        cls.v3 = read_json("governance/CURRENT_STAGE.json")
        cls.copy_doc = read_json("working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json")
        cls.canonical_copy = cls.copy_doc["records"][0]
        cls.fixtures = read_json("governance/v4/tests/fixtures/NEGATIVE_CASES.json")

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

    def test_02_v4_generic_validator_passes(self) -> None:
        result = validator.validate_repository(ROOT, validator.EXPECTED_BRANCH)
        self.assertEqual(result["changed_files"], 10)
        self.assertTrue(all(result["parity"].values()))
        self.assertFalse(result["cutover_performed"])

    def test_03_parity_matrix_is_complete(self) -> None:
        parity = validator.compare_v3_v4(self.v3, self.state)
        self.assertEqual(
            set(parity),
            {
                "write_authority", "active_task", "v26_tree", "active_candidate",
                "open_blockers", "permissions", "workstream_heads",
                "accepted_art_direction",
            },
        )
        self.assertTrue(all(parity.values()), parity)

    def test_04_locked_tree_and_source_are_exact(self) -> None:
        tree = validator.git(ROOT, "rev-parse", "HEAD:releases/v2.6")
        validator.validate_locked_tree(tree)
        self.assertEqual(
            self.state["source_checkpoint"]["commit"], validator.EXPECTED_SOURCE
        )

    def test_05_role_partition_and_independent_framing(self) -> None:
        roles = self.registry["roles"]
        self.assertEqual(set(roles), validator.EXPECTED_ROLES)
        self.assertNotIn("RULES_EDITOR", roles)
        self.assertNotIn("FRAMING_DECISION", roles["VISUAL_DESIGN"]["allowed_actions"])
        self.assertIn("FRAMING_DECISION", roles["ART_DIRECTION"]["allowed_actions"])

    def test_06_protected_quality_gate_parity(self) -> None:
        self.assertEqual(
            set(self.contracts["protected_quality_gates"]), validator.EXPECTED_GATES
        )
        self.assertEqual(self.contracts["quality_principle"], validator.QUALITY_PRINCIPLE)

    def test_07_kaptan_source_copy_and_framing_contract(self) -> None:
        owner = self.contracts["owner_controls"]
        self.assertEqual(owner["kaptan"]["technical_id"], "SET-KP-01")
        self.assertIn("NOT_STYLE_ONLY", owner["kaptan"]["source_policy"])
        self.assertFalse(owner["exact_copy"]["image_model_may_generate_or_rewrite_copy"])
        self.assertFalse(owner["framing"]["producer_self_approval"])
        self.assertEqual(
            owner["framing"]["allowed_dispositions"],
            ["FRAMING_PASS", "REFRAME_REQUIRED"],
        )

    def test_08_history_and_external_draft_cannot_authorize(self) -> None:
        self.assertFalse(self.history["canonical"])
        self.assertFalse(self.history["may_authorize_work"])
        draft = next(
            row for row in self.history["records"]
            if row["evidence_id"] == "EXTERNAL-RULEBOOK-DRAFT"
        )
        self.assertEqual(draft["status"], "NON_CANONICAL_DRAFT / REFERENCE_ONLY")
        tracked = validator.git(ROOT, "ls-files").splitlines()
        self.assertFalse(any(PurePosixPath(path).name == draft["filename"] for path in tracked))

    def test_09_art_direction_framing_positive_path(self) -> None:
        validator.authorize_request(
            self.state,
            self.task,
            self.registry,
            self.contracts,
            {
                "role": "ART_DIRECTION",
                "action": "FRAMING_DECISION",
                "producer_role": "VISUAL_DESIGN",
                "disposition": "FRAMING_PASS",
            },
            self.canonical_copy,
        )
        validator.authorize_request(
            self.state,
            self.task,
            self.registry,
            self.contracts,
            {
                "role": "PROJECT_OWNER",
                "action": "CUTOVER_DECISION",
                "task_id": "GOV4-MIGRATION-001",
            },
            self.canonical_copy,
        )

    def test_10_exact_copy_positive_path(self) -> None:
        validator.authorize_request(
            self.state,
            self.task,
            self.registry,
            self.contracts,
            {
                "role": "SIMULATION_QA",
                "action": "COPY_CHECK",
                "copy_record": self.canonical_copy,
            },
            self.canonical_copy,
        )

    def test_11_bootstrap_is_concise_noncanonical_and_fail_closed(self) -> None:
        idle = bootstrap.build_bootstrap(ROOT, "VISUAL_DESIGN")
        self.assertIn("GENERATED / NON_CANONICAL", idle)
        self.assertIn("ACTIVE_PROJECT_TASK: NONE", idle)
        self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", idle)
        migration = bootstrap.build_bootstrap(ROOT, "CHIEF_EDITOR", "GOV4-MIGRATION-001")
        self.assertIn("TASK_STATUS: DELIVERED", migration)
        self.assertIn("CURRENT_WRITE_AUTHORIZED: FALSE", migration)

    def test_12_all_required_negative_cases_are_rejected(self) -> None:
        cases = self.fixtures["cases"]
        self.assertEqual(len(cases), 9)
        for case in cases:
            with self.subTest(case=case["id"]):
                with self.assertRaises(validator.GovernanceViolation) as caught:
                    self._run_negative(case)
                self.assertEqual(caught.exception.code, case["expected_code"])

    def _run_negative(self, case: dict) -> None:
        case_type = case["type"]
        if case_type == "DELIVERY_SCOPE":
            paths = case["paths"]
            if paths == "TASK_EXPECTED_PATHS":
                paths = self.task["delivery_scope"]["expected_paths"]
            validator.audit_delivery_scope(self.task, case["branch"], paths)
            return
        if case_type == "LOCKED_TREE":
            validator.validate_locked_tree(case["actual"])
            return
        if case_type == "COPY_MUTATION":
            supplied = copy.deepcopy(self.canonical_copy)
            supplied.update(case["mutation"])
            validator.validate_exact_copy(supplied, self.canonical_copy)
            return
        if case_type == "ACTION":
            validator.authorize_request(
                self.state,
                self.task,
                self.registry,
                self.contracts,
                case["request"],
                self.canonical_copy,
            )
            return
        self.fail(f"unknown negative fixture type: {case_type}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
