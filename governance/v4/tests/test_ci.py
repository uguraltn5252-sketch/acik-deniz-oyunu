#!/usr/bin/env python3
"""Git-backed tests of trusted CI routing and hostile specialist changes."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "governance/v4"))
import ci
from validator import GovernanceViolation, validate_integration_request, authorize_request, validate_execution_scope


class TrustedCITests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="foulwake-ci-test-")
        self.repo = Path(self.temporary.name) / "repo"
        subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", str(ROOT), str(self.repo)], check=True)
        # A completed live task must not disable these negative controls. Keep
        # their real active-task fixture explicit and separate from live state.
        scenarios = json.loads((ROOT / "governance/v4/tests/fixtures/RUNTIME_SCENARIOS.json").read_text())
        self.git("checkout", "--quiet", "--detach", scenarios["trusted_ci_fixture"]["authority_commit"])
        state = json.loads(self.git("show", "HEAD:governance/v4/runtime/STATE.json"))
        self.task_id = state["active_project_task_id"]
        self.task = json.loads(self.git("show", f"HEAD:governance/v4/tasks/{self.task_id}.json"))
        self.branch = self.task["scope"]["branch"]
        self.baseline = self.git("log", "--diff-filter=A", "--format=%H", "HEAD", "--", f"governance/v4/tasks/{self.task_id}.json").splitlines()[0]
        self.git("checkout", "--quiet", "--detach", "HEAD")
        # Install current checker on an independent integration commit. The
        # specialist branch stays at its real activation baseline.
        for name in ("ci.py", "validator.py"):
            shutil.copy2(ROOT / "governance/v4" / name, self.repo / "governance/v4" / name)
        self.authority = self.commit("test only: trusted integration checker", allow_empty=True)
        self.git("update-ref", "refs/remotes/origin/v2.7-design", self.authority)
        self.git("checkout", "--quiet", "-b", self.branch, self.baseline)
        self.output = self.task["scope"]["allowed_exact_paths"][0]

    def tearDown(self):
        self.temporary.cleanup()

    def git(self, *args):
        return ci.git(self.repo, *args).decode().strip()

    def commit(self, message, allow_empty=False):
        self.git("add", "-A")
        args = ["-c", "user.name=CI test", "-c", "user.email=test@example.invalid", "commit", "--quiet", "-m", message]
        if allow_empty:
            args.append("--allow-empty")
        self.git(*args)
        return self.git("rev-parse", "HEAD")

    def check(self, head=None):
        return ci.validate_branch(self.repo, self.authority, self.branch, head or self.git("rev-parse", "HEAD"))

    def write(self, relative, data):
        p = self.repo / relative
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    def test_real_activation_and_scoped_delivery_pass(self):
        self.assertEqual(self.check()["changed_files"], 0)
        self.write(self.output, b"# test fixture only; no game simulation\n")
        self.commit("test only: valid scoped output")
        self.assertEqual(self.check()["changed_files"], 1)

    def test_specialist_cannot_change_its_own_authority(self):
        self.write("governance/v4/contracts/CONTRACTS.json", b'{"allow_everything":true}\n')
        self.commit("test only: hostile policy")
        with self.assertRaisesRegex(GovernanceViolation, "CI_OUT_OF_SCOPE_PATH"):
            self.check()

    def test_binary_and_symlink_rejected(self):
        self.write(self.output, b"\x00\xff")
        self.commit("test only: binary output")
        with self.assertRaisesRegex(GovernanceViolation, "CI_BINARY_FORBIDDEN"):
            self.check()
        self.git("checkout", "--quiet", "--detach", self.baseline)
        p = self.repo / self.output
        p.parent.mkdir(parents=True, exist_ok=True)
        p.symlink_to("/etc/passwd")
        self.commit("test only: symlink output")
        with self.assertRaisesRegex(GovernanceViolation, "CI_UNSAFE_FILE_MODE_OR_DELETION"):
            self.check()

    def test_input_drift_and_wrong_baseline_rejected(self):
        p = self.task["inputs"][-1]["path"]
        self.write(p, (self.repo / p).read_bytes() + b"\n")
        self.commit("test only: input drift")
        with self.assertRaisesRegex(GovernanceViolation, "CI_TASK_INPUT_DRIFT"):
            self.check()
        with self.assertRaisesRegex(GovernanceViolation, "CI_WRONG_BASELINE"):
            self.check(self.task["source"]["commit"])

    def test_old_workflow_entry_loads_current_trusted_checker(self):
        result = subprocess.run([sys.executable, "-B", str(ROOT / "governance/validate_workstream_scope.py"),
                                 "--config", "governance/WORKSTREAM_SCOPE_BASELINES.json",
                                 "--branch", self.branch, "--head", self.baseline], cwd=self.repo,
                                text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS / TASK_SCOPE_ONLY", result.stdout)

    def test_coordinator_integrates_only_independently_reviewed_bytes(self):
        self.write(self.output, b"# accepted test fixture; no game simulation\n")
        delivery = self.commit("test only: specialist delivery")
        self.git("update-ref", f"refs/remotes/origin/{self.branch}", delivery)
        self.git("checkout", "--quiet", "-B", "v2.7-design", self.authority)
        state = json.loads(self.git("show", f"{self.authority}:governance/v4/runtime/STATE.json"))
        control_id = state["coordination_control"]["task_id"]
        control = json.loads(self.git("show", f"{self.authority}:governance/v4/tasks/{control_id}.json"))
        tasks = {self.task_id: self.task, control_id: control}
        contracts = json.loads(self.git("show", f"{self.authority}:governance/v4/contracts/CONTRACTS.json"))
        roles = json.loads(self.git("show", f"{self.authority}:governance/v4/roles/REGISTRY.json"))
        ref = "governance/v4/evidence/TEST_ACCEPTANCE.json"
        accepted = {"task_id": self.task_id, "status": "ACCEPTED", "reviewer_role": "CHIEF_EDITOR",
                    "delivery_commit": delivery, "accepted_blobs": {self.output: self.git("rev-parse", f"{delivery}:{self.output}")}}
        self.write(ref, json.dumps(accepted).encode())
        request = {"role": "CHIEF_EDITOR", "action": "INTEGRATE", "task_id": control_id,
                   "branch": "v2.7-design", "path": self.output, "acceptance_ref": ref}
        authorize_request(state, tasks, roles, contracts, request)
        validate_integration_request(self.repo, state, tasks, request)
        for role in ("SIMULATION_QA", "VISUAL_DESIGN", "STORY_EDITOR", "ART_DIRECTION"):
            with self.assertRaisesRegex(GovernanceViolation, "COORDINATION_ROLE_REQUIRED"):
                authorize_request(state, tasks, roles, contracts, {**request, "role": role})
        accepted["reviewer_role"] = "SIMULATION_QA"
        self.write(ref, json.dumps(accepted).encode())
        with self.assertRaisesRegex(GovernanceViolation, "INDEPENDENT_ACCEPTANCE_MISSING"):
            validate_integration_request(self.repo, state, tasks, request)
        accepted["reviewer_role"] = "CHIEF_EDITOR"
        self.write(ref, json.dumps(accepted).encode())
        self.write(self.output, ci.git(self.repo, "show", f"{delivery}:{self.output}"))
        validate_integration_request(self.repo, state, tasks, request)
        self.write(self.output, b"# unauthorized editorial change\n")
        with self.assertRaisesRegex(GovernanceViolation, "INTEGRATION_CONTENT_EDIT"):
            validate_integration_request(self.repo, state, tasks, request)

    def test_idle_authority_freezes_workstream_at_recorded_head(self):
        self.git("checkout", "--quiet", "--detach", self.authority)
        path = "governance/v4/runtime/STATE.json"
        state = json.loads((self.repo / path).read_text())
        state["active_project_task_id"] = None
        state["permissions"] = {key: False for key in state["permissions"]}
        row = next(row for row in state["workstreams"].values() if row["branch"] == self.branch)
        row["head"] = self.baseline
        self.write(path, json.dumps(state).encode())
        idle = self.commit("test only: idle branch authority")
        checked = ci.validate_branch(self.repo, idle, self.branch, self.baseline)
        self.assertEqual(checked["status"], "PASS / FROZEN / NO_WRITE_AUTHORITY")
        self.git("checkout", "--quiet", "--detach", self.baseline)
        self.write(self.output, b"# unauthorized output after task closure\n")
        changed = self.commit("test only: write after closure")
        with self.assertRaisesRegex(GovernanceViolation, "CI_UNAUTHORIZED_BRANCH_CHANGE"):
            ci.validate_branch(self.repo, idle, self.branch, changed)

    def test_coordination_after_accepted_merge_preserves_content_boundaries(self):
        outputs = self.task["required_outputs"]
        for path in outputs:
            self.write(path, b"# independently accepted test evidence\n")
        delivery = self.commit("test only: complete specialist delivery")
        blobs = {path: self.git("rev-parse", f"{delivery}:{path}") for path in outputs}
        self.git("checkout", "--quiet", "-B", "v2.7-design", self.authority)
        self.git("-c", "user.name=CI test", "-c", "user.email=test@example.invalid",
                 "merge", "--no-ff", "--no-commit", delivery)
        ref = "governance/v4/evidence/TEST_ACCEPTANCE.json"
        accepted = {"task_id": self.task_id, "status": "ACCEPTED", "reviewer_role": "CHIEF_EDITOR",
                    "delivery_commit": delivery, "accepted_blobs": blobs}
        self.write(ref, json.dumps(accepted).encode())
        integrated = self.commit("test only: accepted specialist integration")
        state = json.loads((self.repo / "governance/v4/runtime/STATE.json").read_text())
        control_id = state["coordination_control"]["task_id"]
        control = json.loads((self.repo / f"governance/v4/tasks/{control_id}.json").read_text())
        request = {"role": "CHIEF_EDITOR", "action": "MANAGE_STATE", "task_id": control_id,
                   "branch": "v2.7-design", "path": "governance/v4/runtime/STATE.json"}
        validate_execution_scope(self.repo, control, request)
        with self.assertRaisesRegex(GovernanceViolation, "OUT_OF_SCOPE_PATH"):
            validate_execution_scope(self.repo, control, {**request, "path": self.output})
        self.write(self.output, b"# unauthorized edit after acceptance\n")
        with self.assertRaisesRegex(GovernanceViolation, "ACCEPTED_ARTIFACT_DRIFT"):
            validate_execution_scope(self.repo, control, request)
        self.git("reset", "--hard", integrated)
        self.write("working/v2.7/qa/unaccepted.md", b"# never accepted\n")
        self.commit("test only: unaccepted content history")
        with self.assertRaisesRegex(GovernanceViolation, "OUT_OF_SCOPE_PATH"):
            validate_execution_scope(self.repo, control, request)
        self.git("reset", "--hard", integrated)
        accepted["reviewer_role"] = "SIMULATION_QA"
        self.write(ref, json.dumps(accepted).encode())
        self.commit("test only: producer self acceptance")
        with self.assertRaisesRegex(GovernanceViolation, "INDEPENDENT_ACCEPTANCE_MISSING"):
            validate_execution_scope(self.repo, control, request)


if __name__ == "__main__":
    unittest.main(verbosity=2)
