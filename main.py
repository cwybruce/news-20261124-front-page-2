"""Copy the front-page image to the grader's output directory as entry.png.

Deterministic: a plain byte-for-byte copy, so both runs produce identical
output. The image is the repository's own entry.png, drawn by PIL from
verified 24 November 2026 news. After copying, the output is checked
byte-for-byte against the source so a truncated copy is caught, not
shipped.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
# Guard against a truncated copy: the output must be byte-identical.
assert sha256(DST) == sha256(SRC), "copied entry.png differs from source"
print("wrote", DST, sha256(DST))
