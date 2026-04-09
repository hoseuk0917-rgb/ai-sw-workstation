# Codyssey 과제 자동 수집기

Codyssey AI 올인원 과정(2026.03.30 ~ 2027.09.30) 수강생들의 GitHub 레포에서 매주 과제 내용을 자동 수집하고, AI로 요약·정리하여 `reports/` 폴더에 마크다운 보고서로 저장합니다.

## 동작 방식

매주 **일요일 오후 9시(KST)** 에 GitHub Actions가 자동으로 실행됩니다. 수동으로 즉시 실행하려면 레포 상단 **Actions** 탭 → **Codyssey 주간 과제 수집** → **Run workflow** 버튼을 누르면 됩니다.

## 최신 보고서

[reports/latest.md](reports/latest.md)

## 초기 설정 방법 (최초 1회)

### OpenAI API 키 등록

GitHub 레포 → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| 이름 | 값 |
|------|----|
| `OPENAI_API_KEY` | OpenAI API 키 (`sk-...`) |

## 후보 수강생 관리

`collect.py` 파일 상단의 `CANDIDATES` 목록을 수정하면 추적 대상을 변경할 수 있습니다.

중도 포기자가 생기면 해당 항목의 `"active"` 값을 `False`로 변경하세요.

```python
{
    "username": "계정명",
    "display_name": "표시 이름",
    "active": False,  # ← 이렇게 변경
    ...
}
```

## 파일 구조

```
codyssey-tracker/
├── collect.py          # 수집 스크립트
├── README.md           # 이 파일
└── reports/
    ├── latest.md       # 가장 최근 보고서
    ├── 2026-04-13.md   # 날짜별 보고서
    └── 2026-04-13.json # 원본 데이터
```
