"""One-time transport of two owner-authorized, hash-pinned publication PDFs.

No content generation, release, policy update, force push or unbounded path write.
Removed from runnable use after the task is delivered.
"""
from pathlib import Path
import base64
import hashlib
import json
import os
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
TASK = 'FOULWAKE-PUBLICATION-REDESIGN-001'
REPO = 'uguraltn5252-sketch/acik-deniz-oyunu'
PINNED = {
    'working/v2.7/publication_20260909/pdf/FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf':
        ('3eb6b291417bdefcbf5ed9f35a012738c12cc33f855e5a5d53bd586ff415c87f', 74699858),
    'working/v2.7/publication_20260909/pdf/FOULWAKE_KURAL_KITABI_A4_v2.7.pdf':
        ('dde37e8dd7a2aa846e5e44d9d06a10f52ebcd834d885986de6c07c863277b91f', 14300745),
}

def read(path):
    return json.loads((ROOT / path).read_text())

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def main():
    assert os.environ['GITHUB_REPOSITORY'] == REPO
    assert os.environ['GITHUB_REF'] == 'refs/heads/v2.7-design'
    head = os.environ['GITHUB_SHA']
    assert git('rev-parse', 'HEAD') == head
    assert not git('status', '--porcelain')
    state = read('governance/v4/runtime/STATE.json')
    task = read(f'governance/v4/tasks/{TASK}.json')
    assert state['active_project_task_id'] == TASK and task['status'] == 'ACTIVE'
    assert task['authorization']['enabled'] and task['authorization']['write_authorized']
    assert task['runtime_permissions']['pdf_or_print_package']
    assert task['executor_role'] == 'CHIEF_EDITOR'
    assert git('rev-parse', 'HEAD:releases/v2.6') == 'efb41c46f06174c42dcdab2859b7c0ba517f86f0'
    manifest = read('governance/v4/evidence/PUBLICATION_BINARY_TRANSFER_20260909.json')
    verification = read('working/v2.7/qa/publication_20260909/verification.json')
    assert verification['status'] == 'PASS'
    assert {r['path'] for r in manifest['targets']} == set(PINNED)
    for target in manifest['targets']:
        path = target['path']
        digest, size = PINNED[path]
        assert (target['sha256'], target['bytes']) == (digest, size)
        label = 'cards' if 'KARTLAR' in path else 'book'
        assert verification['pdf_sha256'][label] == digest
        data = bytearray()
        for index, part in enumerate(target['parts']):
            assert part['index'] == index and part['offset'] == len(data)
            sha = part['sha']
            assert len(sha) == 40 and all(c in '0123456789abcdef' for c in sha)
            request = urllib.request.Request(
                f'https://api.github.com/repos/{REPO}/git/blobs/{sha}',
                headers={'Accept': 'application/vnd.github+json',
                         'Authorization': 'Bearer ' + os.environ['GH_TRANSFER_TOKEN'],
                         'User-Agent': 'FOULWAKE-publication-transfer'})
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.load(response)
            assert payload['encoding'] == 'base64' and payload['sha'] == sha
            piece = base64.b64decode(payload['content'])
            assert len(piece) == part['bytes'] and blob_sha(piece) == sha
            data.extend(piece)
        assert len(data) == size and hashlib.sha256(data).hexdigest() == digest
        assert blob_sha(data) == target['git_blob']
        output = ROOT / path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
        print(f'Verified {output.name}: {size} bytes, SHA-256 {digest}')
    git('add', '--sparse', '--', *sorted(PINNED))
    assert set(git('diff', '--cached', '--name-only').splitlines()) == set(PINNED)
    remote = git('ls-remote', 'origin', 'refs/heads/v2.7-design').split()[0]
    assert remote == head, 'Branch advanced; do not overwrite concurrent work'
    git('config', 'user.name', 'FOULWAKE publication transfer')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    git('commit', '-m', 'Deliver verified combined A4 card and rulebook PDFs')
    subprocess.run(['git', 'push', 'origin', 'HEAD:refs/heads/v2.7-design'], cwd=ROOT, check=True)
    print('DELIVERY_COMMIT=' + git('rev-parse', 'HEAD'))

if __name__ == '__main__':
    main()
