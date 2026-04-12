# Codyssey registry-backed collection report v5.3 (2026-04-13)

- 총 수집 건수: 37건
- candidate pool size: 39
- 2026 본과정 확정: 32건
- 제외된 레거시/파일럿: 1건
- 후보/검토 필요: 4건
- active watchlist size: 2
- archived candidate size: 2
- discovered candidate size: 0
- overwrite-suspected repos: 0
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

# Codyssey AI/SW 교육 과정 1주차 학습 문서: AI/SW 개발 워크스테이션 구축

## 1. 미션 개요

이번 1주차 미션은 AI/SW 개발자로서 필수적으로 갖춰야 할 기초 도구인 **터미널(CLI)**, **Docker(컨테이너)**, **Git/GitHub(버전 관리)**를 활용하여 **재현 가능한 개발 워크스테이션 환경**을 구축하는 것입니다.

"내 컴퓨터에서만 동작하는" 코드를 넘어, 어떤 환경에서도 동일하게 실행 및 배포, 디버깅이 가능한 환경을 구성하고, 그 과정을 체계적으로 문서화하는 것을 목표로 합니다.

## 2. 학습 목표

*   **터미널(CLI) 활용 능력 향상:** 파일 및 디렉토리 관리, 권한 설정 등 기본적인 터미널 명령어 사용법을 익힙니다.
*   **Docker 기본 이해 및 활용:** Docker 설치, 이미지 및 컨테이너 생성/관리, Dockerfile을 이용한 커스텀 이미지 빌드, 포트 매핑, 바인드 마운트, 볼륨 사용법을 숙지합니다.
*   **Git/GitHub 기초:** Git 초기 설정 및 VSCode와의 연동을 통해 기본적인 버전 관리 흐름을 이해합니다.
*   **개발 환경 재현성 확보:** Docker를 활용하여 개발 환경의 일관성을 유지하고 재현성을 높이는 방법을 배웁니다.
*   **기술 문서 작성 능력 향상:** 학습 과정을 구조화하고 명확하게 설명하는 문서 작성 능력을 기릅니다.

## 3. 기능 요구사항

1.  **터미널 기본 조작:** `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm` 등의 명령어 활용
2.  **권한 변경:** `chmod` 명령어를 사용하여 파일 및 디렉토리 권한을 변경하고 이해합니다.
3.  **Docker 설치 및 점검:** Docker가 올바르게 설치되었는지 확인하고, `docker version`, `docker info` 등으로 상태를 점검합니다.
4.  **Docker 기본 명령어 실습:**
    *   `hello-world` 컨테이너 실행
    *   `ubuntu` 컨테이너 실행 및 내부 접근 (`attach`, `exec` 차이 이해)
    *   `docker images`, `docker ps`, `docker logs`, `docker stats` 등 기본 명령어 활용
5.  **Dockerfile 기반 커스텀 이미지 제작:** 제공된 Nginx 이미지를 기반으로 `index.html`을 포함하는 커스텀 Nginx 이미지를 빌드합니다.
6.  **컨테이너 실행 및 연동:**
    *   **포트 매핑:** 로컬 포트와 컨테이너 포트를 연결하여 웹 서버에 접속합니다. (최소 2회 이상)
    *   **바인드 마운트:** 로컬 디렉토리를 컨테이너 내부 디렉토리에 연결하여 파일 변경 사항을 실시간으로 반영합니다.
    *   **볼륨:** 컨테이너 데이터를 영속적으로 저장하기 위해 Docker 볼륨을 사용합니다.
7.  **Git/GitHub 연동:** Git의 사용자 설정을 하고, VSCode와 GitHub를 연동하여 기본적인 버전 관리 워크플로우를 구현합니다.
8.  **실행 환경 및 수행 항목 문서화:** README 파일을 통해 프로젝트 개요, 실행 환경, 수행 항목 체크리스트, 명령어 사용 로그, 트러블슈팅 등을 상세하게 기록합니다.

## 4. 핵심 기술 스택

*   **운영체제 (OS):** macOS (Windows, Linux 환경에서도 적용 가능)
*   **셸 (Shell):** bash, zsh 등
*   **터미널 (Terminal/CLI):** 명령줄 인터페이스
*   **Docker:** 컨테이너화 기술
*   **Git:** 분산 버전 관리 시스템
*   **GitHub:** Git 기반의 협업 플랫폼
*   **VSCode:** 코드 에디터 (GitHub 연동을 위해)
*   **Nginx:** 웹 서버 (Dockerfile 실습을 위해)

## 5. 권장 프로젝트 구조

각 수강생의 레포지토리 구조를 참고하여 다음과 같은 구조를 권장합니다.

```
your-repo-name/
├── README.md             # 프로젝트 개요, 설명, 로그, 트러블슈팅 등
├── Dockerfile            # 커스텀 Nginx 이미지 빌드를 위한 Dockerfile
├── docker-compose.yml    # (선택 사항) Docker Compose를 활용할 경우
├── src/                  # 웹 서버에 배포할 정적 파일 (예: index.html)
│   └── index.html
├── scripts/              # (선택 사항) 권한 변경 등 스크립트 파일
│   └── permission_test.sh
└── screenshots/          # (선택 사항) 명령어 실행 결과, GitHub 연동 등의 이미지
    ├── image-name.png
```

**참고:**

*   `codewhite7777`님은 `workstation`이라는 최상위 디렉토리를 사용하여 구성했습니다.
*   `mov-hyun`님은 `src` 디렉토리 안에 `index.html`을 두었습니다.
*   `yejoo0310`님은 `app` 디렉토리를 사용했습니다.

## 6. 구현 핵심 포인트

### 6.1 터미널 기본 명령어

*   **경로 이해:** 절대 경로 (`/Users/user/project`)와 상대 경로 (`../folder`, `./file`)의 차이를 명확히 이해하고 상황에 맞게 사용합니다.
*   **파일/디렉토리 관리:** `mkdir`로 원하는 구조를 만들고, `cp`, `mv`, `rm`으로 파일을 복사, 이동, 삭제하며 작업 공간을 정리합니다.
*   **내용 확인 및 작성:** `cat`으로 파일 내용을 확인하고, `echo "content" > file.txt`를 사용하여 파일에 내용을 씁니다. (쉘 확장 방지를 위해 작은따옴표 `'` 사용 고려)
*   **권한 변경:** `chmod` 명령어를 사용하여 `rwx` (읽기, 쓰기, 실행) 권한을 사용자, 그룹, 기타(others)에게 부여합니다.
    *   `chmod 755 script.sh`: 소유자에게 모든 권한(rwx=4+2+1=7), 그룹과 기타 사용자에게 읽기 및 실행 권한(rx=4+1=5)을 부여합니다.

### 6.2 Dockerfile 작성 및 빌드

```dockerfile
# 베이스 이미지: Nginx의 경량 alpine 버전
FROM nginx:alpine

# (선택 사항) 이미지 메타데이터
LABEL maintainer="YourName"
LABEL description="Codyssey workstation mission - custom nginx"

# 정적 콘텐츠 복사: 로컬의 src/index.html을 컨테이너의 웹 루트로 복사
COPY src/index.html /usr/share/nginx/html/index.html

# 컨테이너가 노출할 포트 선언
EXPOSE 80
```
*   `FROM`: 사용할 기반 이미지를 지정합니다.
*   `COPY`: 로컬 파일 시스템의 파일을 이미지 안으로 복사합니다.
*   `EXPOSE`: 컨테이너가 해당 포트에서 리스닝함을 명시하지만, 실제 외부 연결은 `docker run`의 `-p` 옵션으로 설정합니다.

### 6.3 Docker 컨테이너 실행 및 옵션 활용

*   **이미지 빌드:** `docker build -t your-custom-nginx-image:latest .`
*   **컨테이너 실행 (포트 매핑 + 바인드 마운트):**
    ```bash
    docker run -d \
      -p 8080:80 \
      -v $(pwd)/src:/usr/share/nginx/html:ro \
      your-custom-nginx-image:latest
    ```
    *   `-d`: 백그라운드에서 실행
    *   `-p 8080:80`: 호스트의 8080 포트를 컨테이너의 80 포트로 매핑
    *   `-v $(pwd)/src:/usr/share/nginx/html:ro`: 현재 디렉토리의 `src` 폴더를 컨테이너의 `/usr/share/nginx/html` 경로에 마운트합니다. `:ro`는 읽기 전용(read-only)으로 마운트함을 의미합니다. (변경 사항을 로컬에서만 적용하거나, 컨테이너 내부에서 실수로 변경되는 것을 방지할 때 유용)
*   **컨테이너 실행 (볼륨 영속성):**
    ```bash
    docker run -d \
      -p 8081:80 \
      --name my-nginx-volume-container \
      -v my-nginx-data:/usr/share/nginx/html \
      your-custom-nginx-image:latest
    ```
    *   `--name`: 컨테이너 이름을 지정하여 관리 편의성을 높입니다.
    *   `-v my-nginx-data:/usr/share/nginx/html`: `my-nginx-data`라는 이름의 Docker 볼륨을 생성하여 컨테이너의 `/usr/share/nginx/html` 경로에 마운트합니다. 컨테이너가 삭제되어도 볼륨의 데이터는 유지됩니다.

### 6.4 Git/GitHub 연동

1.  **Git 전역 설정:**
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```
2.  **VSCode GitHub 연동:**
    *   Source Control 뷰에서 "Sign in to GitHub" 클릭
    *   GitHub 계정으로 로그인 후 VSCode에 권한 부여
    *   GitHub에서 새 Repository 생성 후, VSCode에서 "Publish to GitHub" 선택

## 7. 트러블슈팅 & 팁

*   **`echo "..."` vs `echo '...'`:** `echo` 명령어 사용 시, 내용에 `!`와 같은 문자가 포함되면 쉘 히스토리 확장이 발생할 수 있습니다. 이를 방지하기 위해 문자열을 작은따옴표(`'`)로 감싸는 것이 안전합니다. (`mov-hyun`님 레포 참고)
*   **Docker Desktop 설치:** Docker Desktop이 설치되지 않거나 제대로 작동하지 않는 경우, 재설치하거나 OrbStack과 같은 대안 도구를 고려할 수 있습니다. (`codewhite7777`님 레포 참고)
*   **권한 문제:** Docker 컨테이너 내부에서 파일 권한 문제로 실행이 안 되는 경우, Dockerfile에서 `RUN chown ...` 또는 `RUN chmod ...`를 사용하여 적절한 권한을 부여해야 할 수 있습니다. (이번 미션에서는 주로 호스트 OS의 권한 및 Docker 이미지의 기본 권한으로 해결될 가능성이 높음)
*   **바인드 마운트 경로:** 로컬 경로를 지정할 때 `$(pwd)` (또는 macOS/Linux의 경우 `` `pwd` ``)를 사용하면 현재 작업 디렉토리를 기준으로 경로를 지정할 수 있어 편리합니다.
*   **Docker Compose:** 여러 개의 컨테이너가 서로 연동되는 복잡한 애플리케이션의 경우, `docker-compose.yml` 파일을 사용하여 한 번에 컨테이너들을 관리하는 것이 효율적입니다. (`mov-hyun`님 레포에서 예시 확인 가능)
*   **GitHub Commit 메시지:** 명확하고 간결한 커밋 메시지는 코드 변경 이력을 파악하는 데 매우 중요합니다. (예: `feat: Add Nginx configuration`, `fix: Correct Dockerfile path`)

## 8. 추가 학습 자료

*   **터미널 기본 명령어:**
    *   [Linux/macOS 명령어 사전](https://www.inflearn.com/pages/command-list) (생활코딩)
    *   [터미널 cheat sheet](https://www.google.com/search?q=terminal+cheat+sheet&oq=terminal+cheat+sheet&aqs=chrome..69i57j0i512l9.2733j0j7&sourceid=chrome&ie=UTF-8) (검색 결과 활용)
*   **Docker 공식 문서:**
    *   [Docker Get Started](https://docs.docker.com/get-started/)
    *   [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
    *   [docker run reference](https://docs.docker.com/engine/reference/run/)
*   **Git 공식 문서:**
    *   [Pro Git book](https://git-scm.com/book/en/v2)
    *   [Git cheat sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf)

이 문서를 바탕으로 1주차 미션의 각 항목을 꼼꼼히 확인하고, 수강생들의 코드를 참고하여 자신의 워크스테이션 구축 과정을 더욱 견고하게 다지시길 바랍니다.

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

_이번 실행에서는 뚜렷한 덮어쓰기/변조 의심 레포가 없었습니다._

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
