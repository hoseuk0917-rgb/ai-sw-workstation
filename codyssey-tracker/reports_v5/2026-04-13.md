# Codyssey registry-backed collection report v5 (2026-04-13)

- 총 수집 건수: 37건
- 2026 본과정 확정: 29건
- 제외된 레거시/파일럿: 1건
- 후보/검토 필요: 7건
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

## Codyssey 1주차: AI/SW 개발 워크스테이션 구축 완벽 가이드

### 1. 미션 개요

Codyssey 1주차 미션은 **터미널(CLI), Docker, Git/GitHub**와 같은 개발자의 필수 도구를 익히고 활용하여, **재현 가능한 개발 워크스테이션 환경**을 구축하는 것을 목표로 합니다. 이는 "내 컴퓨터에서만 돌아가는" 문제를 해결하고, 어떤 환경에서도 동일한 개발 환경을 유지하며 협업을 용이하게 하기 위한 기초 다지기 과정입니다.

### 2. 학습 목표

*   **터미널(CLI) 기본 조작:** 파일 및 디렉토리 생성, 이동, 복사, 삭제, 내용 확인 등 기본적인 명령어 사용법을 숙달합니다.
*   **파일 권한 이해 및 조작:** `chmod` 명령어를 사용하여 파일 및 디렉토리의 권한을 이해하고 변경하는 방법을 습득합니다.
*   **Docker 기본 개념 및 활용:**
    *   Docker 설치 및 점검 방법을 익힙니다.
    *   `hello-world`, `ubuntu`와 같은 기본 이미지를 실행하고 컨테이너를 관리합니다.
    *   `attach`와 `exec` 명령어의 차이를 이해하고 활용합니다.
    *   `Dockerfile`을 이용해 자신만의 Docker 이미지를 빌드하는 방법을 배웁니다.
    *   포트 매핑, 바인드 마운트, 볼륨을 사용하여 컨테이너와 호스트 간의 데이터 교환 및 영속성을 확보하는 방법을 실습합니다.
*   **Git/GitHub 기초:** Git의 기본적인 설정을 완료하고, VSCode와 연동하여 GitHub 저장소와 연결하는 방법을 익힙니다.

### 3. 기능 요구사항

본 미션을 통해 학습자는 다음 기능을 수행할 수 있어야 합니다.

*   터미널에서 기본적인 파일/디렉토리 관리 명령어를 사용하여 원하는 구조를 만들고 조작할 수 있습니다.
*   `chmod` 명령어를 사용하여 파일의 실행 권한을 부여하고 확인할 수 있습니다.
*   `docker version`, `docker info` 명령어로 Docker 설치를 확인합니다.
*   `docker run hello-world` 명령어로 Docker 작동 여부를 확인합니다.
*   `docker run -it ubuntu bash` 명령어로 Ubuntu 컨테이너에 접속하고 명령어를 실행할 수 있습니다.
*   `Dockerfile`을 작성하여 Nginx 웹 서버 이미지를 빌드하고, `docker build` 명령어를 사용합니다.
*   `docker run -p <host_port>:<container_port> <image_name>` 명령어로 컨테이너의 포트를 외부와 연결합니다.
*   `docker run -v <host_path>:<container_path> <image_name>` 명령어로 바인드 마운트를 설정하여 호스트와 컨테이너 간 파일 변경 사항을 동기화합니다.
*   Docker 볼륨을 사용하여 컨테이너 데이터의 영속성을 확보합니다.
*   `git config --global user.name` 및 `git config --global user.email` 명령어로 Git 설정을 완료합니다.
*   VSCode에서 GitHub 계정을 연동하여 원격 저장소와 연결할 수 있습니다.

### 4. 핵심 기술 스택

*   **터미널 (Command Line Interface):** `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm`, `chmod` 등
*   **Docker:** Dockerfile, `docker build`, `docker run`, `docker ps`, `docker logs`, `docker stop`, `docker rm`, `docker exec`, `docker attach`, Port Mapping, Bind Mount, Volume
*   **Git/GitHub:** `git config`, VSCode GitHub Extension

### 5. 권장 프로젝트 구조

여러 수강생의 레포지토리를 분석한 결과, 다음과 같은 구조가 학습 목표 달성에 효과적입니다.

```
your-repo-name/
├── README.md             # 프로젝트 개요, 목표, 실행 환경, 수행 항목, 트러블슈팅 등 문서화
├── app/                  # (또는 workstation/, codyssey-m1/ 등)
│   ├── Dockerfile        # 커스텀 Docker 이미지 빌드를 위한 설정 파일
│   ├── index.html        # Dockerfile에서 복사할 웹 페이지 파일
│   └── (기타 필요한 파일) # 예: practice 디렉토리, 스크린샷 등
├── screenshots/          # (선택 사항) 명령어 실행 결과, UI 등을 캡처한 이미지 파일
└── (기타 필요한 파일)     # 예: permission_test.sh, docker-compose.yml 등
```

**설명:**

*   **`README.md`**: 프로젝트의 모든 내용을 체계적으로 담는 것이 중요합니다. 각 항목별로 상세히 작성하여 본인의 학습 과정을 기록하고, 타인이 이해하기 쉽도록 구성합니다.
*   **`app/` (또는 유사한 이름의 디렉토리):** Dockerfile과 함께 사용될 파일들을 모아둡니다. Nginx 웹 서버를 위한 `index.html` 파일이 여기에 위치합니다.
*   **`Dockerfile`**: Nginx를 기반으로 하여 `index.html`을 복사하는 간단한 형태를 권장합니다.
*   **`screenshots/`**: 각 단계별 명령어 실행 결과나 Docker Hub 등의 UI를 캡처하여 시각적인 이해를 돕습니다. (선택 사항)

### 6. 구현 핵심 포인트

#### 1. 터미널 기본 명령어 및 권한

*   **`pwd`**: 현재 위치를 절대 경로로 확인합니다.
*   **`ls -alh`**: 현재 디렉토리의 모든 파일(숨김 파일 포함)과 상세 정보를 확인합니다.
*   **`cd`**: 디렉토리 이동 (상위: `..`, 특정 경로: `dir_name/`)
*   **`mkdir`**: 디렉토리 생성
*   **`touch`**: 빈 파일 생성
*   **`echo "내용" > 파일명`**: 파일에 내용 쓰기 (덮어쓰기)
*   **`echo "내용" >> 파일명`**: 파일에 내용 추가 (이어쓰기)
*   **`cat`**: 파일 내용 출력
*   **`cp`**: 파일/디렉토리 복사 (`cp -r`로 디렉토리 복사)
*   **`mv`**: 파일/디렉토리 이동 또는 이름 변경
*   **`rm`**: 파일 삭제 (`rm -r`로 디렉토리 삭제)
*   **`chmod 755 script.sh`**: 파일 권한 변경 (Owner: 읽기, 쓰기, 실행 / Group: 읽기, 실행 / Others: 읽기, 실행). 스크립트 파일 실행을 위해 `x` 권한이 필요합니다.

#### 2. Dockerfile 기반 커스텀 이미지 제작

*   **`FROM nginx:alpine`**: 가볍고 빠른 `nginx:alpine` 이미지를 베이스로 사용합니다.
*   **`COPY ./src/index.html /usr/share/nginx/html/`**: 호스트의 `src/index.html` 파일을 컨테이너 내 Nginx 웹 서버의 기본 경로로 복사합니다.
*   **`EXPOSE 80`**: 컨테이너가 80번 포트를 사용함을 명시합니다.

#### 3. Docker 컨테이너 실행 및 관리

*   **`docker build -t my-nginx-image .`**: 현재 디렉토리의 `Dockerfile`을 사용하여 `my-nginx-image`라는 이름의 이미지를 빌드합니다.
*   **`docker run -d -p 8080:80 --name my-nginx-container my-nginx-image`**:
    *   `-d`: 백그라운드에서 컨테이너 실행 (detached mode)
    *   `-p 8080:80`: 호스트의 8080번 포트와 컨테이너의 80번 포트를 연결합니다. (클라이언트 요청은 호스트 8080번으로 들어와 컨테이너 80번으로 전달)
    *   `--name my-nginx-container`: 컨테이너에 이름을 지정하여 관리하기 쉽게 합니다.
    *   `my-nginx-image`: 실행할 이미지 이름
*   **`docker ps`**: 현재 실행 중인 컨테이너 목록을 확인합니다.
*   **`docker logs my-nginx-container`**: 컨테이너의 로그를 확인합니다.
*   **`docker stop my-nginx-container`**: 실행 중인 컨테이너를 중지합니다.
*   **`docker rm my-nginx-container`**: 중지된 컨테이너를 삭제합니다.
*   **`docker exec -it <container_name_or_id> bash`**: 실행 중인 컨테이너 내부에서 `bash` 쉘을 실행하여 명령어를 입력합니다. (`-i`: 대화형, `-t`: TTY 할당)
*   **`docker attach <container_name_or_id>`**: 컨테이너의 메인 프로세스에 연결합니다. (`Ctrl+C` 등으로 종료 시 컨테이너도 종료될 수 있으므로 주의)

#### 4. 바인드 마운트와 볼륨

*   **바인드 마운트 (`-v /host/path:/container/path`)**:
    *   호스트의 특정 디렉토리를 컨테이너 내부의 디렉토리와 연결합니다.
    *   호스트에서 파일을 수정하면 컨테이너에도 즉시 반영됩니다. 개발 중 코드 변경 사항을 실시간으로 확인하는 데 유용합니다.
    *   **예시:** `docker run -d -p 8080:80 -v $(pwd)/src:/usr/share/nginx/html --name my-nginx-bind my-nginx-image`
        *   `$(pwd)/src`: 현재 작업 디렉토리의 `src` 폴더를 나타냅니다.
        *   `/usr/share/nginx/html`: Nginx의 기본 웹 루트 디렉토리입니다.
*   **볼륨 (`-v volume_name:/container/path`)**:
    *   Docker에서 관리하는 영속적인 저장 공간을 생성하여 컨테이너와 연결합니다.
    *   컨테이너가 삭제되어도 볼륨에 저장된 데이터는 유지됩니다. 데이터베이스 파일, 로그 파일 등의 영속성이 필요한 경우에 사용합니다.
    *   **예시:** `docker run -d -p 8080:80 -v my-nginx-data:/usr/share/nginx/html --name my-nginx-volume my-nginx-image` (명시적으로 볼륨 이름 지정)
        *   `my-nginx-data`: Docker가 관리하는 볼륨 이름입니다. 명시하지 않으면 Docker가 임의의 이름을 생성합니다.

#### 5. Git 설정 및 VSCode 연동

*   **Git 전역 설정:**
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```
*   **VSCode GitHub 연동:**
    1.  VSCode에서 GitHub Extension을 설치합니다.
    2.  Extension을 통해 GitHub 계정으로 로그인합니다.
    3.  새로운 Repository를 생성하거나 기존 Repository를 Clone하여 연결합니다.
    4.  변경 사항을 Staging하고 Commit한 후 Push하여 GitHub 저장소에 동기화합니다.

### 7. 트러블슈팅 & 팁

*   **`echo` 명령어 사용 시 따옴표 문제:** `echo "hello!" > file.txt` 와 같이 `!` 문자를 사용할 때 쉘 히스토리 확장으로 인해 오작동할 수 있습니다. 이 경우, 작은따옴표(`'`)를 사용하여 `echo 'hello!' > file.txt` 와 같이 사용하면 문제를 해결할 수 있습니다.
*   **Docker 설치 문제:** Docker Desktop이 제대로 설치되지 않았거나, OrbStack과 같은 대안 솔루션을 사용하는 경우 설정에 오류가 있을 수 있습니다. Docker 명령어가 작동하지 않는다면 Docker Desktop 또는 OrbStack 설정을 다시 확인하고 재시작해보세요.
*   **포트 충돌:** 이미 사용 중인 포트로 컨테이너를 실행하려고 하면 오류가 발생합니다. `8080:80` 대신 `8081:80`과 같이 다른 호스트 포트를 사용해보세요.
*   **바인드 마운트 경로 오류:** 호스트 경로를 정확하게 지정해야 합니다. `$(pwd)`를 사용하여 현재 작업 디렉토리를 기준으로 상대 경로를 명시하는 것이 좋습니다.
*   **권한 문제:** 컨테이너 내에서 파일이나 디렉토리에 접근하거나 생성할 때 권한 문제가 발생할 수 있습니다. Dockerfile 내에서 `RUN chown` 등으로 소유자를 변경하거나, `chmod`를 사용하여 적절한 권한을 부여해야 합니다.
*   **`docker attach` vs `docker exec`:**
    *   `attach`: 컨테이너의 **메인 프로세스**에 연결합니다. 컨테이너를 시작할 때 실행되는 명령 (예: `nginx -g 'daemon off;'`)에 직접 연결되며, 이 연결을 종료하면 컨테이너도 종료될 수 있습니다.
    *   `exec`: 실행 중인 컨테이너 내에서 **새로운 프로세스**를 실행합니다. 컨테이너는 그대로 유지된 상태로 새로운 쉘이나 명령어를 실행할 수 있어 디버깅이나 파일 조작에 더 유용합니다.
*   **VSCode GitHub Push 실패:** Git 전역 설정이 제대로 되어 있는지, 원격 저장소(origin)가 올바르게 설정되어 있는지 확인합니다. `git remote -v` 명령어로 확인 가능하며, 필요하다면 `git remote add origin <repository_url>` 명령어로 추가할 수 있습니다.

### 8. 추가 학습 자료

*   **터미널 기본 명령어:**
    *   [Ubuntu Terminal Cheat Sheet](https://ubuntu.com/tutorials/command-line-ubuntu) (영어)
    *   [macOS Terminal Cheat Sheet](https://www.codecademy.com/articles/command-line-basics) (영어)
*   **Docker 공식 문서:**
    *   [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) (영어)
    *   [Docker Run Reference](https://docs.docker.com/engine/reference/commandline/run/) (영어)
    *   [Docker Volumes](https://docs.docker.com/storage/volumes/) (영어)
*   **Git 공식 문서:**
    *   [Git Getting Started](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) (영어)
    *   [Pro Git book](https://git-scm.com/book/en/v2) (한국어 번역본도 제공)
*   **VSCode GitHub Extension:**
    *   [GitHub Copilot](https://github.com/features/copilot/) (AI 페어 프로그래머)
    *   [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) (VSCode 내에서 PR 관리)

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
| ikasoon | [codyssey-e1-1](https://github.com/ikasoon/codyssey-e1-1) | 2026-04-06 | tier2:Dockerfile, week-readme:workstation, week-readme:docker, readme:workstation |

---

### 2주차

## AI/SW 교육 과정 Codyssey 프로그램 2주차 학습 문서

### 1. 미션 개요

본 문서는 Codyssey 프로그램 2주차 과제 수행 결과를 종합하여 학습자가 퀴즈 애플리케이션 개발을 통해 **Python 기초 문법, 객체지향 프로그래밍, 파일 입출력, Git 협업** 등 핵심 개념을 완벽히 이해하고 내재화할 수 있도록 돕기 위해 작성되었습니다.

수강생들은 Python을 사용하여 콘솔 기반의 퀴즈 게임을 개발했습니다. 이 게임은 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 최고 점수 확인, 퀴즈 삭제 등의 기능을 제공하며, 프로그램 종료 후에도 데이터가 유지되도록 `state.json` 파일에 저장 및 복구하는 기능을 구현했습니다. 또한, Git을 활용한 프로젝트 관리 및 협업 과정을 경험하며 실질적인 SW 개발 역량을 함양했습니다.

### 2. 학습 목표

본 2주차 과제를 통해 학습자는 다음 목표를 달성합니다.

*   **Python 기초 문법 내재화:** 변수, 자료형, 조건문, 반복문, 함수 등의 기본 문법을 실제 애플리케이션 개발에 적용합니다.
*   **객체지향 프로그래밍(OOP) 이해 및 활용:** 클래스와 객체의 개념을 이해하고, `Quiz` 및 `QuizGame`과 같이 관련 데이터와 기능을 묶어 관리하는 방법을 습득합니다. `__init__` 메서드와 `self`의 역할을 명확히 이해합니다.
*   **데이터 관리 및 파일 입출력:** JSON 형식의 데이터를 이해하고, Python에서 파일을 읽고 쓰는 방법을 익혀 프로그램의 데이터 지속성을 확보합니다.
*   **예외 처리:** `try-except` 구문을 사용하여 프로그램의 안정성을 높이고, 예기치 못한 오류 상황에 대처하는 방법을 배웁니다.
*   **Git 협업 도구 활용:** Git의 기본 명령어(init, add, commit, push, pull, branch, checkout, merge 등)를 사용하여 프로젝트를 효과적으로 관리하고, 브랜치를 활용한 기능 개발 및 병합 과정을 경험합니다.
*   **문제 해결 능력 향상:** 개발 과정에서 발생하는 다양한 문제(예: 잘못된 입력 처리, 파일 손상 복구 등)를 분석하고 해결하는 경험을 통해 문제 해결 능력을 강화합니다.

### 3. 기능 요구사항

개발된 퀴즈 애플리케이션은 다음 기능들을 포함해야 합니다.

1.  **메인 메뉴 제공:** 사용자에게 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인, 종료 등의 옵션을 제공합니다.
2.  **퀴즈 풀기:**
    *   저장된 퀴즈를 사용자에게 제시합니다.
    *   사용자로부터 답을 입력받아 정답 여부를 판별합니다.
    *   맞힌 문제 수에 따라 점수를 누적하고 최고 점수를 갱신합니다.
    *   (선택 사항) 문제 및 선택지 순서를 무작위로 섞어 출제합니다.
    *   (선택 사항) 힌트 기능을 제공합니다.
3.  **퀴즈 추가:**
    *   사용자가 직접 문제, 선택지 4개, 정답 번호, 힌트 등을 입력하여 새로운 퀴즈를 생성합니다.
    *   추가된 퀴즈는 데이터 파일에 저장됩니다.
4.  **퀴즈 목록 확인:**
    *   현재 저장된 모든 퀴즈 목록을 보여줍니다.
    *   (선택 사항) 퀴즈의 정답 정보까지 함께 표시할 수 있습니다.
5.  **최고 점수 확인:**
    *   지금까지 기록된 최고 점수를 표시합니다.
    *   (선택 사항) 최고 점수 당시의 전체 문제 수, 맞힌 문제 수, 닉네임 등을 함께 표시할 수 있습니다.
6.  **퀴즈 삭제:**
    *   사용자가 직접 추가한 퀴즈를 선택하여 삭제할 수 있습니다.
    *   (선택 사항) 기본 제공 퀴즈는 삭제되지 않도록 처리할 수 있습니다.
7.  **데이터 저장 및 복구:**
    *   퀴즈 목록, 최고 점수 등의 데이터는 프로그램 종료 시 `state.json` 파일에 저장됩니다.
    *   프로그램 시작 시 `state.json` 파일에서 데이터를 불러옵니다.
    *   `state.json` 파일이 존재하지 않거나 손상된 경우, 기본 퀴즈 데이터로 복구합니다.
8.  **예외 처리:**
    *   숫자 입력이 필요한 곳에 숫자가 아닌 값이 입력되었을 때 오류를 방지하고 재입력을 유도합니다.
    *   `KeyboardInterrupt` (Ctrl+C) 및 `EOFError` (Ctrl+D) 발생 시 안전하게 프로그램을 종료합니다.

### 4. 핵심 기술 스택

*   **프로그래밍 언어:** Python 3.10 이상
*   **주요 라이브러리:**
    *   `json`: JSON 데이터 처리 (파일 입출력)
    *   `random`: 문제 순서 섞기, 무작위 선택 등 (선택 사항)
*   **버전 관리 시스템:** Git

### 5. 권장 프로젝트 구조

수강생들의 레포지토리를 종합하여 다음과 같은 프로젝트 구조를 권장합니다.

```
quiz_project/
├── .gitignore          # Git 무시 파일 설정
├── README.md           # 프로젝트 설명 및 학습 내용 정리
├── main.py             # 프로그램 실행 진입점
├── state.json          # 퀴즈 데이터 및 최고 점수 저장 파일
├── src/                # 소스 코드 디렉토리
│   ├── __init__.py     # Python 패키지 설정
│   ├── quiz.py         # Quiz 클래스 정의
│   ├── quiz_game.py    # QuizGame 클래스 정의 (게임 로직)
│   └── utils.py        # 공통 유틸리티 함수 (입력 처리 등) (선택 사항)
└── docs/               # 문서 및 스크린샷 (선택 사항)
    └── screenshots/
```

**설명:**

*   `main.py`: 프로그램 실행을 위한 메인 파일입니다. `QuizGame` 객체를 생성하고 게임을 실행하는 역할을 합니다.
*   `src/`: 프로젝트의 핵심 소스 코드를 모아두는 디렉토리입니다.
    *   `quiz.py`: 퀴즈 하나의 데이터를 담는 `Quiz` 클래스를 정의합니다. (문제, 선택지, 정답 등)
    *   `quiz_game.py`: 게임 전체의 로직을 관리하는 `QuizGame` 클래스를 정의합니다. (메뉴, 퀴즈 진행, 데이터 로드/저장, 점수 관리 등)
    *   `utils.py` (선택 사항): 입력값 검증, 데이터 변환 등 여러 곳에서 재사용될 수 있는 함수들을 모아둡니다.
*   `state.json`: 프로그램의 상태(퀴즈 목록, 최고 점수 등)를 저장하는 파일입니다.
*   `README.md`: 프로젝트 소개, 실행 방법, 학습 내용 정리, Git 명령어 정리 등을 상세하게 기술하여 다른 사람이나 미래의 자신에게 정보를 제공합니다.
*   `.gitignore`: Git이 추적하지 않아야 할 파일(예: `__pycache__` 디렉토리)을 지정합니다.

### 6. 구현 핵심 포인트

#### 6.1 클래스 설계: `Quiz`와 `QuizGame`

*   **`Quiz` 클래스:**
    *   **역할:** 퀴즈 한 개에 대한 데이터와 관련된 메서드를 캡슐화합니다.
    *   **속성:** `question` (str), `choices` (list of str), `answer` (int - 정답 번호).
    *   **메서드:**
        *   `display()`: 문제를 보기와 함께 화면에 출력합니다.
        *   `is_correct(user_answer)`: 사용자의 답변과 실제 정답을 비교합니다.
        *   `to_dict()`: 퀴즈 객체를 JSON 저장에 적합한 딕셔너리 형태로 변환합니다.
        *   `from_dict(data)`: 딕셔너리 데이터를 받아 `Quiz` 객체를 생성합니다. (클래스 메서드로 구현하면 편리)
*   **`QuizGame` 클래스:**
    *   **역할:** 게임 전체의 흐름, 데이터 관리, 사용자 인터페이스를 담당합니다. "게임 운영자"와 같은 역할을 합니다.
    *   **속성:** `quizzes` (list of Quiz objects), `best_score` (int), `best_correct_count` (int), `best_total_count` (int), `state_path` (str).
    *   **메서드:**
        *   `__init__()`: 객체 초기화. `state.json`에서 데이터를 불러오거나 기본 데이터로 초기화합니다.
        *   `run()`: 게임의 메인 루프를 실행하며 메뉴를 반복적으로 보여줍니다.
        *   `show_menu()`: 사용자에게 메뉴 옵션을 출력합니다.
        *   `play_quiz()`: 퀴즈 풀이 로직을 실행합니다. (랜덤 선택, 문제 표시, 정답 확인, 점수 계산 및 갱신)
        *   `add_quiz()`: 새로운 퀴즈를 추가하는 로직을 처리합니다.
        *   `show_quiz_list()`: 현재 저장된 퀴즈 목록을 보여줍니다.
        *   `show_best_score()`: 최고 점수 관련 정보를 출력합니다.
        *   `delete_quiz()`: 퀴즈 삭제 기능을 처리합니다.
        *   `load_state()`: `state.json` 파일에서 데이터를 불러옵니다.
        *   `save_state()`: 현재 게임 상태를 `state.json` 파일에 저장합니다.
        *   `prompt_number(message, min_val, max_val)`: 숫자 입력을 안전하게 받고 유효 범위를 검증하는 유틸리티 메서드.

#### 6.2 데이터 저장 및 복구 (`state.json`)

*   **JSON 활용:** Python의 `dict`와 `list`는 JSON 구조와 매우 유사하여 데이터 직렬화/역직렬화에 용이합니다.
    *   `json.dump(data, file_object)`: Python 객체를 JSON 파일로 저장합니다.
    *   `json.load(file_object)`: JSON 파일에서 데이터를 읽어 Python 객체로 변환합니다.
*   **데이터 구조:** `state.json` 파일은 보통 다음과 같은 구조를 가집니다.
    ```json
    {
      "quizzes": [
        {
          "question": "...",
          "choices": ["...", "...", "...", "..."],
          "answer": 1
        },
        // ... 다른 퀴즈들 ...
      ],
      "best_score": 5,
      "best_correct_count": 4,
      "best_total_count": 5
    }
    ```
*   **예외 처리:** `load_state` 메서드 내에서 `try-except FileNotFoundError`를 사용하여 파일이 없을 때, `try-except json.JSONDecodeError`를 사용하여 파일이 손상되었을 때를 대비하여 초기 데이터로 복구하는 로직을 구현합니다.

#### 6.3 입력 검증 및 안전 종료

*   **입력 함수 `prompt_number` (또는 유사 메서드):**
    *   사용자 입력이 숫자인지, 그리고 요구되는 범위 내인지 반복적으로 검증합니다.
    *   `try-except ValueError`를 사용하여 `int()` 변환 오류를 처리합니다.
    *   루프를 사용하여 올바른 입력이 들어올 때까지 계속해서 입력을 요구합니다.
*   **안전 종료:**
    *   `main.py` 또는 `QuizGame.run()` 메서드에서 `try-except (KeyboardInterrupt, EOFError)` 블록을 사용하여 사용자의 종료 신호(`Ctrl+C`, `Ctrl+D`)를 감지합니다.
    *   이벤트 발생 시, `save_state()` 메서드를 호출하여 현재까지의 변경 사항을 저장한 후 프로그램을 종료합니다.

#### 6.4 Git 활용

*   **기능별 브랜치:** 새로운 기능을 개발할 때는 `main` 또는 `develop` 브랜치에서 분기하여 자신만의 기능 브랜치(예: `feature/add-quiz`, `fix/input-validation`)를 생성합니다.
*   **의미 있는 커밋 메시지:** 각 커밋은 변경 내용을 명확히 나타내는 메시지(예: `feat: 퀴즈 추가 기능 구현`, `fix: 숫자 입력 오류 수정`)와 함께 작성합니다.
*   **정기적인 푸시:** 작업 중간중간 원격 저장소에 변경 사항을 푸시하여 백업하고 다른 팀원과 공유합니다.
*   **병합:** 기능 개발이 완료되면 `main` 또는 `develop` 브랜치로 돌아와 `git merge` 명령어를 사용하여 작업 내용을 병합합니다. `git log --oneline --graph` 명령어로 병합 과정을 시각적으로 확인합니다.

### 7. 트러블슈팅 & 팁

*   **JSON 파일이 없거나 손상되었을 때:** `load_state` 메서드에서 `FileNotFoundError`와 `json.JSONDecodeError`를 처리하여 기본 데이터로 복구하는 로직을 반드시 포함해야 합니다. `_init_data()`와 같은 헬퍼 메서드를 만들어 기본 데이터를 생성하고 저장하도록 구현하면 좋습니다.
*   **잘못된 사용자 입력:** 사용자 입력은 항상 검증이 필요합니다. `input()` 함수로 받은 값은 문자열이므로, 숫자가 필요한 경우 `int()` 또는 `float()`로 변환 시 `ValueError`가 발생할 수 있습니다. 이를 `try-except`로 처리하고, 입력 범위를 검증하는 로직을 추가하세요.
*   **객체 직렬화/역직렬화:** `Quiz` 객체를 `state.json`에 저장하려면, `Quiz` 객체를 `dict` 형태로 변환하는 `to_dict()` 메서드가 필요합니다. 반대로 `json.load`로 불러온 딕셔너리를 `Quiz` 객체로 복원하기 위해 `from_dict()` 클래스 메서드를 구현하는 것이 효율적입니다.
*   ** 최고 점수 갱신 로직:** 퀴즈를 풀고 나서 현재 점수가 `best_score`보다 높은 경우에만 `best_score`를 갱신하도록 조건을 명확히 해야 합니다. 또한, `best_score`를 갱신할 때 `state.json`에도 반드시 반영해야 합니다.
*   **Git 충돌:** 여러 사람이 같은 파일을 동시에 수정하고 병합할 때 Git 충돌이 발생할 수 있습니다. 충돌 발생 시, Git이 알려주는 지시를 따라 수동으로 코드를 병합하고 충돌 부분을 해결해야 합니다. `git status`와 `git diff` 명령어로 충돌 지점을 파악하고 수정합니다.
*   ** 코드 재사용:** 입력 검증, 메뉴 출력, 데이터 로드/저장 등 반복적으로 사용되는 로직은 함수나 메서드로 분리하여 `src/utils.py` 등에 관리하면 코드의 가독성과 유지보수성이 향상됩니다.

### 8. 추가 학습 자료

*   **Python 공식 문서:**
    *   `json` 모듈: [https://docs.python.org/ko/3/library/json.html](https://docs.python.org/ko/3/library/json.html)
    *   `random` 모듈: [https://docs.python.org/ko/3/library/random.html](https://docs.python.org/ko/3/library/random.html)
*   **Git 공식 문서 및 튜토리얼:**
    *   [https://git-scm.com/doc](https://git-scm.com/doc)
    *   [https://www.youtube.com/watch?v=3W9PqS-oNys](https://www.youtube.com/watch?v=3W9PqS-oNys) ( 생활코딩 Git)
*   **객체지향 프로그래밍 (OOP) 개념:**
    *   [https://opentutorials.org/course/2507/12577](https://opentutorials.org/course/2507/12577) (생활코딩 OOP)
    *   [https://www.inflearn.com/courses/inflearn-react-deep-dive](https://www.inflearn.com/courses/inflearn-react-deep-dive) (다양한 OOP 관련 강좌 검색)
*   **JSON 관련 자료:**
    *   [https://www.json.org/json-en.html](https://www.json.org/json-en.html)

이 학습 문서를 통해 2주차 과제를 완벽히 이해하고, 앞으로 이어질 학습 과정에서 튼튼한 기반을 다지기를 바랍니다.

| 수강생 | 레포 | 업데이트 | 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-10 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-12 | tier1:quiz_game.py, week-repo:quiz, week-readme:quiz_game, repo:quiz |
| yeowon083 | [quiz-game](https://github.com/yeowon083/quiz-game) | 2026-04-12 | tier2:main.py, tier2:state.json, week-repo:quiz, week-readme:state.json |
| jhkr1 | [Codyssey_mission2](https://github.com/jhkr1/Codyssey_mission2) | 2026-04-11 | tier2:main.py, tier2:state.json, week-readme:quiz, week-readme:state.json |
| yejoo0310 | [codyssey-m2](https://github.com/yejoo0310/codyssey-m2) | 2026-04-10 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| yejibaek12 | [Python-Quiz-Game](https://github.com/yejibaek12/Python-Quiz-Game) | 2026-04-11 | tier2:main.py, tier2:state.json, week-repo:quiz, week-readme:state.json |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |
| leehnmn | [codyssey_2026/project-2](https://github.com/leehnmn/codyssey_2026/tree/main/project-2) | 2026-04-08 | tier1:quiz_game.py, week-readme:quiz, week-readme:quiz_game, readme:quiz |

---

### 3주차

## Codyssey 3주차 과제 학습 자료

### 1. 미션 개요

본 미션은 **Mini NPU Simulator**를 Python으로 구현하여, 컴퓨터가 시각적 패턴을 어떻게 숫자 연산으로 인지하고 판별하는지에 대한 원리를 학습하는 것을 목표로 합니다. 2차원 배열, 필터(Filter), MAC(Multiply-Accumulate) 연산, 라벨 정규화, 부동소수점 비교 정책, 시간 복잡도 분석 등 AI 및 SW 개발의 핵심 개념을 실습을 통해 내재화합니다.

### 2. 학습 목표

이 과제를 통해 학습자는 다음 내용을 이해하고 설명할 수 있어야 합니다.

*   **MAC 연산의 개념 및 원리**: Multiply-Accumulate 연산이 무엇이며, 입력 패턴과 필터를 곱하고 더하여 유사도를 구하는 과정을 설명할 수 있습니다.
*   **데이터 구조 및 규칙 이해**: `data.json` 파일의 키 규칙과 라벨 규칙을 해석하고, 2차원 배열(행렬)의 데이터 구조를 다룰 수 있습니다.
*   **라벨 정규화의 필요성**: 다양한 형태의 라벨 표기를 일관된 내부 표준으로 변환하는 라벨 정규화의 중요성과 필요성을 설명할 수 있습니다.
*   **부동소수점 비교 정책**: `epsilon` 기반 비교가 필요한 이유와 동점 처리 정책의 역할을 이해할 수 있습니다.
*   **시간 복잡도 분석**: 패턴 크기가 커질수록 연산량이 `O(N^2)`로 증가하는 이유를 설명하고, 성능 측정 및 분석 방법을 익힐 수 있습니다.
*   **문제 해결 및 디버깅**: 실패 케이스를 데이터 문제, 스키마 문제, 로직 문제, 수치 비교 문제 등으로 나누어 진단하고 해결할 수 있습니다.

### 3. 기능 요구사항

1.  **MAC 연산 구현**: 주어진 2차원 배열(패턴)과 필터를 이용하여 MAC 연산을 수행하고 유사도 점수를 계산합니다.
2.  **라벨 정규화**: 다양한 형태의 라벨(예: `+`, `cross`, `x`)을 내부 표준 라벨(`Cross`, `X`)로 변환합니다.
3.  **판정 로직**: 계산된 MAC 점수를 기반으로 패턴의 라벨을 판정합니다.
4.  **부동소수점 비교**: `epsilon` 값을 사용하여 부동소수점 연산의 오차를 고려한 비교를 수행하고, 동점(UNDECIDED)을 처리합니다.
5.  **사용자 입력 모드**: 사용자가 직접 3x3 크기의 필터와 패턴을 입력받아 MAC 연산 및 판정을 수행합니다. (선택 사항)
6.  **`data.json` 분석 모드**: `data.json` 파일에서 필터와 패턴 데이터를 로드하여 일괄적으로 MAC 연산, 판정, 결과 비교를 수행합니다.
7.  **스키마 검증**: `data.json` 파일의 구조(키 규칙, 크기 일치 등)를 검증하고, 오류 발생 시 적절하게 처리합니다.
8.  **성능 측정 및 분석**: 각 크기별 MAC 연산에 걸리는 시간을 측정하고, `O(N^2)` 복잡도를 확인할 수 있는 성능 지표를 출력합니다.
9.  **결과 리포트**: 전체 테스트 수, 통과 수, 실패 수, 실패 케이스 목록 및 사유를 요약하여 출력합니다.

### 4. 핵심 기술 스택

*   **Python**: 핵심 프로그래밍 언어
*   **List (2D Array)**: 패턴 및 필터 데이터를 표현하는 기본 자료구조
*   **JSON**: 데이터 파일(`data.json`) 로딩 및 파싱
*   **`sys` 모듈**: 표준 입출력 및 시스템 관련 기능 활용
*   **`json` 모듈**: JSON 파일 처리
*   **`time` 모듈**: 성능 측정 (시간 복잡도 분석)
*   **(선택) `unittest` 또는 `pytest`**: 단위 테스트 작성

### 5. 권장 프로젝트 구조

```
.
├── README.md
├── requirements.txt        # (필요시) 외부 라이브러리 명시
├── data.json               # 필터 및 패턴 데이터
├── main.py                 # 애플리케이션 진입점
├── src/
│   ├── __init__.py
│   ├── core/               # 핵심 로직 (MAC, 판정 등)
│   │   ├── __init__.py
│   │   ├── mac.py          # MAC 연산 구현
│   │   ├── judgement.py    # 판정 로직, epsilon 비교
│   │   └── labels.py       # 라벨 정규화
│   ├── io/                 # 데이터 입출력 및 파싱
│   │   ├── __init__.py
│   │   ├── json_loader.py  # data.json 로딩 및 스키마 검증
│   │   └── console_parser.py # 사용자 입력 파싱
│   ├── app/                # 애플리케이션 흐름 및 UI
│   │   ├── __init__.py
│   │   ├── console_flow.py # 메인 메뉴 및 모드 전환
│   │   ├── report.py       # 결과 리포트 생성
│   │   └── benchmark.py    # 성능 측정 및 분석
│   └── utils/              # 공통 유틸리티 함수
│       ├── __init__.py
│       └── grid_validator.py # 2차원 배열(행렬) 검증
└── tests/                  # 단위 테스트
    ├── __init__.py
    ├── core/
    │   ├── __init__.py
    │   ├── test_mac.py
    │   ├── test_judgement.py
    │   └── test_labels.py
    ├── io/
    │   ├── __init__.py
    │   ├── test_json_loader.py
    │   └── test_console_parser.py
    └── app/
        ├── __init__.py
        └── test_console_flow.py
```

*   `main.py`: 애플리케이션 실행 진입점. `src/app/console_flow.py`의 `run()` 함수 등을 호출합니다.
*   `data.json`: `filters`와 `patterns` 섹션을 포함하는 필터 및 패턴 데이터 파일입니다.
*   `src/core/`: MAC 연산, 판정 로직, 라벨 정규화 등 핵심 비즈니스 로직을 담당합니다.
*   `src/io/`: `data.json` 파일 로딩, 스키마 검증, 사용자 콘솔 입력 파싱 등을 담당합니다.
*   `src/app/`: 사용자 인터페이스, 메뉴 흐름, 결과 리포트 생성, 성능 측정 등 애플리케이션의 전반적인 흐름을 관리합니다.
*   `src/utils/`: 2차원 배열 유효성 검증과 같이 여러 모듈에서 공통으로 사용될 수 있는 유틸리티 함수들을 모아둡니다.
*   `tests/`: 각 모듈별 단위 테스트 코드를 작성하여 코드의 안정성을 확보합니다. `src` 폴더 구조를 미러링하는 것이 일반적입니다.

### 6. 구현 핵심 포인트

1.  **MAC 연산 (`compute_mac`)**:
    *   두 2차원 배열 `pattern`과 `matrix_filter`를 입력받아, 같은 위치의 요소끼리 곱하고 그 결과를 모두 누적합니다.
    *   이중 반복문 (`for row in range(size): for col in range(size):`)을 사용하여 모든 요소를 순회합니다.
    *   `size`는 패턴과 필터의 한 변의 길이를 의미하며, 입력 검증 시 동일해야 합니다.
    *   `score += pattern[row][col] * matrix_filter[row][col]` 와 같이 구현됩니다.

2.  **라벨 정규화 (`normalize_label`)**:
    *   `data.json`의 `expected` 값이나 필터 키(예: `cross`)에서 다양한 표기를 내부 표준 라벨(`Cross`, `X`)로 변환합니다.
    *   예: `+` -> `Cross`, `cross` -> `Cross`, `x` -> `X`.
    *   별도의 함수로 분리하여 코드 중복을 줄이고 유지보수성을 높입니다.

3.  **`data.json` 스키마 검증**:
    *   **필터 섹션**: `filters` 키 아래 `size_<N>` 형태의 키를 확인하고, 해당 값은 `cross` 및 `x` 키를 포함하는 객체인지 검증합니다.
    *   **패턴 섹션**: `patterns` 키 아래 `size_<N>_<idx>` 형태의 키만 허용하며, 여기서 `<N>` 값을 추출합니다.
    *   **크기 일치**: 패턴의 `input` 배열 크기와 추출된 `N`, 그리고 선택된 필터의 크기가 모두 일치하는지 검증합니다. 불일치 시 오류를 발생시키거나 기록합니다.
    *   JSON 로딩 시 `try-except` 블록을 사용하여 파일이 없거나 형식이 잘못된 경우에도 프로그램이 비정상 종료되지 않도록 합니다.

4.  **`epsilon` 기반 비교**:
    *   MAC 연산 결과(점수)를 비교할 때, 단순 `==` 대신 `abs(score_a - score_b) < epsilon`과 같이 `epsilon` 값을 사용하여 부동소수점 오차를 고려합니다.
    *   `epsilon`은 보통 `1e-9` 정도의 작은 값을 사용합니다.
    *   점수 차이가 `epsilon`보다 작으면 동점(`UNDECIDED`)으로 처리합니다.

5.  **성능 측정 (`benchmark`)**:
    *   `time.time()` 또는 `time.perf_counter()`를 사용하여 특정 연산(MAC 계산)의 시작 시간과 종료 시간을 기록합니다.
    *   여러 번 반복 측정한 후 평균 시간을 계산하여 제시합니다.
    *   시간 복잡도 `O(N^2)`를 확인하기 위해, `N`이 커짐에 따라 연산 횟수(`N*N`)와 평균 시간이 어떻게 변화하는지 분석합니다.

6.  **결과 리포트 (`report.py`)**:
    *   각 케이스별 PASS/FAIL 여부, MAC 점수, 판정 라벨, 기대 라벨, 측정 시간 등을 수집합니다.
    *   최종적으로 전체 테스트 수, 통과 수, 실패 수를 집계하고, 실패한 케이스 목록과 실패 사유(스키마 오류, 라벨 불일치, 판정 오류 등)를 명확하게 출력합니다.

7.  **입력 검증 (사용자 입력 모드)**:
    *   3x3 사용자 입력 모드에서 각 줄마다 행/열 개수, 숫자 파싱 가능 여부를 검증합니다.
    *   오류 발생 시 프로그램이 종료되지 않고, 올바른 입력이 들어올 때까지 재입력을 유도하는 방식으로 구현합니다. (예: `while` 루프와 예외 처리 활용)

### 7. 트러블슈팅 & 팁

*   **"동일 위치"의 중요성**: MAC 연산은 반드시 같은 `row`와 `col` 인덱스를 가진 요소끼리만 곱해야 합니다. 인덱싱 실수는 흔한 오류입니다.
*   **JSON 구조 오류**: `data.json` 파일의 구조가 명세와 다르면 `json.JSONDecodeError` 또는 `KeyError` 등이 발생합니다. `try-except`로 예외 처리를 하고, 오류 메시지를 명확히 출력하여 디버깅에 활용하세요.
*   **라벨 표기 불일치**: `data.json`의 `expected` 값이나 필터 키에 오탈자가 있거나, 정규화되지 않은 표기가 있으면 비교에서 실패합니다. 라벨 정규화 함수를 꼼꼼히 테스트하세요.
*   **부동소수점 비교**: `0.1 + 0.2`가 `0.3`이 아닌 경우가 발생하는 것처럼, 부동소수점 연산은 미세한 오차를 포함할 수 있습니다. `epsilon` 비교는 필수입니다.
*   **크기 불일치**: 패턴의 `N` 값, `input` 배열의 행/열 수, 필터 배열의 행/열 수가 일치하지 않으면 `IndexError`나 예상치 못한 결과가 나옵니다. 철저한 입력 검증이 필요합니다.
*   **시간 복잡도 확인**: `N`이 13 또는 25로 커질 때, 연산 시간이 예상대로 `N^2`에 비례하여 증가하는지 확인하는 것이 중요합니다. 만약 선형으로 증가한다면 MAC 연산 구현에 문제가 있을 가능성이 높습니다.
*   **코드 분리**: `main.py`는 단순 진입점으로만 사용하고, 실제 로직(MAC, 파싱, 판정, 리포트 등)은 각각의 모듈(`.py` 파일)로 분리하여 관리하면 가독성과 유지보수성이 크게 향상됩니다.
*   **테스트 코드 작성**: 각 기능별로 `unittest`나 `pytest`를 사용하여 테스트 코드를 작성하는 것을 강력히 권장합니다. 이는 코드 변경 시 예기치 않은 버그 발생을 줄여주고, 기능 구현 후 검증을 용이하게 합니다.
*   **README 활용**: README 파일에 프로젝트 구조, 실행 방법, 각 파일의 역할, 과제 목표 등을 상세히 기술하여 다른 사람(또는 미래의 자신)이 프로젝트를 쉽게 이해하고 활용할 수 있도록 하세요.

### 8. 추가 학습 자료

*   **MAC 연산**:
    *   [Multiply-Accumulate (MAC) Operation](https://www.youtube.com/watch?v=0-1gN0w6Y5c) (YouTube 영상, 영어)
    *   [MAC operation](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation) (Wikipedia, 영어)
*   **2차원 배열/행렬 연산**:
    *   [Python List of Lists (2D Array)](https://www.programiz.com/python-programming/list-of-lists) (Programiz, 영어)
*   **JSON 파싱**:
    *   [Python json module](https://docs.python.org/ko/3/library/json.html) (Python 공식 문서, 한국어)
*   **시간 복잡도**:
    *   [시간 복잡도(Time Complexity)란 무엇인가?](https://www.youtube.com/watch?v=o_L8QG1m-pA) (YouTube 영상, 한국어)
    *   [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation) (Wikipedia, 영어)
*   **AI/NPU 기초**:
    *   [CPU, GPU, NPU의 차이점](https://www.techtarget.com/searchenterprisecpu/definition/CPU-GPU-NPU) (TechTarget, 영어 - 번역기 활용)
    *   [Codyssey 3주차 과제 관련 개념 정리 (대화 요약)](docs/insights/discussion_summary.md) (수강생 mulloc1의 저장소 내 문서 참조 - MAC의 의미, NPU의 역할 이해에 도움)
    *   [CPU, GPU, NPU 차이와 딥러닝에서 NPU를 쓰는 이유](docs/insights/cpu_gpu_npu_deep_learning.md) (수강생 mulloc1의 저장소 내 문서 참조 - NPU의 필요성 이해)

본 학습 자료를 통해 Codyssey 3주차 과제를 완벽히 이해하고 성공적으로 완료하시기를 바랍니다!

| 수강생 | 레포 | 업데이트 | 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-12 | tier1:data.json, tier2:main.py, week-repo:npu, week-readme:mac |
| jhkr1 | [Codyssey_mission3](https://github.com/jhkr1/Codyssey_mission3) | 2026-04-11 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| yejoo0310 | [codyssey-m3](https://github.com/yejoo0310/codyssey-m3) | 2026-04-12 | tier1:mini_npu_simulator.py, tier2:main.py |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-09 | week-repo:npu, week-repo:npu_simulator, week-repo:mini_npu, repo:npu |

---

## 2. 후보/검토 레포 (watchlist 대상)

### 미분류

| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |
| --- | --- | --- | --- | --- |
| ntt65 | [codyssey/e1_2](https://github.com/ntt65/codyssey/tree/main/e1_2) | 2026-04-12 | 0.25 | repo:codyssey, tier2:main.py |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | 0.25 | repo:codyssey, readme:npu, readme:mac, tier2:main.py |
| junhnno | [Codyssey_WorkSpace_Week2](https://github.com/junhnno/Codyssey_WorkSpace_Week2) | 2026-04-11 | 0.25 | week-readme:quiz, week-readme:state.json, repo:codyssey, readme:quiz |
| sungho255 | [codyssey_2](https://github.com/sungho255/codyssey_2) | 2026-04-07 | 0.25 | repo:codyssey, tier2:state.json |
| sungho255 | [codyssey_1](https://github.com/sungho255/codyssey_1) | 2026-04-07 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, readme:mac |
| peachily | [codyssey11-E1](https://github.com/peachily/codyssey11-E1) | 2026-04-09 | 0.25 | repo:codyssey, tier2:main.py, tier2:Dockerfile |
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-09 | 0.25 | week-repo:python_with_git, week-readme:state.json, repo:codyssey, repo:python_with_git |

## 3. 제외된 레거시/파일럿 레포

| 수강생 | 레포 | 업데이트 | 제외 근거 |
| --- | --- | --- | --- |
| doji-kr | [codyssey_day1_bear1](https://github.com/doji-kr/codyssey_day1_bear1) | 2025-07-11 | updated_at:2025-07-11, rule:legacy-hard-cutoff |
