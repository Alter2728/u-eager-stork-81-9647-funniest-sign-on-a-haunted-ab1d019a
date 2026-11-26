"""Draft flaw: the first line was a generic warning that could hang anywhere.
Revision fix: the final line gives the ghost a rack, a schedule, and a ticketing rule."""

import os

TEXT = "WARNING: The ghost in Rack 4 only haunts during maintenance windows. Do not reboot him without an approved ticket."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT
assert 1 <= len(TEXT) <= 120

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
