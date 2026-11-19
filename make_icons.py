"""PhotoCraft 명령줄로 봇 아이콘을 그린다 — 이 스크립트가 정본이고 icons/*.png 는 산출물이다.

고칠 때는 이 파일을 고쳐 다시 돌린다: python3 make_icons.py
PhotoCraft 위치가 다르면 PHOTOCRAFT_CLI 로 준다.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

CLI = os.environ.get("PHOTOCRAFT_CLI", "/Applications/PhotoCraft.app/Contents/MacOS/photocraft-cli")
OUT = Path(__file__).resolve().parent / "icons"
SIZE = 256  # 디스코드가 원으로 잘라 보인다 — 상징은 가운데 반지름 ~90px 안에 둔다
WHITE = "#ffffff"


def bg(top, bottom):
    return ("shape.create", {"kind": "rect", "rect": [0, 0, SIZE, SIZE], "name": "bg",
                             "fill": {"gradient": {"stops": [[0, top], [1, bottom]], "angle": -90, "style": "linear"}},
                             "stroke": None})


def path(name, knots, fill=WHITE, stroke=None, closed=True):
    return ("shape.create", {"kind": "path", "name": name, "fill": fill, "stroke": stroke,
                             "path": {"subpaths": [{"closed": closed, "knots": knots}]}})


def rrect(name, rect, radii, fill=WHITE):
    return ("shape.create", {"kind": "roundedRect", "name": name, "rect": rect, "radii": radii,
                             "fill": fill, "stroke": None})


SHADOW = ("layer.layerStyle.dropShadow", {"color": "#000000", "opacity": 30, "distance": 4, "size": 6, "angle": 90})

# 이름은 그림이 무엇인지로 짓는다 — 어느 봇이 쓰는지는 notify-hub 의 표가 정한다.
ICONS = {
    "page": [  # 접힌 귀퉁이 종이 + 글줄 — 새 글
        bg("#66bb6a", "#1b5e20"),
        path("sheet", [[84, 62], [150, 62], [176, 88], [176, 194], [84, 194]]), SHADOW,
        path("fold", [[150, 62], [150, 88], [176, 88]], fill="#c8e6c9"),
        rrect("line1", [100, 108, 60, 10], 5, fill="#2e7d32"),
        rrect("line2", [100, 130, 60, 10], 5, fill="#2e7d32"),
        rrect("line3", [100, 152, 38, 10], 5, fill="#2e7d32"),
    ],
    "calendar": [  # 달력 + 체크 — 하루 요약
        bg("#42a5f5", "#0d47a1"),
        rrect("body", [66, 76, 124, 114], 14), SHADOW,
        rrect("header", [66, 76, 124, 32], [14, 14, 0, 0], fill="#1565c0"),
        rrect("ring1", [92, 62, 14, 30], 7),
        rrect("ring2", [150, 62, 14, 30], 7),
        path("check", [[100, 148], [120, 168], [158, 126]], fill=None, closed=False,
             stroke={"width": 14, "color": "#1565c0", "cap": "round", "join": "round", "align": "center"}),
    ],
    "chart": [  # 오르는 막대 — 통계 보고
        bg("#ffa726", "#e65100"),
        rrect("bar1", [74, 138, 28, 48], 6), SHADOW,
        rrect("bar2", [114, 108, 28, 78], 6), SHADOW,
        rrect("bar3", [154, 74, 28, 112], 6), SHADOW,
        rrect("base", [64, 190, 128, 8], 4),
    ],
    "house": [  # 집 — 집 구하기
        bg("#ab47bc", "#4a148c"),
        path("house", [[128, 60], [200, 124], [180, 124], [180, 194], [76, 194], [76, 124], [56, 124]]), SHADOW,
        rrect("door", [114, 148, 28, 46], [10, 10, 0, 0], fill="#6a1b9a"),
        rrect("window", [146, 136, 20, 20], 4, fill="#6a1b9a"),
    ],
}


def main() -> int:
    if not Path(CLI).is_file():
        print(f"PhotoCraft 명령줄이 없다: {CLI} — PHOTOCRAFT_CLI 로 자리를 준다", file=sys.stderr)
        return 1
    OUT.mkdir(exist_ok=True)
    for name, steps in ICONS.items():
        args = [CLI, "run", "--new", json.dumps({"width": SIZE, "height": SIZE, "background": "transparent"})]
        for cmd, params in steps:
            args += ["--cmd", cmd, "--params", json.dumps(params)]
        args += ["--out", str(OUT / f"{name}.png")]
        r = subprocess.run(args, capture_output=True, text=True)
        if r.returncode != 0:
            print(f"{name} 실패 ({r.returncode}):\n{r.stderr}", file=sys.stderr)
            return 1
        print(f"{name}.png {(OUT / f'{name}.png').stat().st_size} B")
    return 0


if __name__ == "__main__":
    sys.exit(main())
