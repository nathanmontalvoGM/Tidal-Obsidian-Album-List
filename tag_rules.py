"""
Shared tag rules, loaded from _scripts/tags.json.

Every script that writes tags goes through normalize_tag(), so the same genre is
always spelled the same way and non-genre tags never get written.
"""
import json
import os
import re

RULES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_scripts", "tags.json")

with open(RULES_PATH, encoding="utf-8") as _f:
    _rules = json.load(_f)

ALIASES = _rules["aliases"]
BLOCKLIST = set(_rules["blocklist"])
CANONICAL = sorted(set(ALIASES.values()))


def tag_key(tag):
    """'Nu-Metal', 'nu metal', '#Numetal' -> 'numetal'."""
    return re.sub(r"[^a-z0-9]", "", str(tag).strip().strip('"\'').lstrip("#").lower())


def normalize_tag(tag):
    """Return the canonical tag, None if the tag is blocklisted or empty,
    or the cleaned original if it isn't in tags.json yet."""
    k = tag_key(tag)
    if not k or k in BLOCKLIST or re.fullmatch(r"\d+s?", k):  # also drops years and decades
        return None
    if k in ALIASES:
        return ALIASES[k]
    cleaned = str(tag).strip().strip('"\'').lstrip("#")
    return cleaned[:1].upper() + cleaned[1:]


def is_known(tag):
    k = tag_key(tag)
    return k in ALIASES or k in BLOCKLIST or bool(re.fullmatch(r"\d+s?", k))


def normalize_list(tags):
    """Normalize, drop blocked, de-duplicate (keeping order)."""
    out = []
    for t in tags:
        n = normalize_tag(t)
        if n and n not in out:
            out.append(n)
    return out
