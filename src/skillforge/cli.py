import argparse
import sys
from pathlib import Path
from .compiler import SkillCompiler

def main():
    parser = argparse.ArgumentParser(description="SkillForge: Agent Skill Compiler.")
    parser.add_argument("--spec", required=True)
    parser.add_argument("--out", default="compiled_skill.py")
    args = parser.parse_args()
    try:
        code = SkillCompiler.compile_from_spec(args.spec)
        Path(args.out).write_text(code, encoding="utf-8")
        print(f"[+] Compiled skill to {args.out}")
    except Exception as e:
        print(f"[!] Error: {e}", file=sys.stderr); sys.exit(1)

if __name__ == "__main__": main()
