#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def main():
    commit_msg_path = Path(sys.argv[1])
    commit_msg = commit_msg_path.read_text().strip()

    pattern = re.compile(
        r"^(chore|feat|fix|refactor|test)\("
        r"(?:\s*DBS-\d+\s*(?:,\s*DBS-\d+\s*)*)"
        r"\):.+",
    )

    if pattern.match(commit_msg):
        return 0
    else:
        print("❌ Commit message inválido!")
        print("")
        print("Formatos esperados:")
        print("  chore(DBS-123): descrição")
        print("  feat(DBS-123,DBS-456): descrição")
        print("  fix(DBS-123, DBS-456): descrição")
        print("  refactor(DBS-123): descrição")
        print("  test(DBS-123): descrição")
        return 1


if __name__ == "__main__":
    sys.exit(main())
