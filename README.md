# bot-icons

알림 봇이 쓰는 아이콘 묶음. 디스코드 웹후크의 `avatar_url` 이 공개 주소만 받아서 이 저장소를 공개로 둔다.

| 파일 | 그림 |
|---|---|
| `icons/page.png` | 초록 · 접힌 종이와 글줄 |
| `icons/calendar.png` | 파랑 · 달력과 체크 |
| `icons/chart.png` | 주황 · 오르는 막대 |
| `icons/shield.png` | 청록 · 방패와 체크 |
| `icons/house.png` | 보라 · 집 |

- **정본은 [make_icons.py](make_icons.py)** 다. PNG 는 산출물이라 손으로 고치지 않는다 — 스크립트를 고쳐 `python3 make_icons.py` 로 다시 그린다(PhotoCraft 0.21.0 명령줄 · 256×256).
- 같은 기기에서 두 번 그린 결과는 sha256 이 같았다(2026-11-20).
- 어느 봇이 어느 그림을 쓰는지는 이 저장소가 아니라 쓰는 쪽(notify-hub)이 정한다.
- 그림을 바꾸면 디스코드가 옛 그림을 붙잡고 있을 수 있다 — 쓰는 쪽 주소에 `?v=<번호>` 를 올린다.
