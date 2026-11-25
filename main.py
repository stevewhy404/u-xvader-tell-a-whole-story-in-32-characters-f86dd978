"""Wi-Fi network name entry: one line, at most 32 characters.

Final: the network name is a breakup note left for Dave — the locks
are changed and Dave is the one locked out. A situation, a named
character, and something that happened, in 25 characters.
"""
import os

LINE = "I changed the locks, Dave"
MAX_CHARS = 32


def resolve_output_dir() -> str:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return out or "/output"


def verify(text: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-32 chars, not whitespace-only."""
    if not isinstance(text, str):
        raise SystemExit("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be whitespace only")
    text.encode("utf-8")


def main() -> None:
    text = LINE
    verify(text)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
