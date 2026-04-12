# Codyssey 과정 분리형 수집 보고서 v4 (2026-04-13)

- 총 수집 건수: 37건
- 2026 본과정 확정: 29건
- 제외된 레거시/파일럿: 1건
- 후보/검토 필요: 7건
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

## Codyssey 1주차: AI/SW 개발 워크스테이션 구축 완벽 가이드

이 문서는 Codyssey 프로그램 1주차 과제인 "AI/SW 개발 워크스테이션 구축"에 대한 학습 자료를 종합하여, 여러분이 과제를 완벽하게 이해하고 내재화하는 데 도움을 드리고자 작성되었습니다.

### 1. 미션 개요

본 미션은 AI/SW 개발 환경의 필수 요소인 **터미널(CLI)**, **Docker(컨테이너)**, **Git/GitHub(버전 관리)**를 직접 설정하고 활용하는 과정을 통해, "내 컴퓨터에서만 돌아가는" 문제를 해결하고 누구나 동일한 환경에서 개발, 배포, 디버깅할 수 있는 **재현 가능한 개발 워크스테이션**을 구축하는 것을 목표로 합니다.

### 2. 학습 목표

*   **터미널(CLI) 숙달:** 기본적인 파일 및 디렉토리 조작, 권한 관리 등 터미널 명령어 활용 능력을 향상시킵니다.
*   **Docker 이해 및 활용:** Docker의 기본 개념을 이해하고, 컨테이너 생성, 실행, 관리, 커스텀 이미지 빌드 및 배포 방법을 습득합니다.
*   **Dockerfile 작성:** 간단한 웹 서버를 실행하는 Dockerfile을 작성하고 빌드하는 과정을 익힙니다.
*   **컨테이너 네트워킹:** 포트 매핑을 통해 컨테이너 외부에서 서비스에 접근하는 방법을 이해합니다.
*   **데이터 관리:** 바인드 마운트와 볼륨을 활용하여 컨테이너 외부 파일/디렉토리와 컨테이너 내부의 데이터를 연동하고, 데이터 영속성을 확보하는 방법을 학습합니다.
*   **Git & GitHub 활용:** Git의 기본 설정을 완료하고, VS Code와 GitHub를 연동하여 코드 버전 관리를 시작합니다.
*   **재현 가능한 환경 구축:** 위 기술들을 종합하여 일관성 있는 개발 환경을 구축하는 경험을 쌓습니다.

### 3. 기능 요구사항

1.  **터미널 기본 조작:** `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm` 등 기본 명령어 활용
2.  **권한 변경:** `chmod` 명령어를 사용하여 파일 및 디렉토리 권한을 변경하고 이해합니다.
3.  **Docker 설치 및 점검:** Docker가 제대로 설치되었는지 확인하고 기본적인 명령(`docker version`, `docker info`)을 실행합니다.
4.  **Docker 컨테이너 실행:** `hello-world` 및 `ubuntu`와 같은 기본 이미지를 실행하고 컨테이너 내부를 탐색합니다. (`attach`, `exec`의 차이 이해)
5.  **Dockerfile 기반 이미지 빌드:** 제공된 Nginx 웹 서버 Dockerfile을 기반으로 커스텀 이미지를 빌드합니다.
6.  **포트 매핑:** 빌드된 이미지로 실행된 컨테이너의 특정 포트를 호스트 머신의 포트와 연결하여 외부에서 접근 가능하게 합니다. (최소 2회)
7.  **바인드 마운트:** 호스트 머신의 디렉토리를 컨테이너 내부 디렉토리와 연결하여, 호스트에서의 변경 사항이 컨테이너에 즉시 반영되도록 합니다.
8.  **볼륨 (Volume):** Docker 볼륨을 사용하여 컨테이너 내의 데이터를 영속적으로 저장하고 관리합니다.
9.  **Git & GitHub 연동:** Git의 사용자 정보를 설정하고, VS Code에서 GitHub 저장소에 코드를 Push/Pull 할 수 있도록 연동합니다.
10. **README 작성:** 프로젝트 개요, 실행 환경, 수행 항목, 터미널 조작 로그, 트러블슈팅 등 과제 수행 과정을 상세히 기록합니다.

### 4. 핵심 기술 스택

*   **운영체제 (OS):** macOS (다양한 Shell 환경 포함: bash, zsh)
*   **터미널 (CLI):** Command Line Interface (명령줄 인터페이스)
*   **Docker:** 컨테이너화 플랫폼
*   **Dockerfile:** Docker 이미지를 빌드하기 위한 스크립트
*   **Git:** 분산 버전 관리 시스템
*   **GitHub:** Git 저장소 호스팅 서비스
*   **VS Code:** 코드 에디터 (Git 연동 활용)
*   **Nginx (Optional but common):** 웹 서버 (Dockerfile 예시에서 사용)

### 5. 권장 프로젝트 구조

수강생들의 레포지토리를 종합한 결과, 다음과 같은 구조가 일반적이고 권장됩니다.

```
your-repo-name/
├── README.md              # 프로젝트 설명, 설정, 수행 과정 기록
├── Dockerfile             # 커스텀 Docker 이미지 빌드를 위한 설정 파일
├── app/ (or workstation/, src/) # 애플리케이션 소스 코드 또는 관련 파일
│   ├── index.html         # 간단한 웹 페이지 파일
│   └── ...                # 기타 필요한 파일
├── screenshots/ (Optional) # 과정 중 스크린샷 저장
│   ├── ...
└── docker-compose.yml (Optional) # Docker Compose 설정을 위한 파일 (본 미션의 핵심은 아니나, 다음 단계에서 유용)
```

**설명:**

*   `README.md`: 프로젝트의 모든 정보를 담는 핵심 파일입니다. (필수)
*   `Dockerfile`: Nginx 등의 이미지를 커스터마이징할 때 사용됩니다. (필수)
*   `app/` (또는 유사한 이름의 디렉토리): 웹 서버에서 제공할 `index.html` 파일 등을 저장합니다.
*   `screenshots/`: 각 단계별 결과나 설정을 시각적으로 보여주기 위해 활용됩니다. (선택 사항)
*   `docker-compose.yml`: 여러 컨테이너를 묶어서 관리할 때 유용하지만, 1주차 미션에서는 Dockerfile과 개별 Docker 명령 실행에 집중해도 좋습니다.

### 6. 구현 핵심 포인트

#### 6.1. 터미널 기본 조작

*   **현재 위치 확인:** `pwd`는 현재 작업 중인 디렉토리의 절대 경로를 보여줍니다.
*   **파일/디렉토리 목록:** `ls`는 현재 디렉토리의 내용을 보여주며, `-a` (숨김 파일 포함), `-l` (자세한 정보), `-h` (읽기 쉬운 크기) 옵션을 함께 사용하는 것이 유용합니다.
*   **디렉토리 이동:** `cd [디렉토리명]`으로 이동하고, `cd ..`으로 상위 디렉토리로 이동합니다.
*   **파일/디렉토리 생성:** `mkdir [디렉토리명]`으로 디렉토리를, `touch [파일명]`으로 빈 파일을 생성합니다.
*   **파일 내용:** `cat [파일명]`으로 파일 내용을 출력하고, `echo "[내용]" > [파일명]`으로 파일에 내용을 덮어씁니다. `>>`를 사용하면 내용을 추가할 수 있습니다.
*   **복사/이동/삭제:** `cp` (복사), `mv` (이동/이름 변경), `rm` (삭제) 명령어를 사용합니다. 디렉토리 삭제 시 `-r` 옵션을 사용합니다.

#### 6.2. 권한 변경 (chmod)

`chmod` 명령어는 파일 또는 디렉토리의 권한을 변경합니다.

*   **기본 권한:** `r` (읽기), `w` (쓰기), `x` (실행)
*   **권한 대상:**
    *   `u` (user, 소유자)
    *   `g` (group, 그룹)
    *   `o` (others, 그 외)
    *   `a` (all, 모두)
*   **숫자 표현:** `r=4`, `w=2`, `x=1`로 각 권한에 숫자를 부여하고, 이를 합산하여 3자리 숫자로 표현합니다.
    *   `755`: 소유자는 읽기/쓰기/실행 (4+2+1=7), 그룹과 그 외는 읽기/실행 (4+1=5) - **스크립트 실행에 자주 사용**
    *   `644`: 소유자는 읽기/쓰기 (4+2=6), 그룹과 그 외는 읽기 (4) - **일반 파일에 많이 사용**

**예시:**
```bash
chmod 755 my_script.sh  # my_script.sh 파일에 실행 권한 부여
chmod u+x another_script.sh # another_script.sh 파일에 소유자만 실행 권한 추가
```

#### 6.3. Dockerfile 작성 및 빌드

*   **`FROM`:** 기반 이미지를 지정합니다. (예: `FROM nginx:latest`, `FROM nginx:alpine`)
*   **`COPY`:** 호스트 머신의 파일을 이미지 안으로 복사합니다. (예: `COPY ./app/index.html /usr/share/nginx/html/index.html`)
*   **`EXPOSE`:** 컨테이너가 해당 포트를 사용함을 나타냅니다. (실제 포트 개방은 `docker run`에서)
*   **`LABEL`:** 이미지에 메타데이터를 추가합니다. (선택 사항)
*   **`ENV`:** 환경 변수를 설정합니다. (선택 사항)

**빌드 명령어:**
```bash
docker build -t my-custom-nginx:v1 .
```
*   `-t`: 이미지 이름과 태그를 지정합니다.
*   `.`: Dockerfile이 있는 현재 디렉토리를 지정합니다.

#### 6.4. Docker 컨테이너 실행

*   **기본 실행:** `docker run [이미지명]`
*   **포트 매핑:** `docker run -p [호스트포트]:[컨테이너포트] [이미지명]`
    *   예: `docker run -p 8080:80 my-custom-nginx:v1` (호스트 8080 포트를 컨테이너 80 포트와 연결)
*   **바인드 마운트:** `docker run -v [호스트경로]:[컨테이너경로] [이미지명]`
    *   예: `docker run -v $(pwd)/app:/usr/share/nginx/html my-custom-nginx:v1` (현재 디렉토리의 `app` 폴더를 컨테이너의 `/usr/share/nginx/html`과 연결)
*   **볼륨:** `docker run -v [볼륨이름]:[컨테이너경로] [이미지명]`
    *   볼륨은 Docker가 관리하는 영역에 데이터를 저장하여 영속성을 보장합니다.
    *   예: `docker run -v my-data-volume:/usr/share/nginx/html my-custom-nginx:v1`
*   **백그라운드 실행:** `-d` 옵션을 추가합니다. (예: `docker run -d -p 8080:80 my-custom-nginx:v1`)
*   **컨테이너 연결 (attach/exec):**
    *   `docker attach [컨테이너ID]`: 컨테이너의 표준 입출력에 직접 연결합니다. (컨테이너 종료 시 같이 종료될 수 있음)
    *   `docker exec -it [컨테이너ID] [명령어]`: 실행 중인 컨테이너 안에서 새로운 명령을 실행합니다. (`-it`는 대화형 터미널을 의미)
        *   예: `docker exec -it my-running-container bash` (컨테이너 안에서 bash 쉘 실행)

#### 6.5. Git & GitHub 연동

1.  **Git 전역 설정:**
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```
2.  **새로운 저장소 생성:**
    ```bash
    git init
    ```
3.  **파일 스테이징:**
    ```bash
    git add .  # 모든 변경 사항 스테이징
    git add [파일명] # 특정 파일 스테이징
    ```
4.  **커밋:**
    ```bash
    git commit -m "Your commit message"
    ```
5.  **GitHub 저장소 생성:** GitHub 웹사이트에서 새로운 Repository를 생성합니다.
6.  **원격 저장소 연결:**
    ```bash
    git remote add origin [GitHub 저장소 URL]
    ```
7.  **Push:**
    ```bash
    git push -u origin main (또는 master)
    ```
    *   `-u` 옵션은 다음 push부터 `git push`만 사용해도 자동으로 origin main으로 푸시하도록 설정합니다.

### 7. 트러블슈팅 & 팁

*   **`echo "..." > file.txt` 오류:** `echo` 명령어 사용 시, 쉘의 히스토리 확장 기능 때문에 `!` 문자가 포함된 경우 오류가 발생할 수 있습니다. 이 경우, 문자열을 작은 따옴표(`'`)로 감싸면 문제를 해결할 수 있습니다. (예: `echo 'this is a test!' > test.txt`)
*   **Docker 권한 문제 (macOS):** Docker Desktop을 설치하면 일반적으로 권한 문제가 해결됩니다. 만약 권한 문제가 발생한다면 Docker Desktop 설정을 확인하거나, Docker 데몬 재시작을 시도해 보세요.
*   **컨테이너 실행 후 바로 종료:** `nginx`와 같은 웹 서버 이미지는 실행 후에도 계속 동작하지만, `ubuntu`와 같이 단순한 이미지로 `docker run`만 하면 즉시 종료될 수 있습니다. 이 경우, `docker run -it ubuntu bash`와 같이 대화형 모드로 실행하여 쉘을 유지하거나, `docker run -d ubuntu sleep infinity`와 같이 무한 루프를 실행시켜 컨테이너를 유지할 수 있습니다.
*   **포트 충돌:** 이미 사용 중인 호스트 포트를 컨테이너에 매핑하려고 할 때 오류가 발생합니다. 다른 포트 번호로 변경하여 시도해 보세요. (예: `-p 8081:80`)
*   **바인드 마운트 경로 오류:** 호스트 경로가 존재하지 않거나 오타가 있는 경우 제대로 마운트되지 않습니다. `$(pwd)`를 사용하여 현재 작업 디렉토리를 기준으로 경로를 지정하는 것이 안전합니다.
*   **`docker ps` 명령어:** 실행 중인 컨테이너 목록을 보여줍니다. `-a` 옵션을 사용하면 종료된 컨테이너까지 모두 볼 수 있습니다.
*   **`docker logs [컨테이너ID]`:** 컨테이너에서 발생하는 로그를 확인할 때 유용합니다.
*   **README 작성:** 각 명령어를 실행한 결과와 스크린샷을 함께 첨부하면 이해도를 높이는 데 큰 도움이 됩니다. 특히 터미널 조작 로그는 각 명령어의 의미와 변화를 명확히 보여주는 좋은 자료가 됩니다.

### 8. 추가 학습 자료

*   **Docker 공식 문서:**
    *   [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
    *   [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)
    *   [Volumes](https://docs.docker.com/storage/volumes/)
*   **Git 공식 문서:**
    *   [Git User Manual](https://git-scm.com/doc)
*   **터미널 명령어 Cheat Sheet:**
    *   [Linux Command Line Cheat Sheet](https://www.cheatography.com/big-w/cheat-sheets/linux-command-line/)
    *   [macOS Terminal Commands](https://www.codecademy.com/articles/command-line-basics)

이 가이드가 Codyssey 1주차 미션을 성공적으로 완료하는 데 든든한 밑거름이 되기를 바랍니다. 각자의 레포지토리에서 시행착오를 겪으며 배우는 과정 자체가 가장 값진 경험이 될 것입니다. 화이팅!

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
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

## Codyssey 2주차 AI/SW 교육 과정 학습 문서

### 1. 미션 개요

본 문서는 Codyssey 프로그램 2주차 과제 수행을 위한 학습 자료를 정리한 것입니다. 수강생들이 개발한 콘솔 기반 퀴즈 게임 프로젝트를 바탕으로, 과제의 핵심 내용을 명확히 이해하고 관련 기술을 내재화할 수 있도록 구성되었습니다.

주요 목표는 **Python의 객체 지향 프로그래밍(OOP) 개념, 파일 입출력, 데이터 직렬화/역직렬화, 그리고 Git 버전 관리 시스템의 활용**을 학습하고 실제 프로젝트에 적용하는 것입니다.

### 2. 학습 목표

*   **Python 기본 문법 숙지:** 변수, 자료형, 조건문, 반복문, 함수 등 Python의 핵심 요소들을 복습하고 활용 능력을 향상시킵니다.
*   **객체 지향 프로그래밍(OOP) 이해 및 적용:** 클래스, 객체, `__init__` 메서드, `self`의 역할을 정확히 이해하고, `Quiz`와 `QuizGame`과 같은 클래스를 설계 및 구현합니다.
*   **데이터 지속성 구현:** 프로그램 종료 후에도 데이터가 유지되도록 `state.json` 파일을 활용하여 퀴즈 데이터와 최고 점수를 저장하고 불러오는 기능을 구현합니다.
*   **JSON 데이터 처리:** JSON 형식의 데이터 구조를 이해하고, Python의 `json` 모듈을 사용하여 데이터를 직렬화(Python 객체 -> JSON 문자열) 및 역직렬화(JSON 문자열 -> Python 객체)하는 방법을 익힙니다.
*   **에러 처리 및 안정성 확보:** `try-except` 구문을 활용하여 `KeyboardInterrupt`, `EOFError`와 같은 예외 상황을 안전하게 처리하고 프로그램의 안정성을 높입니다.
*   **Git 버전 관리 시스템 활용:** Git을 사용하여 코드 변경 이력을 관리하고, 브랜치 생성, 커밋, 병합 등의 기본적인 워크플로우를 실습합니다.
*   **프로젝트 구조 설계:** 코드의 가독성과 유지보수성을 높이기 위해 모듈별, 기능별로 파일을 분리하고 적절한 디렉토리 구조를 설계합니다.

### 3. 기능 요구사항

*   **메인 메뉴 제공:** 사용자에게 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 최고 점수 확인, 퀴즈 삭제, 종료 등의 기능을 선택할 수 있는 메뉴를 제공해야 합니다.
*   **퀴즈 풀기:**
    *   저장된 퀴즈를 랜덤하게 선택하여 사용자에게 제시합니다.
    *   사용자는 숫자(예: 1~4)로 답을 입력합니다.
    *   정답 여부를 판별하고 점수를 누적합니다.
    *   (선택 사항) 힌트 기능을 제공할 수 있습니다.
    *   (선택 사항) 문제 및 선택지의 순서를 랜덤하게 섞을 수 있습니다.
*   **퀴즈 추가:** 사용자가 직접 새로운 퀴즈 문제, 선택지 4개, 정답 번호, (선택 사항) 힌트를 입력하여 게임에 추가할 수 있어야 합니다.
*   **퀴즈 목록 확인:** 현재 저장된 모든 퀴즈의 목록을 확인할 수 있어야 합니다.
*   **최고 점수 확인:** 게임을 통해 달성한 최고 점수를 출력해야 합니다.
*   **퀴즈 삭제:** 사용자가 추가한 퀴즈를 목록에서 삭제할 수 있어야 합니다. (기본 제공 퀴즈는 삭제되지 않도록 구현할 수 있습니다.)
*   **데이터 저장 및 복구:**
    *   프로그램 종료 시 퀴즈 데이터와 최고 점수를 `state.json` 파일에 저장합니다.
    *   프로그램 시작 시 `state.json` 파일에서 데이터를 불러옵니다.
    *   `state.json` 파일이 없거나 손상된 경우, 기본 퀴즈 데이터로 초기화하고 저장합니다.
*   **입력 유효성 검사:** 사용자가 숫자가 아닌 값을 입력하거나 범위를 벗어난 숫자를 입력하는 경우, 적절한 안내 메시지를 출력하고 재입력을 요구해야 합니다.
*   **안전 종료:** `KeyboardInterrupt` (Ctrl+C) 또는 `EOFError` (Ctrl+D) 와 같은 예외 발생 시, 데이터를 안전하게 저장하고 프로그램을 종료해야 합니다.

### 4. 핵심 기술 스택

*   **프로그래밍 언어:** Python
*   **주요 Python 라이브러리:**
    *   `json`: JSON 데이터 처리 (데이터 저장/불러오기)
    *   `random`: 퀴즈 순서 섞기, 문제 선택
    *   `sys`: 프로그램 종료 (`sys.exit()`)
*   **데이터 저장 형식:** JSON
*   **버전 관리:** Git

### 5. 권장 프로젝트 구조

수강생들의 레포지토리를 종합하여 다음과 같은 프로젝트 구조를 권장합니다.

```
your_project_root/
├── .gitignore
├── README.md
├── main.py            # 프로그램 실행 진입점
├── quiz_app/          # 또는 src/ 등
│   ├── __init__.py
│   ├── models.py      # Quiz 클래스 등 데이터 모델 정의
│   ├── game.py        # QuizGame 클래스 등 게임 로직 구현
│   ├── utils.py       # 입력 처리, 데이터 로드/저장 등 공통 유틸리티 함수
│   └── ...            # 필요한 추가 모듈
├── state.json         # 게임 데이터 저장 파일
└── docs/              # (선택 사항) 스크린샷, 추가 문서
    └── screenshots/
```

**구조 설명:**

*   **`main.py`**: 프로그램의 시작점 역할을 하며, `QuizGame` 객체를 생성하고 게임의 메인 루프를 실행합니다.
*   **`quiz_app/` (또는 `src/`)**: 애플리케이션의 소스 코드를 모아두는 디렉토리입니다.
    *   **`models.py`**: 퀴즈 문제 자체를 표현하는 `Quiz` 클래스와 같이, 데이터 구조를 정의하는 모듈입니다.
    *   **`game.py`**: 게임의 전체 로직을 관리하는 `QuizGame` 클래스와 같은 핵심 게임 로직을 담습니다.
    *   **`utils.py`**: 여러 모듈에서 공통적으로 사용되는 함수(예: 사용자 입력값 검증, JSON 파일 입출력)를 모아두어 코드 재활용성을 높입니다.
*   **`state.json`**: 프로그램의 상태(퀴즈 목록, 최고 점수 등)를 저장하는 파일입니다.
*   **`.gitignore`**: Git이 추적하지 않아야 할 파일/디렉토리(예: `__pycache__`, `.env`)를 명시합니다.

### 6. 구현 핵심 포인트

1.  **`Quiz` 클래스 설계:**
    *   **목적:** 퀴즈 문제 하나를 구조화하여 관리합니다.
    *   **속성:** `question` (문제 내용), `choices` (선택지 리스트), `answer` (정답 번호) 등을 가집니다.
    *   **메서드:**
        *   `display()`: 문제를 형식에 맞게 출력합니다.
        *   `is_correct(user_answer)`: 사용자의 입력이 정답인지 판별합니다.
        *   `to_dict()`: JSON 저장을 위해 객체를 딕셔너리 형태로 변환합니다. (또는 `from_dict()` 메서드를 통해 딕셔너리에서 객체를 복원)

2.  **`QuizGame` 클래스 설계:**
    *   **목적:** 게임 전체의 상태를 관리하고, 메뉴 기반 인터페이스를 처리하며, 퀴즈 풀이, 추가, 삭제 등의 주요 기능을 수행합니다.
    *   **속성:** `quizzes` (등록된 `Quiz` 객체들의 리스트), `best_score` (최고 점수), `state_path` (저장 파일 경로) 등을 가집니다.
    *   **메서드:**
        *   `__init__(self, state_path)`: 객체 초기화, 데이터 로드, 기본 퀴즈 설정.
        *   `load_state(self)`: `state.json` 파일에서 데이터를 불러와 `self.quizzes`와 `self.best_score`를 채웁니다. 파일이 없거나 유효하지 않으면 기본 데이터를 설정합니다.
        *   `save_state(self)`: 현재 `self.quizzes`와 `self.best_score`를 `state.json` 파일에 저장합니다.
        *   `run(self)`: 메인 메뉴 루프를 실행합니다.
        *   `show_menu(self)`: 메뉴 옵션을 출력합니다.
        *   `play_quiz(self)`: 퀴즈 풀이 로직을 진행합니다.
        *   `add_quiz(self)`: 새로운 퀴즈를 사용자로부터 입력받아 `self.quizzes`에 추가합니다.
        *   `show_quiz_list(self)`: `self.quizzes`에 있는 퀴즈 목록을 출력합니다.
        *   `show_best_score(self)`: `self.best_score`를 출력합니다.
        *   `delete_quiz(self)`: 퀴즈 삭제 기능을 구현합니다.
        *   `prompt_number(self, message, min_val, max_val)` (또는 `utils.py`에 별도 함수): 사용자로부터 유효한 숫자 입력을 받는 공통 로직을 처리합니다.

3.  **데이터 저장 및 불러오기 (`state.json`):**
    *   **`json` 모듈 활용:** `json.dump()` 함수로 Python 객체(리스트, 딕셔너리)를 JSON 파일로 저장하고, `json.load()` 함수로 JSON 파일에서 Python 객체로 불러옵니다.
    *   **구조:** JSON 파일은 일반적으로 퀴즈 목록을 담는 `quizzes` 키와 최고 점수를 담는 `best_score` 키를 가진 딕셔너리 형태로 저장됩니다.
        ```json
        {
          "quizzes": [
            {"question": "...", "choices": ["...", "..."], "answer": 1},
            ...
          ],
          "best_score": 5
        }
        ```
    *   **예외 처리:** `FileNotFoundError` (파일 없음), `json.JSONDecodeError` (파일 손상) 등을 `try-except` 블록으로 처리하여 안전하게 초기 데이터를 설정하도록 합니다.

4.  **예외 처리 (`try-except`):**
    *   **`main.py`:** `QuizGame`의 `run()` 메서드를 `try-except (KeyboardInterrupt, EOFError)` 블록으로 감싸 안전 종료를 구현합니다.
    *   **입력 처리:** 숫자 변환 시 `ValueError`를 처리하여 유효하지 않은 입력에 대응합니다.

5.  **Git 워크플로우:**
    *   **초기 설정:** `git init`, `git add .`, `git commit -m "Initial commit"`
    *   **기능 개발:** 각 기능을 구현할 때마다 `git branch <feature_name>`, `git checkout <feature_name>`으로 새 브랜치를 만들고, 코드를 작성한 후 `git add .`, `git commit -m "feat: <기능 설명>"`으로 커밋합니다.
    *   **병합:** 기능 구현 완료 후 `git checkout main` (또는 `master`), `git merge <feature_name>`으로 메인 브랜치에 병합합니다.
    *   **원격 저장소:** `git push origin main` (또는 `master`)으로 원격 저장소에 반영합니다.

### 7. 트러블슈팅 & 팁

*   **`state.json` 파일이 생성되지 않아요:** `save_state()` 함수가 제대로 호출되지 않았거나, 파일 쓰기 권한 문제가 있을 수 있습니다. `QuizGame` 객체가 생성된 후 `run()` 메서드 호출 전후, 또는 프로그램 종료 직전에 `save_state()`가 실행되는지 확인하세요.
*   **`json.load()` 시 `FileNotFoundError` 발생:** `state.json` 파일의 경로가 올바른지 확인하세요. `QuizGame` 클래스에서 `state_path`를 초기화할 때 현재 작업 디렉토리 기준으로 올바르게 설정되었는지 확인해야 합니다.
*   **`JSONDecodeError` 발생:** `state.json` 파일의 형식이 올바르지 않아 발생합니다. 파일 내용을 직접 열어보거나, `json.loads()` 시 `try-except json.JSONDecodeError`로 감싸서 빈 딕셔너리 등으로 초기화하는 방법을 사용하세요.
*   **퀴즈 삭제 후 `state.json`에 반영되지 않아요:** `delete_quiz()` 메서드 실행 후 `save_state()` 함수를 호출하여 변경 사항을 파일에 저장해야 합니다.
*   **랜덤 퀴즈 출력이 항상 같아요:** `random.sample()` 또는 `random.shuffle()` 함수를 `play_quiz()` 메서드 시작 부분에서 호출하여 퀴즈 목록을 섞어주는지 확인하세요.
*   **클래스 간의 데이터 전달이 어려워요:** `QuizGame` 클래스가 `Quiz` 객체들을 리스트로 관리하도록 설계하고, `Quiz` 객체는 자신의 데이터만 가지고 있도록 하는 것이 좋습니다. `QuizGame`이 `Quiz` 객체에 메서드를 호출하는 방식으로 상호작용합니다.
*   **`self`가 `NameError`를 일으켜요:** `self`는 클래스 내부 메서드에서만 유효합니다. 클래스 외부에서 함수를 정의하고 호출할 경우 `self`를 전달해야 하거나, 해당 함수를 클래스 내부 메서드로 옮겨야 합니다.
*   **Git 병합 시 충돌이 발생해요:** 여러 브랜치에서 같은 파일의 같은 부분을 수정했을 때 발생합니다. 충돌이 발생한 파일을 열어 수정 내용을 직접 확인하고, 원하는 코드를 남긴 후 `git add` 및 `git commit`으로 병합을 완료해야 합니다.

### 8. 추가 학습 자료

*   **Python 공식 문서 - JSON 인코딩 및 디코딩:**
    [https://docs.python.org/ko/3/library/json.html](https://docs.python.org/ko/3/library/json.html)
*   **Python 공식 문서 - `random` 모듈:**
    [https://docs.python.org/ko/3/library/random.html](https://docs.python.org/ko/3/library/random.html)
*   **Python 공식 문서 - `sys` 모듈:**
    [https://docs.python.org/ko/3/library/sys.html](https://docs.python.org/ko/3/library/sys.html)
*   **Git 공식 문서:**
    [https://git-scm.com/doc](https://git-scm.com/doc)
*   **점프 투 파이썬 - 클래스와 객체:**
    [https://wikidocs.net/24](https://wikidocs.net/24)
*   **점프 투 파이썬 - 파일 입출력:**
    [https://wikidocs.net/20](https://wikidocs.net/20)
*   **점프 투 파이썬 - 예외 처리:**
    [https://wikidocs.net/21](https://wikidocs.net/21)

본 학습 문서를 통해 2주차 과제를 성공적으로 완수하시고, Python 프로그래밍 역량을 한 단계 더 발전시키시기를 바랍니다.

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
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

## Codyssey 3주차 AI/SW 교육 과정 학습 자료

### 1. 미션 개요

본 미션은 Python 콘솔 애플리케이션을 통해 "Mini NPU Simulator"를 구현하는 것입니다. 핵심은 사람이 직관적으로 인식하는 `십자가(Cross)`와 `X` 패턴을 컴퓨터가 **2차원 배열, 필터(Filter), MAC(Multiply-Accumulate) 연산, 라벨 정규화, 부동소수점 비교 정책** 등을 활용하여 어떻게 숫자 연산으로 판별하는지를 이해하는 것입니다. 이를 통해 딥러닝 연산의 근간이 되는 MAC 연산의 원리를 내재화하고, 실제 개발 과정에서 마주치는 데이터 스키마 검증, 입력값 처리, 결과 판정 및 성능 분석 등 다양한 소프트웨어 개발 요소를 학습합니다.

### 2. 학습 목표

본 주차 과제를 완료하면 다음과 같은 내용을 스스로 설명하고 적용할 수 있습니다.

*   **MAC 연산의 원리**: 입력 패턴과 필터의 대응 위치 값을 곱하고 누적 합하는 과정을 설명할 수 있습니다.
*   **패턴 판별의 기본 원리**: MAC 연산을 통해 계산된 유사도 점수를 바탕으로 기준 패턴과의 유사성을 판단하는 방법을 이해합니다.
*   **데이터 형식 이해**: `data.json` 파일의 키 규칙, 패턴 및 필터 데이터 구조를 해석하고, 이를 코드에서 어떻게 활용하는지 이해합니다.
*   **라벨 정규화의 필요성**: 다양한 형태의 라벨(예: `+`, `cross`, `x`)을 일관된 내부 표현(예: `Cross`, `X`)으로 통일하는 이유와 방법을 설명할 수 있습니다.
*   **부동소수점 비교 정책**: `epsilon` 기반 비교가 왜 필요한지, 그리고 이를 통해 동점(undecided) 상황을 어떻게 처리하는지 이해합니다.
*   **시간 복잡도 분석**: 패턴 크기가 커짐에 따라 MAC 연산량이 `O(N^2)`으로 증가하는 이유를 설명할 수 있습니다.
*   **문제 진단 능력**: 실패 케이스를 데이터 문제, 스키마 문제, 로직 문제, 수치 비교 문제 등으로 분류하고 진단하는 능력을 함양합니다.

### 3. 기능 요구사항

*   **MAC 연산 구현**: 주어진 2차원 배열 형태의 입력 패턴과 필터를 사용하여 MAC 연산을 수행하고 유사도 점수를 계산해야 합니다.
*   **패턴 판별 로직**: 계산된 MAC 점수를 기반으로 입력 패턴이 `Cross`인지 `X`인지, 또는 판정 불가(`UNDECIDED`)인지 판별하는 로직을 구현해야 합니다.
*   **데이터 처리**: `data.json` 파일에서 필터와 패턴 데이터를 읽어와 처리할 수 있어야 합니다.
*   **라벨 정규화**: 다양한 형태의 입력 라벨을 표준화된 내부 라벨로 변환하는 기능을 구현해야 합니다.
*   **부동소수점 비교**: `epsilon` 값을 사용하여 부동소수점 오차를 고려한 비교 및 판정을 수행해야 합니다.
*   **성능 측정 및 분석**: 각 패턴 처리 시 MAC 연산에 소요되는 시간을 측정하고, 패턴 크기에 따른 시간 복잡도(`O(N^2)`)를 보여주는 성능 분석 기능을 구현해야 합니다.
*   **결과 리포트**: 전체 테스트 케이스에 대한 요약 정보(총 테스트 수, 통과 수, 실패 수, 실패 케이스 목록)를 제공해야 합니다.
*   **사용자 입력 모드 (선택 사항)**: 3x3 크기의 필터와 패턴을 직접 입력받아 MAC 연산 및 판정을 수행하는 모드를 구현할 수 있습니다. (수강생 2, 3 구현)
*   **입력 검증**: 사용자 입력 또는 JSON 파일 처리 시, 행/열 개수 불일치, 숫자 파싱 오류 등을 검증하고 프로그램이 비정상 종료되지 않도록 처리해야 합니다. (수강생 2, 3 구현)

### 4. 핵심 기술 스택

*   **Python**: 프로그래밍 언어
*   **2차원 배열 (List of Lists)**: 패턴 및 필터 데이터 표현
*   **MAC (Multiply-Accumulate)**: 핵심 연산 로직
*   **JSON**: 데이터 파일 형식
*   **시간 복잡도 분석**: `O(N^2)`
*   **부동소수점 비교**: `epsilon`
*   **모듈화**: 기능별 코드 분리 (예: `src/npu/mac.py`, `src/app/console_flow.py` 등)

### 5. 권장 프로젝트 구조 (수강생 3번 레포 기준 참고)

```
your_project_root/
├── main.py                 # 애플리케이션 진입점
├── data.json               # JSON 분석 모드용 필터·패턴 데이터
├── README.md
├── src/
│   ├── app/                # 콘솔 UI·흐름 관련 모듈
│   │   ├── __init__.py
│   │   ├── console_flow.py     # 메인 메뉴 및 모드 라우팅
│   │   ├── user_input_3x3.py   # 3x3 수동 입력 모드
│   │   ├── data_json_mode.py   # data.json 분석 모드
│   │   ├── report.py           # 결과 리포트 생성
│   │   └── constants.py        # 앱 관련 상수
│   ├── npu/                # MAC·판정·벤치마크 코어 로직
│   │   ├── __init__.py
│   │   ├── mac.py              # MAC 연산 구현
│   │   ├── grid.py             # 2차원 배열 검증 (정사각형 등)
│   │   ├── judgement.py        # MAC 점수 비교 기반 판정
│   │   ├── labels.py           # 라벨 정규화 및 관리
│   │   ├── constants.py        # NPU 관련 상수 (epsilon 등)
│   │   └── benchmark.py        # 성능 측정 및 분석
│   └── npu_io/             # JSON/입력 파싱 및 스키마 검증
│       ├── __init__.py
│       ├── json_loader.py      # data.json 로드
│       ├── schema.py           # JSON 스키마 검증, 필터/패턴 매칭
│       └── parse.py            # 콘솔 입력 파싱
├── tests/                  # 단위 테스트
│   ├── __init__.py
│   ├── app/                # app 모듈 테스트
│   ├── npu/                # npu 모듈 테스트
│   └── npu_io/             # npu_io 모듈 테스트
└── docs/                   # 과제 관련 문서, 인사이트
    ├── README.md           # 프로젝트 설명
    ├── subject.md          # 과제 주제 및 요구사항
    ├── commit_guidelines.md # Git 커밋 규칙
    └── insights/           # 학습 내용 관련 문서
```

### 6. 구현 핵심 포인트

1.  **MAC 연산 (`compute_mac`)**:
    *   `pattern`과 `filter`라는 두 개의 `N x N` 2차원 리스트를 입력받습니다.
    *   `size` (N)를 이용해 행과 열을 순회하는 이중 반복문을 사용합니다.
    *   각 위치 `(row, col)`에서 `pattern[row][col] * filter[row][col]` 연산을 수행하고, 이 결과를 누적 변수에 더합니다.
    *   최종 누적 합을 반환합니다.
    *   **핵심**: 같은 위치의 값끼리만 연산한다는 점을 명확히 해야 합니다.

2.  **입력 검증 (`validate_matrix`, `validate_mac_inputs`)**:
    *   패턴과 필터가 정사각형(`N x N`)인지 확인합니다. (모든 행의 길이가 같고, 행의 개수와 열의 개수가 같아야 함)
    *   MAC 연산 전에 패턴과 필터의 크기(`N`)가 일치하는지 확인합니다.
    *   입력값(`0`, `1`, 실수 등)이 유효한지 검사합니다.
    *   `data.json`의 경우, 키(`size_<N>_<idx>`)의 형식이 올바른지, 추출된 `N`값과 실제 `input` 배열의 크기가 일치하는지 등을 검증합니다.

3.  **라벨 정규화 (`normalize_label`, `normalize_expected`, `normalize_filter_key` 등)**:
    *   다양한 형태의 라벨(예: `+`, `cross`, `x`, `X`, `Cross`, `+ ` 등)을 내부적으로 사용할 일관된 표준 라벨(예: `Cross`, `X`)로 매핑하는 함수를 만듭니다.
    *   `data.json`의 `expected` 값과 필터 키(예: `filters.size_5.cross`)를 모두 표준 라벨로 변환하여 비교해야 합니다.
    *   정규화 로직은 한 곳에 모아 관리하는 것이 유지보수에 용이합니다.

4.  **판정 로직 (`decide_label`)**:
    *   `Cross` 필터와 `X` 필터에 대한 MAC 점수를 각각 계산합니다.
    *   `Cross` 점수와 `X` 점수를 비교하여 최종 라벨을 결정합니다.
    *   **`epsilon` 비교**: 두 점수의 차이가 `epsilon` 값보다 작으면 동점(`UNDECIDED`)으로 처리합니다.
    *   `Cross` 점수가 높으면 `Cross`, `X` 점수가 높으면 `X`, 동점이면 `UNDECIDED`를 반환합니다.

5.  **성능 측정 및 `O(N^2)` 설명**:
    *   MAC 연산 함수 호출 전후의 시간을 측정하여 연산 시간을 계산합니다. (Python의 `time` 모듈 활용)
    *   패턴 크기 `N`이 증가할 때 MAC 연산 횟수(`N * N`)가 어떻게 증가하는지 확인합니다.
    *   결과 리포트 또는 별도의 성능 분석 표에 `N`, `N^2`, 측정 시간 등을 함께 표시하여 `O(N^2)` 복잡도를 시각적으로 보여줍니다.

6.  **결과 리포트**:
    *   모든 테스트 케이스에 대해 PASS/FAIL 여부를 기록합니다.
    *   마지막에 총 테스트 수, 통과 수, 실패 수를 집계하여 출력합니다.
    *   실패한 케이스의 경우, 실패한 패턴 키와 간략한 실패 사유(예: `Schema Error`, `Label Mismatch`, `Score Mismatch`)를 함께 출력합니다.

### 7. 트러블슈팅 & 팁

*   **인덱스 오류 (IndexError)**: 2차원 배열 접근 시 `row` 또는 `col` 인덱스가 범위를 벗어나는 경우입니다. 이중 반복문의 범위를 `range(size)`로 정확히 지정했는지 확인하세요.
*   **부동소수점 비교 문제**: `==` 연산자로 부동소수점을 직접 비교하면 미세한 오차로 인해 예상치 못한 결과가 나올 수 있습니다. 반드시 `abs(a - b) < epsilon`과 같은 형태로 비교하세요.
*   **JSON 스키마 오류**: `data.json` 파일의 구조가 정의된 형식과 다를 때 발생합니다. 키 이름(`size_<N>_<idx>`), 필드 존재 여부(`input`, `expected`), 값의 타입(리스트, 문자열, 실수) 등을 꼼꼼히 확인하세요.
*   **라벨 정규화 실수**: `+`, `x`, `cross` 등 다양한 라벨이 내부 표준 라벨(`Cross`, `X`)로 일관되게 변환되지 않으면 판정 결과가 달라집니다. 모든 경우의 수를 고려한 정규화 함수를 작성하세요.
*   **`O(N^2)` 연산량 증가**: 패턴 크기가 작을 때는 체감이 어렵지만, `N`이 커질수록 연산 시간이 기하급수적으로 늘어납니다. 이는 딥러닝 모델이 커질수록 계산량이 폭증하는 이유와 같습니다.
*   **"실패"의 원인 분석**: 단순히 PASS/FAIL만 보는 것이 아니라, 왜 실패했는지(데이터 오류, 스키마 오류, 라벨 오류, 수치 비교 오류 등)를 분석하는 것이 중요합니다. 이는 실제 개발에서 버그를 잡는 능력과 직결됩니다.
*   **모듈화의 중요성**: 코드가 복잡해질수록 기능을 여러 파일(예: `mac.py`, `labels.py`, `console_flow.py`)로 분리하는 것이 가독성과 유지보수성을 높입니다. (수강생 3번 레포의 `src/` 구조 참고)
*   **테스트 코드 작성**: 각 기능(MAC 계산, 라벨 정규화, 판정 로직 등)별로 유닛 테스트를 작성하면 코드 변경 시에도 안정성을 유지하는 데 큰 도움이 됩니다. (`tests/` 폴더 활용)

### 8. 추가 학습 자료

*   **MAC 연산**:
    *   [Multiply–accumulate operation - Wikipedia](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation) (영문)
    *   AI/HW에서의 MAC 연산 관련 블로그 글이나 강의 자료 검색 (예: "AI MAC 연산", "NPU MAC operation")
*   **2차원 배열 처리**: Python 공식 문서의 리스트 및 자료구조 관련 내용
*   **JSON 파싱**: Python `json` 모듈 공식 문서
*   **시간 복잡도**: 기본적인 알고리즘 기초 강의 자료 (예: "시간 복잡도 Big O")
*   **부동소수점 오차**: "부동소수점 비교 epsilon" 등으로 검색하여 관련 개념 학습
*   **NPU 관련 개요**:
    *   [CPU, GPU, NPU 비교](https://github.com/mulloc1/codyssey_python_with_npu/blob/main/docs/insights/cpu_gpu_npu_deep_learning.md) (수강생 3번 레포) - NPU의 역할과 기본 원리를 이해하는 데 도움이 됩니다.
*   **Git 커밋 컨벤션**:
    *   [Conventional Commits](https://www.conventionalcommits.org/) (영문)
    *   [Git 커밋 가이드라인](https://github.com/mulloc1/codyssey_python_with_npu/blob/main/docs/commit_guidelines.md) (수강생 3번 레포) - 협업 시 필수적인 커밋 규칙을 이해합니다.

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-12 | tier1:data.json, tier2:main.py, week-repo:npu, week-readme:mac |
| jhkr1 | [Codyssey_mission3](https://github.com/jhkr1/Codyssey_mission3) | 2026-04-11 | tier1:data.json, tier2:main.py, week-readme:npu, week-readme:mac |
| yejoo0310 | [codyssey-m3](https://github.com/yejoo0310/codyssey-m3) | 2026-04-12 | tier1:mini_npu_simulator.py, tier2:main.py |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-09 | week-repo:npu, week-repo:npu_simulator, week-repo:mini_npu, repo:npu |

---

## 2. 후보 과정 / 미분류 / 혼합 레포

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
