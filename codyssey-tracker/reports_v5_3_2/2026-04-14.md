# Codyssey registry-backed collection report v5.3.2 (2026-04-14)

- 총 수집 건수: 38건
- candidate pool size: 39
- 2026 본과정 확정: 33건
- 제외된 레거시/파일럿: 1건
- active watchlist items shown: 4건
- active watchlist size: 4
- archived candidate size: 2
- discovered candidate size: 0
- overwrite-suspected repos: 0
- signature version: v5.3.1
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

# codyssey-m1
코디세이 AI 올인원 입학연수과정 미션1

### 1. 프로젝트 개요
이 프로젝트의 목표는 터미널, Docker, Git/GitHub를 활용하여 재현 가능한 개발 워크스테이션 환경을 구성하고, 그 과정을 문서로 정리하는 것이다. 터미널을 이용해 작업 디렉토리와 권한을 부여하고, Docker를 설치 및 점검한 뒤 컨테이너를 실행 및 관리한다. 또한 Dockerfile을 기반으로 간단한 웹 서버 이미지를 제작하고, 포트 매핑으로 접속을 확인하며 바인드 마운트와 볼륨을 사용해 변경 반영과 데이터 영속성을 확인한다.

### 2. 실행 환경
- OS: macOS
- Shell: bash
- Docker: 28.3.2
- Git: 2.45.2

### 3. 수행 항목 체크리스트
- [x] 터미널 기본 조작 및 폴더 구성
- [x] 권한 변경 실습
- [x] Docker 설치/점검
- [x] hello-world 실행
- [x] ubuntu 실행
- [x] attach, exec 차이 실습
- [x] 기존 Dockerfile 기반 커스텀 이미지 제작
- [x] 포트 매핑 접속
- [x] 바인드 마운트 반영
- [x] 볼륨 영속성
- [x] Git 설정 + VSCode GitHub 연동
- [x] 트러블슈팅 정리

### 4. 터미널 조작 로그 기록

#### 1) 현재 위치 확인
현재 작업 중인 디렉토리의 절대 경로를 확인할 수 있음
```
➜  codyssey-m1 git:(main) pwd
/Users/kim-yejoo/Codyssey-2026/codyssey-m1
```
절대 경로와 상대 경로의 차이
- 파일의 위치를 찾을 때 기준점이 어디냐에 따라 절대 경로와 상대 경로가 구분됨
- 절대 경로는 파일 시스템의 루트부터 시작해서 특정 파일이나 디렉토리에 도달하는 전체 경로로 어디서 실행하든 항상 같은 파일을 가리킨다. 어느 곳에서든 경로에 접근할 수 있다는 장점이 있지만 경로가 변경되면 경로를 일일히 수정해야 한다는 불편함이 있다.
- 상대 경로는 현재 내가 위치한 디렉토리를 기준으로 파일 위치를 표현한다. 디렉토리 위치나 주소가 바뀌어도 내부 구조만 그대로라면 수정없이 그대로 사용할 수 있다는 장점이 있다.
- 절대 경로는 외부 파일을 참조할 때 주로 사용하고, 상대 경로는 내부 파일을 연결할 때 주로 사용한다.

#### 2) 목록 확인(숨김 파일 포함)
현재 위치나 특정 디렉토리의 리스트를 출력
```
➜  codyssey-m1 git:(main) ✗ ls -alh
total 8
drwxr-xr-x   4 kim-yejoo  staff   128B Mar 31 17:24 .
drwxr-xr-x   3 kim-yejoo  staff    96B Mar 31 17:24 ..
drwxr-xr-x  13 kim-yejoo  staff   416B Apr  1 09:16 .git
-rw-r--r--   1 kim-yejoo  staff   1.5K Apr  1 09:26 README.md
```
```
➜  codyssey-m1 git:(main) ✗ ls -alh ../
total 0
drwxr-xr-x    3 kim-yejoo  staff    96B Mar 31 17:24 .
drwxr-x---+ 110 kim-yejoo  staff   3.4K Apr  1 10:18 ..
drwxr-xr-x    6 kim-yejoo  staff   192B Apr  1 09:41 codyssey-m1
```
옵션
- `-a`: all의 줄임말로, 숨김 파일 및 디렉토리를 포함한 모든 파일을 출력
- `-l`: long의 줄임말로, 파일 출력 형식을 긴 목록 형식으로 출력 (파일 타입, 권한, 소유자, 그룹, 파일 크기, 수정시간 등)
 - `-h`: human의 줄임말로, 사용자가 보기 좋은 형태의 단위로 출력
  
#### 3) 이동
현재 작업 중인 디렉토리 위치를 변경
```
➜  codyssey-m1 git:(main) ✗ pwd
/Users/kim-yejoo/Codyssey-2026/codysse

_*(API 키 없음 — 원문 일부)*_

| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 판정 증거 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week1](https://github.com/kimch0612/Codyssey_Week1) | 2026-03-31 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:docker, readme:docker, tier2:Dockerfile |
| sonjehyun123-maker | [Codyssey-w1-E1](https://github.com/sonjehyun123-maker/Codyssey-w1-E1) | 2026-04-03 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:docker, readme:docker, tier2:Dockerfile |
| mulloc1 | [codyssey_workstation](https://github.com/mulloc1/codyssey_workstation) | 2026-03-31 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-repo:workstation, week-readme:docker, repo:workstation |
| ntt65 | [codyssey/e1_1](https://github.com/ntt65/codyssey/tree/main/e1_1) | 2026-04-12 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:docker, readme:docker, tier2:Dockerfile |
| codewhite7777 | [codyssey_E-1](https://github.com/codewhite7777/codyssey_E-1) | 2026-03-30 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:workstation, week-readme:docker, readme:workstation |
| mov-hyun | [e1-1-workstation-setup](https://github.com/mov-hyun/e1-1-workstation-setup) | 2026-04-05 | cohort_2026_current | admission_bootcamp | 1 | 0.00 | tier2:Dockerfile, week-repo:workstation, week-readme:docker, repo:workstation |
| jhkr1 | [Codyssey_mission1](https://github.com/jhkr1/Codyssey_mission1) | 2026-04-07 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:workstation, week-readme:docker, readme:workstation |
| junhnno | [Codyssey_WorkSpace_Week1](https://github.com/junhnno/Codyssey_WorkSpace_Week1) | 2026-04-09 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:docker, readme:docker, tier2:Dockerfile |
| yejoo0310 | [codyssey-m1](https://github.com/yejoo0310/codyssey-m1) | 2026-04-05 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:docker, readme:docker, tier2:Dockerfile |
| clae-dev | [ia-codyssey-Docker](https://github.com/clae-dev/ia-codyssey-Docker) | 2026-04-02 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-repo:docker, repo:docker, tier2:Dockerfile |
| leehnmn | [codyssey_2026/project-1](https://github.com/leehnmn/codyssey_2026/tree/main/project-1) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:docker, readme:docker, tier2:Dockerfile |
| I-nkamanda | [codyssey2026/Problem1_AI_SW_Setup](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem1_AI_SW_Setup) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:docker, week-repo:setup, readme:docker |
| peachily | [codyssey11-E1](https://github.com/peachily/codyssey11-E1) | 2026-04-13 | - | - | 1 | 0.00 | rule:v5_1_e1_docker_promote, tier2:main.py, tier2:Dockerfile, repo:codyssey |
| ikasoon | [codyssey-e1-1](https://github.com/ikasoon/codyssey-e1-1) | 2026-04-06 | cohort_2026_current | admission_bootcamp | 1 | 0.04 | tier2:Dockerfile, week-readme:workstation, week-readme:docker, readme:workstation |

---

### 2주차

# 나만의 퀴즈 게임

## 1. 프로젝트 개요

이 프로젝트는 Python으로 만든 콘솔 기반 퀴즈 게임이다.  
사용자는 메뉴를 통해 퀴즈를 풀고, 새로운 퀴즈를 추가하고, 등록된 퀴즈 목록을 확인하고, 최고 점수를 확인하고, 퀴즈를 삭제할 수 있다.  
프로그램을 종료해도 퀴즈와 최고 점수가 유지되도록 프로젝트 루트의 `state.json` 파일에 데이터를 저장한다.

이 README는 단순한 소개 문서가 아니라, 이 과제를 통해 배운 내용을 정리한 기록서다.  
따라서 "무엇을 만들었는가"만 적지 않고, "왜 이렇게 구현했는가", "이 구현으로 어떤 결과가 나오는가", "이 과정에서 어떤 Python 개념을 이해하게 되었는가"까지 함께 기록한다.

## 2. 퀴즈 주제 선정 이유

퀴즈 주제는 `Python 기초 문법`이다.

이 주제를 선택한 이유는 다음과 같다.

- 프로젝트를 구현하면서 동시에 Python 핵심 개념을 복습할 수 있다.
- 변수, 조건문, 반복문, 함수, 클래스 같은 기본 개념을 문제로 다시 정리할 수 있다.
- 학습이 진행될수록 새로운 퀴즈를 직접 추가하며 프로젝트를 확장하기 쉽다.
- "프로그램을 만들면서 언어를 배운다"는 미션 의도와 가장 잘 맞는다.

## 3. 실행 방법

### 3-1. 실행 환경

- Python 3.10 이상 권장
- 외부 라이브러리 없이 표준 라이브러리만 사용

### 3-2. 실행 명령어

```bash
python3 main.py
```

## 4. 기능 목록

- 메인 메뉴 출력
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- 퀴즈 삭제
- `state.json` 저장 및 불러오기
- 잘못된 입력 처리
- `KeyboardInterrupt`, `EOFError` 안전 종료

## 5. 파일 구조

```text
Codyssey_mission2/
├── main.py
├── README.md
├── state.json
├── docs/
│   └── screenshots/
└── quiz_app/
    ├── __init__.py
    ├── game.py
    └── models.py
```

## 6. 코드 구조를 이렇게 잡은 이유

이번 버전은 코드 리뷰를 쉽게 하기 위해 구조를 일부러 단순하게 유지했다.  
클래스는 `Quiz`, `QuizGame` 두 개만 두고, 나머지 기능은 `QuizGame`의 메서드로 정리했다.

- `Quiz`: 문제 1개를 표현하는 클래스
- `QuizGame`: 메뉴, 입력 처리, 게임 진행, 저장/불러오기, 점수 갱신을 관리하는 클래스

이렇게 구성한 이유는 다음과 같다.

- 초보자가 읽을 때 파일을 너무 많이 넘나들지 않아도 된다.
- "문제 하나"와 "게임 전체"라는 책임 구분이 명확하다.
- 코드 리뷰 때 `main.py -> QuizGame.run() -> 각 기능 메서드` 순서로 설명하기 쉽다.
- 기능은 분리하되, 과도한 모듈 분리는 줄여서 전체 흐름을 놓치지 않게 했다.

즉 이 프로젝트의 목표는 "복잡하게 잘게 나누는 것"이 아니라, "흐름이 보이게 구조화하는 것"이다.

## 7. 프로그램 전체 흐름

프로그램은 아래 순서로 동작한다.

1. `main.py`가 실행된다.
2. `QuizGame()` 객체가 생성된다.
3. `QuizGame.__init__()` 안에서 `load_state()`가 호출된다.
4. `state.json`이 있으면 저장된 퀴즈와 점수를 불러온다.
5. 파일이 없거나 손상되었으면 기본 퀴즈 데이터로 복구한다.
6. `run()` 메서드가 메뉴를 반복해서 출력한다.
7. 사용자는 메뉴 번호를 입력한다.
8. 입력한 번호에 따라 퀴즈 풀기, 추가, 목록, 점수 확인, 삭제, 종료 기능이 실행된다.
9. 데이터가 바뀌면 `save_state()`가 현재 상태를 다시 `state.json`에 저장한다.

이 흐름을 기준으로 코드를 읽으면 프로그램 전체 동작이 훨씬 쉽게 보인다.

## 8. 핵심 클래스 설명

### 8-1. `Quiz` 클래스


_*(API 키 없음 — 원문 일부)*_

| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 판정 증거 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-10 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 2 | 0.00 | tier1:quiz_game.py, week-repo:quiz, week-readme:quiz_game, repo:quiz |
| yeowon083 | [quiz-game](https://github.com/yeowon083/quiz-game) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 2 | 0.00 | tier2:main.py, tier2:state.json, week-repo:quiz, week-readme:state.json |
| jhkr1 | [Codyssey_mission2](https://github.com/jhkr1/Codyssey_mission2) | 2026-04-11 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| junhnno | [Codyssey_WorkSpace_Week2](https://github.com/junhnno/Codyssey_WorkSpace_Week2) | 2026-04-11 | - | - | 2 | 0.00 | rule:v5_1_week2_workspace_promote, tier2:main.py, repo:codyssey, week-readme:quiz |
| yejoo0310 | [codyssey-m2](https://github.com/yejoo0310/codyssey-m2) | 2026-04-10 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| yejibaek12 | [Python-Quiz-Game](https://github.com/yejibaek12/Python-Quiz-Game) | 2026-04-13 | cohort_2026_current | admission_bootcamp | 2 | 0.00 | tier2:main.py, tier2:state.json, week-repo:quiz, week-readme:state.json |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| leehnmn | [codyssey_2026/project-2](https://github.com/leehnmn/codyssey_2026/tree/main/project-2) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 2 | 0.04 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-14 | - | - | 2 | 0.00 | rule:v5_1_python_with_git_promote, repo:codyssey, repo:python_with_git, week-repo:python_with_git |

---

### 3주차

# Mini NPU Simulator

이 프로젝트는 사람이 직관적으로 구별하는 `십자가(Cross)`와 `X` 패턴을 컴퓨터가 어떻게 숫자 연산으로 판별하는지 직접 구현해 보는 Python 콘솔 애플리케이션이다.  
핵심은 시각적 인식이 아니라 `2차원 배열`, `필터(Filter)`, `MAC(Multiply-Accumulate)` 연산, `라벨 정규화`, `부동소수점 비교 정책`, `시간 복잡도 분석`, 그리고 보너스 과제인 `1차원 배열 최적화`와 `패턴 자동 생성기`에 있다.

이 README는 단순 실행 가이드를 넘어서, 이번 미션을 학습용 한 권의 책처럼 다시 복습할 수 있도록 구성했다.

## 1. 프로젝트 목표

이 프로젝트를 끝내면 아래 내용을 스스로 설명할 수 있어야 한다.

1. MAC 연산이 무엇인지 설명할 수 있다.
2. 입력 패턴과 필터를 곱하고 더해 유사도를 구하는 원리를 설명할 수 있다.
3. `data.json`의 키 규칙과 라벨 규칙을 해석할 수 있다.
4. 왜 라벨 정규화가 필요한지 설명할 수 있다.
5. 왜 `epsilon` 기반 비교가 필요한지 설명할 수 있다.
6. 패턴 크기가 커질수록 연산량이 왜 `O(N^2)`로 증가하는지 설명할 수 있다.
7. 실패 케이스를 데이터 문제, 스키마 문제, 로직 문제, 수치 비교 문제로 나누어 진단할 수 있다.

## 2. 왜 컴퓨터는 모양을 그대로 이해하지 못할까?

사람은 아래 두 모양을 보면 거의 즉시 서로 다른 패턴이라고 인식한다.

```text
0 1 0      1 0 1
1 1 1      0 1 0
0 1 0      1 0 1
Cross      X
```

하지만 컴퓨터는 "십자가처럼 보인다", "대각선처럼 보인다" 같은 표현을 직접 이해하지 못한다.  
컴퓨터가 이해하는 것은 숫자와 메모리 위치뿐이다.  
따라서 모양을 판별하려면 먼저 그림을 숫자 배열로 바꾸고, 그 숫자 배열이 기준 패턴과 얼마나 비슷한지 수치로 계산해야 한다.

이때 등장하는 기준 패턴이 바로 `필터(Filter)`다.

## 3. 필터란 무엇인가?

필터는 "이런 모양이면 점수를 높게 주겠다"라는 기준표다.  
예를 들어 `Cross` 필터는 중심 가로줄과 중심 세로줄에 1이 있고, 나머지는 0이다.  
`X` 필터는 두 대각선 위치에 1이 있고, 나머지는 0이다.

즉, 필터는 사람이 가진 시각적 기준을 숫자 규칙으로 번역한 것이다.

## 4. MAC 연산의 핵심

MAC는 `Multiply-Accumulate`의 줄임말이다.

1. 입력 패턴과 필터의 같은 위치 값을 곱한다.
2. 그 결과를 누적해서 모두 더한다.
3. 최종 합계를 유사도 점수로 사용한다.

예를 들어 3x3 `Cross` 패턴에 `Cross` 필터를 적용하면 일치하는 위치에서 `1 x 1`이 많이 발생하므로 점수가 높다.  
반대로 `Cross` 패턴에 `X` 필터를 적용하면 같은 위치에서 동시에 1인 경우가 적어서 점수가 낮다.

수식으로 쓰면 다음과 같다.

```text
score = Σ(pattern[r][c] * filter[r][c])
```

여기서 `r`, `c`는 행과 열 인덱스다.

## 5. 왜 AI에서 MAC가 중요한가?

이번 미션의 예시는 3x3, 5x5, 13x13, 25x25 수준이지만 실제 AI 모델은 훨씬 큰 텐서와 훨씬 많은 필터를 사용한다.  
이미지 처리, 음성 처리, 자연어 처리 모두 결국 매우 많은 곱셈과 덧셈을 반복한다.  
그래서 AI 하드웨어는 복잡한 제어보다 `대량의 단순 반복 연산`을 빠르게 수행하는 데 최적화된다.

CPU는 범용 처리에 강하지만, 대량의 동일 연산을 한 번에 밀어붙이는 데는 상대적으로 비효율적일 수 있다.  
NPU는 이런 MAC 연산을 병렬로 빠르게 수행하기 위해 설계된 전용 장치다.

이번 프로젝트는 아주 작은 형태지만, 그 철학을 그대로 흉내 낸 `Mini NPU Simulator`라고 볼 수 있다.

## 6. 이번 과제를 구현하기 전에 꼭 알아야 할 개념

이번 과제는 단순히 "곱하고 더하는 코

_*(API 키 없음 — 원문 일부)*_

| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 판정 증거 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | cohort_2026_current | admission_bootcamp | 3 | 0.04 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-13 | cohort_2026_current | admission_bootcamp | 3 | 0.04 | tier1:data.json, tier2:main.py, week-repo:npu, week-readme:mac |
| mov-hyun | [e1-3-mini-npu-simulator](https://github.com/mov-hyun/e1-3-mini-npu-simulator) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 3 | 0.00 | tier1:data.json, tier2:main.py, week-repo:npu, week-readme:mac |
| jhkr1 | [Codyssey_mission3](https://github.com/jhkr1/Codyssey_mission3) | 2026-04-11 | cohort_2026_current | admission_bootcamp | 3 | 0.04 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| yejoo0310 | [codyssey-m3](https://github.com/yejoo0310/codyssey-m3) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 3 | 0.04 | tier1:mini_npu_simulator.py, tier2:main.py, tier1:mini_npu_simulator.py, tier1:data.json |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-14 | cohort_2026_current | admission_bootcamp | 3 | 0.04 | week-repo:npu, week-repo:npu_simulator, week-repo:mini_npu, repo:npu |

---

## 2. 동일 레포 덮어쓰기/변조 의심 정리

_이번 실행에서는 뚜렷한 덮어쓰기/변조 의심 레포가 없었습니다._

## 3. 후보/검토 레포 (actual active watchlist)

### unknown

| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 신뢰도 | 근거 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ntt65 | [codyssey/e1_2](https://github.com/ntt65/codyssey/tree/main/e1_2) | 2026-04-12 | unknown_watch | admission_bootcamp | 2 | 0.04 | 0.29 | tier2:main.py, repo:codyssey, repo:codyssey, tier2:main.py, continuity:repo-codyssey |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | unknown_watch | admission_bootcamp | 1 | 0.04 | 0.29 | tier2:main.py, repo:codyssey, repo:codyssey, readme:npu, readme:mac |
| sungho255 | [codyssey_2](https://github.com/sungho255/codyssey_2) | 2026-04-07 | unknown_watch | admission_bootcamp | 2 | 0.04 | 0.29 | tier2:state.json, repo:codyssey, repo:codyssey, tier2:state.json, continuity:repo-codyssey |
| sungho255 | [codyssey_1](https://github.com/sungho255/codyssey_1) | 2026-04-07 | unknown_watch | admission_bootcamp | 1 | 0.04 | 0.29 | repo:codyssey, week-readme:docker, repo:codyssey, readme:docker, readme:mac |

## 4. 후보풀 청소 요약

- active watch 유지 개수: 4
- archive로 이동한 누적 후보 개수: 2
- discovered 후보 누적 개수: 0

## 5. 제외된 레거시/파일럿 레포

| 수강생 | 레포 | 업데이트 | 제외 근거 |
| --- | --- | --- | --- |
| doji-kr | [codyssey_day1_bear1](https://github.com/doji-kr/codyssey_day1_bear1) | 2025-07-11 | updated_at:2025-07-11, rule:legacy-hard-cutoff, repo:codyssey |
