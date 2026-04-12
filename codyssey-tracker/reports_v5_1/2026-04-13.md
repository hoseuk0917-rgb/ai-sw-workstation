# Codyssey registry-backed collection report v5.1 (2026-04-13)

- 총 수집 건수: 37건
- candidate pool size: 44
- 2026 본과정 확정: 32건
- 제외된 레거시/파일럿: 1건
- 후보/검토 필요: 4건
- watchlist size after run: 4
- discovered candidate count: 0
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

## Codyssey AI 올인원 입학연수과정 1주차: AI/SW 개발 워크스테이션 구축

### 1. 미션 개요

본 미션은 AI/SW 개발의 필수적인 기본 도구인 **터미널(CLI)**, **Docker(컨테이너)**, **Git/GitHub(버전 관리)**를 사용하여 **재현 가능한 개발 워크스테이션 환경**을 구축하는 것을 목표로 합니다. "내 컴퓨터에서만 돌아가는" 문제를 해결하고, 언제 어디서든 동일한 개발 환경을 구성하고 실행할 수 있는 능력을 배양합니다.

### 2. 학습 목표

*   **터미널(CLI) 기본 조작 능력 습득**: 파일 및 디렉토리 관리, 권한 변경 등 기본적인 명령어 사용법을 익힙니다.
*   **Docker 컨테이너 이해 및 활용**: Docker 설치, 이미지 빌드, 컨테이너 실행 및 관리, 포트 매핑, 볼륨 마운트 등 핵심 기능을 이해하고 활용할 수 있습니다.
*   **Dockerfile을 활용한 이미지 제작**: 간단한 웹 서버 이미지를 Dockerfile을 통해 직접 만들어봅니다.
*   **Git/GitHub 기본 사용법 숙지**: Git 설정 및 GitHub 연동을 통해 버전 관리의 기초를 다집니다.
*   **개발 환경 구축 및 문서화 능력 향상**: 프로젝트 목표, 실행 환경, 수행 과정을 README.md 파일에 명확하게 문서화하는 연습을 합니다.

### 3. 기능 요구사항

1.  **터미널 기본 조작**: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm` 명령어 등을 활용하여 파일 및 디렉토리를 생성, 이동, 복사, 삭제, 수정하고 내용을 확인합니다.
2.  **파일/디렉토리 권한 변경**: `chmod` 명령어를 사용하여 파일 및 디렉토리의 접근 권한을 설정합니다.
3.  **Docker 설치 및 점검**: Docker가 정상적으로 설치되었는지 확인하고, `docker version` 및 `docker info` 등으로 상태를 점검합니다.
4.  **Docker 기본 명령어 실습**:
    *   `docker run hello-world`를 실행하여 Docker 동작을 확인합니다.
    *   `docker run -it ubuntu`를 실행하여 Ubuntu 컨테이너에 접속하고 내부를 탐색합니다.
    *   `attach`와 `exec`의 차이를 이해하고 실습합니다.
    *   `docker images`, `docker ps`, `docker logs`, `docker stats` 등의 명령어를 사용합니다.
5.  **Dockerfile 기반 커스텀 이미지 제작**: 제공된 Nginx 기반 Dockerfile을 수정하거나 직접 작성하여 간단한 웹 서버 이미지를 빌드합니다.
6.  **포트 매핑**: 빌드된 이미지를 실행할 때 호스트와 컨테이너 간의 포트를 매핑하여 웹 브라우저로 접속을 확인합니다 (최소 2회).
7.  **바인드 마운트**: 호스트의 디렉토리를 컨테이너에 마운트하여, 호스트에서 파일을 수정했을 때 컨테이너 내부에 변경 사항이 반영되는 것을 확인합니다.
8.  **Docker 볼륨(Volume) 활용**: Docker 볼륨을 사용하여 컨테이너 데이터를 영속적으로 관리하는 방법을 실습합니다.
9.  **Git 설정 및 GitHub 연동**: Git의 사용자 이름과 이메일을 설정하고, VSCode를 통해 GitHub Repository에 코드를 Push하는 과정을 연동합니다.
10. **README.md 작성**: 프로젝트 개요, 실행 환경, 수행 항목 체크리스트, 터미널 조작 로그, 트러블슈팅 내용 등을 포함하여 README.md 파일을 상세하게 작성합니다.

### 4. 핵심 기술 스택

*   **터미널 (Command Line Interface)**: macOS/Linux/Windows CLI (Bash, Zsh 등)
*   **Docker**: 컨테이너화 기술
*   **Git/GitHub**: 버전 관리 시스템
*   **Dockerfile**: Docker 이미지 빌드 스크립트
*   **Nginx**: 웹 서버 (Dockerfile 실습에 활용)
*   **VSCode**: 코드 에디터 및 Git 연동 도구

### 5. 권장 프로젝트 구조

다음은 수강생들의 레포지토리를 참고하여 구성한 권장 프로젝트 구조입니다.

```
your-repository-name/
├── README.md             # 프로젝트 설명, 개요, 사용법, 환경, 로그 등
├── Dockerfile            # 커스텀 Docker 이미지 빌드를 위한 설정 파일
├── src/                  # 웹 서버에서 제공할 정적 파일 (예: index.html)
│   └── index.html
├── screenshots/          # 학습 과정 중 캡처한 이미지 (옵션)
│   ├── port_mapping.png
│   └── vscode_github.png
└── script/               # 터미널 실습 등 보조 스크립트 (옵션)
    └── permission_test.sh
```

*   **README.md**: 프로젝트의 핵심 문서로, 전체 학습 내용을 담습니다.
*   **Dockerfile**: Nginx와 같은 웹 서버 이미지를 기반으로, `COPY` 명령어를 사용하여 `src` 디렉토리의 `index.html` 파일을 복사하여 커스텀 이미지를 만듭니다.
*   **src/**: 웹 서버가 제공할 HTML, CSS, JS 등의 정적 파일을 저장하는 공간입니다.
*   **screenshots/**: 터미널 명령어 실행 결과, Docker 명령어 결과, Git 연동 화면 등을 시각적으로 보여주기 위해 사용합니다.
*   **script/**: 권한 변경과 같이 별도 스크립트로 테스트하거나, 터미널 명령어 실행 과정을 기록하는 데 활용할 수 있습니다.

### 6. 구현 핵심 포인트

**1. 터미널 기본 조작 및 권한 부여**

*   **절대 경로 vs 상대 경로**: `pwd` 명령어로 현재 위치를 확인하고, `cd` 명령어로 이동하며 절대 경로와 상대 경로의 차이를 이해합니다.
*   **파일/디렉토리 관리**: `ls -alh`로 숨김 파일을 포함한 상세 목록을 확인하고, `mkdir`, `touch`, `cp`, `mv`, `rm`을 사용하여 파일을 생성, 복사, 이동, 삭제합니다.
*   **파일 내용 조작**: `cat`으로 내용을 확인하고, `echo "..." > file.txt` 또는 `echo '...' >> file.txt`를 사용하여 파일에 내용을 작성합니다.
    *   **주의**: `echo "hello"`와 같이 큰따옴표 안에 `$`가 포함된 경우, 쉘에서 변수로 해석될 수 있으므로 작은따옴표(`'`)를 사용하거나 백슬래시(`\`)로 이스케이프 해야 합니다. (mov-hyun님 참고)
*   **권한 변경**: `chmod` 명령어를 사용하여 파일의 실행 권한을 부여합니다. 일반적으로 `chmod 755 script.sh`와 같이 사용하며, 이는 소유자에게 읽기, 쓰기, 실행 권한을, 그룹 및 타인에게는 읽기, 실행 권한을 부여합니다.

**2. Docker 기본 활용**

*   **Docker 설치 및 점검**: `docker version`, `docker info` 명령어로 설치 상태를 확인합니다. macOS의 경우, Docker Desktop 또는 OrbStack을 사용할 수 있습니다. (codewhite7777님 참고)
*   **기본 컨테이너 실행**:
    *   `docker run hello-world`: Docker 설치 확인 및 기본 동작 테스트
    *   `docker run -it ubuntu`: Ubuntu 컨테이너에 접속하여 내부 명령 실행 (exit로 컨테이너 종료)
*   **Attach vs Exec**:
    *   `attach`: 컨테이너의 메인 프로세스에 직접 연결하여 상호작용합니다. (주로 컨테이너 실행 시 `-it` 옵션과 함께 사용)
    *   `exec`: 이미 실행 중인 컨테이너에 새로운 프로세스를 실행하여 명령을 전달합니다. (예: `docker exec -it <container_id> bash`)
*   **이미지 및 컨테이너 관리**: `docker images`, `docker ps -a`, `docker logs <container_id>`, `docker stats` 명령어로 이미지 및 컨테이너 상태를 확인합니다.

**3. Dockerfile 기반 커스텀 이미지 제작**

*   **기본 Nginx 이미지 활용**: `FROM nginx:latest` 또는 `FROM nginx:alpine`을 베이스 이미지로 사용합니다. Alpine 버전은 용량이 작아 효율적입니다. (codewhite7777, mov-hyun님 참고)
*   **정적 파일 복사**: `COPY ./src/index.html /usr/share/nginx/html/index.html` 명령어를 사용하여 로컬의 `src` 디렉토리에 있는 `index.html` 파일을 컨테이너의 Nginx 웹 서버 디렉토리로 복사합니다. (yejoo0310, codewhite7777, mov-hyun님 모두 유사하게 사용)
*   **포트 노출**: `EXPOSE 80` 명령어로 컨테이너가 80번 포트를 사용함을 명시합니다.
*   **이미지 빌드**: `docker build -t custom-nginx:latest .` 명령어로 Dockerfile이 있는 디렉토리에서 이미지를 빌드합니다. `-t` 옵션으로 이미지 이름을 지정합니다.

**4. 포트 매핑 및 마운트**

*   **포트 매핑**: `docker run -p <host_port>:<container_port> custom-nginx:latest` 명령어를 사용하여 호스트의 포트와 컨테이너의 포트를 연결합니다. (예: `-p 8080:80`) 이렇게 하면 호스트의 8080 포트로 접속 시 컨테이너의 80번 포트로 요청이 전달됩니다. (yejoo0310, codewhite7777, mov-hyun님 모두 활용)
*   **바인드 마운트**: `docker run -v <host_path>:<container_path> custom-nginx:latest` 명령어를 사용하여 호스트의 디렉토리를 컨테이너에 연결합니다. (예: `-v $(pwd)/src:/usr/share/nginx/html`) 이를 통해 호스트의 `src` 디렉토리 내용을 컨테이너가 실시간으로 읽어오게 되어, `index.html` 수정 시 바로 웹에서 확인 가능합니다. (yejoo0310, codewhite7777, mov-hyun님 모두 활용)
*   **볼륨(Volume)**: `docker run -v <volume_name>:<container_path> custom-nginx:latest` 또는 `docker volume create <volume_name>` 과 같이 Docker 볼륨을 사용하여 데이터를 영속적으로 관리합니다. 볼륨은 Docker에 의해 관리되며, 컨테이너가 삭제되어도 데이터가 유지됩니다. (yejoo0310님 명시적으로 언급)

**5. Git 설정 및 GitHub 연동**

*   **Git 전역 설정**:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```
*   **GitHub Repository 생성**: GitHub 웹사이트에서 새 Repository를 생성합니다.
*   **로컬 Repository 연동**:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/your-username/your-repository-name.git
    git push -u origin main  # 또는 master
    ```
*   **VSCode 연동**: VSCode의 Git Extension을 활용하여 파일 변경 사항을 확인하고, Staging, Commit, Push 등의 작업을 GUI로 수행합니다. (yejoo0310, codewhite7777님 모두 VSCode 연동 확인)

### 7. 트러블슈팅 & 팁

*   **Docker 설치 오류**: macOS 환경에서는 Docker Desktop 또는 OrbStack 설치 시 발생하는 문제들을 해결해야 할 수 있습니다. Docker 설치 가이드를 따르고, 공식 문서의 문제 해결 섹션을 참고하세요.
*   **Dockerfile 빌드 실패**: `COPY` 경로 오류, 베이스 이미지 문제, 명령어 오타 등을 확인합니다. `docker build .` 명령 실행 시 출력되는 에러 메시지를 주의 깊게 읽어봅니다.
*   **`echo` 명령어와 따옴표**: `echo "hello $USER"`와 같이 따옴표 안에 변수가 포함된 경우, 쉘이 변수를 확장하려 시도합니다. 이를 방지하려면 작은따옴표(`echo 'hello $USER'`)를 사용하거나, 변수 앞에 백슬래시(`echo "hello \$USER"`)를 붙여 이스케이프해야 합니다. (mov-hyun님 경험)
*   **포트 충돌**: 이미 사용 중인 호스트 포트로 Docker 컨테이너를 실행하면 오류가 발생합니다. 다른 포트로 변경하거나, 사용 중인 프로세스를 찾아 종료해야 합니다. (codewhite7777님 8080, 8081 포트 사용 예시)
*   **권한 문제**: 컨테이너 내에서 파일 쓰기 권한이 없거나, 호스트에서 컨테이너로 마운트한 디렉토리에 접근 권한이 없을 경우 발생할 수 있습니다. `chmod` 또는 Dockerfile 내에서 권한 설정을 확인합니다.
*   **`docker-compose.yml` 활용 (mov-hyun님)**: 여러 개의 Docker 컨테이너를 묶어 관리할 때 `docker-compose`를 사용하면 편리합니다. `docker-compose up` 명령 하나로 여러 서비스를 동시에 실행하고 관리할 수 있습니다. (mov-hyun님은 docker-compose.yml 파일을 추가로 구성)
*   **`LABEL` 활용**: Dockerfile 내 `LABEL` 지시어는 이미지에 메타데이터를 추가하는 데 사용됩니다. 이미지의 정보성이나 관리 목적으로 활용할 수 있습니다. (codewhite7777, mov-hyun님 활용)

### 8. 추가 학습 자료

*   **터미널(CLI) Cheat Sheet**:
    *   [cheat.sh](https://cheat.sh/) (다양한 명령어 치트시트 제공)
    *   [macOS Terminal Commands](https://www.google.com/search?q=macos+terminal+commands+cheat+sheet)
*   **Docker 공식 문서**:
    *   [Docker Overview](https://docs.docker.com/get-started/)
    *   [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
    *   [Docker Run Reference](https://docs.docker.com/engine/reference/run/)
*   **Git 공식 문서**:
    *   [Pro Git Book](https://git-scm.com/book/ko/v2)
    *   [Git Cheat Sheet](https://www.google.com/search?q=git+cheat+sheet)
*   **Nginx 공식 문서**:
    *   [Nginx Official Documentation](https://nginx.org/en/docs/)
*   **VSCode GitHub 연동**:
    *   [VS Code Docs - Version Control](https://code.visualstudio.com/docs/editor/versioncontrol)

이 문서를 통해 1주차 미션의 핵심 내용을 숙지하고, 자신의 GitHub Repository에 충실하게 기록하여 AI/SW 개발 역량의 탄탄한 기초를 다지시길 바랍니다.

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

## 2. 타과정/비본과정 정리

_현재 실행에서는 타과정 확정/후보 레포가 뚜렷하게 분리되지 않았습니다._

## 3. 후보/검토 레포 (watchlist 대상)

### 미분류

| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |
| --- | --- | --- | --- | --- |
| ntt65 | [codyssey/e1_2](https://github.com/ntt65/codyssey/tree/main/e1_2) | 2026-04-12 | 0.25 | repo:codyssey, tier2:main.py |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | 0.25 | repo:codyssey, readme:npu, readme:mac, tier2:main.py |
| sungho255 | [codyssey_2](https://github.com/sungho255/codyssey_2) | 2026-04-07 | 0.25 | repo:codyssey, tier2:state.json |
| sungho255 | [codyssey_1](https://github.com/sungho255/codyssey_1) | 2026-04-07 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, readme:mac |

## 4. 후보 확장 정리

_이번 실행에서 새 후보 확장은 없었습니다. (전역 탐색 OFF 또는 신규 미발견)_

## 5. 제외된 레거시/파일럿 레포

| 수강생 | 레포 | 업데이트 | 제외 근거 |
| --- | --- | --- | --- |
| doji-kr | [codyssey_day1_bear1](https://github.com/doji-kr/codyssey_day1_bear1) | 2025-07-11 | updated_at:2025-07-11, rule:legacy-hard-cutoff |
