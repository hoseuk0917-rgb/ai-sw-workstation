# Codyssey 과정 분리형 수집 보고서 v2 (2026-04-13)

- 총 수집 건수: 37건
- 2026 본과정 확정: 36건
- 제외된 레거시/파일럿: 0건
- 후보/검토 필요: 1건
- 전역 신규 탐색 활성화: OFF

## 1. 2026 본과정 확정 자료

### 1주차

## Codyssey AI/SW 교육 과정 - 1주차 과제 학습 문서

### 1. 미션 개요

이번 1주차 미션은 AI/SW 개발자로서 필수적인 **터미널(CLI), Docker, Git/GitHub**를 학습하고 이를 활용하여 **재현 가능한 개발 워크스테이션 환경**을 구축하는 것입니다. 단순히 명령어를 익히는 것을 넘어, 각 도구가 왜 필요하며 어떻게 협력하여 개발 환경을 효율적으로 관리할 수 있는지 깊이 이해하는 것을 목표로 합니다.

### 2. 학습 목표

*   **터미널(CLI) 활용 능력 향상:** 파일 및 디렉토리 조작, 권한 관리 등 기본적인 터미널 명령어의 사용법을 익힙니다.
*   **Docker 기초 이해 및 실습:** Docker의 기본 개념을 이해하고, 이미지 빌드, 컨테이너 실행, 포트 매핑, 볼륨 마운트 등 핵심 기능을 직접 실습합니다.
*   **Git & GitHub 기본 활용:** Git의 기본 설정을 완료하고, GitHub와의 연동을 통해 코드 버전 관리의 중요성을 체감합니다.
*   **재현 가능한 개발 환경 구축:** 터미널, Docker, Git을 유기적으로 활용하여 언제 어디서든 동일한 개발 환경을 구축하고 관리하는 방법을 학습합니다.
*   **문서화 및 공유 능력 강화:** 학습 과정에서 얻은 지식과 경험을 README 파일을 통해 체계적으로 정리하고 공유합니다.

### 3. 기능 요구사항

본 미션은 다음 기능들을 성공적으로 수행해야 합니다.

*   **터미널:**
    *   `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm` 등 기본 명령어 숙달
    *   `chmod`를 사용한 파일/디렉토리 권한 변경 실습
*   **Docker:**
    *   Docker 설치 및 버전 확인
    *   `hello-world` 컨테이너 실행
    *   `ubuntu` 컨테이너 실행 및 내부 진입 (`attach` vs `exec` 차이 이해)
    *   `Dockerfile`을 이용한 커스텀 Nginx 웹 서버 이미지 빌드
    *   빌드된 이미지를 사용하여 컨테이너 실행
    *   포트 매핑 (`-p`)을 통한 컨테이너 접속 및 웹 페이지 확인 (최소 2회)
    *   바인드 마운트 (`-v`)를 사용하여 호스트와 컨테이너 간 파일/디렉토리 동기화 및 변경 사항 반영 확인
    *   Docker 볼륨을 사용하여 데이터 영속성 확보 및 확인
*   **Git/GitHub:**
    *   Git 기본 설정 (`user.name`, `user.email`)
    *   GitHub 레포지토리 생성 및 연동 (Push)
    *   VSCode와 GitHub 연동 확인

### 4. 핵심 기술 스택

*   **터미널 (CLI):** macOS, Linux, Windows (WSL) 환경의 기본 쉘 (bash, zsh 등)
*   **Docker:** Docker Desktop (macOS, Windows), Docker Engine (Linux)
*   **Git:** Git CLI
*   **에디터:** Visual Studio Code (VSCode)
*   **호스팅:** GitHub

### 5. 권장 프로젝트 구조

각 수강생은 프로젝트 루트 디렉토리에 `README.md` 파일을 포함하고, 필요에 따라 하위 디렉토리를 구성하여 학습 내용을 정리합니다.

```
your-github-username/codyssey-m1/
├── README.md           # 프로젝트 개요, 학습 목표, 수행 내용, 터미널 로그, 트러블슈팅 등
├── app/                # (선택 사항) Dockerfile, 웹 서버 코드 등
│   ├── Dockerfile
│   └── index.html
├── workstation/        # (선택 사항) Dockerfile, 설정 파일 등
│   ├── Dockerfile
│   └── permission_test.sh
├── src/                # (선택 사항) 웹 서버 소스 코드
│   └── index.html
├── screenshots/        # (선택 사항) 실습 과정을 담은 스크린샷
└── .gitignore          # Git 무시 파일 설정 (선택 사항)
```

**팁:** 수강생 1, 2, 3의 레포지토리 구조를 참고하여 자신에게 가장 효율적인 구조를 선택하는 것이 좋습니다. `app/`, `workstation/`, `src/` 와 같은 디렉토리 명명 규칙은 프로젝트의 성격에 맞게 자유롭게 변경 가능합니다.

### 6. 구현 핵심 포인트

#### 6.1. 터미널 기본 조작 및 권한 관리

*   **디렉토리 구조 탐색:** `pwd`로 현재 위치를 파악하고, `ls`로 내용을 확인하며 `cd`로 원하는 디렉토리로 이동하는 일련의 과정을 자연스럽게 익힙니다. `ls -alh`는 파일 권한, 소유자, 크기, 수정 시간 등을 한눈에 볼 수 있어 유용합니다.
*   **파일/디렉토리 생성 및 조작:** `mkdir`로 폴더를 만들고, `touch`로 파일을 생성합니다. `echo "..." > file.txt`는 파일에 내용을 덮어쓰고, `echo "..." >> file.txt`는 내용을 추가합니다. `cp`와 `mv`를 이용한 복사, 이동, 이름 변경을 익힙니다.
*   **권한 부여:** `chmod` 명령어는 파일 및 디렉토리의 접근 권한을 설정합니다.
    *   `rwx` (읽기, 쓰기, 실행) 권한은 숫자 4, 2, 1에 대응됩니다.
    *   `chmod 755 script.sh` 와 같이 소유자(7), 그룹(5), 그 외(5)에게 권한을 부여하는 방식을 이해합니다. (예: 7 = 4+2+1 = rwx, 5 = 4+1 = r-x)
    *   실행 가능한 스크립트 파일(`permission_test.sh` 등)에 실행 권한을 부여하는 실습을 통해 그 필요성을 체감합니다.

#### 6.2. Docker 활용

*   **기본 명령어:**
    *   `docker version`: Docker 설치 및 버전 확인
    *   `docker info`: Docker 시스템 정보 확인
    *   `docker run [image_name]`: 이미지 실행 (컨테이너 생성 및 시작)
    *   `docker run hello-world`: Docker 설치 및 작동 여부 확인
    *   `docker run -it ubuntu bash`: 대화형 모드로 Ubuntu 컨테이너 실행 및 bash 쉘 접속
    *   `docker attach [container_id]`: 컨테이너의 표준 입출력에 연결 (컨테이너 시작 시 사용)
    *   `docker exec -it [container_id] bash`: 실행 중인 컨테이너에 새로운 프로세스로 접속 (이미 실행 중인 컨테이너에 명령 실행 시 사용) - `attach`와 `exec`의 차이를 명확히 이해하는 것이 중요합니다.
    *   `docker ps`: 실행 중인 컨테이너 목록 확인
    *   `docker ps -a`: 모든 컨테이너 목록 확인 (종료된 컨테이너 포함)
    *   `docker logs [container_id]`: 컨테이너 로그 확인
    *   `docker images`: 이미지 목록 확인
    *   `docker build -t [image_name] [path_to_dockerfile]`: Dockerfile 기반 이미지 빌드
*   **Dockerfile 이해 및 작성:**
    *   `FROM`: 베이스 이미지 지정 (예: `nginx:alpine`)
    *   `COPY`: 호스트의 파일을 이미지 안으로 복사 (예: `COPY ./site/ /usr/share/nginx/html/`)
    *   `EXPOSE`: 컨테이너가 사용할 포트 선언 (런타임 시 포트 매핑과는 다름)
    *   `LABEL`: 이미지에 메타데이터 추가 (선택 사항)
*   **포트 매핑 (`-p`):**
    *   `docker run -p [host_port]:[container_port] [image_name]`
    *   호스트 머신의 특정 포트와 컨테이너 내부의 포트를 연결합니다. 예를 들어, `docker run -p 8080:80 my-nginx-image`는 호스트의 8080 포트로 접속하면 컨테이너의 80번 포트(nginx 기본값)로 연결됩니다.
    *   여러 번의 포트 매핑 실습 (예: 8080:80, 8081:80)을 통해 각기 다른 포트로 접속되는 것을 확인합니다.
*   **바인드 마운트 (`-v`):**
    *   `docker run -v [host_path]:[container_path] [image_name]`
    *   호스트 머신의 디렉토리를 컨테이너 내부의 디렉토리와 연결합니다.
    *   호스트에서 수정된 내용이 컨테이너에 실시간으로 반영되고, 컨테이너에서 생성된 파일이 호스트에 저장됩니다. 웹 서버 개발 시 코드 수정 사항을 바로 확인할 때 매우 유용합니다.
*   **볼륨 (Volumes):**
    *   Docker에서 데이터를 영속적으로 저장하는 방식입니다. 컨테이너가 삭제되어도 볼륨에 저장된 데이터는 유지됩니다.
    *   `docker volume create [volume_name]`으로 볼륨을 생성하고, `docker run -v [volume_name]:[container_path] [image_name]`와 같이 컨테이너에 마운트하여 사용합니다.
    *   바인드 마운트와 마찬가지로, 컨테이너 내 데이터를 영구적으로 보존해야 하는 경우에 사용됩니다.

#### 6.3. Git & GitHub 연동

*   **Git 설정:**
    *   `git config --global user.name "[Your Name]"`: Git 커밋 시 사용할 사용자 이름 설정
    *   `git config --global user.email "[your_email@example.com]"`: Git 커밋 시 사용할 이메일 설정
*   **GitHub 연동:**
    *   GitHub에서 새 리포지토리를 생성합니다.
    *   로컬 프로젝트 디렉토리에서 `git init`으로 Git 저장소를 초기화합니다.
    *   `git add .` 명령어로 모든 변경 사항을 스테이징 영역에 추가합니다.
    *   `git commit -m "Initial commit"` 명령어로 변경 사항을 커밋합니다.
    *   `git remote add origin [GitHub_repository_URL]` 명령어로 원격 저장소(GitHub)를 연결합니다.
    *   `git push -u origin main` (또는 `master`) 명령어로 로컬 커밋을 GitHub 리포지토리로 푸시합니다.
*   **VSCode GitHub 연동:** VSCode의 Extensions 탭에서 'GitHub'를 검색하여 설치하고, 계정 연동을 통해 IDE 내에서 Commit, Push, Pull 등의 Git 작업을 편리하게 수행할 수 있습니다.

### 7. 트러블슈팅 & 팁

*   **`echo` 명령어의 따옴표 문제:** `echo "hello codyssey!" > hello.txt` 와 같이 큰따옴표(`"`)를 사용하면 쉘이 `!`를 히스토리 확장 문자로 해석하여 오류가 발생할 수 있습니다. 이 경우 작은따옴표(`'`)를 사용하거나, `\`를 사용하여 이스케이프 처리하는 방법을 사용합니다. (예: `echo "hello codyssey!" > hello.txt` 에서 `echo \"hello codyssey!\" > hello.txt` 또는 `echo 'hello codyssey!' > hello.txt`)
*   **Docker 설치 문제:** Docker Desktop 설치 후에도 `docker` 명령어가 인식되지 않는 경우, 환경 변수 설정이나 PATH 설정을 확인해야 합니다. macOS에서는 Docker Desktop을 설치하면 자동으로 필요한 설정이 되는 경우가 많지만, Linux나 Windows WSL 환경에서는 추가 설정이 필요할 수 있습니다.
*   **포트 충돌:** 이미 사용 중인 호스트 포트에 Docker 컨테이너의 포트를 매핑하려고 할 때 오류가 발생할 수 있습니다. 이 경우, 호스트에서 해당 포트를 사용 중인 프로세스를 확인하거나, Docker 컨테이너의 호스트 포트를 다른 번호로 변경해야 합니다. (예: 8080 대신 8081 사용)
*   **바인드 마운트 권한 문제:** macOS 또는 Linux에서 Docker 컨테이너 내부에 파일을 쓰려고 할 때 권한 문제가 발생할 수 있습니다. 호스트의 디렉토리 권한을 확인하거나, Docker Desktop 설정에서 파일 공유 설정을 점검해야 합니다.
*   **Dockerfile 빌드 시 캐시 활용:** Docker는 빌드 과정을 캐시합니다. 코드나 Dockerfile 내용이 변경되지 않은 경우, 이전 빌드 결과를 재활용하여 빌드 속도를 높일 수 있습니다. 변경 사항이 제대로 반영되지 않는다면 `--no-cache` 옵션을 사용하여 캐시를 무시하고 빌드해 볼 수 있습니다.
*   **`docker-compose.yml` 활용:** 미션에서는 Dockerfile과 `docker run` 명령어를 주로 사용했지만, 여러 컨테이너를 묶어서 관리해야 할 경우 `docker-compose.yml` 파일을 활용하는 것이 훨씬 효율적입니다. (수강생 3의 레포지토리 참고)
*   **주석 활용:** `README.md` 파일에 각 단계별 명령어 사용 이유, 결과, 주의사항 등을 상세하게 주석으로 남기면 본인뿐만 아니라 다른 사람도 쉽게 이해할 수 있습니다.

### 8. 추가 학습 자료

*   **터미널 (CLI):**
    *   [Linux Command Line Basics (Linux Foundation)](https://training.linuxfoundation.org/resources/free-resources/linux-command-line-basics/)
    *   [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu/)
*   **Docker:**
    *   [Docker Documentation](https://docs.docker.com/) (공식 문서)
    *   [Docker Get Started](https://docs.docker.com/get-started/)
    *   [Inflearn - Docker & Kubernetes로 시작하는 DevOps](https://www.inflearn.com/course/Docker-Kubernetes) (유료 강의지만 관련 내용 학습에 유용)
*   **Git & GitHub:**
    *   [Git Documentation](https://git-scm.com/doc)
    *   [Pro Git Book](https://git-scm.com/book/en/v2) (무료 전자책)
    *   [GitHub Skills](https://skills.github.com/)

이 학습 문서를 통해 1주차 미션을 성공적으로 완료하고, AI/SW 개발의 탄탄한 기초를 다지기를 바랍니다. 궁금한 점은 언제든지 커뮤니티나 멘토에게 질문하세요!

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week1](https://github.com/kimch0612/Codyssey_Week1) | 2026-03-31 | tier2:Dockerfile, hint:docker, hint:codyssey |
| sonjehyun123-maker | [Codyssey-w1-E1](https://github.com/sonjehyun123-maker/Codyssey-w1-E1) | 2026-04-03 | tier2:Dockerfile, hint:docker, hint:codyssey |
| mulloc1 | [codyssey_workstation](https://github.com/mulloc1/codyssey_workstation) | 2026-03-31 | tier2:Dockerfile, hint:workstation, hint:docker, hint:codyssey |
| ntt65 | [codyssey/e1_1](https://github.com/ntt65/codyssey/tree/main/e1_1) | 2026-04-12 | tier2:Dockerfile, hint:docker, hint:codyssey |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | tier2:main.py, hint:npu, hint:mini npu, hint:codyssey |
| codewhite7777 | [codyssey_E-1](https://github.com/codewhite7777/codyssey_E-1) | 2026-03-30 | tier2:Dockerfile, hint:workstation, hint:docker, hint:codyssey |
| mov-hyun | [e1-1-workstation-setup](https://github.com/mov-hyun/e1-1-workstation-setup) | 2026-04-05 | tier2:Dockerfile, hint:workstation, hint:docker, hint:codyssey |
| jhkr1 | [Codyssey_mission1](https://github.com/jhkr1/Codyssey_mission1) | 2026-04-07 | tier2:Dockerfile, hint:workstation, hint:docker, hint:codyssey |
| junhnno | [Codyssey_WorkSpace_Week1](https://github.com/junhnno/Codyssey_WorkSpace_Week1) | 2026-04-09 | tier2:Dockerfile, hint:docker, hint:codyssey |
| sungho255 | [codyssey_1](https://github.com/sungho255/codyssey_1) | 2026-04-07 | hint:docker, hint:codyssey |
| yejoo0310 | [codyssey-m1](https://github.com/yejoo0310/codyssey-m1) | 2026-04-05 | tier2:Dockerfile, hint:docker, hint:입학연수, hint:codyssey |
| clae-dev | [ia-codyssey-Docker](https://github.com/clae-dev/ia-codyssey-Docker) | 2026-04-02 | tier2:Dockerfile, hint:docker, hint:codyssey |
| leehnmn | [codyssey_2026/project-1](https://github.com/leehnmn/codyssey_2026/tree/main/project-1) | 2026-04-08 | tier2:Dockerfile, hint:docker, hint:codyssey |
| I-nkamanda | [codyssey2026/Problem1_AI_SW_Setup](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem1_AI_SW_Setup) | 2026-04-09 | tier2:Dockerfile, hint:docker, hint:codyssey |
| peachily | [codyssey11-E1](https://github.com/peachily/codyssey11-E1) | 2026-04-09 | tier2:main.py, tier2:Dockerfile, hint:docker, hint:quiz |
| ikasoon | [codyssey-e1-1](https://github.com/ikasoon/codyssey-e1-1) | 2026-04-06 | tier2:Dockerfile, hint:workstation, hint:docker, hint:codyssey |

---

### 2주차

## Codyssey 2주차 과제 학습 문서: 나만의 퀴즈 게임 만들기

본 문서는 Codyssey 2주차 과제인 "나만의 퀴즈 게임"을 완벽하게 이해하고 내재화할 수 있도록 돕기 위해 수강생들의 GitHub 레포지토리 정보를 종합하여 작성되었습니다.

---

### 1. 미션 개요

이번 과제는 Python의 기본 문법, 객체 지향 프로그래밍 개념, 파일 입출력, 그리고 Git을 활용한 협업 및 프로젝트 관리 능력을 종합적으로 함양하는 것을 목표로 합니다. 사용자는 콘솔 환경에서 동작하는 퀴즈 게임을 개발하게 됩니다. 게임은 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 최고 점수 확인, 퀴즈 삭제 등의 기능을 포함하며, 프로그램 종료 후에도 데이터가 유지되도록 파일에 저장하는 기능을 구현해야 합니다.

---

### 2. 학습 목표

*   **Python 기초 문법 복습 및 활용:** 변수, 자료형, 조건문, 반복문, 함수 등 Python의 핵심 문법을 실제 프로젝트에 적용하고 이해를 심화합니다.
*   **객체 지향 프로그래밍 (OOP) 이해:** 클래스와 객체의 개념을 이해하고, `Quiz` (문제 자체)와 `QuizGame` (게임 전체 관리)과 같이 관련된 데이터와 기능을 묶어 효과적으로 설계 및 구현하는 능력을 기릅니다.
*   **데이터 영속성 구현:** 파일 입출력(특히 JSON 형식)을 사용하여 프로그램 실행 간에 데이터를 저장하고 불러오는 방법을 익힙니다.
*   **사용자 인터페이스 (CLI) 설계:** 콘솔 환경에서 사용자에게 명확한 메뉴를 제공하고, 직관적인 상호작용을 구현하는 방법을 배웁니다.
*   **예외 처리:** 프로그램 실행 중 발생할 수 있는 오류(잘못된 입력, 파일 손상 등)를 효과적으로 처리하여 프로그램의 안정성을 높입니다.
*   **Git 활용 능력 향상:** Git의 기본적인 명령어 (init, add, commit, push, pull, branch, checkout, merge)를 사용하여 코드 변경 이력을 관리하고, 기능별 브랜치 개발 및 병합 과정을 실습합니다.

---

### 3. 기능 요구사항

*   **메인 메뉴 제공:** 프로그램 실행 시 사용자가 원하는 기능을 선택할 수 있는 메뉴를 출력합니다. (퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인, 종료 등)
*   **퀴즈 풀기:**
    *   저장된 퀴즈를 무작위 순서로 제시합니다.
    *   사용자는 선택지 중 정답을 선택합니다.
    *   정답/오답 여부를 판별하고 점수를 누적합니다.
    *   **[보너스]** 퀴즈 풀이 시 보기 순서를 무작위로 섞는 기능을 구현할 수 있습니다.
    *   **[보너스]** 힌트 기능을 제공하고, 힌트 사용 여부에 따라 점수에 차등을 둘 수 있습니다.
*   **퀴즈 추가:**
    *   사용자가 직접 문제, 4개의 선택지, 정답 번호, (선택적으로) 힌트를 입력하여 새로운 퀴즈를 생성합니다.
*   **퀴즈 목록 확인:**
    *   현재 저장된 모든 퀴즈 목록을 번호와 함께 출력합니다.
    *   **[보너스]** 퀴즈의 정답 정보까지 함께 출력할 수 있습니다.
*   **최고 점수 확인:**
    *   게임을 진행하며 달성한 최고 점수와 당시의 전체 문제 수, 맞힌 개수 등을 표시합니다.
    *   **[보너스]** 닉네임, 점수, 날짜/시간 등을 포함하는 퀴즈 랭킹 시스템을 구현할 수 있습니다.
*   **퀴즈 삭제:**
    *   사용자가 추가한 퀴즈를 선택하여 삭제하는 기능을 제공합니다.
    *   **[권장]** 프로그램 기본 퀴즈는 삭제되지 않도록 보호합니다.
*   **데이터 저장 및 복구:**
    *   퀴즈 데이터 (문제, 선택지, 정답) 및 최고 점수 등의 게임 상태를 `state.json` 파일에 저장합니다.
    *   프로그램 시작 시 `state.json` 파일에서 데이터를 불러옵니다.
    *   `state.json` 파일이 없거나 손상되었을 경우, 기본 퀴즈 데이터로 초기화합니다.
*   **예외 처리:**
    *   사용자의 잘못된 입력 (숫자가 아닌 문자 입력, 범위를 벗어난 숫자 입력 등)을 처리하고 재입력을 유도합니다.
    *   `KeyboardInterrupt` (Ctrl+C) 또는 `EOFError` (Ctrl+D)와 같은 입력 중단 시 안전하게 프로그램을 종료하고 데이터를 저장합니다.

---

### 4. 핵심 기술 스택

*   **프로그래밍 언어:** Python (3.10 이상 권장)
*   **주요 라이브러리:** Python 표준 라이브러리 (별도의 외부 라이브러리 설치 불필요)
    *   `json`: JSON 형식의 데이터 저장 및 불러오기
    *   `random`: 퀴즈 순서 섞기, 보기 순서 섞기 등 무작위 기능 활용
    *   `sys`: 프로그램 종료 등 시스템 관련 기능
*   **데이터 저장 형식:** JSON (`state.json`)
*   **버전 관리:** Git

---

### 5. 권장 프로젝트 구조

수강생들의 레포지토리에서 공통적으로 나타나는 효율적인 구조를 따르는 것을 권장합니다.

```
your-repo-name/
├── .gitignore       # Git에서 추적하지 않을 파일 목록
├── README.md        # 프로젝트 설명 문서
├── main.py          # 프로그램 실행 진입점
├── src/             # 핵심 로직 및 클래스 파일들을 담는 디렉토리
│   ├── __init__.py  # Python 패키지로 인식하기 위한 파일
│   ├── quiz.py      # 퀴즈 문제를 나타내는 Quiz 클래스 정의
│   ├── quiz_game.py # 게임 전체 로직을 관리하는 QuizGame 클래스 정의
│   └── utils.py     # (선택 사항) 공통 함수 (예: 입력 처리 함수) 정의
├── state.json       # 게임 데이터 (퀴즈, 점수 등) 저장 파일
└── docs/            # (선택 사항) 스크린샷, 디자인 등 문서 관련 파일
    └── screenshots/
```

**구조 설명:**

*   `main.py`: 프로그램 실행의 시작점 역할을 합니다. `QuizGame` 객체를 생성하고, 게임의 메인 루프를 실행하는 역할을 합니다.
*   `src/` 디렉토리: 프로젝트의 핵심 코드를 모아 관리합니다.
    *   `quiz.py`: 퀴즈 문제 하나를 표현하는 `Quiz` 클래스를 정의합니다. (문제 내용, 선택지, 정답 등)
    *   `quiz_game.py`: 게임 전체의 흐름, 메뉴 관리, 퀴즈 풀이 로직, 데이터 로드/저장 등을 담당하는 `QuizGame` 클래스를 정의합니다.
    *   `utils.py` (선택 사항): 여러 모듈에서 공통적으로 사용되는 함수(예: 사용자 입력값 검증 함수 `get_int()`, `prompt_text()` 등)를 모아두면 코드의 중복을 줄이고 가독성을 높일 수 있습니다.
*   `state.json`: 프로그램이 종료되어도 유지되어야 할 퀴즈 데이터와 최고 점수 등의 정보를 저장합니다.
*   `.gitignore`: `__pycache__` 와 같이 Git에서 추적할 필요가 없는 파일이나 디렉토리를 명시합니다.

---

### 6. 구현 핵심 포인트

*   **`Quiz` 클래스 설계:**
    *   `question`: 퀴즈 문제 문자열
    *   `choices`: 4개의 선택지를 담은 리스트
    *   `answer`: 정답 번호 (1부터 시작하는 숫자 권장)
    *   (선택 사항) `hint`: 힌트 문구
    *   **주요 메서드:**
        *   `display()`: 문제와 선택지를 보기 좋게 출력합니다.
        *   `is_correct(user_answer)`: 사용자의 입력이 정답인지 판별합니다.
        *   `to_dict()`: JSON 저장을 위해 객체를 딕셔너리 형태로 변환합니다.
        *   `from_dict(data)`: 딕셔너리 데이터를 `Quiz` 객체로 복원합니다.

*   **`QuizGame` 클래스 설계:**
    *   **속성:**
        *   `quizzes`: `Quiz` 객체들의 리스트 (현재 등록된 퀴즈 목록)
        *   `best_score`: 현재까지의 최고 점수
        *   `best_correct_count`, `best_total_count`: 최고 점수를 기록했을 때의 맞힌 개수 및 총 문제 수
        *   `state_path`: `state.json` 파일의 경로
    *   **주요 메서드:**
        *   `__init__()`: 객체 초기화, `load_state()` 호출, 기본 데이터 설정 등
        *   `load_state()`: `state.json` 파일을 읽어 퀴즈 목록과 최고 점수를 불러옵니다. 파일이 없거나 형식이 잘못된 경우 기본 데이터로 복구합니다.
        *   `save_state()`: 현재 퀴즈 목록과 최고 점수 정보를 `state.json` 파일에 저장합니다.
        *   `run()`: 메인 메뉴를 반복적으로 보여주고 사용자 입력을 받아 해당 기능을 실행합니다.
        *   `play_quiz()`: 퀴즈 풀이 로직을 담당합니다. 퀴즈 선택, 문제 제시, 정답 확인, 점수 계산, 최고 점수 갱신 등을 수행합니다.
        *   `add_quiz()`: 사용자로부터 퀴즈 정보를 입력받아 새로운 `Quiz` 객체를 생성하고 `quizzes` 리스트에 추가합니다.
        *   `show_quiz_list()`: `quizzes` 리스트를 순회하며 퀴즈 목록을 출력합니다.
        *   `show_best_score()`: `best_score` 및 관련 정보를 출력합니다.
        *   `delete_quiz()`: 사용자로부터 삭제할 퀴즈 번호를 입력받아 제거합니다.
        *   `prompt_number(prompt_message, min_val, max_val)` (또는 `utils.py`에 구현): 사용자로부터 숫자를 입력받고, 입력값이 유효한 범위 내에 있는지 검증하여 올바른 값만 반환합니다. 잘못된 입력 시 재입력을 요구합니다.

*   **데이터 영속성 (`state.json`):**
    *   JSON은 Python의 `dict`, `list`, `str`, `int`, `float`, `bool`, `None`과 같은 기본 자료형을 직관적으로 표현할 수 있어 데이터를 저장하기에 적합합니다.
    *   `json.dump(data, file)`: Python 객체를 JSON 파일로 저장합니다.
    *   `json.load(file)`: JSON 파일 내용을 읽어 Python 객체로 변환합니다.
    *   **주의:** `Quiz` 객체 자체를 직접 저장할 수는 없으므로, `to_dict()` 메서드를 사용하여 딕셔너리로 변환 후 저장하고, `from_dict()` 메서드를 사용하여 복원해야 합니다.

*   **Git 브랜치 전략:**
    *   `main` (또는 `master`) 브랜치: 안정적인 배포 가능한 코드를 유지합니다.
    *   기능별 브랜치 (`feature/add-quiz`, `feature/play-quiz` 등): 새로운 기능을 개발할 때 사용합니다.
    *   개발 완료 후 `main` 브랜치로 `merge`합니다. `git merge --no-ff`를 사용하여 merge commit을 남기면 이력 추적이 용이합니다.
    *   `git log --oneline --graph --decorate --all` 명령어로 브랜치 및 병합 과정을 시각적으로 확인합니다.

---

### 7. 트러블슈팅 & 팁

*   **`JSONDecodeError` 발생 시:**
    *   `state.json` 파일이 손상되었거나, Python 객체에서 JSON으로 변환하는 과정에서 문제가 발생했을 수 있습니다.
    *   **해결책:**
        *   `state.json` 파일 내용을 직접 확인하여 문법 오류(예: 쉼표 누락, 잘못된 문자)가 없는지 검사합니다.
        *   `load_state()` 메서드에서 `try-except json.JSONDecodeError:` 구문을 사용하여 파일 읽기 오류를 잡아내고, 기본 데이터로 복구하는 로직을 구현합니다.
        *   `Quiz` 객체를 `to_dict()`로 변환하는 과정에서 `TypeError`가 발생한다면, `Quiz` 클래스의 속성이 JSON 직렬화 가능한 타입인지 확인합니다. (일반적으로는 문제 없음)

*   **`Quiz` 객체 직렬화/역직렬화 문제:**
    *   `state.json`에 퀴즈 데이터를 저장하고 불러올 때, `Quiz` 객체 그대로 저장/불러올 수 없습니다.
    *   **해결책:**
        *   `Quiz` 클래스에 `to_dict()` 메서드를 만들어 `{'question': self.question, 'choices': self.choices, 'answer': self.answer}`와 같이 딕셔너리 형태로 반환하도록 합니다.
        *   `QuizGame`의 `save_state()`에서 퀴즈 목록을 순회하며 각 `Quiz` 객체를 `to_dict()`로 변환하여 딕셔너리 리스트를 만듭니다.
        *   `load_state()`에서 딕셔너리 리스트를 불러온 후, 각 딕셔너리를 `Quiz` 클래스의 `from_dict()` 메서드(또는 `Quiz(data['question'], data['choices'], data['answer'])`와 같은 방식으로)를 사용하여 `Quiz` 객체로 복원합니다.

*   **`IndexError` 또는 `ValueError` (입력 처리 관련):**
    *   사용자 입력이 예상치 못한 값이거나, 리스트 인덱스 범위를 벗어나는 경우 발생합니다.
    *   **해결책:**
        *   `prompt_number`와 같은 입력 검증 함수를 만들어 `try-except` 블록으로 `ValueError` (숫자 변환 실패)를 처리하고, `if` 문으로 입력값이 유효한 범위(`min_val` ~ `max_val`)에 있는지 확인합니다.
        *   올바른 입력이 들어올 때까지 `while` 루프를 사용하여 재입력을 받도록 합니다.

*   **`AttributeError` (메서드 또는 속성 접근 오류):**
    *   객체가 존재하지 않는 메서드나 속성에 접근하려고 할 때 발생합니다.
    *   **해결책:**
        *   `self`를 사용하여 클래스 내부의 속성과 메서드에 접근하고 있는지 확인합니다.
        *   객체가 제대로 생성되었는지, 해당 메서드나 속성이 올바르게 정의되었는지 코드를 다시 확인합니다.

*   **Git 병합 충돌 (`Merge Conflict`) 해결:**
    *   여러 브랜치에서 같은 파일의 같은 부분을 수정하고 병합할 때 발생합니다.
    *   **해결책:**
        *   충돌이 발생한 파일을 열어 `<<<<<<<`, `=======`, `>>>>>>>` 표시를 확인합니다.
        *   두 브랜치의 변경 내용 중 필요한 부분을 선택하거나, 새로운 내용으로 수정하여 충돌을 해결합니다.
        *   해결 후에는 `git add`와 `git commit`으로 병합을 완료합니다.

*   **코딩 스타일 일관성:**
    *   PEP 8 스타일 가이드를 준수하여 코드의 가독성을 높입니다. (변수명, 함수명, 클래스명 규칙, 들여쓰기 등)
    *   `main.py`, `quiz.py`, `quiz_game.py` 파일 간의 책임 분리를 명확히 합니다. `main.py`는 실행 및 흐름 제어, `quiz.py`는 데이터 표현, `quiz_game.py`는 비즈니스 로직 처리에 집중합니다.

---

### 8. 추가 학습 자료

*   **Python 공식 튜토리얼:** [https://docs.python.org/ko/3/tutorial/index.html](https://docs.python.org/ko/3/tutorial/index.html)
    *   Python의 기본적인 문법부터 고급 기능까지 상세하게 다룹니다.
*   **Python 객체 지향 프로그래밍 (OOP):** [https://wikidocs.net/22733](https://wikidocs.net/22733) (점프 투 파이썬)
    *   클래스와 객체, 상속, 다형성 등 OOP의 핵심 개념을 쉽게 설명합니다.
*   **JSON 파이썬 라이브러리:** [https://docs.python.org/ko/3/library/json.html](https://docs.python.org/ko/3/library/json.html)
    *   `json` 모듈의 사용법을 공식 문서에서 확인할 수 있습니다.
*   **Git 공식 문서:** [https://git-scm.com/doc](https://git-scm.com/doc)
    *   Git의 모든 명령어와 사용법에 대한 방대한 자료를 제공합니다.
*   **Git Handbook (by GitHub):** [https://guides.github.com/introduction/git-handbook/](https://guides.github.com/introduction/git-handbook/)
    *   Git의 기본적인 사용법을 그림과 함께 쉽게 설명합니다.
*   **PEP 8 -- Style Guide for Python Code:** [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
    *   Python 코드 작성 시 따라야 할 스타일 가이드라인입니다.

---

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | tier2:main.py, tier2:state.json, hint:quiz, hint:npu |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-10 | tier2:main.py, tier2:state.json, tier2:utils.py, hint:quiz |
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | tier1:quiz_game.py, tier2:main.py, hint:quiz, hint:quiz_game |
| ntt65 | [codyssey/e1_2](https://github.com/ntt65/codyssey/tree/main/e1_2) | 2026-04-12 | tier2:main.py, hint:quiz, hint:codyssey |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | tier2:main.py, tier2:state.json, hint:quiz, hint:codyssey |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-12 | tier1:quiz_game.py, tier2:main.py, tier2:state.json, hint:quiz |
| yeowon083 | [quiz-game](https://github.com/yeowon083/quiz-game) | 2026-04-12 | tier2:main.py, tier2:state.json, hint:quiz |
| jhkr1 | [Codyssey_mission2](https://github.com/jhkr1/Codyssey_mission2) | 2026-04-11 | tier2:main.py, tier2:state.json, hint:quiz, hint:codyssey |
| junhnno | [Codyssey_WorkSpace_Week2](https://github.com/junhnno/Codyssey_WorkSpace_Week2) | 2026-04-11 | tier2:main.py, hint:quiz, hint:npu, hint:codyssey |
| sungho255 | [codyssey_2](https://github.com/sungho255/codyssey_2) | 2026-04-07 | tier2:state.json, hint:codyssey |
| yejoo0310 | [codyssey-m2](https://github.com/yejoo0310/codyssey-m2) | 2026-04-10 | tier1:quiz_game.py, tier2:main.py, tier2:state.json, hint:quiz |
| yejibaek12 | [Python-Quiz-Game](https://github.com/yejibaek12/Python-Quiz-Game) | 2026-04-11 | tier2:main.py, tier2:state.json, hint:quiz |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | tier1:quiz_game.py, tier2:main.py, hint:quiz, hint:quiz_game |
| leehnmn | [codyssey_2026/project-2](https://github.com/leehnmn/codyssey_2026/tree/main/project-2) | 2026-04-08 | tier1:quiz_game.py, tier2:main.py, tier2:state.json, hint:quiz |
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-09 | hint:codyssey |

---

### 3주차

## Codyssey 3주차 과제 학습 문서: Mini NPU Simulator

### 1. 미션 개요

본 미션은 **Mini NPU Simulator**를 Python 콘솔 애플리케이션으로 구현하는 것을 목표로 합니다. 이를 통해 컴퓨터가 시각적 패턴을 어떻게 숫자로 인식하고, **MAC(Multiply-Accumulate)** 연산을 통해 패턴의 유사도를 측정하는지 학습합니다. 단순히 코드를 작성하는 것을 넘어, 입력 데이터의 구조, 라벨 정규화, 수치 비교 정책, 그리고 시간 복잡도 분석까지 종합적으로 이해하고 내재화하는 데 중점을 둡니다.

### 2. 학습 목표

이 미션을 성공적으로 완료하고 나면, 학습자는 다음 내용을 스스로 설명하고 구현할 수 있어야 합니다.

*   **MAC 연산의 개념 및 원리**: MAC 연산이 무엇이며, 입력 패턴과 필터를 곱하고 더하여 유사도를 구하는 과정을 설명할 수 있습니다.
*   **데이터 구조 및 스키마 이해**: `data.json` 파일의 키 규칙과 라벨 규칙을 해석하고, 이에 따른 데이터 구조를 이해할 수 있습니다.
*   **라벨 정규화의 필요성**: 다양한 형태의 라벨(예: `+`, `cross`)이 존재할 때, 이를 표준화된 라벨(예: `Cross`)로 변환하는 정규화 과정이 왜 필요한지 설명할 수 있습니다.
*   **부동소수점 비교 정책**: `epsilon` 기반의 비교가 왜 필요한지, 특히 동점(tie) 상황에서 어떻게 판정에 영향을 미치는지 이해할 수 있습니다.
*   **시간 복잡도 분석**: 패턴 크기가 커질수록 연산량이 `O(N^2)`로 증가하는 이유를 수학적으로 설명할 수 있습니다.
*   **문제 해결 및 디버깅**: 실패 케이스를 데이터, 스키마, 로직, 수치 비교 문제로 분류하고, 각 문제에 대한 진단 및 해결 방안을 제시할 수 있습니다.

### 3. 기능 요구사항

*   **MAC 연산 구현**: 입력 패턴과 필터 간의 MAC 연산을 수행하여 유사도 점수를 계산합니다.
*   **패턴 및 필터 처리**: `data.json` 파일에서 필터와 패턴 데이터를 로드하고 처리합니다.
*   **라벨 정규화**: 다양한 형태의 입력 라벨을 표준화된 라벨로 변환합니다.
*   **판정 로직**: 계산된 MAC 점수를 기반으로 패턴의 라벨(`Cross`, `X`, `UNDECIDED`)을 판정합니다.
*   **입력 검증**: 필터 및 패턴 데이터의 크기, 형식 등을 검증하여 오류를 방지합니다.
*   **성능 측정 및 분석**: MAC 연산에 소요되는 시간을 측정하고, 패턴 크기에 따른 시간 복잡도를 분석하여 출력합니다.
*   **결과 리포트**: 전체 테스트 케이스에 대한 요약 정보(총 테스트 수, 통과 수, 실패 수, 실패 케이스 목록)를 제공합니다.
*   **사용자 인터페이스**: 콘솔 기반의 사용자 입력 모드와 `data.json` 분석 모드를 제공합니다.

### 4. 핵심 기술 스택

*   **Python**: 프로그래밍 언어
*   **JSON**: 데이터 직렬화/역직렬화
*   **2차원 배열(List of Lists)**: 패턴 및 필터 데이터 표현
*   **수치 연산**: 곱셈, 덧셈, 부동소수점 비교
*   **시간 복잡도 분석**: `O(N^2)` 분석

### 5. 권장 프로젝트 구조

```
your_project_root/
├── README.md               # 프로젝트 설명, 실행 방법, 목표 등
├── main.py                 # 애플리케이션 진입점 (모드 선택 및 라우팅)
├── data.json               # 필터 및 패턴 데이터 파일
├── src/
│   ├── __init__.py
│   ├── app/                # 애플리케이션 레벨 로직 (UI, 흐름 제어)
│   │   ├── __init__.py
│   │   ├── console_flow.py   # 메인 메뉴 및 모드 선택 로직
│   │   ├── user_input_3x3.py # 3x3 사용자 입력 모드 구현
│   │   ├── data_json_mode.py # data.json 분석 모드 구현
│   │   ├── report.py         # 결과 리포트 생성
│   │   └── constants.py      # 앱 레벨 상수 (메뉴 선택값 등)
│   ├── npu/                # NPU 핵심 로직 (MAC, 판정, 벤치마크)
│   │   ├── __init__.py
│   │   ├── mac.py            # MAC 연산 구현
│   │   ├── judgement.py      # 판정 로직 (epsilon 기반)
│   │   ├── labels.py         # 라벨 정규화 (Cross/X)
│   │   ├── constants.py      # NPU 레벨 상수 (epsilon 등)
│   │   └── benchmark.py      # 성능 측정 및 분석
│   └── npu_io/             # 입출력 및 데이터 파싱, 스키마 검증
│       ├── __init__.py
│       ├── json_loader.py    # data.json 로딩
│       ├── schema.py         # 스키마 검증, 패턴 키 파싱
│       └── parse.py          # 콘솔 입력 파싱
├── tests/                  # 단위 테스트
│   ├── __init__.py
│   ├── app/                # app 모듈 테스트
│   ├── npu/                # npu 모듈 테스트
│   └── npu_io/             # npu_io 모듈 테스트
└── docs/                   # 추가 문서 (과제 요구사항, 설계 가이드 등)
    └── ...
```

### 6. 구현 핵심 포인트

1.  **MAC 연산 (`src/npu/mac.py`)**:
    *   `compute_mac(pattern, filter_matrix, size)` 함수는 두 `N x N` 2차원 배열을 입력받아, 같은 위치의 값들을 곱한 후 누적 합을 반환합니다.
    *   중첩 반복문(`for row in range(size): for col in range(size):`)을 사용하여 모든 위치를 순회하며 계산합니다.
    *   입력값의 유효성(정사각형 배열, 크기 일치 등)은 별도의 검증 함수(`validate_mac_inputs` 등)에서 처리하여 `compute_mac` 함수 자체는 순수 연산에 집중하도록 설계하는 것이 좋습니다.

2.  **데이터 구조 및 스키마 (`src/npu_io/schema.py`, `src/npu_io/json_loader.py`)**:
    *   `data.json` 파일은 `filters`와 `patterns` 두 개의 최상위 키를 가집니다.
    *   `filters`: `"size_<N>"` 형태의 키를 가지며, 각 키의 값은 해당 크기(`N x N`)의 `cross`와 `x` 필터 2차원 배열을 포함하는 객체입니다.
    *   `patterns`: `"size_<N>_<idx>"` 형태의 키를 가지며, 각 키의 값은 `input` (패턴 2차원 배열)과 `expected` (기대 라벨 문자열)를 포함하는 객체입니다.
    *   **핵심**: 패턴 키에서 `N`을 정확히 추출하고, 해당 `N`에 맞는 필터 (`filters.size_<N>`)를 선택하는 로직이 중요합니다. 패턴의 `input` 크기와 추출된 `N`, 선택된 필터의 크기가 모두 일치해야 합니다.

3.  **라벨 정규화 (`src/npu/labels.py`, `src/npu_io/label_normalization.py`)**:
    *   다양한 입력 라벨(예: `+`, `cross`, `x`, `X`, `Cross`)을 프로그램 내부에서 일관되게 사용될 표준 라벨(`Cross`, `X`)로 변환해야 합니다.
    *   `normalize_label(label)` 함수를 만들어 `expected` 값과 필터 키(`cross` -> `Cross`)를 통일합니다.
    *   이 과정은 `data.json` 분석 및 사용자 입력 모드 모두에 적용되어야 합니다.
    *   `src/npu_io/label_normalization.py`는 필터 키 집합을 표준 라벨로 변환하는 복잡한 로직을 다룹니다.

4.  **판정 로직 (`src/npu/judgement.py`)**:
    *   MAC 연산 결과로 얻은 `score_cross`와 `score_x`를 비교하여 최종 라벨을 결정합니다.
    *   `epsilon` 기반 비교: 두 점수 간의 차이가 매우 작은 경우(예: `abs(score_cross - score_x) < epsilon`) 동점(`UNDECIDED`)으로 처리합니다. `epsilon` 값은 `src/npu/constants.py` 등에 정의합니다.
    *   `decide_label(score_cross, score_x, epsilon)` 함수가 이 로직을 수행합니다.

5.  **성능 분석 (`src/npu/benchmark.py`)**:
    *   `time` 모듈을 사용하여 MAC 연산 수행 시간을 측정합니다.
    *   `3x3`, `5x5`, `13x13`, `25x25` 등 다양한 크기의 패턴에 대해 MAC 연산을 반복 수행하고 평균 시간을 기록합니다.
    *   패턴 크기 `N`에 따른 연산 횟수(`N^2`)를 계산하고, 시간 복잡도 `O(N^2)`에 따른 성능 변화를 표 형태로 출력합니다.

6.  **예외 처리 및 안전한 실패 (`main.py`, `src/app/console_flow.py`, `src/app/data_json_mode.py`)**:
    *   JSON 파싱 오류, 잘못된 입력 형식, 크기 불일치 등 다양한 오류 상황에서 프로그램이 갑자기 종료되지 않도록 `try-except` 구문을 적극적으로 사용합니다.
    *   실패 원인을 구체적으로 명시하여 사용자에게 오류 정보를 전달합니다. (예: "JSON 스키마 오류: 패턴 키 형식 불일치", "크기 불일치: 패턴 5x5, 필터 13x13")
    *   `data.json` 분석 모드에서는 한 케이스의 실패가 전체 실행을 중단시키지 않도록, 각 케이스별로 PASS/FAIL을 기록하고 마지막에 종합 결과를 보여줍니다.

### 7. 트러블슈팅 & 팁

*   **부동소수점 비교 오류**: `score_cross == score_x` 와 같이 직접 비교하면 미세한 오차로 인해 예상과 다른 결과가 나올 수 있습니다. 반드시 `abs(score_cross - score_x) < epsilon` 과 같은 방식으로 비교하세요.
*   **JSON 스키마 불일치**: `data.json` 파일의 키 이름, 값의 타입, 배열 구조가 요구사항과 일치하는지 꼼꼼히 확인하세요. 특히 패턴 키(`size_<N>_<idx>`)와 필터 키(`size_<N>`)의 형식을 정확히 맞춰야 합니다.
*   **라벨 정규화 누락**: `expected` 라벨(`+`, `x` 등)과 내부 처리 라벨(`Cross`, `X`), 그리고 필터 키(`cross`, `x`) 간의 불일치로 인해 PASS/FAIL 오류가 발생할 수 있습니다. 모든 라벨을 일관된 기준으로 정규화하는 함수를 만들어 활용하세요.
*   **크기 불일치**: 패턴과 필터의 크기가 다르면 MAC 연산이 불가능합니다. 입력 데이터 로딩 시, 또는 MAC 연산 직전에 반드시 크기를 검증하는 로직을 추가하세요.
*   **시간 복잡도 측정**: 실제 시간 측정은 환경에 따라 달라질 수 있으므로, `O(N^2)`라는 이론적 복잡도를 이해하고, 패턴 크기가 커짐에 따라 연산 횟수가 어떻게 증가하는지(N^2)를 `benchmark.py`에서 보여주는 데 집중하는 것이 좋습니다.
*   **디버깅**: `print` 문을 활용하여 각 단계별 변수 값, 계산 결과, 판정 로직의 중간값을 확인하며 디버깅하는 것이 효과적입니다. 특히 `src/npu/mac.py`, `src/npu/judgement.py`, `src/npu_io/schema.py` 파일들을 집중적으로 살펴보세요.
*   **테스트 주도 개발 (TDD)**: 가능하다면, 각 함수 구현 전에 해당 함수가 어떤 입력을 받고 어떤 출력을 반환해야 하는지에 대한 테스트 케이스를 먼저 작성하고, 테스트를 통과시키는 방식으로 개발하면 코드의 견고성을 높일 수 있습니다. (예: `tests/npu/test_mac.py`, `tests/npu/test_judgement.py`)

### 8. 추가 학습 자료

*   **[학습노트] docs/subject.md**: 과제의 상세 요구사항 및 목표를 담고 있습니다.
*   **[학습노트] docs/commit_guidelines.md**: Git 커밋 메시지 작성 규칙을 안내합니다.
*   **[학습노트] docs/implementation_checklist.md**: 구현 단계를 상세하게 나누고 테스트 구조를 제시합니다.
*   **[학습노트] docs/insights/code_structure_principles_interview.md**: 코드 구조 설계 원칙 및 MAC 연산의 흐름을 심층적으로 다룹니다.
*   **[학습노트] docs/insights/cpu_gpu_npu_deep_learning.md**: CPU, GPU, NPU의 차이점과 딥러닝에서의 NPU 활용 이유를 설명합니다.
*   **[학습노트] docs/insights/discussion_summary.md**: 과제 관련 핵심 개념에 대한 요약을 제공합니다.
*   **Python 공식 문서 - JSON Encoding and Decoding**: `json` 모듈 사용법에 대한 공식 문서입니다.
    *   [https://docs.python.org/ko/3/library/json.html](https://docs.python.org/ko/3/library/json.html)
*   **Python 공식 문서 - Time Module**: 시간 측정 방법에 대한 공식 문서입니다.
    *   [https://docs.python.org/ko/3/library/time.html](https://docs.python.org/ko/3/library/time.html)

#### 참여 수강생 및 증거
| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | tier1:data.json, tier2:main.py, hint:npu, hint:mini npu |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-12 | tier1:data.json, tier2:main.py, hint:npu, hint:mini npu |
| jhkr1 | [Codyssey_mission3](https://github.com/jhkr1/Codyssey_mission3) | 2026-04-11 | tier1:data.json, tier2:main.py, hint:npu, hint:mini npu |
| yejoo0310 | [codyssey-m3](https://github.com/yejoo0310/codyssey-m3) | 2026-04-12 | tier1:mini_npu_simulator.py, tier2:main.py, hint:npu, hint:npu_simulator |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-09 | hint:npu, hint:npu_simulator, hint:codyssey |

---

## 2. 후보 과정 / 미분류 / 혼합 레포

### 미분류

| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |
| --- | --- | --- | --- | --- |
| doji-kr | [codyssey_day1_bear1](https://github.com/doji-kr/codyssey_day1_bear1) | 2025-07-11 | 0.30 | hint:codyssey |

## 3. 제외된 레거시/파일럿 레포

_제외된 레거시/파일럿 레포 없음._
