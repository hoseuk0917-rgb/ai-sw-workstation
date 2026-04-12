# Codyssey 주간 과제 수집 보고서 (2026-04-12)

- 총 수집 건수: 37건
- 신규 발견 레포: 16건
- 소요 시간: 86초

## 1. 주차별 학습 문서

### 1주차 과제 종합

# Codyssey AI/SW 교육 과정 - 1주차 학습 문서: 재현 가능한 개발 워크스테이션 구축

## 1. 미션 개요

본 미션은 AI/SW 개발자로서 필수적인 세 가지 도구, 즉 **터미널(CLI)**, **Docker(컨테이너)**, **Git/GitHub(버전 관리)**를 직접 설정하고 활용하는 경험을 통해 **재현 가능한 개발 워크스테이션**을 구축하는 것을 목표로 합니다. "내 컴퓨터에서만 돌아가는" 문제를 해결하고, 언제 어디서든 동일한 개발 환경을 구성하며, 프로젝트를 효과적으로 관리하는 능력을 키웁니다.

## 2. 학습 목표

*   **터미널(CLI) 활용 능력 향상:** 파일 및 디렉토리 관리, 권한 설정 등 기본적인 터미널 명령어를 능숙하게 사용합니다.
*   **Docker 기초 이해 및 활용:** Docker 설치, 이미지 빌드, 컨테이너 실행 및 관리, 볼륨 및 마운트의 개념과 활용법을 익힙니다.
*   **Dockerfile 작성 및 이미지 빌드:** 간단한 웹 서버 이미지를 Dockerfile을 통해 직접 생성합니다.
*   **Git & GitHub 기초:** Git의 기본 설정과 VS Code 연동을 통해 소스 코드의 버전 관리를 시작합니다.
*   **재현 가능한 개발 환경 구축:** 위 도구들을 조합하여 환경에 구애받지 않는 개발 환경의 중요성을 이해하고 구축합니다.

## 3. 기능 요구사항

*   **터미널:**
    *   `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm` 등 기본 명령어 사용
    *   파일 및 디렉토리 권한 변경 (`chmod`) 실습
*   **Docker:**
    *   Docker 설치 및 정상 작동 확인 (`docker version`, `docker info`)
    *   기본 이미지 실행 (`hello-world`, `ubuntu`)
    *   컨테이너 실행 및 관리 (`docker run`, `docker ps`, `docker logs`, `docker stats`)
    *   컨테이너 내부 진입 (`docker attach`, `docker exec`) 차이 이해
    *   Dockerfile을 이용한 커스텀 Nginx 웹 서버 이미지 빌드
    *   이미지 빌드 및 컨테이너 실행 시 포트 매핑 (`-p`) 실습 (최소 2회)
    *   바인드 마운트 (`-v`)를 이용한 호스트 파일 시스템 동기화 실습
    *   Docker 볼륨을 이용한 데이터 영속성(persistence) 실습
*   **Git & GitHub:**
    *   Git 사용자 설정 (`git config`)
    *   VS Code와 GitHub 연동 및 기본적인 GitHub 사용
*   **문서화:**
    *   수행 과정 및 결과를 README.md 파일에 상세히 기록
    *   트러블슈팅 내용을 정리

## 4. 핵심 기술 스택

*   **운영체제(OS):** macOS (Windows, Linux 환경에서도 유사하게 적용 가능)
*   **Shell:** Bash, Zsh 등 (터미널 환경)
*   **Docker:** 컨테이너 기반 가상화 도구
*   **Git:** 버전 관리 시스템
*   **VS Code:** 코드 에디터 (GitHub 연동)
*   **Nginx:** 웹 서버 (Docker 이미지 활용)

## 5. 권장 프로젝트 구조

수강생들의 레포지토리를 종합하여 다음과 같은 구조를 권장합니다.

```
codyssey-m1/
├── README.md             # 프로젝트 설명, 진행 과정, 트러블슈팅 기록
├── app/                  # Dockerfile, 웹 서버 소스 코드 등 애플리케이션 관련 파일
│   ├── Dockerfile
│   └── index.html
├── practice/             # 터미널 명령어 실습 파일 (선택 사항)
│   ├── permission_test.sh
│   └── test.txt
├── screenshots/          # 실습 과정을 증빙하는 이미지 파일 (선택 사항)
│   ├── ...
├── .git/                 # Git 설정 파일 (자동 생성)
└── .gitignore            # Git에서 무시할 파일 설정 (선택 사항)
```

**핵심:** `README.md`에 모든 내용을 상세하게 기록하고, `Dockerfile`과 웹 서버 소스 코드를 잘 정리하는 것이 중요합니다.

## 6. 구현 핵심 포인트

### 6.1 터미널 기본 조작 및 권한

*   **경로 이해:** 절대 경로와 상대 경로의 차이를 이해하고 상황에 맞게 사용합니다.
    *   `pwd`: 현재 작업 디렉토리의 절대 경로 출력
    *   `ls -alh`: 숨김 파일 포함 모든 파일의 상세 목록을 보기 좋은 형식으로 출력
    *   `cd`, `mkdir`, `touch`, `cat`, `echo` 등을 활용하여 파일/디렉토리를 생성, 이동, 확인합니다.
*   **파일/디렉토리 관리:**
    *   `cp`: 파일 또는 디렉토리 복사
    *   `mv`: 파일 또는 디렉토리 이동 또는 이름 변경
    *   `rm`: 파일 또는 디렉토리 삭제 (`-r` 옵션 필수)
*   **권한 변경 (`chmod`):**
    *   `chmod 755 script.sh`: 소유자는 모든 권한(rwx=4+2+1=7), 그룹과 기타 사용자는 읽기 및 실행 권한(r-x=4+0+1=5) 부여. 스크립트 파일 실행에 필수적입니다.
    *   파일 권한의 `rwx` (읽기, 쓰기, 실행)와 숫자(4, 2, 1)의 조합을 이해하는 것이 중요합니다.

### 6.2 Docker 핵심 개념

*   **Dockerfile:**
    ```dockerfile
    # 베이스 이미지: Nginx의 가벼운 Alpine 버전 사용
    FROM nginx:alpine

    # 컨테이너 내부에 복사할 파일 설정
    # src/index.html 파일을 nginx 기본 웹 서버 경로로 복사
    COPY src/index.html /usr/share/nginx/html/index.html

    # 컨테이너가 사용할 포트 명시 (빌드 결과물 아님, 문서화 목적)
    EXPOSE 80
    ```
    *   `FROM`: 어떤 이미지로부터 시작할지 지정
    *   `COPY`: 로컬 파일을 컨테이너 이미지 안으로 복사
    *   `EXPOSE`: 컨테이너가 어떤 포트를 사용할지 명시 (실제 포트 개방은 `docker run -p`에서 수행)
*   **Docker 이미지 빌드:**
    ```bash
    docker build -t my-custom-nginx .
    ```
    *   `-t`: 이미지 이름 지정
    *   `.`: Dockerfile이 있는 현재 디렉토리를 빌드 컨텍스트로 지정
*   **컨테이너 실행:**
    *   **포트 매핑 (`-p`):**
        ```bash
        docker run -d -p 8080:80 my-custom-nginx
        ```
        *   `-d`: 백그라운드 실행
        *   `-p 8080:80`: 호스트 머신의 8080번 포트를 컨테이너의 80번 포트로 연결. `http://localhost:8080`으로 접속 가능.
        *   **2회 실행:** 다양한 포트 조합 (`8081:80` 등)으로 실행하여 포트 매핑의 유연성을 확인합니다.
    *   **바인드 마운트 (`-v`):**
        ```bash
        docker run -d -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html my-custom-nginx
        ```
        *   `-v $(pwd)/html:/usr/share/nginx/html`: 호스트 머신의 현재 디렉토리 아래 `html` 폴더를 컨테이너 내부의 `/usr/share/nginx/html`로 연결. 호스트에서 `html` 폴더의 `index.html` 파일을 수정하면 컨테이너 안의 웹 페이지도 즉시 변경됩니다.
    *   **볼륨 (Volume):**
        ```bash
        docker run -d -p 8080:80 -v my-nginx-data:/usr/share/nginx/html my-custom-nginx
        ```
        *   `-v my-nginx-data:/usr/share/nginx/html`: Docker가 관리하는 'my-nginx-data'라는 이름의 볼륨을 컨테이너 내부 경로에 연결. 컨테이너가 삭제되어도 볼륨에 저장된 데이터는 유지됩니다. 데이터를 영속적으로 관리할 때 사용합니다.
*   **컨테이너 관리:**
    *   `docker ps`: 실행 중인 컨테이너 목록 확인
    *   `docker ps -a`: 모든 컨테이너 목록 확인 (종료된 컨테이너 포함)
    *   `docker logs [container_id]`: 컨테이너 로그 확인
    *   `docker attach [container_id]`: 컨테이너의 메인 프로세스 STDIN/STDOUT/STDERR에 연결 (Ctrl+C로 종료될 수 있음)
    *   `docker exec -it [container_id] /bin/bash`: 실행 중인 컨테이너 내부에 새로운 쉘로 접속 (`-it` 옵션 중요)

### 6.3 Git & GitHub 연동

*   **Git 기본 설정:**
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```
    *   `--global` 옵션으로 시스템 전체에 적용
*   **VS Code 연동:**
    *   VS Code의 Source Control 뷰를 통해 Git 저장소를 초기화하고, 변경 사항을 Staging, Commit합니다.
    *   GitHub Extension을 설치하면 VS Code 내에서 Push, Pull, Branch 관리 등을 편리하게 할 수 있습니다.

## 7. 트러블슈팅 & 팁

*   **`echo` 명령어 사용 시 따옴표 주의:** `echo "hello!" > file.txt` 와 같이 큰따옴표(`"`) 안에서 `!` 와 같은 특수 문자가 쉘 히스토리 확장으로 잘못 해석될 수 있습니다. 이 경우 작은따옴표(`'`)를 사용하거나, 역슬래시(`\`)로 이스케이프 처리합니다. (예: `echo 'hello!' > file.txt` 또는 `echo "hello\!" > file.txt`)
*   **권한 문제:** 스크립트 파일을 실행할 때 `permission denied` 에러가 발생하면, `chmod +x script.sh` 또는 `chmod 755 script.sh` 명령어로 실행 권한을 부여해야 합니다.
*   **Docker 실행 관련:**
    *   Docker Desktop이 제대로 실행 중인지 확인합니다.
    *   `docker` 명령어가 인식되지 않으면 PATH 환경변수 설정이 올바른지 확인합니다.
    *   포트가 이미 사용 중일 경우 (`port is already allocated`) 다른 포트를 사용합니다.
*   **VS Code GitHub 연동:**
    *   SSH 키 생성 및 GitHub 등록이 올바르게 되었는지 확인합니다.
    *   Repository 권한이 있는지 확인합니다.
*   **Dockerfile 빌드 오류:** 각 명령어의 오타, 파일 경로 오류 등을 꼼꼼히 확인합니다.

## 8. 추가 학습 자료

*   **터미널 명령어 Cheat Sheet:** [https://devhints.io/bash](https://devhints.io/bash)
*   **Docker 공식 문서:**
    *   Get Started: [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
    *   Dockerfile Reference: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
*   **Git 공식 문서:** [https://git-scm.com/doc](https://git-scm.com/doc)
*   **VS Code GitHub Extension:** [https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions) (GitHub Extension Pack 등)

이 학습 문서를 바탕으로 1주차 미션을 성공적으로 완수하시길 바랍니다! 궁금한 점은 언제든지 커뮤니티나 멘토에게 질문해주세요.

#### 참여 수강생 및 자료
| 수강생 | 레포 | 업데이트 | 추가 자료 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week1](https://github.com/kimch0612/Codyssey_Week1) | 2026-03-31 | 마크다운, 인프라설정 |
| sonjehyun123-maker | [Codyssey-w1-E1](https://github.com/sonjehyun123-maker/Codyssey-w1-E1) | 2026-04-03 | 인프라설정 |
| mulloc1 | [codyssey_workstation](https://github.com/mulloc1/codyssey_workstation) | 2026-03-31 | 학습노트, 마크다운, 인프라설정 |
| ntt65 | [codyssey/e1_1](https://github.com/ntt65/codyssey/tree/main/e1_1) | 2026-04-12 | 학습노트, 분석보고서, 마크다운, 인프라설정 |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | - |
| codewhite7777 | [codyssey_E-1](https://github.com/codewhite7777/codyssey_E-1) | 2026-03-30 | 인프라설정 |
| mov-hyun | [e1-1-workstation-setup](https://github.com/mov-hyun/e1-1-workstation-setup) | 2026-04-05 | 인프라설정 |
| jhkr1 | [Codyssey_mission1](https://github.com/jhkr1/Codyssey_mission1) | 2026-04-07 | 인프라설정 |
| junhnno | [Codyssey_WorkSpace_Week1](https://github.com/junhnno/Codyssey_WorkSpace_Week1) | 2026-04-09 | 인프라설정 |
| sungho255 | [codyssey_1](https://github.com/sungho255/codyssey_1) | 2026-04-07 | - |
| yejoo0310 | [codyssey-m1](https://github.com/yejoo0310/codyssey-m1) | 2026-04-05 | 인프라설정 |
| clae-dev | [ia-codyssey-Docker](https://github.com/clae-dev/ia-codyssey-Docker) | 2026-04-02 | 인프라설정 |
| leehnmn | [codyssey_2026/project-1](https://github.com/leehnmn/codyssey_2026/tree/main/project-1) | 2026-04-08 | 인프라설정 |
| I-nkamanda | [codyssey2026/Problem1_AI_SW_Setup](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem1_AI_SW_Setup) | 2026-04-09 | 마크다운, 설정파일, 인프라설정 |
| peachily | [codyssey11-E1](https://github.com/peachily/codyssey11-E1) | 2026-04-09 | 인프라설정 |
| ikasoon | [codyssey-e1-1](https://github.com/ikasoon/codyssey-e1-1) | 2026-04-06 | 학습노트, 마크다운, 인프라설정 |
| doji-kr | [codyssey_day1_bear1](https://github.com/doji-kr/codyssey_day1_bear1) | 2025-07-11 | 마크다운 |

---

### 2주차 과제 종합

## Codyssey 2주차 AI/SW 교육 과정 학습 문서: 나만의 퀴즈 게임

본 문서는 Codyssey 프로그램 2주차 과제로 진행된 "나만의 퀴즈 게임" 프로젝트를 학습자가 완벽히 이해하고 내재화할 수 있도록 돕기 위해 작성되었습니다. 여러 수강생의 GitHub 레포지토리 정보를 종합하여 프로젝트의 개요, 목표, 요구사항, 핵심 기술, 구현 팁 등을 상세히 다룹니다.

---

### 1. 미션 개요

이번 2주차 미션은 Python을 활용하여 콘솔 기반의 퀴즈 게임을 개발하는 것입니다. 사용자는 퀴즈를 풀고, 새로운 퀴즈를 추가하며, 등록된 퀴즈 목록을 확인하고, 최고 점수를 조회하는 등 다양한 기능을 수행할 수 있습니다. 특히, 프로그램 종료 후에도 퀴즈 데이터와 최고 점수가 유지될 수 있도록 데이터를 파일에 저장하고 불러오는 기능을 구현해야 합니다. 이 과정을 통해 Python의 기본 문법, 객체지향 프로그래밍 개념, 파일 입출력, 예외 처리 등 AI/SW 개발에 필수적인 기초 역량을 다지는 것을 목표로 합니다.

---

### 2. 학습 목표

*   **Python 기본 문법 심화:** 변수, 자료형, 조건문, 반복문, 함수, 클래스 등 Python의 핵심 문법을 실제 프로젝트에 적용하며 복습하고 이해도를 높입니다.
*   **객체지향 프로그래밍(OOP) 이해:** `클래스`와 `객체`의 개념을 이해하고, `Quiz`와 `QuizGame`과 같이 관련된 데이터와 기능을 묶어 설계하는 경험을 쌓습니다. `__init__` 메서드와 `self`의 역할을 명확히 이해합니다.
*   **파일 입출력 및 데이터 관리:** `JSON` 형식을 활용하여 데이터를 파일에 저장하고 불러오는 방법을 익힙니다. 프로그램 종료 후에도 데이터가 유지되는 경험을 통해 데이터 관리의 중요성을 인지합니다.
*   **예외 처리:** `try-except` 구문을 사용하여 프로그램 실행 중 발생할 수 있는 오류(예: 잘못된 입력, 파일 손상)를 안전하게 처리하는 방법을 배웁니다.
*   **모듈화 및 코드 구조화:** 관련 기능을 함수나 클래스로 분리하고, `main.py`, `quiz_app/game.py`, `quiz_app/models.py`와 같이 논리적인 파일 구조를 설계하는 연습을 합니다.
*   **Git 활용:** Git의 기본적인 명령어(`init`, `add`, `commit`, `push`, `branch`, `checkout`, `merge` 등)를 사용하여 버전 관리 및 협업의 기초를 다집니다.

---

### 3. 기능 요구사항

*   **메인 메뉴 제공:** 사용자가 게임을 시작할 때 선택할 수 있는 메뉴(퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 최고 점수 확인, 종료 등)를 제공합니다.
*   **퀴즈 풀기:**
    *   저장된 퀴즈 목록에서 문제를 랜덤으로 선택하여 출제합니다.
    *   사용자는 선택지를 보고 답을 입력합니다.
    *   정답 여부를 판별하고 점수를 누적합니다.
    *   (선택 사항) 문제별 힌트 기능을 제공합니다.
    *   (선택 사항) 출제될 문제 개수를 사용자가 선택할 수 있도록 합니다.
    *   (선택 사항) 문제의 선택지 순서를 랜덤으로 섞습니다.
*   **퀴즈 추가:** 사용자가 직접 새로운 퀴즈(문제, 선택지 4개, 정답 번호, (선택 사항) 힌트)를 입력하여 게임에 추가할 수 있어야 합니다.
*   **퀴즈 목록 확인:** 현재 게임에 등록된 모든 퀴즈의 목록을 보여줍니다.
*   **최고 점수 확인:** 게임 플레이를 통해 얻은 최고 점수와 해당 점수를 얻었을 때의 맞힌 문제 수, 전체 문제 수를 표시합니다.
*   **데이터 저장 및 불러오기:**
    *   퀴즈 데이터와 최고 점수 정보는 `state.json` 파일에 저장되어야 합니다.
    *   프로그램 시작 시 `state.json` 파일이 존재하면 해당 데이터를 불러와 게임에 반영해야 합니다.
    *   파일이 없거나 손상되었을 경우, 기본 퀴즈 데이터로 초기화하고 저장해야 합니다.
*   **예외 처리:**
    *   숫자 입력이 필요한 곳에 숫자가 아닌 값이 입력되었을 경우, 재입력을 요청하거나 오류 메시지를 출력합니다.
    *   `Ctrl+C` 또는 `Ctrl+D`(`EOFError`)와 같은 키보드 인터럽트 시 안전하게 프로그램을 종료하고 데이터를 저장합니다.
*   **Git 활용:** 프로젝트의 개발 과정에서 Git을 사용하여 코드 변경 이력을 관리하고, 필요하다면 브랜치 전략을 활용합니다.

---

### 4. 핵심 기술 스택

*   **프로그래밍 언어:** Python 3.10 이상 권장
*   **주요 라이브러리:** Python 표준 라이브러리 (별도의 외부 라이브러리 설치 없이 구현 가능)
    *   `json`: JSON 데이터 처리
    *   `random`: 문제 랜덤 선택, 선택지 섞기 등
    *   `os`: (선택 사항) 파일 경로 관리 등
*   **데이터 저장 형식:** JSON (`state.json`)
*   **버전 관리:** Git

---

### 5. 권장 프로젝트 구조

수강생들의 레포지토리를 종합하여 다음과 같은 프로젝트 구조를 권장합니다.

```
your_repository_name/
├── .gitignore         # Git 추적에서 제외할 파일 목록
├── README.md          # 프로젝트 설명 및 학습 내용 기록
├── main.py            # 프로그램 실행 진입점
├── quiz_app/          # 퀴즈 게임 관련 모듈을 담는 패키지
│   ├── __init__.py    # 패키지 초기화 파일
│   ├── models.py      # 데이터 모델 (예: Quiz 클래스)
│   ├── game.py        # 게임 로직 관리 (예: QuizGame 클래스)
│   └── utils.py       # (선택 사항) 범용 유틸리티 함수 (예: 입력 처리)
└── state.json         # 퀴즈 데이터 및 최고 점수 저장 파일
└── docs/              # (선택 사항) 스크린샷, 문서 등
    └── screenshots/
```

*   **`main.py`**: 프로그램의 시작점으로서 `QuizGame` 객체를 생성하고 게임 실행(`run()`)을 담당합니다. 예외 처리를 위한 `try-except` 블록을 포함하는 것이 좋습니다.
*   **`quiz_app/` 패키지**:
    *   **`models.py`**: 퀴즈 문제 자체를 나타내는 `Quiz` 클래스 등 데이터 구조를 정의합니다.
    *   **`game.py`**: 게임 전체의 흐름을 관리하는 `QuizGame` 클래스를 정의합니다. 메뉴 표시, 퀴즈 진행, 데이터 로드/저장, 퀴즈 추가/삭제 등의 로직을 포함합니다.
    *   **`utils.py`**: (선택 사항) 사용자 입력 처리, 메뉴 출력 등 반복적으로 사용되는 함수들을 모아놓는 곳입니다.
*   **`state.json`**: JSON 형식으로 퀴즈 목록(`quizzes` 배열)과 최고 점수(`best_score`, `best_correct_count`, `best_total_count` 등)를 저장합니다.

---

### 6. 구현 핵심 포인트

#### 6.1 데이터 모델링 (`models.py`)

*   **`Quiz` 클래스:**
    *   **속성:** `question` (str), `choices` (list of str), `answer` (int, 1-based index).
    *   **메서드:**
        *   `display()`: 문제와 선택지를 보기 좋게 출력합니다.
        *   `is_correct(user_answer)`: 사용자가 입력한 답과 실제 정답을 비교하여 boolean 값을 반환합니다.
        *   `to_dict()`: `Quiz` 객체를 JSON 저장을 위한 딕셔너리 형태로 변환합니다.
        *   `from_dict(data)`: 딕셔너리 데이터를 받아 `Quiz` 객체를 생성합니다. (클래스 메서드 또는 별도 함수로 구현)

#### 6.2 게임 로직 (`game.py`)

*   **`QuizGame` 클래스:**
    *   **속성:** `quizzes` (list of Quiz objects), `best_score` (int), `best_correct_count` (int), `best_total_count` (int), `state_path` (str).
    *   **메서드:**
        *   `__init__()`: `quizzes` 리스트와 `best_score` 등을 초기화하고, `load_state()`를 호출하여 데이터를 불러옵니다.
        *   `load_state()`: `state.json` 파일을 읽어 퀴즈 데이터와 최고 점수를 불러옵니다. 파일이 없거나 오류 발생 시 `_initialize_data()`를 호출합니다.
        *   `save_state()`: 현재 `quizzes` 리스트와 `best_score` 등을 `state.json` 파일에 저장합니다. `Quiz` 객체를 딕셔너리 리스트로 변환하는 과정이 필요합니다.
        *   `_initialize_data()`: 프로그램 시작 시 기본 퀴즈 데이터를 설정하고 `state.json`에 저장합니다.
        *   `run()`: 메인 메뉴를 반복적으로 보여주고 사용자 입력을 받아 해당 기능을 실행합니다.
        *   `show_menu()`: 메뉴 옵션을 출력합니다.
        *   `play_quiz()`: 퀴즈 풀이 로직을 담당합니다. `random.sample`로 문제 선택, `Quiz.display()` 호출, 사용자 입력 처리, `Quiz.is_correct()`로 정답 판별, 점수 계산 및 최고 점수 갱신 등의 과정을 수행합니다.
        *   `add_quiz()`: 사용자로부터 새로운 퀴즈 정보를 입력받아 `Quiz` 객체를 생성하고 `quizzes` 리스트에 추가합니다.
        *   `show_quiz_list()`: `quizzes` 리스트를 순회하며 모든 퀴즈를 출력합니다.
        *   `show_best_score()`: 저장된 최고 점수 정보를 출력합니다.
        *   `delete_quiz()`: (선택 사항) 사용자가 추가한 퀴즈를 삭제하는 기능을 구현합니다.
        *   `prompt_number(prompt_message, min_val, max_val)`: (utils.py 또는 game.py) 숫자 입력을 받고 유효성을 검사하는 함수. 잘못된 입력 시 재시도하도록 합니다.
        *   `prompt_text(prompt_message)`: (utils.py 또는 game.py) 문자열 입력을 받는 함수.

#### 6.3 데이터 관리

*   **JSON 활용:**
    *   `state.json` 파일은 다음과 같은 구조를 가집니다.
    ```json
    {
      "quizzes": [
        {
          "question": "파이썬의 창시자는 누구인가요?",
          "choices": ["귀도 반 로섬", "리누스 토르발스", "제임스 고슬링", "브렌던 아이크"],
          "answer": 1
        },
        // ... 다른 퀴즈들
      ],
      "best_score": 10,
      "best_correct_count": 5,
      "best_total_count": 5
    }
    ```
    *   `load_state()`에서는 `json.load()`를, `save_state()`에서는 `json.dump()`를 사용합니다.

#### 6.4 예외 처리

*   **숫자 입력:** `prompt_number`와 같은 함수 내에서 `try-except ValueError`를 사용하여 `int()` 변환 오류를 처리합니다.
*   **프로그램 종료:** `main.py`에서 `try-except (KeyboardInterrupt, EOFError)`를 사용하여 `Ctrl+C`나 `Ctrl+D` 입력 시 `game.save_state()`를 호출하고 안전하게 종료합니다.
*   **파일/JSON 오류:** `load_state()`에서 `try-except (FileNotFoundError, json.JSONDecodeError)` 등을 사용하여 파일이 없거나 JSON 형식이 잘못되었을 경우를 처리하고 `_initialize_data()`를 호출합니다.

---

### 7. 트러블슈팅 & 팁

*   **정답 인덱스 처리:**
    *   사용자 입력은 보통 1부터 시작하지만, Python 리스트 인덱스는 0부터 시작합니다. 정답 저장 시 0-based index로 저장하고, 사용자에게 보여줄 때는 1-based index로 변환하거나, 반대로 사용자 입력(1-based)을 받아 1을 빼서 0-based index로 처리하는 일관된 규칙을 정하는 것이 중요합니다. (jhkr1 수강생은 1-based index로 저장 후 `is_correct` 등에서 활용)
*   **데이터 로드/저장 시 객체와 딕셔너리 변환:**
    *   `Quiz` 객체를 `state.json`에 직접 저장할 수 없습니다. `save_state()` 메서드에서 `quizzes` 리스트의 각 `Quiz` 객체를 `to_dict()` 메서드를 통해 딕셔너리 형태로 변환한 후 JSON으로 저장해야 합니다.
    *   `load_state()`에서는 JSON에서 읽어온 딕셔너리 리스트를 다시 `Quiz` 객체 리스트로 복원하는 과정이 필요합니다. `Quiz.from_dict()` 클래스 메서드를 활용하거나, 딕셔너리 데이터를 받아 `Quiz` 객체를 생성하는 별도의 함수를 사용할 수 있습니다.
*   **랜덤 기능 활용:**
    *   `random.shuffle(list)`: 리스트의 요소를 무작위로 섞습니다. (예: 선택지 순서 섞기)
    *   `random.sample(population, k)`: 주어진 시퀀스에서 중복 없이 `k`개의 요소를 무작위로 선택합니다. (예: 퀴즈 풀이 시 문제 N개 선택)
*   **메서드 vs 함수:**
    *   "하나의 독립적인 동작"은 함수로, "특정 객체의 상태와 연관된 동작"은 해당 객체의 메서드로 구현하는 것이 객체지향 설계 원칙에 부합합니다. (jhkr1 수강생의 README 참고)
*   **README의 중요성:**
    *   자신의 코드와 학습 내용을 README에 상세히 기록하는 것은 매우 중요합니다. "왜 이렇게 구현했는지", "어떤 Python 개념을 이해했는지" 등을 기록하며 스스로 복습하고, 다른 사람에게 코드를 설명하는 좋은 연습이 됩니다. (jhkr1, sonjehyun123-maker, mov-hyun 수강생 모두 README를 잘 작성했습니다.)
*   **Git 브랜치 활용:**
    *   기능별로 새로운 브랜치를 만들어 작업하고, 완료 후 `main` 또는 `master` 브랜치에 병합하는 워크플로우는 코드의 안정성을 높이고 충돌을 줄이는 데 도움이 됩니다. (mov-hyun 수강생의 README 참고)

---

### 8. 추가 학습 자료

*   **Python 공식 문서:**
    *   [JSON encoding and decoding](https://docs.python.org/ko/3/library/json.html)
    *   [random — Pseudo-random number generator algorithms](https://docs.python.org/ko/3/library/random.html)
*   **객체지향 프로그래밍 (OOP) 개념:**
    *   [점프 투 파이썬 - 클래스와 객체](https://wikidocs.net/28)
    *   [Real Python - Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
*   **Git 학습:**
    *   [Pro Git Book (한국어 번역판)](https://git-scm.com/book/ko/v2)
    *   [생활코딩 - Git & GitHub](https://opentutorials.org/course/1653)
*   **JSON 형식:**
    *   [MDN Web Docs - JSON](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/JSON)

---

본 학습 문서를 통해 2주차 미션에 대한 깊이 있는 이해를 얻으시길 바랍니다. 프로젝트를 완성하며 얻은 지식과 경험은 향후 AI/SW 개발 학습의 훌륭한 밑거름이 될 것입니다.

#### 참여 수강생 및 자료
| 수강생 | 레포 | 업데이트 | 추가 자료 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | 마크다운 |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-10 | - |
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | 학습노트, 마크다운 |
| ntt65 | [codyssey/e1_2](https://github.com/ntt65/codyssey/tree/main/e1_2) | 2026-04-12 | 마크다운 |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | - |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-12 | - |
| yeowon083 | [quiz-game](https://github.com/yeowon083/quiz-game) | 2026-04-12 | - |
| jhkr1 | [Codyssey_mission2](https://github.com/jhkr1/Codyssey_mission2) | 2026-04-11 | - |
| junhnno | [Codyssey_WorkSpace_Week2](https://github.com/junhnno/Codyssey_WorkSpace_Week2) | 2026-04-11 | - |
| sungho255 | [codyssey_2](https://github.com/sungho255/codyssey_2) | 2026-04-07 | - |
| yejoo0310 | [codyssey-m2](https://github.com/yejoo0310/codyssey-m2) | 2026-04-10 | 마크다운 |
| yejibaek12 | [Python-Quiz-Game](https://github.com/yejibaek12/Python-Quiz-Game) | 2026-04-11 | - |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | 마크다운 |
| leehnmn | [codyssey_2026/project-2](https://github.com/leehnmn/codyssey_2026/tree/main/project-2) | 2026-04-08 | - |
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-09 | 마크다운 |

---

### 3주차 과제 종합

## Codyssey 3주차 과제 학습 문서: Mini NPU Simulator

### 1. 미션 개요

본 미션은 사람이 시각적으로 인식하는 '십자가(Cross)'와 'X' 패턴을 컴퓨터가 숫자 연산을 통해 판별하는 원리를 구현해보는 **Python 콘솔 애플리케이션** 개발입니다. 단순한 패턴 인식이 아닌, **2차원 배열, 필터, MAC(Multiply-Accumulate) 연산, 라벨 정규화, 부동소수점 비교 정책, 시간 복잡도 분석** 등 AI/SW의 근간을 이루는 핵심 개념들을 직접 코드로 구현하고 이해하는 것을 목표로 합니다.

### 2. 학습 목표

이 과제를 성공적으로 완료하고 내재화했다면, 다음 내용을 스스로 설명하고 적용할 수 있어야 합니다.

1.  **MAC 연산의 정의 및 원리**: Multiply-Accumulate 연산이 무엇이며, 입력 패턴과 필터를 곱하고 더해 유사도를 구하는 과정을 설명할 수 있습니다.
2.  **데이터 형식 이해**: `data.json` 파일의 키 규칙(필터, 패턴)과 라벨 규칙을 해석할 수 있습니다.
3.  **라벨 정규화의 필요성**: 왜 라벨 정규화 과정이 필요한지, 그리고 이를 통해 얻는 이점을 설명할 수 있습니다.
4.  **부동소수점 비교 정책**: `epsilon` 기반 비교가 왜 필요한지, 그리고 동점(tie) 상황을 어떻게 처리하는지 이해할 수 있습니다.
5.  **시간 복잡도 분석**: 패턴 크기가 커질수록 연산량(`O(N^2)`)이 왜 증가하는지, 그리고 이는 실제 AI 하드웨어(NPU)의 동작 원리와 어떻게 연결되는지 설명할 수 있습니다.
6.  **실패 케이스 진단**: 프로그램 실행 중 발생하는 실패를 데이터 문제, 스키마 문제, 로직 문제, 수치 비교 문제 등으로 분류하고 진단할 수 있습니다.

### 3. 기능 요구사항

*   **MAC 연산 구현**: 입력 패턴과 필터 간의 MAC 연산을 수행하여 유사도 점수를 계산합니다.
*   **패턴 판별**: 계산된 MAC 점수를 기반으로 입력 패턴이 'Cross'인지 'X'인지 판별합니다.
*   **라벨 정규화**: 다양한 형식의 라벨(예: '+', 'cross', 'x')을 내부 표준 라벨('Cross', 'X')로 통일합니다.
*   **동점 처리**: 부동소수점 오차를 고려하여 `epsilon` 기반으로 동점(tie) 상황을 처리하고 'UNDECIDED' 또는 '판정 불가'로 표시합니다.
*   **데이터 처리**: `data.json` 파일에서 필터와 패턴 데이터를 읽어와 일괄 처리합니다.
*   **성능 분석**: 각 패턴별 MAC 연산 시간 측정 및 `O(N^2)`에 따른 연산량 변화를 측정하고 보고합니다.
*   **결과 리포트**: 전체 테스트 수, 통과 수, 실패 수, 실패 케이스 목록을 요약하여 출력합니다.
*   **예외 처리**: 잘못된 입력 데이터, 스키마 오류, 숫자 파싱 오류 등 다양한 예외 상황에 대해 프로그램이 비정상 종료되지 않고 명확한 오류 메시지를 출력하도록 합니다.

### 4. 핵심 기술 스택

*   **Python**: 프로그래밍 언어
*   **JSON**: 데이터 형식 (필터 및 패턴 데이터 저장)
*   **2차원 배열 (List of Lists)**: 패턴 및 필터 데이터 표현
*   **Numpy (Optional)**: 행렬 연산 및 시간 측정 라이브러리 (본 과제에서는 외부 라이브러리 없이 구현하는 것을 권장)
*   **Time Module**: 연산 시간 측정
*   **Sys Module**: 프로그램 종료 및 인자 처리 (선택 사항)
*   **Json Module**: JSON 파일 파싱

### 5. 권장 프로젝트 구조

수강생들의 레포지토리를 종합하여 다음과 같은 구조를 권장합니다. 이는 코드의 모듈화, 재사용성, 테스트 용이성을 높여줍니다.

```
your_repo_name/
├── .gitignore
├── README.md              # 프로젝트 전반 설명, 실행 가이드, 학습 내용 요약
├── data.json              # 필터 및 패턴 데이터 (JSON 형식)
├── main.py                # 애플리케이션 진입점, 모드 선택 및 흐름 제어
├── src/                   # 핵심 소스 코드
│   ├── __init__.py
│   ├── app/               # 콘솔 UI, 사용자 입력/출력, 메뉴 흐름 제어
│   │   ├── __init__.py
│   │   ├── console_flow.py   # 메인 메뉴 라우팅, 모드 선택 분기
│   │   ├── user_input_3x3.py # 3x3 사용자 입력 모드 처리
│   │   ├── data_json_mode.py # data.json 분석 모드 처리
│   │   ├── report.py         # 결과 리포트 생성
│   │   └── constants.py      # 앱 관련 상수 정의 (메뉴 번호 등)
│   ├── npu/               # NPU 핵심 로직 (MAC, 판정, 벤치마크)
│   │   ├── __init__.py
│   │   ├── mac.py            # MAC 연산 구현, 입력 검증
│   │   ├── judgement.py      # MAC 점수 기반 판정 로직 (epsilon 포함)
│   │   ├── labels.py         # 라벨 정규화 로직
│   │   ├── constants.py      # NPU 로직 관련 상수 (epsilon 값 등)
│   │   └── benchmark.py      # 성능 측정 및 시간 복잡도 분석
│   └── npu_io/            # 데이터 입출력 및 스키마 검증
│       ├── __init__.py
│       ├── json_loader.py    # data.json 파일 로딩
│       ├── schema.py         # JSON 스키마 검증, 패턴/필터 매칭
│       └── parse.py          # 콘솔 입력 등 문자열 파싱
├── tests/                 # 단위 테스트 코드
│   ├── __init__.py
│   ├── app/
│   ├── npu/
│   └── npu_io/
└── docs/                  # 과제 관련 문서
    ├── subject.md         # 과제 요구사항
    ├── commit_guidelines.md # Git 커밋 컨벤션
    ├── implementation_checklist.md # 구현 체크리스트
    └── insights/          # 학습 인사이트, 심층 개념 정리
        ├── cpu_gpu_npu_deep_learning.md
        ├── code_structure_principles_interview.md
        └── ...
```

**참고:**
*   `src/` 하위의 `app`, `npu`, `npu_io`는 역할 기반 분리로, 실제 프로젝트에서는 더 세분화되거나 통합될 수 있습니다.
*   `tests/` 폴더 구조는 `src/` 폴더 구조를 미러링하는 것이 테스트 관리 용이성을 높입니다.

### 6. 구현 핵심 포인트

#### 6-1. MAC 연산 (`compute_mac`)

*   **입력**: `pattern` (2D list), `filter` (2D list), `size` (정사각형 한 변의 길이)
*   **로직**:
    ```python
    total_score = 0.0
    for r in range(size):
        for c in range(size):
            total_score += pattern[r][c] * filter[r][c]
    return total_score
    ```
*   **주의**: 입력 패턴과 필터의 크기가 반드시 일치해야 합니다. `validate_mac_inputs` 함수 등에서 사전 검증이 필요합니다.

#### 6-2. 라벨 정규화 (`normalize_label`)

*   다양한 입력 라벨('+', 'cross', 'x', 'Cross', 'X' 등)을 내부적으로 사용할 표준 라벨('Cross', 'X')로 통일하는 함수입니다.
*   **예시**:
    ```python
    def normalize_label(label):
        label = label.lower().strip()
        if label in ['+', 'cross', 'c']:
            return 'Cross'
        elif label in ['x', 'ex']:
            return 'X'
        else:
            return label # 또는 오류 발생/None 반환
    ```
*   이 함수는 `data.json`의 `expected` 값, 필터 키(`size_N.cross` -> 'Cross') 등 다양한 곳에서 사용됩니다.

#### 6-3. `epsilon` 기반 비교 (`is_close`, `decide_label`)

*   부동소수점 연산의 오차 때문에 `score1 == score2` 와 같은 직접 비교는 지양해야 합니다.
*   `abs(score1 - score2) < epsilon` (예: `epsilon = 1e-9`)을 사용하여 두 점수가 매우 가까우면 같은 것으로 간주합니다.
*   **판정 로직**:
    ```python
    epsilon = 1e-9
    if abs(score_cross - score_x) < epsilon:
        return 'UNDECIDED'
    elif score_cross > score_x:
        return 'Cross'
    else:
        return 'X'
    ```

#### 6-4. `data.json` 스키마 검증

*   **필터**: `filters` 객체 내부에 `size_<N>` 키를 가지며, 각 값은 `<N>x<N>` 2차원 배열이어야 합니다.
*   **패턴**: `patterns` 객체는 `size_<N>_<idx>` 형식의 키를 가지며, 여기서 `<N>`은 패턴의 실제 크기와 일치해야 합니다. 패턴의 `input` 값 역시 `<N>x<N>` 2차원 배열이어야 합니다.
*   **검증**: 패턴 키에서 `N`을 추출하고, 해당 `N`에 맞는 필터를 `filters`에서 찾습니다. 이후 패턴 `input`과 선택된 필터의 크기가 모두 `<N>x<N>`인지 확인합니다.

#### 6-5. 시간 복잡도 분석 (`O(N^2)`)

*   MAC 연산은 `N x N` 배열의 모든 요소를 순회하며 곱하고 더하므로, 연산 횟수는 `N * N = N^2`에 비례합니다.
*   `benchmark.py` 등에서 크기별(`3x3`, `5x5`, `13x13`, `25x25` 등) MAC 연산을 반복 수행하고 평균 시간을 측정하여, `N`이 커짐에 따라 시간이 `N^2` 스케일로 증가함을 보여주어야 합니다.

#### 6-6. 결과 리포트

*   **요약**: 전체 테스트 수, 통과 수, 실패 수, 실패 케이스 목록(패턴 키, 실패 사유)을 명확하게 출력합니다.
*   **실패 사유 분류**:
    *   **데이터/스키마 오류**: `data.json` 형식 불량, 패턴 키 불일치, 크기 불일치 등.
    *   **라벨 오류**: `expected` 라벨이 지원되지 않거나 정규화되지 않은 경우.
    *   **수치/판정 오류**: MAC 점수 계산 오류, `epsilon` 미적용으로 인한 오판정, 동점 처리 미흡.

### 7. 트러블슈팅 & 팁

*   **"JSON 파일이 로드되지 않아요"**:
    *   `data.json` 파일이 코드와 같은 디렉토리에 있는지 확인하세요.
    *   JSON 문법 오류(콤마 누락, 따옴표 오류 등)가 없는지 JSON 검증 도구를 사용해 확인하세요.
*   **"패턴과 필터 크기가 안 맞아요"**:
    *   `data.json`의 패턴 키(`size_<N>_<idx>`)에서 추출한 `N` 값이 실제 `input` 배열의 행/열 개수와 일치하는지 확인하세요.
    *   `filters`에서 해당 `N`에 맞는 필터 묶음(`size_<N>`)을 제대로 선택했는지 확인하세요.
*   **"MAC 점수가 이상하게 나와요"**:
    *   `pattern`과 `filter`의 두중 반복문 인덱스가 `r`, `c`로 정확히 일치하는지 확인하세요.
    *   2차원 배열에서 요소를 가져올 때 `matrix[r][c]` 형식이 올바른지 확인하세요.
*   **"동일한 점수인데 Pass/Fail이 달라져요"**:
    *   `epsilon` 값을 설정하고, `abs(score1 - score2) < epsilon` 조건을 사용하여 비교하는지 확인하세요.
    *   `data.json`의 `expected` 라벨과 실제 판정 라벨이 `normalize_label` 함수를 통해 일관되게 처리되는지 확인하세요.
*   **"시간 측정 결과가 예상과 달라요"**:
    *   `time.time()` 또는 `time.perf_counter()`를 사용하여 연산 시작 전후 시간을 측정하고 차이를 계산하세요.
    *   작은 크기에서는 측정 오차가 클 수 있으니, 여러 번 반복하여 평균 시간을 내는 것이 좋습니다.
    *   MAC 연산만 측정하고 다른 로직(JSON 로딩, 라벨 정규화 등)은 제외했는지 확인하세요.
*   **"모든 테스트를 `main.py`에서 하지 않고 분리하는 이유는 무엇인가요?"**:
    *   `main.py`는 프로그램의 실행 흐름을 제어하는 역할만 하고, 실제 계산, 판정, 데이터 처리 로직은 별도의 모듈(`src/npu/mac.py`, `src/npu_io/json_loader.py` 등)로 분리하는 것이 좋습니다.
    *   이는 각 기능의 **단일 책임 원칙**을 따르고, **테스트하기 쉽게** 만듭니다. `tests/` 폴더에 각 모듈별로 `test_*.py` 파일을 만들어 단위 테스트를 작성하면 코드의 안정성을 높일 수 있습니다.

### 8. 추가 학습 자료

*   **MAC 연산**:
    *   [Machine Learning & Deep Learning: What is MAC Operation?](https://www.youtube.com/watch?v=hOq_9t1x0bA) (영문 영상)
    *   NPU 관련 문서에서 MAC 연산의 중요성에 대해 찾아보세요.
*   **2차원 배열 및 행렬 연산**:
    *   Python 공식 튜토리얼의 리스트 관련 섹션
    *   Numpy 공식 문서 (행렬 연산, 슬라이싱)
*   **JSON 데이터 형식**:
    *   [JSON 공식 가이드](https://www.json.org/json-en.html)
    *   Python `json` 모듈 사용법
*   **시간 복잡도**:
    *   알고리즘 관련 서적 또는 온라인 강의 (예: Coursera, edX)
*   **AI 하드웨어 (NPU, GPU, CPU)**:
    *   [AI 하드웨어 관련 블로그 글 및 논문](https://github.com/mulloc1/codyssey_python_with_npu/blob/main/docs/insights/cpu_gpu_npu_deep_learning.md) (수강생 레포에서 발췌)
*   **코드 구조 및 설계 원칙**:
    *   SOLID 원칙, 단일 책임 원칙 (SRP)
    *   [수강생 레포의 코드 구조 인사이트](https://github.com/mulloc1/codyssey_python_with_npu/blob/main/docs/insights/code_structure_principles_interview.md) (수강생 레포에서 발췌)

#### 참여 수강생 및 자료
| 수강생 | 레포 | 업데이트 | 추가 자료 |
| --- | --- | --- | --- |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | - |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-12 | 학습노트, 마크다운 |
| jhkr1 | [Codyssey_mission3](https://github.com/jhkr1/Codyssey_mission3) | 2026-04-11 | - |
| yejoo0310 | [codyssey-m3](https://github.com/yejoo0310/codyssey-m3) | 2026-04-12 | - |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-09 | - |

---

## 2. 지문 기반 신규 발견 레포

| 사용자 | 레포 | 점수 | 발견 증거 |
| --- | --- | --- | --- |
| impelfin | [neo](https://github.com/impelfin/neo) | 25 | [Tier1] data.json, [Tier2] main.py, [Tier2] requirements.txt, [Tier2] Dockerfile |
| SuperNinjaCat5 | [music](https://github.com/SuperNinjaCat5/music) | 20 | [Tier1] quiz_game.py, [Tier2] requirements.txt, [Tier2] Dockerfile |
| maheshjainckd | [Hacktoberfest2022-for-everyone](https://github.com/maheshjainckd/Hacktoberfest2022-for-everyone) | 15 | [Tier1] quiz_game.py, [Tier2] requirements.txt |
| ChadwickyN | [Projects](https://github.com/ChadwickyN/Projects) | 15 | [Tier1] quiz_game.py, [Tier2] requirements.txt |
| atr0z0z | [geo-wars](https://github.com/atr0z0z/geo-wars) | 15 | [Tier1] questions.json, [Tier2] requirements.txt |
| moshe | [elasticsearch_loader](https://github.com/moshe/elasticsearch_loader) | 15 | [Tier1] data.json, [Tier2] Dockerfile |
| researchlab | [gbp](https://github.com/researchlab/gbp) | 15 | [Tier1] data.json, [Tier2] Dockerfile |
| Ritesh-456 | [awesome-python-project-ideas](https://github.com/Ritesh-456/awesome-python-project-ideas) | 13 | [Tier2] main.py, [Tier2] requirements.txt, [키워드] quiz game |
| kavyakoli12 | [python-mini-projects](https://github.com/kavyakoli12/python-mini-projects) | 13 | [Tier1] quiz_game.py, [키워드] quiz game |
| SaiAshish-Konchada | [Python-Projects-for-Beginners](https://github.com/SaiAshish-Konchada/Python-Projects-for-Beginners) | 10 | [Tier1] quiz_game.py |
| pratikshayadav101010 | [MOTIONCUT_INTERNSHIP_PROJECTS](https://github.com/pratikshayadav101010/MOTIONCUT_INTERNSHIP_PROJECTS) | 10 | [Tier1] quiz_game.py |
| Mtawarira | [quiz_game](https://github.com/Mtawarira/quiz_game) | 10 | [Tier1] quiz_game.py |
| EesunMoon | [leetcode](https://github.com/EesunMoon/leetcode) | 10 | [Tier1] npu_simulator.py |
| fabi1cazenave | [webL10n](https://github.com/fabi1cazenave/webL10n) | 10 | [Tier1] data.json |
| alvaroferran | [MotioSuit](https://github.com/alvaroferran/MotioSuit) | 10 | [Tier1] data.json |
| dovy | [Pedigree-Viewer](https://github.com/dovy/Pedigree-Viewer) | 10 | [Tier1] data.json |

