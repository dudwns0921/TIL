#!/usr/bin/env python3
"""저장소 안 모든 .md 의 상대 링크와 이미지가 실제 파일을 가리키는지 확인한다. GitHub 은 대소문자를 가리므로 철자까지 비교한다.
  python3 scripts/check_links.py        깨진 링크 목록, 있으면 종료코드 1
코드 블록(```) 안의 링크는 예시이므로 건너뛴다."""
import os, re, sys, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'!?\[[^\]]*\]\(\s*<?([^)>\s]+)>?(?:\s+"[^"]*")?\s*\)|<img[^>]+src="([^"]+)"')

def exists_exact(path):
    """대소문자까지 일치하는지 (macOS 는 대소문자를 안 가려서 os.path.exists 만으로는 부족)"""
    path = os.path.normpath(path)
    if not os.path.exists(path): return False
    rel = os.path.relpath(path, ROOT)
    cur = ROOT
    for part in rel.split(os.sep):
        if part in (".", ""): continue
        if part not in os.listdir(cur): return False
        cur = os.path.join(cur, part)
    return True

bad = []
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if d not in (".git", ".obsidian", "node_modules")]
    for fn in fns:
        if not fn.endswith(".md"): continue
        p = os.path.join(dp, fn); fence = False
        for n, line in enumerate(open(p, encoding="utf-8", errors="ignore"), 1):
            if line.lstrip().startswith("```"): fence = not fence; continue
            if fence: continue
            line = re.sub(r'`[^`]*`', '', line)   # 인라인 코드 속 예시는 링크가 아니다
            for m in LINK.finditer(line):
                t = m.group(1) or m.group(2)
                if re.match(r"^(https?:|mailto:|#|data:|tel:)", t): continue
                t = urllib.parse.unquote(t.split("#")[0].split("?")[0])
                if not t: continue
                target = os.path.join(ROOT, t.lstrip("/")) if t.startswith("/") else os.path.join(dp, t)
                if not exists_exact(target):
                    bad.append(f"{os.path.relpath(p, ROOT)}:{n}: {t}")
print("\n".join(bad)); print(f"깨진 링크 {len(bad)}건", file=sys.stderr)
sys.exit(1 if bad else 0)
