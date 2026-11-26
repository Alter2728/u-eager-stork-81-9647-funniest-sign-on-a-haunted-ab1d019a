"""Draft is a generic do not enter ghost pun with no IT life in it.
Revision makes the ghost the old sysadmin and lands on unread tickets."""

import os

TEXT = "PLEASE KNOCK — our old sysadmin haunts Rack 4. He still closes tickets unread."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT and "\r" not in TEXT
assert 1 <= len(TEXT) <= 120

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
