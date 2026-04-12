# Codyssey 과정 분리형 수집 보고서 v3 (2026-04-13)

- 총 수집 건수: 37건
- 2026 본과정 확정: 20건
- 제외된 레거시/파일럿: 1건
- 후보/검토 필요: 16건
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

# AI/SW 교육 과정 Codyssey 1주차 학습 문서: 개발 워크스테이션 구축

## 1. 미션 개요

이번 1주차 미션은 AI/SW 개발을 위한 필수적인 **개발 환경 구축**에 초점을 맞추었습니다. 학습자들은 터미널 기본 명령어 습득, Docker를 활용한 컨테이너 기반 환경 구축, Dockerfile을 이용한 커스텀 이미지 제작, 그리고 포트 매핑, 바인드 마운트, 볼륨 영속성과 같은 핵심 Docker 기능을 실습했습니다. 또한, Git을 활용한 버전 관리 및 GitHub 연동을 통해 협업 가능한 개발 환경의 기초를 다졌습니다.

본 학습 문서는 수강생들의 GitHub 레포지토리 제출 내용을 종합하여, 각 학습 목표 달성을 위한 핵심 내용, 구현 포인트, 그리고 발생 가능한 문제에 대한 해결 방안을 제공합니다.

## 2. 학습 목표

*   **터미널 활용 능력 향상**: 기본적인 파일/디렉토리 조작 및 권한 변경 명령어를 능숙하게 사용합니다.
*   **Docker 기본 개념 이해 및 활용**: Docker 엔진 작동 원리를 이해하고, 이미지/컨테이너 관리, Dockerfile을 통한 커스텀 이미지 빌드 및 실행 방법을 익힙니다.
*   **컨테이너 네트워킹 및 스토리지 이해**: 포트 매핑, 바인드 마운트, 볼륨 영속성의 개념을 이해하고 실제 적용하여 데이터를 관리하는 방법을 학습합니다.
*   **협업 기반 환경 구축**: Git 설정을 완료하고 GitHub와 연동하여 코드 버전 관리 및 협업의 기초를 마련합니다.
*   **문제 해결 능력 강화**: 개발 과정에서 발생하는 일반적인 오류와 트러블슈팅 경험을 통해 문제 해결 능력을 향상시킵니다.

## 3. 기능 요구사항

*   **터미널 기본 명령어**: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm` 등의 명령어를 사용하여 파일 및 디렉토리를 조작할 수 있어야 합니다.
*   **파일/디렉토리 권한**: `chmod` 명령어를 사용하여 파일 및 디렉토리의 읽기, 쓰기, 실행 권한을 변경하고 그 결과를 확인할 수 있어야 합니다.
*   **Docker 기본**: Docker 설치 및 정상 작동 여부를 확인하고, `hello-world`, `ubuntu` 컨테이너를 실행할 수 있어야 합니다.
*   **Dockerfile**: `FROM`, `COPY`, `RUN`, `EXPOSE`, `CMD`, `LABEL`, `ENV` 등의 지시어를 사용하여 커스텀 Docker 이미지를 빌드하고 실행할 수 있어야 합니다.
*   **포트 매핑**: `docker run -p <host_port>:<container_port>` 명령을 사용하여 컨테이너 내부의 서비스를 외부에서 접근 가능하도록 설정할 수 있어야 합니다.
*   **바인드 마운트**: `docker run -v <host_path>:<container_path>` 명령을 사용하여 호스트 디렉토리/파일을 컨테이너 내부로 연결하고, 양방향 동기화가 이루어지는 것을 확인할 수 있어야 합니다.
*   **볼륨 영속성**: `docker volume create` 또는 `docker run -v <volume_name>:<container_path>` 를 사용하여 컨테이너 삭제 후에도 데이터가 유지되는 것을 확인할 수 있어야 합니다.
*   **Git 및 GitHub 연동**: Git 사용자 정보 설정, GitHub Repository 생성 및 연동 (add, commit, push)을 수행할 수 있어야 합니다.
*   **Docker Compose (선택)**: `docker-compose.yml` 파일을 작성하여 여러 컨테이너를 정의하고, `docker-compose up/down/ps` 명령으로 관리할 수 있어야 합니다.

## 4. 핵심 기술 스택

*   **Shell Scripting**: Bash, Zsh 등 (터미널 명령어 활용)
*   **Docker**: Docker Engine, Dockerfile, Docker Compose
*   **Git**: Git CLI
*   **Web Server (예시)**: Nginx
*   **Programming Language (예시)**: HTML (간단한 웹 페이지 서빙)

## 5. 권장 프로젝트 구조

수강생들의 레포지토리를 종합하여 다음과 같은 프로젝트 구조를 권장합니다.

```
your-project-repo/
├── .gitignore        # Git에서 추적하지 않을 파일 목록
├── Dockerfile        # 커스텀 Docker 이미지 빌드 파일
├── docker-compose.yml # Docker Compose 설정 파일 (선택 사항, 멀티 컨테이너 시 유용)
├── .env              # 환경 변수 설정 파일 (예: 포트 번호)
├── README.md         # 프로젝트 설명 및 학습 내용 정리 문서
├── src/              # 애플리케이션 소스 코드 (예: index.html)
│   └── index.html
├── storage/          # Docker Volume 또는 Bind Mount 테스트 데이터 저장용 (예시)
│   └── bind/
│       └── message.txt
└── docs/             # 학습 과정 상세 기록, 스크린샷 등을 위한 폴더 (선택 사항)
    └── logs/
        ├── 1.terminal-operations.md
        ├── 2.permission-lab.md
        └── ...
```

**구조 설명:**

*   **루트 디렉토리**: `Dockerfile`, `docker-compose.yml`, `.env`, `README.md` 등 프로젝트 실행 및 설명에 필요한 핵심 파일들을 위치시켜 명령 실행 편의성을 높입니다.
*   **`src/`**: 웹 서버가 서비스할 정적 파일이나 애플리케이션 소스 코드를 모아둡니다. `Dockerfile`의 `COPY` 명령이나 Bind Mount 시 경로 지정에 용이합니다.
*   **`storage/`**: Docker Volume이나 Bind Mount를 통해 컨테이너 내부와 연결될 데이터를 저장하는 용도로 활용될 수 있습니다.
*   **`docs/`**: 학습 과정에서 수행한 명령어 실행 결과, 스크린샷, 트러블슈팅 기록 등 상세 내용을 정리하는 폴더입니다. README 파일이 너무 길어지는 것을 방지하고 내용을 구조화하는 데 도움이 됩니다.
*   **`.gitignore`**: `.env` 파일, IDE 설정 파일, 로그 파일 등 민감하거나 불필요한 파일들이 Git에 커밋되지 않도록 설정합니다.

## 6. 구현 핵심 포인트

### 6.1 터미널 기본 명령어 & 권한

*   **경로:** `pwd`로 현재 위치를 항상 인지하고, `cd`를 활용하여 원하는 디렉토리로 이동합니다.
*   **파일/디렉토리 조작:** `ls -la`로 상세 목록을 확인하며, `mkdir`, `touch`, `echo`, `cp`, `mv`, `rm`을 적절히 사용합니다. `rm -r`은 디렉토리 삭제 시 사용하며 주의해야 합니다.
*   **권한:** `chmod <권한_숫자> <파일/디렉토리>` 형식으로 사용하며, `rwx` (4, 2, 1)의 조합으로 권한을 설정합니다.
    *   `r`: 읽기 (파일 내용 보기, 디렉토리 목록 보기)
    *   `w`: 쓰기 (파일 내용 수정, 디렉토리 내 파일 생성/삭제)
    *   `x`: 실행 (스크립트 실행, 디렉토리 진입)
    *   **중요**: 파일 자체의 권한보다 **부모 디렉토리의 쓰기 권한**이 파일 삭제 여부를 결정하는 데 더 중요합니다.

### 6.2 Dockerfile 기반 커스텀 이미지

*   **`FROM`**: 어떤 베이스 이미지를 사용할지 지정합니다. (예: `nginx:alpine`)
*   **`COPY`**: 호스트의 파일/디렉토리를 이미지 내부로 복사합니다. (예: `COPY src/ /usr/share/nginx/html/`)
*   **`RUN`**: 이미지 빌드 과정에서 명령어를 실행합니다. (예: `RUN apt-get update && apt-get install -y some-package`)
*   **`EXPOSE`**: 컨테이너가 리스닝할 포트를 명시합니다. (실제 포트 개방은 `docker run -p` 옵션으로)
*   **`CMD`**: 컨테이너 실행 시 기본적으로 실행될 명령어를 지정합니다. (예: `CMD ["nginx", "-g", "daemon off;"]`)
*   **`LABEL`**: 이미지에 메타데이터를 추가합니다.
*   **`ENV`**: 환경 변수를 설정합니다.

**실습 예시:** `nginx:alpine` 이미지를 기반으로 `src/index.html` 파일을 `/usr/share/nginx/html/` 경로에 복사하여 간단한 웹 서버 이미지를 만듭니다.

### 6.3 포트 매핑

*   **`docker run -p <호스트_포트>:<컨테이너_포트>`**: 호스트의 지정된 포트와 컨테이너 내부의 포트를 연결합니다.
    *   예: `docker run -p 8080:80 my-web-image` -> 호스트의 8080 포트로 접속하면 컨테이너의 80 포트에 연결됩니다.
*   **`docker-compose.yml`**: `ports:` 섹션에서 설정합니다.
    ```yaml
    services:
      web:
        image: nginx:alpine
        ports:
          - "8080:80"
    ```
*   **접속 확인**: `curl http://localhost:<호스트_포트>` 또는 웹 브라우저를 통해 접속합니다.

### 6.4 바인드 마운트

*   **`docker run -v <호스트_경로>:<컨테이너_경로>`**: 호스트의 디렉토리나 파일을 컨테이너 내부의 특정 경로에 연결합니다.
    *   **특징**: 호스트 파일/디렉토리가 변경되면 컨테이너에서도 실시간으로 반영됩니다. 개발 중 코드 수정 시 매우 유용합니다.
    *   예: `docker run -v $(pwd)/src:/usr/share/nginx/html my-web-image`
*   **`docker-compose.yml`**: `volumes:` 섹션에서 설정합니다.
    ```yaml
    services:
      web:
        image: nginx:alpine
        volumes:
          - ./src:/usr/share/nginx/html
    ```

### 6.5 볼륨 영속성

*   **`docker volume create <볼륨_이름>`**: Docker가 관리하는 별도의 스토리지 공간을 생성합니다.
*   **`docker run -v <볼륨_이름>:<컨테이너_경로>`**: 생성된 볼륨을 컨테이너 내부 경로에 연결합니다.
    *   **특징**: 컨테이너가 삭제되어도 볼륨에 저장된 데이터는 그대로 유지됩니다. 데이터베이스 데이터, 로그 파일 등 영구적인 저장이 필요한 경우에 사용합니다.
    *   예: `docker volume create my-data`
        `docker run -v my-data:/var/lib/mysql mysql:latest`
*   **`docker-compose.yml`**: `volumes:` 섹션에서 설정합니다.
    ```yaml
    services:
      db:
        image: mysql:latest
        volumes:
          - db_data:/var/lib/mysql

    volumes:
      db_data:
    ```

### 6.6 Git & GitHub 연동

*   **Git 설정**: `git config --global user.name "Your Name"` 및 `git config --global user.email "your.email@example.com"`
*   **Repository 생성**: GitHub에서 새 Repository를 생성합니다.
*   **연동**:
    1.  로컬 프로젝트 디렉토리에서 `git init` (기존 레포는 생략)
    2.  `git remote add origin <GitHub_Repo_URL>`
    3.  `git add .`
    4.  `git commit -m "Initial commit"`
    5.  `git push -u origin main` (또는 `master`)

## 7. 트러블슈팅 & 팁

### 7.1 Docker Daemon 미실행 오류

*   **증상**: `docker ps`, `docker images` 등 Docker 명령 실행 시 "Cannot connect to the Docker daemon..." 오류 발생
*   **원인**: Docker Desktop 또는 OrbStack과 같은 Docker 엔진이 실행되지 않았거나, 접근 권한 문제가 있을 수 있습니다.
*   **해결**:
    1.  Docker Desktop/OrbStack을 실행합니다.
    2.  macOS의 경우, Docker Engine이 정상적으로 실행 중인지 확인합니다.
    3.  간혹 Docker를 재시작하면 문제가 해결될 수 있습니다.
*   **팁**: Docker 명령 실행 전에 항상 Docker 엔진이 활성화되어 있는지 확인하는 습관을 들입니다.

### 7.2 포트 충돌 오류

*   **증상**: `docker run -p 8080:80 ...` 실행 시 "Bind for 0.0.0.0:8080 failed: port is already allocated" 오류 발생
*   **원인**: 호스트의 8080 포트가 다른 프로세스(이전 컨테이너 포함)에 의해 이미 사용 중입니다.
*   **해결**:
    1.  `docker ps -a` 명령으로 현재 실행 중이거나 종료된 컨테이너를 확인하고, 해당 포트를 사용하는 컨테이너를 `docker rm -f <container_id>` 명령으로 제거합니다.
    2.  다른 사용되지 않는 호스트 포트(예: 8081)를 사용하도록 `docker run -p 8081:80 ...` 와 같이 변경합니다.
*   **팁**: 컨테이너 실행 전에 `netstat -tulnp | grep <port_number>` (Linux/macOS) 또는 `Get-NetTCPConnection -LocalPort <port_number>` (PowerShell) 명령으로 해당 포트가 사용 중인지 미리 확인할 수 있습니다.

### 7.3 Dockerfile `COPY` 시 경로 문제

*   **증상**: `Dockerfile`에서 `COPY` 명령으로 파일을 복사했지만, 이미지 빌드 후 해당 파일이 존재하지 않거나 잘못된 위치에 있습니다.
*   **원인**: `Dockerfile`이 있는 디렉토리를 기준으로 상대 경로가 잘못 지정되었거나, `docker build` 명령 시 잘못된 경로로 실행했을 수 있습니다.
*   **해결**:
    1.  `Dockerfile`의 `COPY` 명령은 `Dockerfile`이 위치한 디렉토리를 기준으로 작동합니다. 경로를 정확히 확인합니다. (예: `COPY src/index.html /usr/share/nginx/html/`)
    2.  `docker build .` 명령을 `Dockerfile`이 있는 프로젝트 루트 디렉토리에서 실행해야 합니다.
*   **팁**: `COPY` 명령 전에 `ls` 명령으로 현재 디렉토리를 확인하여 복사하려는 파일/디렉토리가 존재하는지, 경로가 올바른지 확인합니다.

### 7.4 Git Commit 메시지 규칙

*   **팁**: 명확하고 간결한 커밋 메시지는 코드 변경 이력을 추적하고 협업 시 다른 개발자가 코드를 이해하는 데 큰 도움이 됩니다.
    *   첫 줄: 변경 사항을 요약 (50자 이내 권장)
    *   본문: 변경 이유, 상세 내용 등을 설명 (빈 줄로 분리)

### 7.5 민감 정보 관리

*   **팁**: API 키, 비밀번호, 개인 키 등 민감한 정보는 `.env` 파일에 저장하고, `.gitignore` 파일에 `.env`를 추가하여 Git Repository에 포함되지 않도록 관리해야 합니다.

## 8. 추가 학습 자료

*   **[Docker 공식 문서](https://docs.docker.com/)**: 가장 정확하고 상세한 정보를 얻을 수 있습니다.
    *   [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
    *   [Docker CLI reference](https://docs.docker.com/engine/reference/commandline/cli/)
    *   [Docker Compose reference](https://docs.docker.com/compose/reference/)
*   **[Git 공식 문서](https://git-scm.com/doc)**: Git의 모든 기능을 상세하게 설명합니다.
*   **[Shell Scripting Tutorial](https://www.tutorialspoint.com/unix/unix-shell-scripting.htm)**: 터미널 명령어와 스크립트 작성에 대한 기초를 다질 수 있습니다.
*   **[Nginx 공식 문서](https://nginx.org/en/docs/)**: Nginx 웹 서버 설정 및 활용에 대한 정보를 얻을 수 있습니다.

---

이 학습 문서는 수강생들의 제출 내용을 기반으로 작성되었습니다. 학습 중 발생했던 문제나 궁금증에 대한 해결책을 찾고, 앞으로의 학습에 도움이 되기를 바랍니다.

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
| --- | --- | --- | --- |
| mulloc1 | [codyssey_workstation](https://github.com/mulloc1/codyssey_workstation) | 2026-03-31 | week-repo:workstation, week-readme:docker, repo:codyssey, repo:workstation |
| mov-hyun | [e1-1-workstation-setup](https://github.com/mov-hyun/e1-1-workstation-setup) | 2026-04-05 | week-repo:workstation, week-readme:docker, week-repo:setup, repo:workstation |
| clae-dev | [ia-codyssey-Docker](https://github.com/clae-dev/ia-codyssey-Docker) | 2026-04-02 | week-repo:docker, repo:codyssey, repo:docker, readme:docker |
| I-nkamanda | [codyssey2026/Problem1_AI_SW_Setup](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem1_AI_SW_Setup) | 2026-04-09 | week-readme:docker, week-repo:setup, repo:codyssey, readme:docker |

---

### 2주차

## Codyssey 2주차 AI/SW 교육 과정 학습 자료

### 1. 미션 개요

본 문서는 Codyssey 프로그램 2주차 과제 결과물들을 종합하여, 학습자가 퀴즈 게임 개발 과제를 완벽히 이해하고 내재화할 수 있도록 돕기 위해 작성되었습니다.

이번 과제의 핵심은 **Python의 기본 문법 및 객체지향 프로그래밍 개념을 활용하여, 사용자 입력을 처리하고 데이터를 파일에 저장 및 로드하는 콘솔 기반 퀴즈 애플리케이션을 개발**하는 것입니다.

### 2. 학습 목표

*   **Python 기본 문법 복습 및 심화:** 변수, 자료형, 조건문, 반복문, 함수, 클래스 등의 개념을 실제 프로젝트에 적용하며 이해도를 높입니다.
*   **객체지향 프로그래밍(OOP) 이해:** 클래스와 객체를 활용하여 데이터를 캡슐화하고, 관련된 기능을 메서드로 구현하는 방법을 익힙니다.
*   **데이터 지속성 확보:** JSON 파일을 사용하여 애플리케이션의 상태(퀴즈 목록, 최고 점수 등)를 저장하고, 재실행 시 불러오는 방법을 학습합니다.
*   **사용자 입력 처리 및 예외 관리:** `try-except` 구문을 활용하여 프로그램의 안정성을 높이고, 잘못된 사용자 입력에 대한 처리를 구현합니다.
*   **모듈화 및 코드 구조화:** 관련 기능을 별도의 파일이나 클래스로 분리하여 코드의 가독성과 유지보수성을 향상시키는 경험을 합니다.
*   **Git을 활용한 협업 및 버전 관리 (권장):** Git의 기본 명령어(add, commit, push, pull, branch, merge 등)를 사용하여 코드 변경 이력을 관리하고, 기능별 브랜치 개발 및 병합 경험을 쌓습니다.

### 3. 기능 요구사항

*   **메인 메뉴:** 사용자에게 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 최고 점수 확인, 퀴즈 삭제, 프로그램 종료 등 주요 기능을 선택할 수 있는 메뉴를 제공해야 합니다.
*   **퀴즈 풀기:**
    *   저장된 퀴즈를 랜덤하게 선택하여 사용자에게 제시합니다.
    *   문제와 객관식 선택지를 보여주고, 사용자로부터 답을 입력받습니다.
    *   정답/오답 여부를 판별하고, 사용자에게 결과를 알려줍니다.
    *   정답 개수에 따라 점수를 누적하고, 최고 점수를 갱신합니다.
*   **퀴즈 추가:**
    *   사용자가 직접 문제, 4개의 선택지, 정답 번호, (선택적으로) 힌트 내용을 입력받아 새로운 퀴즈를 생성합니다.
*   **퀴즈 목록 확인:**
    *   현재 시스템에 등록된 모든 퀴즈의 목록을 보여줍니다.
    *   (옵션) 퀴즈의 상세 내용(선택지, 정답 등)도 함께 보여줄 수 있습니다.
*   **최고 점수 확인:**
    *   지금까지 달성한 최고 점수와 최고 점수를 획득했을 당시의 정보를 표시합니다.
*   **퀴즈 삭제:**
    *   사용자가 추가한 퀴즈를 선택하여 삭제할 수 있도록 합니다. (기본 제공 퀴즈는 삭제되지 않도록 처리)
*   **데이터 저장 및 로드:**
    *   프로그램 종료 시 퀴즈 목록, 최고 점수 등의 데이터를 `state.json` 파일에 저장합니다.
    *   프로그램 시작 시 `state.json` 파일에서 데이터를 불러와 게임 상태를 복구합니다.
    *   `state.json` 파일이 없거나 손상된 경우, 기본 퀴즈 데이터로 초기화합니다.
*   **입력 유효성 검사:**
    *   메뉴 선택, 퀴즈 답 입력 등 사용자 입력이 유효한 범위나 형식을 벗어날 경우, 적절한 안내 메시지를 출력하고 다시 입력받도록 처리합니다.
*   **안전 종료:**
    *   `KeyboardInterrupt` (Ctrl+C) 또는 `EOFError` (Ctrl+D)와 같은 예외 발생 시, 데이터가 손실되지 않도록 안전하게 프로그램을 종료하고 필요시 데이터를 저장합니다.

### 4. 핵심 기술 스택

*   **프로그래밍 언어:** Python 3.10 이상 권장
*   **핵심 라이브러리:**
    *   `json`: JSON 데이터 형식의 저장 및 로드를 위해 사용
    *   `random`: 퀴즈 순서 섞기, 문제 선택 등을 위해 사용
    *   `os` (선택 사항): 파일 경로 처리 등에 활용 가능
*   **개발 도구:** Git (버전 관리)

### 5. 권장 프로젝트 구조

수강생들의 레포를 종합하여 다음과 같은 프로젝트 구조를 권장합니다.

```
your_quiz_project/
├── .gitignore
├── README.md
├── main.py          # 프로그램 실행 진입점
├── quiz_app/        # 퀴즈 관련 코드 모듈
│   ├── __init__.py
│   ├── quiz.py      # Quiz 클래스 정의 (문제, 선택지, 정답 등)
│   ├── quiz_game.py # QuizGame 클래스 정의 (게임 로직, 메뉴, 데이터 관리)
│   ├── models.py    # (선택 사항) Quiz 클래스가 여기에 포함될 수 있음
│   └── utils.py     # (선택 사항) 입력 처리 등 유틸리티 함수
├── state.json       # 퀴즈 데이터 및 최고 점수 저장 파일
└── docs/            # (선택 사항) 스크린샷, 설계 문서 등
    └── screenshots/
```

**구조 설명:**

*   `main.py`: 프로그램 실행의 시작점 역할을 하며, `QuizGame` 객체를 생성하고 게임을 실행합니다.
*   `quiz_app/` 디렉토리: 퀴즈 게임과 관련된 모든 로직을 담습니다.
    *   `quiz.py` (또는 `models.py`): 퀴즈 데이터 자체를 표현하는 `Quiz` 클래스를 정의합니다. (문제, 선택지, 정답 등의 속성 포함)
    *   `quiz_game.py`: 게임의 전체 흐름, 메뉴 관리, 퀴즈 진행, 데이터 저장/로드, 점수 관리 등을 담당하는 `QuizGame` 클래스를 정의합니다.
    *   `utils.py`: 반복되는 입력 처리 함수, 유효성 검사 함수 등 재사용 가능한 작은 함수들을 모아둡니다.
*   `state.json`: 프로그램 실행 간 데이터의 영속성을 책임지는 파일입니다.
*   `README.md`: 프로젝트 개요, 실행 방법, 기능 설명, 학습 내용 정리 등을 포함하는 문서입니다.
*   `.gitignore`: Git이 추적하지 않을 파일(예: `__pycache__` 디렉토리, `.env` 파일 등)을 명시합니다.

### 6. 구현 핵심 포인트

#### 6.1. `Quiz` 클래스 (데이터 표현)

*   **역할:** 퀴즈 게임의 개별 '문제' 하나를 나타내는 객체를 만들기 위한 설계도입니다.
*   **핵심 속성:**
    *   `question`: 문제 내용 (문자열)
    *   `choices`: 객관식 선택지 목록 (리스트 형태, 문자열)
    *   `answer`: 정답의 인덱스 (정수, 1부터 시작하거나 0부터 시작할 수 있음 - 일관성 유지 중요)
    *   `hint` (선택 사항): 힌트 내용 (문자열)
*   **핵심 메서드:**
    *   `display(self)`: 문제와 선택지를 보기 좋게 출력합니다.
    *   `is_correct(self, user_answer)`: 사용자의 입력(`user_answer`)과 실제 정답(`self.answer`)을 비교하여 맞는지 여부를 반환합니다.
    *   `to_dict(self)`: `Quiz` 객체의 데이터를 JSON 저장을 위해 딕셔너리 형태로 변환합니다.
    *   `from_dict(cls, data)`: 딕셔너리 데이터를 받아 `Quiz` 객체를 생성하는 클래스 메서드입니다. (JSON 로드 시 사용)

#### 6.2. `QuizGame` 클래스 (게임 로직 및 관리)

*   **역할:** 퀴즈 게임 전체의 흐름을 제어하고, 데이터를 관리하는 "게임 운영자" 역할을 합니다.
*   **핵심 속성:**
    *   `quizzes`: 현재 등록된 모든 `Quiz` 객체의 리스트.
    *   `best_score`: 최고 점수 (정수).
    *   `best_correct_count`, `best_total_count` (선택 사항): 최고 점수 당시의 기록.
    *   `state_path`: `state.json` 파일의 경로.
*   **핵심 메서드:**
    *   `__init__(self)`: 객체 생성 시 초기화. `state.json`에서 데이터를 불러오거나(load\_state), 없을 경우 기본 데이터를 설정합니다.
    *   `load_state(self)`: `state.json` 파일을 읽어 `quizzes`와 `best_score` 등의 속성을 복원합니다. JSON 형식이 잘못되었거나 파일이 없을 경우 예외 처리를 통해 초기화하거나 기본 데이터를 설정합니다.
    *   `save_state(self)`: 현재 `quizzes`와 `best_score` 등의 상태를 `state.json` 파일에 저장합니다.
    *   `run(self)`: 메인 메뉴를 반복적으로 보여주고, 사용자 입력에 따라 해당 기능을 실행하는 메인 루프입니다.
    *   `show_menu(self)`: 사용자에게 메뉴 옵션을 출력합니다.
    *   `play_quiz(self)`: 퀴즈 풀이 로직을 담당합니다. 문제 선택, 제시, 답 입력, 채점, 점수 갱신 등을 처리합니다.
    *   `add_quiz(self)`: 사용자로부터 새 퀴즈 정보를 입력받아 `Quiz` 객체를 생성하고 `quizzes` 리스트에 추가합니다.
    *   `show_quiz_list(self)`: `quizzes` 리스트를 순회하며 퀴즈 목록을 출력합니다.
    *   `show_best_score(self)`: `best_score`와 관련된 정보를 출력합니다.
    *   `delete_quiz(self, quiz_index)`: 지정된 인덱스의 퀴즈를 `quizzes` 리스트에서 삭제합니다.
    *   `prompt_number(self, message, min_val=None, max_val=None)`: 사용자로부터 숫자를 입력받고, 유효성 검사(범위 포함)를 수행하여 올바른 숫자를 반환하는 유틸리티 함수로 활용될 수 있습니다.

#### 6.3. 데이터 저장 및 로드 (`state.json`)

*   **JSON 사용 이유:** Python의 기본 자료형(list, dict, str, int, float, bool)과 직관적으로 매핑되어 데이터 구조를 유지하면서 저장/로드하기 편리합니다.
*   **구현:**
    *   **로드 시:** `json.load(file_object)`를 사용하여 JSON 파일을 읽고 Python 객체로 변환합니다. `Quiz` 객체로 변환하기 위해 `Quiz.from_dict()`와 같은 클래스 메서드를 활용합니다. `try-except` 구문으로 파일이 없거나 JSON 형식이 잘못된 경우를 처리합니다.
    *   **저장 시:** `json.dump(python_object, file_object, indent=4)`를 사용하여 Python 객체를 JSON 형식의 문자열로 파일에 씁니다. `indent=4`는 JSON 파일을 사람이 읽기 쉽게 포맷팅합니다. `Quiz` 객체들을 딕셔너리 리스트로 변환하는 과정이 필요합니다.

#### 6.4. 입력 유효성 검사 및 예외 처리

*   **목표:** 사용자가 프로그램의 흐름을 방해하는 잘못된 입력을 하거나, 예상치 못한 상황이 발생해도 프로그램이 정상적으로 작동하도록 합니다.
*   **구현:**
    *   `while` 루프와 `try-except` 구문을 활용합니다.
    *   **숫자 입력:** `int()` 함수로 변환 시 `ValueError` 발생 가능, `try-except`로 처리하고 범위를 체크합니다.
    *   **메뉴 선택:** 입력된 숫자가 유효한 메뉴 번호인지 확인합니다.
    *   **퀴즈 답 입력:** 입력된 값이 1~4 (또는 0~3) 범위의 숫자인지 확인합니다.
    *   **파일/JSON 처리:** `FileNotFoundError`, `json.JSONDecodeError` 등을 `try-except`로 처리합니다.
    *   **안전 종료:** `main.py`에서 `try-except (KeyboardInterrupt, EOFError)`를 사용하여 프로그램 종료 시 `game.save_state()`를 호출하도록 합니다.

#### 6.5. Git 활용 (권장)

*   **목표:** 개발 과정의 이력을 체계적으로 관리하고, 기능별로 코드를 분리하여 개발하며, 협업 시 충돌을 최소화합니다.
*   **핵심 명령어:**
    *   `git init`: 프로젝트 시작 시 Git 저장소 초기화
    *   `git add .`: 변경된 모든 파일을 스테이징 영역에 추가
    *   `git commit -m "설명"`: 변경 이력 저장
    *   `git branch <새 브랜치명>`: 기능 개발을 위한 새 브랜치 생성
    *   `git checkout <브랜치명>`: 브랜치 이동
    *   `git merge <병합할 브랜치명>`: 다른 브랜치의 코드 병합
    *   `git log --oneline --graph`: 브랜치 및 커밋 히스토리 시각화

### 7. 트러블슈팅 & 팁

*   **`__pycache__` 디렉토리:** Python이 모듈을 컴파일하여 생성하는 캐시 파일입니다. `.gitignore`에 `__pycache__/`를 추가하여 Git에서 추적하지 않도록 합니다.
*   **JSON 파일 깨짐:** `state.json` 파일의 형식이 잘못되었거나, 저장 중 오류가 발생하면 JSON 파싱에 실패할 수 있습니다. `load_state` 메서드에서 `try-except json.JSONDecodeError`를 사용하여 이런 경우를 잡아내고, 기본 데이터로 복구하거나 오류 메시지를 출력합니다.
*   **정답 인덱스 불일치:** 퀴즈 선택지가 4개일 때, 사용자 입력(1~4)과 `Quiz` 객체의 `answer` 속성(0~3 또는 1~4) 간의 인덱스 차이로 인해 정답 판별에 오류가 발생할 수 있습니다. `QuizGame` 클래스 내에서 사용자 입력값과 `Quiz` 객체의 `answer` 값을 일관된 기준으로 통일하여 비교해야 합니다. (예: 사용자 입력 1을 `Quiz` 객체의 answer 0과 비교)
*   **객체 vs 딕셔너리:** `json.load()`는 딕셔너리를 반환합니다. 이 딕셔너리를 `Quiz` 객체로 변환하는 과정(`Quiz.from_dict()`)이 필요합니다. 마찬가지로 `Quiz` 객체를 `json.dump()`로 저장하기 전에 딕셔너리 형태로 변환하는 과정(`quiz.to_dict()`)이 필요합니다.
*   **기본 데이터 관리:** `state.json` 파일이 없을 경우, 프로그램이 최소한의 기능이라도 실행될 수 있도록 `__init__` 메서드나 `load_state` 메서드 내에서 기본 퀴즈 데이터와 초기 점수를 설정하는 로직이 필요합니다.
*   **메뉴 입력 처리:** `while True:` 루프 안에서 사용자 입력을 받고, 올바른 입력일 경우 `break`로 루프를 빠져나오고, 잘못된 입력일 경우 `print` 메시지를 출력 후 다시 입력받도록 구현하는 것이 일반적입니다.
*   **선택지 섞기:** 퀴즈를 풀 때마다 선택지 순서를 섞고 싶다면, `random.shuffle()`을 사용하되, 이때 실제 정답의 인덱스도 함께 조정해 주어야 합니다. (이는 `play_quiz` 메서드의 고급 기능으로 구현할 수 있습니다.)

### 8. 추가 학습 자료

*   **Python 공식 문서:**
    *   [Lists](https://docs.python.org/ko/3/tutorial/datastructures.html#lists)
    *   [Classes](https://docs.python.org/ko/3/tutorial/classes.html)
    *   [Input and Output](https://docs.python.org/ko/3/tutorial/inputoutput.html)
    *   [Errors and Exceptions](https://docs.python.org/ko/3/tutorial/errors.html)
    *   [json — JSON encoder and decoder](https://docs.python.org/ko/3/library/json.html)
    *   [random — Pseudo-random number generator algorithms](https://docs.python.org/ko/3/library/random.html)
*   **MDN Web Docs (JSON):** [JSON이란 무엇인가요?](https://developer.mozilla.org/ko/docs/Web/JSON)
*   **Git 공식 문서 및 튜토리얼:**
    *   [Git HandBook](https://guides.github.com/introduction/git-handbook/) (영어)
    *   [Pro Git Book](https://git-scm.com/book/ko/v2) (한국어 번역본)
*   **객체지향 프로그래밍(OOP) 학습 자료:** 다양한 온라인 강의 플랫폼(Inflearn, Coursera 등) 또는 YouTube에서 "Python OOP", "객체지향 프로그래밍" 관련 강의를 찾아 학습할 수 있습니다.

이 학습 문서를 바탕으로 2주차 과제를 성공적으로 마무리하고, Python 및 SW 개발 역량을 한층 더 발전시키시길 바랍니다.

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | tier2:main.py, tier2:state.json, week-readme:quiz, repo:codyssey |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-10 | tier2:main.py, tier2:state.json, tier2:utils.py, week-readme:quiz |
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | tier1:quiz_game.py, tier2:main.py, week-readme:quiz, week-readme:quiz_game |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | tier2:main.py, tier2:state.json, week-readme:quiz, repo:codyssey |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-12 | tier1:quiz_game.py, tier2:main.py, tier2:state.json, week-repo:quiz |
| yeowon083 | [quiz-game](https://github.com/yeowon083/quiz-game) | 2026-04-12 | tier2:main.py, tier2:state.json, week-repo:quiz, repo:quiz |
| jhkr1 | [Codyssey_mission2](https://github.com/jhkr1/Codyssey_mission2) | 2026-04-11 | tier2:main.py, tier2:state.json, week-readme:quiz, repo:codyssey |
| yejoo0310 | [codyssey-m2](https://github.com/yejoo0310/codyssey-m2) | 2026-04-10 | tier1:quiz_game.py, tier2:main.py, tier2:state.json, week-readme:quiz |
| yejibaek12 | [Python-Quiz-Game](https://github.com/yejibaek12/Python-Quiz-Game) | 2026-04-11 | tier2:main.py, tier2:state.json, week-repo:quiz, repo:quiz |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | tier1:quiz_game.py, tier2:main.py, week-readme:quiz, week-readme:quiz_game |
| leehnmn | [codyssey_2026/project-2](https://github.com/leehnmn/codyssey_2026/tree/main/project-2) | 2026-04-08 | tier1:quiz_game.py, tier2:main.py, tier2:state.json, week-readme:quiz |
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-09 | week-repo:python_with_git, repo:codyssey, repo:python_with_git |

---

### 3주차

# Codyssey 3주차 AI/SW 교육 과정 학습 자료

## 1. 미션 개요

본 문서는 Codyssey 프로그램 3주차 과제인 "Mini NPU Simulator"에 대한 학습 자료입니다. 수강생들이 제출한 GitHub 레포지토리 정보를 종합하여 과제의 목표, 요구사항, 핵심 기술, 구현 팁 등을 상세히 다룹니다. 이 자료를 통해 학습자는 2차원 배열 연산, 필터, MAC 연산, 라벨 정규화, 부동소수점 비교 정책, 시간 복잡도 분석 등 주요 개념을 완벽히 이해하고 내재화할 수 있을 것입니다.

## 2. 학습 목표

본 주차 과제를 통해 학습자는 다음 내용을 달성해야 합니다.

*   MAC(Multiply-Accumulate) 연산의 원리를 설명하고 직접 구현할 수 있습니다.
*   2차원 배열 형태의 패턴과 필터를 사용하여 유사도 점수를 계산하는 원리를 이해하고 적용할 수 있습니다.
*   `data.json` 파일의 구조와 규칙(키, 라벨 등)을 해석하고 활용할 수 있습니다.
*   라벨 정규화(Label Normalization)의 필요성과 구현 방법을 이해하고 적용할 수 있습니다.
*   부동소수점 비교 시 epsilon 기반의 비교 정책이 필요한 이유를 이해하고 구현할 수 있습니다.
*   패턴 크기가 커짐에 따라 연산량이 `O(N^2)`으로 증가하는 이유를 설명할 수 있습니다.
*   다양한 실패 케이스(데이터 문제, 스키마 문제, 로직 문제, 수치 비교 문제)를 진단하고 해결 방안을 모색할 수 있습니다.
*   콘솔 애플리케이션의 사용자 입력 처리, JSON 데이터 파싱, 성능 측정 및 결과 리포트 생성 기능을 구현할 수 있습니다.

## 3. 기능 요구사항

*   **MAC 연산 구현**: 2차원 배열 형태의 패턴과 필터를 입력받아 MAC 연산을 수행하고 유사도 점수를 반환해야 합니다.
*   **모드 선택 기능**:
    *   **사용자 입력 모드 (3x3)**: 사용자가 직접 3x3 필터 두 개와 3x3 패턴을 입력받아 MAC 점수를 계산하고 판정 결과를 출력합니다. 이 과정에서 입력 검증(행/열 개수, 숫자 파싱) 및 재입력 처리가 필요합니다.
    *   **JSON 분석 모드**: `data.json` 파일에 정의된 필터와 패턴 데이터를 읽어와 각 케이스별로 MAC 점수 계산, 판정, `expected` 값과의 비교(PASS/FAIL)를 수행합니다.
*   **라벨 정규화**: `data.json`의 `expected` 값(`+`, `cross`, `x` 등)과 필터 키(`cross`)를 내부 표준 라벨(`Cross`, `X`)로 일관되게 변환해야 합니다.
*   **판정 로직**: 두 개의 MAC 점수(`Cross` 필터 점수, `X` 필터 점수)를 비교하여 최종 라벨(`Cross`, `X`)을 결정합니다.
*   **동점 처리 (Epsilon)**: 두 MAC 점수의 차이가 매우 작을 경우(epsilon(`1e-9`) 이하) 동점으로 간주하고 `UNDECIDED` 또는 `판정 불가`로 처리해야 합니다.
*   **성능 측정 및 분석**:
    *   각 모드에서 MAC 연산에 소요되는 시간을 측정합니다.
    *   패턴 크기별(`3x3`, `5x5`, `13x13`, `25x25`) MAC 연산 횟수(`N^2`)와 평균 소요 시간을 표 형태로 출력합니다.
*   **결과 리포트**: JSON 분석 모드 종료 시, 전체 테스트 수, 통과 수, 실패 수, 실패 케이스 목록(패턴 키, 실패 사유)을 요약하여 출력합니다.
*   **입력 검증 및 오류 처리**: JSON 구조 오류, 패턴/필터 크기 불일치, 잘못된 데이터 형식 등 다양한 예외 상황에 대해 프로그램이 비정상 종료되지 않고 적절한 오류 메시지를 출력하도록 처리해야 합니다.

## 4. 핵심 기술 스택

*   **Python**: 프로그래밍 언어
*   **`sys` 모듈**: 프로그램 실행 환경 및 인자 처리
*   **`json` 모듈**: `data.json` 파일 파싱
*   **`time` 모듈**: 성능 측정
*   **2차원 배열 (List of Lists)**: 패턴 및 필터 데이터 표현
*   **MAC 연산**: `sum(pattern[i][j] * filter[i][j])` 구현
*   **정규 표현식 (Regex)**: `data.json`의 패턴 키에서 크기(`N`) 추출
*   **객체 지향 프로그래밍 (OOP)**: 코드의 모듈화 및 구조화 (mulloc1 레포 참조)
*   **예외 처리**: `try-except` 블록을 활용한 오류 관리

## 5. 권장 프로젝트 구조 (mulloc1 레포 기준)

```
python_with_npu/
├── main.py                 # 애플리케이션 진입점
├── data.json               # JSON 분석 모드용 필터·패턴 데이터
├── README.md
├── src/
│   ├── app/                # 콘솔 UI·흐름, 모드별 로직
│   │   ├── __init__.py
│   │   ├── console_flow.py     # 메인 메뉴·모드 라우팅
│   │   ├── user_input_3x3.py   # 3x3 수동 입력 모드
│   │   ├── data_json_mode.py   # data.json 분석 모드
│   │   ├── constants.py        # 앱 상수
│   │   └── report.py           # 결과 요약 생성
│   ├── npu/                # MAC·판정·벤치마크 코어 로직
│   │   ├── __init__.py
│   │   ├── mac.py              # MAC 연산 구현
│   │   ├── grid.py             # 2차원 배열 유효성 검증
│   │   ├── judgement.py        # MAC 점수 비교 판정
│   │   ├── labels.py           # 라벨 정규화
│   │   ├── constants.py        # NPU 관련 상수 (epsilon 등)
│   │   └── benchmark.py        # 성능 측정 및 표 생성
│   └── npu_io/             # JSON/입력 파싱·스키마 검증
│       ├── __init__.py
│       ├── json_loader.py      # data.json 로드
│       ├── schema.py           # 패턴 키 파싱, 필터 매칭, 스키마 검증
│       ├── parse.py            # 콘솔 입력 파싱
│       └── label_normalization.py # 필터 키 표준화
├── tests/                  # 단위 테스트 (src 폴더 구조 미러링)
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   └── ... (app 모듈별 테스트)
│   ├── npu/
│   │   ├── __init__.py
│   │   └── ... (npu 모듈별 테스트)
│   └── npu_io/
│       ├── __init__.py
│       └── ... (npu_io 모듈별 테스트)
└── docs/                   # 과제·커밋·인사이트 관련 문서
    ├── README.md
    ├── subject.md              # 과제 내용
    ├── commit_guidelines.md    # Git 커밋 규칙
    ├── function_conventions.md # 함수 작성 가이드
    ├── implementation_checklist.md # 구현 체크리스트
    ├── testing_guidelines.md   # 테스트 가이드라인
    └── insights/               # 심층 학습 자료
        └── ...
```

## 6. 구현 핵심 포인트

### 6-1. MAC 연산 (`src/npu/mac.py`)

*   **핵심 로직**: `compute_mac(pattern, filter_matrix, size)` 함수 내에서 두 2차원 배열의 같은 위치 값을 곱해 누적합합니다.
*   **입력 검증**: MAC 연산 전에 `validate_mac_inputs` 함수를 사용하여 패턴과 필터가 정사각 행렬인지, 그리고 크기가 같은지 검증합니다 (`src/npu/grid.py`의 `validate_matrix` 활용).
*   **시간 복잡도**: 패턴과 필터의 크기가 `N x N`일 때, 모든 요소를 순회하므로 `O(N^2)`입니다.

### 6-2. 라벨 정규화 (`src/npu/labels.py`, `src/npu_io/label_normalization.py`)

*   **목적**: `data.json`에 다양하게 표현될 수 있는 라벨(예: `+`, `cross`, `x`, `X`)을 내부에서 일관된 표준 라벨(`Cross`, `X`)로 통일합니다.
*   **구현**:
    *   `normalize_expected` (또는 유사 함수): `expected` 값을 `Cross` 또는 `X`로 변환합니다.
    *   `normalize_filter_key` (또는 유사 함수): 필터 키(예: `cross`)를 `Cross`로 변환합니다.
    *   `src/app/data_json_mode.py` 또는 `src/npu_io/schema.py` 등에서 이 정규화 함수를 호출하여 `expected`와 필터 이름을 통일합니다.

### 6-3. 동점 처리 (Epsilon) (`src/npu/judgement.py`, `src/npu/constants.py`)

*   **목적**: 부동소수점 연산의 미세한 오차로 인해 실제로는 같은 점수인데도 미세한 차이로 결과가 달라지는 것을 방지합니다.
*   **구현**: 두 MAC 점수 `score_a`와 `score_b`를 비교할 때, `abs(score_a - score_b) < constants.DEFAULT_EPSILON` (기본값: `1e-9`) 이면 동점으로 처리합니다.
*   **판정**: 동점일 경우 `UNDECIDED` 또는 `판정 불가`로 출력하며, `data.json` 모드에서는 `expected` 값과 일치하지 않으므로 `FAIL`로 집계됩니다.

### 6-4. `data.json` 파싱 및 스키마 검증 (`src/app/data_json_mode.py`, `src/npu_io/json_loader.py`, `src/npu_io/schema.py`)

*   **JSON 로딩**: `json.load()`를 사용하여 `data.json` 파일을 읽습니다.
*   **스키마 구조**:
    *   `filters`: `{ "size_<N>": { "cross": [[...]], "x": [[...]] } }` 형태.
    *   `patterns`: `{ "size_<N>_<idx>": { "input": [[...]], "expected": "..." } }` 형태.
*   **패턴 키 파싱**: `size_<N>_<idx>` 패턴에서 `N`을 추출하기 위해 정규 표현식(`^size_(\d+)_(\d+)$`)을 사용합니다 (`src/npu_io/schema.py`의 `extract_size_from_pattern_key`).
*   **필터 선택**: 추출된 `N` 값을 사용하여 `filters` 객체에서 해당 크기(`size_<N>`)의 필터 묶음을 선택합니다.
*   **데이터 검증**: 패턴의 `input` 배열 크기, 필터 배열 크기가 패턴 키에서 추출된 `N`과 일치하는지 확인합니다. 크기가 다르면 오류 처리합니다.
*   **케이스별 처리**: 각 패턴 케이스(`size_<N>_<idx>`)에 대해 MAC 연산, 판정, `expected`와의 비교를 수행하고 결과를 기록합니다.

### 6-5. 사용자 입력 모드 (3x3) (`src/app/user_input_3x3.py`)

*   **입력 받기**: `input()` 함수를 사용하여 사용자로부터 필터 A, 필터 B, 패턴을 한 줄씩 입력받습니다.
*   **입력 검증 및 재입력**:
    *   각 줄의 길이가 3인지 확인합니다.
    *   각 요소가 유효한 숫자인지(`float`으로 변환 가능한지) 확인합니다.
    *   유효하지 않은 입력 시 오류 메시지를 출력하고, 유효한 입력이 들어올 때까지 해당 줄의 입력을 반복해서 받습니다.
*   **MAC 및 판정**: 검증된 3x3 데이터를 사용하여 MAC 연산을 수행하고, `UNDECIDED`를 포함한 판정 결과를 출력합니다.

### 6-6. 성능 측정 및 리포트 (`src/npu/benchmark.py`, `src/app/report.py`)

*   **시간 측정**: `time.time()` 또는 `time.perf_counter()`를 사용하여 각 연산의 시작과 끝 시간을 기록하고 차이를 계산합니다.
*   **반복 측정**: 정확도를 높이기 위해 MAC 연산을 여러 번 반복 수행한 후 평균 시간을 계산합니다 (kimch0612 레포 참조).
*   **성능 표**: `3x3`, `5x5`, `13x13`, `25x25` 등 크기별로 `N^2` 연산 횟수와 평균 MAC 시간을 표 형태로 보기 좋게 출력합니다.
*   **결과 요약**: JSON 모드 종료 시, `src/app/report.py`에서 전체 테스트 수, 통과/실패 수, 실패 케이스 목록(키, 오류 메시지)을 종합하여 출력합니다.

## 7. 트러블슈팅 & 팁

*   **"NaN" 또는 "Infinity" 결과**: MAC 연산 시 입력 데이터에 `NaN` 또는 `Inf` 값이 포함되어 있거나, 매우 큰 수로 인해 오버플로우가 발생했을 수 있습니다. 입력 데이터를 확인하거나, 연산 중간에 값이 너무 커지지 않도록 주의합니다.
*   **"Floating point comparison mismatch"**: 부동소수점 비교 시 `==` 연산을 직접 사용하면 미세한 오차 때문에 예상치 못한 결과가 나올 수 있습니다. 반드시 epsilon(`1e-9`)을 사용한 비교(`abs(a - b) < epsilon`)를 적용해야 합니다.
*   **"Index out of bounds"**: 패턴과 필터의 크기가 다르거나, 반복문 인덱스 계산이 잘못되었을 때 발생합니다. `size` 변수와 행/열 인덱스(`row`, `col`)를 정확히 확인하고, `validate_matrix` 함수 등을 통해 크기 일치 여부를 철저히 검증하세요.
*   **JSON 파싱 오류**: `data.json` 파일의 문법 오류(따옴표 누락, 쉼표 오류 등) 또는 예상치 못한 데이터 타입은 `json.JSONDecodeError`를 발생시킵니다. `json.loads()` 또는 `json.load()` 사용 시 `try-except`로 감싸고, 오류 메시지를 자세히 확인합니다.
*   **라벨 불일치로 인한 FAIL**: `expected` 값의 `+`가 `Cross`로 제대로 변환되지 않았거나, 필터 키 `cross`가 `Cross`로 통일되지 않아 비교 시 불일치가 발생합니다. 라벨 정규화 로직이 모든 변환 케이스를 처리하는지 `normalize_label` 함수를 철저히 검토해야 합니다.
*   **성능 측정 편차**: 짧은 시간 동안의 측정은 환경에 따라 편차가 클 수 있습니다. 여러 번 반복 실행하여 평균값을 내거나, `timeit`과 같은 라이브러리를 활용하여 신뢰도를 높입니다.
*   **코드 재사용 및 모듈화**: mulloc1 레포의 `src` 디렉토리 구조를 참고하여, MAC 연산, 라벨 정규화, 입력 검증 등 핵심 로직을 별도의 모듈로 분리하고 테스트 코드를 작성하면 유지보수 및 확장이 용이해집니다. `docs/testing_guidelines.md`의 테스트 구조 원칙을 따르는 것이 좋습니다.
*   **실패 원인 분석**: 실패 케이스가 발생했을 때, 무작정 코드를 수정하기보다 **데이터 문제, 스키마 문제, 라벨 문제, 수치 비교 문제** 등으로 나누어 원인을 진단하는 것이 효율적입니다. (jhkr1, mulloc1 README 참조)

## 8. 추가 학습 자료

*   **README.md (수강생 1: jhkr1)**: 과제 전반의 개념 설명, MAC 연산 원리, 2차원 배열, 라벨 정규화, epsilon 비교, 시간 복잡도 분석 등에 대한 상세한 설명이 담겨 있습니다. 과제를 학습용 책처럼 다시 복습하는 데 최적화되어 있습니다.
*   **README.md (수강생 2: kimch0612)**: 프로젝트 개요, 실행 환경, 수행 항목 체크리스트, 사용자 입력 모드 및 JSON 분석 모드 실행 방법, 구현 요약(데이터 구조, MAC 연산, 라벨 정규화, 동점 처리 등)을 상세히 다룹니다. 라벨 정규화 함수 분리의 장점과 확장 시 고려사항 등 심층적인 내용을 포함합니다.
*   **README.md (수강생 3: mulloc1)**: 프로젝트 구조, `data.json` 구조, 결과 리포트(실패 원인 + 복잡도)에 대한 상세한 설명을 제공합니다. 특히 실패 원인을 데이터/스키마, 라벨/표기, 수치/판정으로 분류하여 분석하는 관점이 유용합니다. Git 커밋 규칙(`commit_guidelines.md`), 구현 체크리스트(`implementation_checklist.md`), 테스트 가이드라인(`testing_guidelines.md`) 등 프로젝트 관리 문서도 함께 참고하면 좋습니다.
*   **[학습노트] docs/insights/cpu_gpu_npu_deep_learning.md**: CPU, GPU, NPU의 차이점과 딥러닝에서 NPU를 사용하는 이유에 대한 심층적인 내용을 다룹니다. (mulloc1 레포)
*   **[학습노트] docs/insights/discussion_summary.md**: MAC 연산의 의미, NPU의 역할, 필터와 입력 데이터의 관계 등에 대한 논의를 요약합니다. (mulloc1 레포)

이 자료들을 종합적으로 학습하여 3주차 과제를 성공적으로 완료하시기를 바랍니다.

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-12 | tier1:data.json, tier2:main.py, week-repo:npu, week-readme:mac |
| jhkr1 | [Codyssey_mission3](https://github.com/jhkr1/Codyssey_mission3) | 2026-04-11 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-09 | week-repo:npu, week-repo:npu_simulator, week-repo:mini_npu, repo:codyssey |

---

## 2. 후보 과정 / 미분류 / 혼합 레포

### 미분류

| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |
| --- | --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week1](https://github.com/kimch0612/Codyssey_Week1) | 2026-03-31 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, tier2:Dockerfile |
| sonjehyun123-maker | [Codyssey-w1-E1](https://github.com/sonjehyun123-maker/Codyssey-w1-E1) | 2026-04-03 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, tier2:Dockerfile |
| ntt65 | [codyssey/e1_1](https://github.com/ntt65/codyssey/tree/main/e1_1) | 2026-04-12 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, tier2:Dockerfile |
| ntt65 | [codyssey/e1_2](https://github.com/ntt65/codyssey/tree/main/e1_2) | 2026-04-12 | 0.25 | repo:codyssey, tier2:main.py |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | 0.25 | repo:codyssey, readme:npu, tier2:main.py |
| codewhite7777 | [codyssey_E-1](https://github.com/codewhite7777/codyssey_E-1) | 2026-03-30 | 0.25 | week-readme:workstation, week-readme:docker, week-readme:setup, repo:codyssey |
| jhkr1 | [Codyssey_mission1](https://github.com/jhkr1/Codyssey_mission1) | 2026-04-07 | 0.25 | week-readme:workstation, week-readme:docker, repo:codyssey, readme:workstation |
| junhnno | [Codyssey_WorkSpace_Week2](https://github.com/junhnno/Codyssey_WorkSpace_Week2) | 2026-04-11 | 0.25 | week-readme:quiz, repo:codyssey, readme:quiz, readme:npu |
| junhnno | [Codyssey_WorkSpace_Week1](https://github.com/junhnno/Codyssey_WorkSpace_Week1) | 2026-04-09 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, tier2:Dockerfile |
| sungho255 | [codyssey_2](https://github.com/sungho255/codyssey_2) | 2026-04-07 | 0.25 | repo:codyssey, tier2:state.json |
| sungho255 | [codyssey_1](https://github.com/sungho255/codyssey_1) | 2026-04-07 | 0.25 | week-readme:docker, repo:codyssey, readme:docker |
| yejoo0310 | [codyssey-m3](https://github.com/yejoo0310/codyssey-m3) | 2026-04-12 | 0.25 | repo:codyssey, tier1:mini_npu_simulator.py, tier2:main.py |
| yejoo0310 | [codyssey-m1](https://github.com/yejoo0310/codyssey-m1) | 2026-04-05 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, tier2:Dockerfile |
| leehnmn | [codyssey_2026/project-1](https://github.com/leehnmn/codyssey_2026/tree/main/project-1) | 2026-04-08 | 0.25 | week-readme:docker, repo:codyssey, readme:docker, tier2:Dockerfile |
| peachily | [codyssey11-E1](https://github.com/peachily/codyssey11-E1) | 2026-04-09 | 0.25 | repo:codyssey, tier2:main.py, tier2:Dockerfile |
| ikasoon | [codyssey-e1-1](https://github.com/ikasoon/codyssey-e1-1) | 2026-04-06 | 0.25 | week-readme:workstation, week-readme:docker, repo:codyssey, readme:workstation |

## 3. 제외된 레거시/파일럿 레포

| 수강생 | 레포 | 업데이트 | 제외 근거 |
| --- | --- | --- | --- |
| doji-kr | [codyssey_day1_bear1](https://github.com/doji-kr/codyssey_day1_bear1) | 2025-07-11 | updated_at:2025-07-11, rule:legacy-hard-cutoff |
