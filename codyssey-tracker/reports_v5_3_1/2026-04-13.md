# Codyssey registry-backed collection report v5.3.1 (2026-04-13)

- 총 수집 건수: 37건
- candidate pool size: 39
- 2026 본과정 확정: 32건
- 제외된 레거시/파일럿: 1건
- 후보/검토 필요: 4건
- active watchlist size: 2
- archived candidate size: 2
- discovered candidate size: 0
- overwrite-suspected repos: 37
- signature version: v5.3.1
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

# AI/SW 개발 워크스테이션 구축: Codyssey 1주차 미션 종합 학습 문서

## 1. 미션 개요

본 미션은 AI/SW 개발 환경의 필수 요소인 **터미널(CLI), Docker, Git/GitHub**를 활용하여 **재현 가능한 개발 워크스테이션**을 구축하고, 그 과정을 이해하고 실습하는 것을 목표로 합니다. "내 컴퓨터에서만 돌아가는" 개발 환경의 한계를 극복하고, 협업 및 배포 효율성을 높이기 위한 기초를 다지는 과정입니다.

## 2. 학습 목표

*   **터미널(CLI) 활용 능력 향상:** 파일 및 디렉토리 관리, 권한 설정 등 기본적인 터미널 명령어를 숙달합니다.
*   **Docker 기본 개념 이해 및 실습:** Docker 설치, 이미지 빌드, 컨테이너 실행 및 관리, 볼륨 및 마운트 활용 방법을 익힙니다.
*   **Dockerfile 작성 및 활용:** 간단한 웹 서버 이미지를 Dockerfile로 빌드하는 경험을 합니다.
*   **Git/GitHub 기초 활용:** Git 설정 및 VSCode 연동을 통해 버전 관리의 중요성을 이해합니다.
*   **재현 가능한 개발 환경 구축의 중요성 인지:** 개발 워크스테이션 구축 과정을 통해 동일한 환경을 만드는 것의 이점을 학습합니다.

## 3. 기능 요구사항

1.  **터미널 기본 조작:**
    *   `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm` 명령어 활용
    *   숨김 파일 포함 목록 확인 (`ls -alh`)
    *   디렉토리 생성, 파일 생성, 내용 쓰기, 복사, 이동, 삭제
2.  **권한 변경:**
    *   `chmod` 명령어를 사용하여 파일/디렉토리 권한 변경 실습
3.  **Docker 기본 점검 및 활용:**
    *   Docker 설치 확인 (`docker version`)
    *   `hello-world` 컨테이너 실행
    *   `ubuntu` 컨테이너 실행 및 내부 접근 (`attach`, `exec` 차이 이해)
4.  **Dockerfile 기반 커스텀 이미지 제작:**
    *   Nginx 등 간단한 웹 서버를 위한 `Dockerfile` 작성
    *   `COPY` 명령어를 사용하여 웹 페이지 파일 복사
    *   `EXPOSE` 명령어로 포트 선언
    *   `docker build` 명령어로 이미지 빌드
5.  **컨테이너 실행 및 관리:**
    *   `docker run` 명령어로 컨테이너 실행
    *   **포트 매핑:** 로컬 포트와 컨테이너 포트 연결 (`-p` 옵션)
    *   **바인드 마운트:** 로컬 디렉토리를 컨테이너 디렉토리에 연결하여 실시간 변경 반영 확인 (`-v` 옵션)
    *   **볼륨:** 데이터 영속성 확보를 위한 Docker 볼륨 활용 (`-v` 또는 `docker volume create` 활용)
6.  **Git/GitHub 연동:**
    *   Git 사용자 설정 (`git config`)
    *   VSCode와 GitHub 연동 및 기본적인 Git 작업 (커밋, 푸시 등)

## 4. 핵심 기술 스택

*   **운영체제 (OS):** macOS (주로 사용됨)
*   **Shell:** bash, zsh (macOS 기본 쉘)
*   **Command Line Interface (CLI) Tools:** `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm`, `chmod`
*   **Containerization:** Docker
    *   Dockerfile
    *   `docker build`, `docker run`, `docker ps`, `docker logs`, `docker exec` 등
*   **Version Control:** Git, GitHub
*   **IDE/Editor:** Visual Studio Code (VSCode)

## 5. 권장 프로젝트 구조

수강생들의 레포지토리를 기반으로 다음과 같은 구조를 권장합니다.

```
your-repo-name/
├── README.md         # 프로젝트 설명, 학습 내용 정리
├── Dockerfile        # 커스텀 Docker 이미지 빌드를 위한 설정 파일
├── docker-compose.yml  # (선택 사항, 더 복잡한 환경 구성을 위해)
├── app/ (또는 workstation/, src/)
│   ├── index.html    # 웹 서버에서 제공할 간단한 HTML 파일
│   └── ...           # 기타 필요한 파일
├── screenshots/      # (선택 사항) 실습 과정을 담은 스크린샷
└── practice/         # (선택 사항) 터미널 명령어 실습을 위한 파일/디렉토리
```

*   `README.md`에는 프로젝트 개요, 학습 목표, 기능 요구사항, 각 단계별 수행 내용, 트러블슈팅 및 팁 등을 상세히 기록하는 것이 좋습니다.
*   `Dockerfile`은 웹 서버 이미지를 빌드하는 핵심 파일입니다.
*   `app/` 또는 `src/`와 같은 디렉토리에 웹 페이지 콘텐츠를 넣어 `Dockerfile`에서 복사하도록 구성합니다.

## 6. 구현 핵심 포인트

### 6.1 터미널 기본 조작 및 권한

*   **절대 경로 vs 상대 경로:** `pwd` 명령어로 현재 위치를 확인하고, `cd` 명령어로 디렉토리를 이동하며 절대 경로와 상대 경로의 차이를 이해해야 합니다.
*   **`ls -alh`:** 숨김 파일(점으로 시작하는 파일)을 포함하여 모든 파일 및 디렉토리의 상세 정보를 확인하는 데 유용합니다.
*   **`chmod`:** 파일의 소유자, 그룹, 기타 사용자별로 읽기(r), 쓰기(w), 실행(x) 권한을 설정합니다. 숫자(예: `755`) 또는 기호(예: `u+x`)로 표현할 수 있습니다. 실행 가능한 스크립트 파일(`.sh`)의 경우 `chmod +x` 또는 `chmod 755` 등을 통해 실행 권한을 부여해야 합니다.

### 6.2 Dockerfile 작성

*   **`FROM`:** 어떤 베이스 이미지를 사용할지 지정합니다. (예: `nginx:latest`, `nginx:alpine`)
*   **`COPY`:** 로컬 디렉토리의 파일을 Docker 이미지 안의 특정 경로로 복사합니다. (예: `COPY index.html /usr/share/nginx/html/`)
*   **`EXPOSE`:** 컨테이너가 어떤 포트를 사용할 것인지 명시합니다. 이는 실제 포트 연결을 하는 것이 아니라, 컨테이너가 해당 포트에서 서비스를 제공한다는 정보를 기록하는 것입니다.

### 6.3 Docker 컨테이너 실행 및 옵션 활용

*   **`docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`**
*   **`-d` (Detached mode):** 컨테이너를 백그라운드에서 실행합니다.
*   **`-p HOST_PORT:CONTAINER_PORT` (Port mapping):** 로컬 머신의 `HOST_PORT`를 컨테이너 내부의 `CONTAINER_PORT`에 연결합니다. 웹 서버 접속에 필수적입니다. (예: `-p 8080:80`)
*   **`-v HOST_PATH:CONTAINER_PATH` (Bind mount):** 로컬 머신의 `HOST_PATH` 디렉토리를 컨테이너 내부의 `CONTAINER_PATH` 디렉토리로 마운트합니다. 로컬에서 파일을 수정하면 컨테이너 내에서도 즉시 반영됩니다. (예: `-v $(pwd)/app:/usr/share/nginx/html`)
*   **`-v VOLUME_NAME:CONTAINER_PATH` (Volume):** Docker 볼륨을 사용하여 데이터를 영속적으로 저장합니다. 컨테이너가 삭제되어도 볼륨의 데이터는 유지됩니다. (예: `-v my-data:/var/lib/nginx`)
*   **`--name CONTAINER_NAME`:** 컨테이너에 이름을 지정하여 관리하기 용이하게 합니다.
*   **`docker exec -it CONTAINER_ID /bin/bash`:** 실행 중인 컨테이너 내부에 접속하여 명령어를 실행합니다. (`-it`는 interactive terminal을 의미합니다.)
*   **`docker attach CONTAINER_ID`:** 컨테이너의 메인 프로세스 STDOUT/STDERR에 연결합니다. `exec`와 달리 컨테이너를 종료할 수 있습니다.

### 6.4 Git/GitHub 연동

*   **`git config --global user.name "Your Name"`**
*   **`git config --global user.email "your.email@example.com"`**
*   VSCode의 Source Control 탭을 통해 변경 사항 확인, 커밋, 푸시 등의 기본적인 Git 작업을 수행합니다.

## 7. 트러블슈팅 & 팁

*   **`echo` 명령어 사용 시 특수 문자 문제:** `echo "hello"`와 같이 큰따옴표(`"`) 안에 특수 문자(예: `!`)가 포함되면 쉘이 히스토리 확장 등으로 잘못 해석할 수 있습니다. 이럴 때는 작은따옴표(`'`)를 사용하거나 백슬래시(`\`)로 이스케이프 처리해야 합니다. (예: `echo 'hello!' > file.txt` 또는 `echo hello\! > file.txt`)
*   **`docker run` 시 포트 충돌:** 이미 사용 중인 로컬 포트를 `docker run -p` 옵션으로 사용하려고 하면 오류가 발생합니다. 다른 포트로 변경하여 시도해야 합니다. (예: `-p 8081:80`)
*   **바인드 마운트 경로 문제:** 로컬 경로가 잘못되었거나 권한 문제가 있을 수 있습니다. `$(pwd)`를 사용하여 현재 작업 디렉토리를 기준으로 마운트 경로를 정확히 지정하는 것이 좋습니다.
*   **Dockerfile `COPY` 시 경로:** `Dockerfile` 내의 `COPY` 명령어는 `Dockerfile`이 위치한 디렉토리를 기준으로 상대 경로를 사용합니다.
*   **VSCode GitHub 연동 시 인증 문제:** GitHub 계정 정보나 Personal Access Token(PAT) 설정에 문제가 있을 수 있습니다. VSCode의 GitHub Extension 관련 문서를 참고하여 설정해야 합니다.
*   **`attach` vs `exec`:**
    *   `attach`: 컨테이너의 메인 프로세스에 연결하여 **STDOUT/STDERR를 함께 보고 제어**합니다. 주로 컨테이너가 실행될 때 출력되는 로그를 보거나, 컨테이너의 메인 프로세스를 제어할 때 사용합니다. Ctrl+C 등으로 컨테이너를 종료할 수 있습니다.
    *   `exec`: 컨테이너 내부에서 **새로운 명령어를 실행**합니다. 컨테이너의 메인 프로세스에는 영향을 주지 않으며, 컨테이너 내부에서 임시로 작업을 수행할 때 유용합니다. (예: `docker exec -it <container_id> bash`)

## 8. 추가 학습 자료

*   **터미널 명령어:**
    *   [Linux Command Line Basics](https://www.youtube.com/playlist?list=PLT32y30rK3a-8HwT0I94e1Pz1t0-8QkXg) (YouTube)
    *   [The Linux Command Line Book](https://www.gitbook.com/book/commandlinefu/the-linux-command-line/details) (e-book)
*   **Docker:**
    *   [Docker Documentation](https://docs.docker.com/) (공식 문서)
    *   [Docker Get Started Tutorial](https://docs.docker.com/get-started/)
    *   [Inflearn - 도커/쿠버네티스를 활용한 실전 인프라 구축](https://www.inflearn.com/course/%EB%8F%84%EC%BB%A4-%EC%BF%B8%EB%B2%84%EB%84%88%ED%8B%B0%EC%8A%A4-%EC%8B%A4%EC%A0%84) (유료 강의 예시)
*   **Git/GitHub:**
    *   [Pro Git book](https://git-scm.com/book/en/v2) (공식 Git 핸드북)
    *   [GitHub Docs](https://docs.github.com/en)
    *   [ 생활코딩 - Git & GitHub](https://opentutorials.org/course/1765/10020)

본 문서를 통해 1주차 미션의 핵심 내용을 명확히 이해하고, 성공적으로 워크스테이션을 구축하시길 바랍니다. 추가적으로 궁금한 점이나 어려운 부분은 각 수강생의 GitHub 레포지토리와 README를 참고하거나, 제공된 추가 학습 자료를 활용하여 깊이 학습해나가세요.

| 수강생 | 레포 | 업데이트 | 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week1](https://github.com/kimch0612/Codyssey_Week1) | 2026-03-31 | tier2:Dockerfile, week-readme:docker, readme:docker |
| sonjehyun123-maker | [Codyssey-w1-E1](https://github.com/sonjehyun123-maker/Codyssey-w1-E1) | 2026-04-03 | tier2:Dockerfile, week-readme:docker, readme:docker |
| mulloc1 | [codyssey_workstation](https://github.com/mulloc1/codyssey_workstation) | 2026-03-31 | tier2:Dockerfile, week-repo:workstation, week-readme:docker, repo:workstation |
| ntt65 | [codyssey/e1_1](https://github.com/ntt65/codyssey/tree/main/e1_1) | 2026-04-12 | tier2:Dockerfile, week-readme:docker, readme:docker |
| codewhite7777 | [codyssey_E-1](https://github.com/codewhite7777/codyssey_E-1) | 2026-03-30 | tier2:Dockerfile, week-readme:workstation, week-readme:docker, readme:workstation |
| mov-hyun | [e1-1-workstation-setup](https://github.com/mov-hyun/e1-1-workstation-setup) | 2026-04-05 | tier2:Dockerfile, week-repo:workstation, week-readme:docker, repo:workstation |
| jhkr1 | [Codyssey_mission1](https://github.com/jhkr1/Codyssey_mission1) | 2026-04-07 | tier2:Dockerfile, week-readme:workstation, week-readme:docker, readme:workstation |
| junhnno | [Codyssey_WorkSpace_Week1](https://github.com/junhnno/Codyssey_WorkSpace_Week1) | 2026-04-09 | tier2:Dockerfile, week-readme:docker, readme:docker |
| yejoo0310 | [codyssey-m1](https://github.com/yejoo0310/codyssey-m1) | 2026-04-05 | tier2:Dockerfile, week-readme:docker, readme:docker |
| clae-dev | [ia-codyssey-Docker](https://github.com/clae-dev/ia-codyssey-Docker) | 2026-04-02 | tier2:Dockerfile, week-repo:docker, repo:docker |
| leehnmn | [codyssey_2026/project-1](https://github.com/leehnmn/codyssey_2026/tree/main/project-1) | 2026-04-08 | tier2:Dockerfile, week-readme:docker, readme:docker |
| I-nkamanda | [codyssey2026/Problem1_AI_SW_Setup](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem1_AI_SW_Setup) | 2026-04-09 | tier2:Dockerfile, week-readme:docker, week-repo:setup, readme:docker |
| peachily | [codyssey11-E1](https://github.com/peachily/codyssey11-E1) | 2026-04-09 | rule:v5_1_e1_docker_promote, repo:codyssey, tier2:main.py, tier2:Dockerfile |
| ikasoon | [codyssey-e1-1](https://github.com/ikasoon/codyssey-e1-1) | 2026-04-06 | tier2:Dockerfile, week-readme:workstation, week-readme:docker, readme:workstation |

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


| 수강생 | 레포 | 업데이트 | 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-10 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-12 | tier1:quiz_game.py, week-repo:quiz, week-readme:quiz_game, repo:quiz |
| yeowon083 | [quiz-game](https://github.com/yeowon083/quiz-game) | 2026-04-12 | tier2:main.py, tier2:state.json, week-repo:quiz, week-readme:state.json |
| jhkr1 | [Codyssey_mission2](https://github.com/jhkr1/Codyssey_mission2) | 2026-04-11 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| junhnno | [Codyssey_WorkSpace_Week2](https://github.com/junhnno/Codyssey_WorkSpace_Week2) | 2026-04-11 | rule:v5_1_week2_workspace_promote, week-readme:quiz, week-readme:state.json, repo:codyssey |
| yejoo0310 | [codyssey-m2](https://github.com/yejoo0310/codyssey-m2) | 2026-04-10 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| yejibaek12 | [Python-Quiz-Game](https://github.com/yejibaek12/Python-Quiz-Game) | 2026-04-11 | tier2:main.py, tier2:state.json, week-repo:quiz, week-readme:state.json |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| leehnmn | [codyssey_2026/project-2](https://github.com/leehnmn/codyssey_2026/tree/main/project-2) | 2026-04-08 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-09 | rule:v5_1_python_with_git_promote, week-repo:python_with_git, week-readme:state.json, repo:codyssey |

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

| 수강생 | 레포 | 업데이트 | 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-12 | tier1:data.json, tier2:main.py, week-repo:npu, week-readme:mac |
| jhkr1 | [Codyssey_mission3](https://github.com/jhkr1/Codyssey_mission3) | 2026-04-11 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| yejoo0310 | [codyssey-m3](https://github.com/yejoo0310/codyssey-m3) | 2026-04-12 | tier1:mini_npu_simulator.py, tier2:main.py |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-09 | week-repo:npu, week-repo:npu_simulator, week-repo:mini_npu, repo:npu |

---

## 2. 동일 레포 덮어쓰기/변조 의심 정리

| 레포 키 | 이전 주차 | 현재 주차 | 이전 상태 | 현재 상태 | 업데이트 변경 | 서명 변경 |
| --- | --- | --- | --- | --- | --- | --- |
| kimch0612/Codyssey_Week3 | 3 | 3 | confirmed | confirmed | N | Y |
| kimch0612/Codyssey_Week2 | 2 | 2 | confirmed | confirmed | N | Y |
| kimch0612/Codyssey_Week1 | 1 | 1 | confirmed | confirmed | N | Y |
| sonjehyun123-maker/Codyssey-w1-E2 | 2 | 2 | confirmed | confirmed | N | Y |
| sonjehyun123-maker/Codyssey-w1-E1 | 1 | 1 | confirmed | confirmed | N | Y |
| mulloc1/codyssey_python_with_npu | 3 | 3 | confirmed | confirmed | N | Y |
| mulloc1/codyssey_first_python | 2 | 2 | confirmed | confirmed | N | Y |
| mulloc1/codyssey_workstation | 1 | 1 | confirmed | confirmed | N | Y |
| ntt65/codyssey/e1_1 | 1 | 1 | confirmed | confirmed | N | Y |
| ntt65/codyssey/e1_2 | 2 | 2 | candidate | candidate | N | Y |
| codewhite7777/codyssey_E1-3 | 1 | 1 | candidate | candidate | N | Y |
| codewhite7777/codyssey_E-2 | 2 | 2 | confirmed | confirmed | N | Y |
| codewhite7777/codyssey_E-1 | 1 | 1 | confirmed | confirmed | N | Y |
| mov-hyun/e1-2-python-basics-quiz-game | 2 | 2 | confirmed | confirmed | N | Y |
| mov-hyun/e1-1-workstation-setup | 1 | 1 | confirmed | confirmed | N | Y |
| yeowon083/quiz-game | 2 | 2 | confirmed | confirmed | N | Y |
| jhkr1/Codyssey_mission3 | 3 | 3 | confirmed | confirmed | N | Y |
| jhkr1/Codyssey_mission2 | 2 | 2 | confirmed | confirmed | N | Y |
| jhkr1/Codyssey_mission1 | 1 | 1 | confirmed | confirmed | N | Y |
| junhnno/Codyssey_WorkSpace_Week2 | 2 | 2 | confirmed | confirmed | N | Y |
| junhnno/Codyssey_WorkSpace_Week1 | 1 | 1 | confirmed | confirmed | N | Y |
| sungho255/codyssey_2 | 2 | 2 | candidate | candidate | N | Y |
| sungho255/codyssey_1 | 1 | 1 | candidate | candidate | N | Y |
| yejoo0310/codyssey-m3 | 3 | 3 | confirmed | confirmed | N | Y |
| yejoo0310/codyssey-m2 | 2 | 2 | confirmed | confirmed | N | Y |
| yejoo0310/codyssey-m1 | 1 | 1 | confirmed | confirmed | N | Y |
| yejibaek12/Python-Quiz-Game | 2 | 2 | confirmed | confirmed | N | Y |
| clae-dev/ia-codyssey-Python | 2 | 2 | confirmed | confirmed | N | Y |
| clae-dev/ia-codyssey-Docker | 1 | 1 | confirmed | confirmed | N | Y |
| leehnmn/codyssey_2026/project-1 | 1 | 1 | confirmed | confirmed | N | Y |
| leehnmn/codyssey_2026/project-2 | 2 | 2 | confirmed | confirmed | N | Y |
| peachily/codyssey11-E1 | 1 | 1 | confirmed | confirmed | N | Y |
| I-nkamanda/codyssey2026/Problem1_AI_SW_Setup | 1 | 1 | confirmed | confirmed | N | Y |
| I-nkamanda/codyssey2026/Problem2_Python_with_git | 2 | 2 | confirmed | confirmed | N | Y |
| I-nkamanda/codyssey2026/Problem3_Mini_NPU_Simulator | 3 | 3 | confirmed | confirmed | N | Y |
| ikasoon/codyssey-e1-1 | 1 | 1 | confirmed | confirmed | N | Y |
| doji-kr/codyssey_day1_bear1 | 1 | 1 | excluded | excluded | N | Y |

## 3. 후보/검토 레포 (active watchlist)

### 미분류

| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |
| --- | --- | --- | --- | --- |
| ntt65 | [codyssey/e1_2](https://github.com/ntt65/codyssey/tree/main/e1_2) | 2026-04-12 | 0.25 | repo:codyssey, tier2:main.py |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | 0.25 | repo:codyssey, readme:npu, readme:mac, tier2:main.py |
| sungho255 | [codyssey_2](https://github.com/sungho255/codyssey_2) | 2026-04-07 | 0.25 | repo:codyssey, tier2:state.json |
| sungho255 | [codyssey_1](https://github.com/sungho255/codyssey_1) | 2026-04-07 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, readme:mac |

## 4. 후보풀 청소 요약

- active watch 유지 개수: 2
- archive로 이동한 누적 후보 개수: 2
- discovered 후보 누적 개수: 0

## 5. 제외된 레거시/파일럿 레포

| 수강생 | 레포 | 업데이트 | 제외 근거 |
| --- | --- | --- | --- |
| doji-kr | [codyssey_day1_bear1](https://github.com/doji-kr/codyssey_day1_bear1) | 2025-07-11 | updated_at:2025-07-11, rule:legacy-hard-cutoff |
