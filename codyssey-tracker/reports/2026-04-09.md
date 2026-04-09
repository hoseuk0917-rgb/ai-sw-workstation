# Codyssey 주간 학습 자료

> **수집 일시**: 2026년 04월 09일 16:09 KST  
> **추적 후보**: 22명  
> **수집 레포**: 48건

이 문서는 Codyssey 프로그램 수강생들의 공개 GitHub 레포를 자동 수집하여,
주차별 과제 내용을 학습 자료 형태로 정리한 것입니다.

---

## 목차

- [1주차 과제](#week-1) (21명 제출)
- [2주차 과제](#week-2) (23명 제출)
- [3주차 과제](#week-3) (4명 제출)

---

<a id="week-1"></a>
## 1주차 과제

## Codyssey E1-1: AI/SW 개발 워크스테이션 구축 학습 문서

### 1. 미션 개요

본 주차 과제는 AI/SW 개발자로서 필수적인 **터미널(CLI), Docker, Git** 환경을 구축하고 익숙해지는 것을 목표로 합니다. 개발 환경의 일관성과 재현성을 확보하는 것은 협업 및 배포 과정에서 발생할 수 있는 "내 컴퓨터에서는 되는데..."와 같은 문제를 방지하는 실무에서 매우 중요한 역량입니다.

### 2. 학습 목표

이 과제를 완료하면 다음 내용을 설명할 수 있어야 합니다.

1.  **터미널 기본 명령어**: 파일/디렉토리 관리, 텍스트 처리 등 자주 사용하는 CLI 명령어의 기능과 옵션을 이해하고 활용할 수 있습니다.
2.  **파일 권한**: Linux/macOS의 파일 권한(읽기, 쓰기, 실행) 개념과 `chmod` 명령어를 사용하여 권한을 변경하는 방법을 설명할 수 있습니다.
3.  **Docker 기본 개념**: 컨테이너, 이미지, Dockerfile의 역할과 이들 간의 관계를 설명할 수 있습니다.
4.  **Docker 컨테이너 관리**: 컨테이너를 실행, 중지, 삭제하고 로그를 확인하는 기본적인 Docker 명령어를 사용할 수 있습니다.
5.  **Docker 네트워크 및 볼륨**: 포트 매핑, 바인드 마운트, 명명된 볼륨의 개념과 차이점을 이해하고 적용할 수 있습니다.

### 3. 기능 요구사항

과제에서 구현/수행해야 하는 항목은 다음과 같습니다.

#### 필수 항목

*   [x] 터미널 기본 명령어 실습 (pwd, ls, mkdir, cd, touch, cat, echo, cp, mv, rm)
*   [x] `chmod` 명령어를 사용하여 파일 및 디렉토리 권한 변경 실습
*   [x] Docker 설치 확인 (`docker version`)
*   [x] `hello-world` 컨테이너 실행 및 출력 확인
*   [x] Dockerfile을 사용하여 커스텀 웹 서버 이미지 빌드
*   [x] 빌드된 커스텀 이미지를 실행하고 포트 매핑 (`8080:80`)하여 웹 서버 접속 확인
*   [x] 바인드 마운트 (`-v` 옵션)를 사용하여 호스트 파일 시스템의 변경 사항이 컨테이너에 반영되는지 확인
*   [x] Docker 볼륨을 사용하여 컨테이너의 데이터 영속성 확인
*   [x] Git 사용자 정보 설정 (`git config`)
*   [x] GitHub 원격 저장소 생성 및 로컬 저장소 연동, 파일 푸시

#### 보너스 항목 (포함 시 추가 점수 획득 가능)

*   [ ] `docker-compose`를 사용하여 멀티 컨테이너 환경 구성
*   [ ] VSCode와 GitHub 연동 및 협업 기능 활용 (PR, Code Review 등)

### 4. 핵심 기술 스택

| 기술        | 용도                                                     | 핵심 명령어/개념                                                                                                                                    |
| :---------- | :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **터미널**  | 개발 환경과의 상호작용, 명령어 실행, 파일/디렉토리 관리    | `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm`, `chmod`                                                                       |
| **Git**     | 소스 코드 버전 관리, 협업, 변경 이력 추적                   | `git init`, `git add`, `git commit`, `git status`, `git log`, `git push`, `git pull`, `git config`                                                  |
| **Docker**  | 애플리케이션 실행 환경 격리, 배포 자동화, 이식성 확보      | `docker run`, `docker ps`, `docker images`, `docker build`, `docker logs`, `docker stop`, `docker rm`, `Dockerfile`, 포트 매핑 (`-p`), 바인드 마운트 (`-v`), 볼륨 (`--volume`) |
| **Dockerfile** | Docker 이미지를 생성하기 위한 명령어 집합                  | `FROM`, `RUN`, `COPY`, `WORKDIR`, `EXPOSE`, `CMD`, `ENTRYPOINT`                                                                                 |
| **VSCode**  | 코드 편집, Git 통합, Docker 확장 기능 활용 (선택 사항) | 통합 터미널, Git 연동 기능, Docker 확장                                                                                                             |

### 5. 권장 프로젝트 구조

수강생들의 레포 구성을 참고하여 일반적이고 효율적인 프로젝트 구조를 제시합니다.

```text
Codyssey-E1-1/
├── .gitignore                 # Git 추적에서 제외할 파일 목록
├── README.md                  # 프로젝트 설명, 학습 내용, 트러블슈팅
├── my-web-server/             # 커스텀 웹 서버를 위한 Dockerfile 및 소스코드
│   ├── Dockerfile
│   └── index.html             # 웹 서버에 배포할 정적 파일
├── test_files/                # 권한 변경 등 터미널 실습용 파일
│   └── test1.txt
├── images/                    # 실습 과정 증빙을 위한 스크린샷
│   ├── BindMountTest.png
│   ├── PortMappingTest.png
│   └── CustomImageBuild.png
└── docker-compose.yml         # (선택 사항) Docker Compose 파일
```

**설명:**

*   `Codyssey-E1-1/`: 프로젝트 루트 디렉토리
*   `.gitignore`: Git이 추적하지 않을 파일 (예: macOS의 `.DS_Store`, IDE 설정 파일 등)을 명시하여 저장소를 깔끔하게 유지합니다.
*   `README.md`: 프로젝트의 목적, 학습 내용, 설정 방법, 트러블슈팅 등 모든 정보를 담는 핵심 문서입니다.
*   `my-web-server/`: Dockerfile과 함께 커스텀 웹 서버를 구성하는 소스 코드를 모아둡니다. `COPY` 명령어로 컨테이너에 복사될 파일들이 위치합니다.
*   `test_files/`: `chmod` 실습 등 터미널 명령어 학습을 위한 임시 파일들을 관리합니다.
*   `images/`: 각 단계별 실습 결과를 시각적으로 증빙하기 위한 스크린샷을 저장합니다.
*   `docker-compose.yml`: (선택 사항) 여러 컨테이너를 함께 관리해야 할 경우 사용하며, `docker-compose up` 명령어로 한 번에 실행/관리가 가능합니다.

### 6. 구현 핵심 포인트

과제를 수행할 때 반드시 숙지해야 할 핵심 구현 사항은 다음과 같습니다.

1.  **Dockerfile의 기본 명령어 이해 및 활용**:
    *   **왜 중요한가?**: Docker 이미지를 생성하는 "설계도" 역할을 합니다. 어떤 환경에서 어떤 파일이 복사되고 어떤 명령이 실행될지 정의하므로, 원하는 컨테이너 환경을 만들기 위한 가장 기본적인 요소입니다.
    *   **어떻게 접근해야 하는가?**: `FROM`으로 베이스 이미지를 선택하고, `RUN`으로 필요한 패키지를 설치하며, `COPY` 또는 `ADD`로 호스트의 파일(예: `index.html`)을 컨테이너 안으로 옮깁니다. `WORKDIR`, `EXPOSE`, `CMD` 등의 명령어를 적절히 사용하여 컨테이너가 실행될 때 수행될 기본 동작을 설정해야 합니다.

2.  **포트 매핑 (`-p` 옵션)**:
    *   **왜 중요한가?**: 컨테이너 내부에서 실행되는 애플리케이션(예: 웹 서버)을 외부(호스트 머신)에서 접근 가능하게 만드는 핵심적인 네트워크 설정입니다.
    *   **어떻게 접근해야 하는가?**: `docker run -p <호스트_포트>:<컨테이너_포트> <이미지_이름>` 형식으로 사용합니다. 예를 들어, 컨테이너 내부에서 80번 포트로 실행되는 웹 서버를 호스트의 8080번 포트로 열고 싶다면 `-p 8080:80`을 사용합니다.

3.  **바인드 마운트 (`-v` 옵션)**:
    *   **왜 중요한가?**: 호스트 머신의 특정 디렉토리나 파일을 컨테이너의 디렉토리와 연결합니다. 이를 통해 호스트에서 파일을 수정하면 컨테이너 내부에서도 즉시 반영되는 효과를 얻을 수 있으며, 개발 중인 소스 코드를 컨테이너에 쉽게 적용할 수 있습니다.
    *   **어떻게 접근해야 하는가?**: `docker run -v <호스트_경로>:<컨테이너_경로> <이미지_이름>` 형식으로 사용합니다. 예를 들어, 호스트의 `./src` 디렉토리를 컨테이너 내부의 `/app/src` 디렉토리에 연결하려면 `-v $(pwd)/src:/app/src` (macOS/Linux) 또는 `-v "%cd%/src":/app/src` (Windows CMD) 와 같이 사용합니다.

4.  **Docker 볼륨**:
    *   **왜 중요한가?**: 컨테이너가 삭제되어도 데이터가 유지되도록 하는 영속성 메커니즘입니다. 데이터베이스의 데이터, 로그 파일 등 중요한 정보가 컨테이너 생명주기와 분리되어 관리될 수 있도록 합니다.
    *   **어떻게 접근해야 하는가?**: `docker run -v <볼륨_이름>:<컨테이너_경로> <이미지_이름>` 형식으로 사용합니다. Docker가 볼륨을 관리해주므로 호스트의 파일 시스템 경로를 직접 지정할 필요가 없습니다. `docker volume ls` 명령어로 생성된 볼륨을 확인할 수 있습니다.

### 7. 트러블슈팅 & 팁

수강생들의 README에서 발견된 내용과 일반적인 문제점을 기반으로 정리한 트러블슈팅 및 팁입니다.

*   **`echo` 명령어 사용 시 특수문자 처리**:
    *   **문제**: `echo "Hello!" > file.txt` 와 같이 `!`와 같은 특수 문자를 파일에 쓰려고 할 때 쉘의 히스토리 확장 기능 때문에 예상과 다르게 동작할 수 있습니다.
    *   **해결**: `echo 'Hello!' > file.txt` 와 같이 **작은따옴표(')**로 감싸서 사용하면 히스토리 확장이 비활성화되어 원하는 대로 문자열을 파일에 쓸 수 있습니다.
    *   **팁**: `echo` 외에도 여러 명령어에서 특수 문자를 사용할 때 쉘의 해석을 피하려면 작은따옴표로 감싸는 것이 좋습니다.

*   **`chmod` 권한 변경 실수**:
    *   **문제**: `chmod` 명령어로 권한을 잘못 변경하여 파일/디렉토리에 접근할 수 없게 되는 경우가 발생할 수 있습니다. 특히 `chmod 777`과 같이 모든 권한을 부여하는 것은 보안상 매우 위험합니다.
    *   **팁**:
        *   `ls -l` 또는 `ls -ld` 명령어로 변경 전후의 권한을 반드시 확인하세요.
        *   `chmod u+x` (소유자에게 실행 권한 부여), `chmod g+w` (그룹에게 쓰기 권한 부여) 와 같이 **기호 모드**를 사용하여 필요한 권한만 선택적으로 부여하는 것을 권장합니다.
        *   실수로 잘못 변경했다면, `sudo` 권한이 있다면 `sudo chmod 644 <파일명>` 등으로 정상적인 기본 권한으로 복구할 수 있습니다. (단, `/etc` 등 시스템 디렉토리의 권한 변경은 신중해야 합니다.)

*   **Docker 포트 충돌**:
    *   **문제**: 이미 사용 중인 호스트 포트로 컨테이너의 포트를 매핑하려고 할 때 에러가 발생합니다. (예: `Bind for 0.0.0.0:8080 failed: port is already allocated`)
    *   **해결**:
        *   `sudo lsof -i :8080` 명령어로 해당 포트를 사용 중인 프로세스를 확인합니다.
        *   불필요한 프로세스를 종료하거나, 컨테이너 실행 시 다른 호스트 포트를 사용합니다. (예: `-p 8081:80`)
    *   **팁**: `docker ps` 명령어로 현재 실행 중인 컨테이너와 해당 컨테이너가 사용 중인 포트를 확인하여 충돌을 미리 방지할 수 있습니다.

*   **바인드 마운트 경로 문제**:
    *   **문제**: 호스트 경로를 잘못 지정하거나, 상대 경로 대신 절대 경로를 사용해야 하는 경우 파일이 제대로 마운트되지 않을 수 있습니다.
    *   **해결**:
        *   `pwd` 명령어를 사용하여 현재 작업 디렉토리를 확인하고, 상대 경로를 사용할 때는 `$(pwd)/<상대경로>` 와 같이 절대 경로로 변환하여 사용하는 것이 안전합니다.
        *   Docker Desktop (macOS/Windows)에서는 파일 공유 설정이 올바르게 되어 있는지 확인해야 합니다.

*   **Git 브랜치 및 원격 저장소 연동**:
    *   **문제**: `git push` 시 `src refspec main does not match any` 와 같은 에러가 발생하는 경우.
    *   **원인**: 로컬 브랜치(일반적으로 `main` 또는 `master`)가 GitHub의 기본 브랜치와 일치하지 않거나, 원격 저장소가 제대로 설정되지 않은 경우입니다.
    *   **해결**:
        1.  `git branch -m main` (브랜치 이름을 `main`으로 통일)
        2.  `git remote add origin <GitHub_URL>` (원격 저장소 추가)
        3.  `git push -u origin main` (원격 저장소로 푸시하며 추적 관계 설정)

### 8. 추가 학습 자료

본 주차 과제를 더 깊이 이해하기 위해 다음 개념, 키워드, 공식 문서를 참고하세요.

*   **개념/키워드**:
    *   Linux Permissions (rwx, octal notation)
    *   Chown, Chgrp (소유자/그룹 변경)
    *   Docker Architecture (Client-Server)
    *   Docker Image Layers
    *   Docker Networking Modes
    *   Docker Volume Driver
    *   Shell Scripting Basics
    *   SSH (Secure Shell)

*   **공식 문서**:
    *   **Linux/macOS 터미널 명령어**:
        *   `man ls`, `man chmod`, `man mkdir` 등 각 명령어의 매뉴얼 페이지 (터미널에서 `man <명령어>` 실행)
    *   **Docker 공식 문서**:
        *   [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
        *   [Run a container](https://docs.docker.com/engine/reference/run/) (포트 매핑, 볼륨 등 옵션 설명)
        *   [Docker volumes](https://docs.docker.com/storage/volumes/)
    *   **Git 공식 문서**:
        *   [Git user documentation](https://git-scm.com/doc)
        *   [Git - `git config` documentation](https://git-scm.com/docs/git-config)
        *   [Git - `git remote` documentation](https://git-scm.com/docs/git-remote)

---

### 참고 레포 목록 (21명)

| 수강생 | 레포 | 최종 업데이트 | README 분량 | 파일 수 |
|--------|------|:------------:|:-----------:|:-------:|
| LimJongHan | [Codyssey-E1-1](https://github.com/LimJongHan/Codyssey-E1-1) | 2026-04-03 | 34,992자 | 8개 |
| codewhite7777 | [codyssey_E-1](https://github.com/codewhite7777/codyssey_E-1) | 2026-03-30 | 28,643자 | 9개 |
| mov-hyun | [e1-1-workstation-setup](https://github.com/mov-hyun/e1-1-workstation-setup) | 2026-04-05 | 28,398자 | 9개 |
| whitecy01 | [codyssey1](https://github.com/whitecy01/codyssey1) | 2026-04-02 | 21,139자 | 7개 |
| xifoxy-ru | [codyssey_week_01](https://github.com/xifoxy-ru/codyssey_week_01) | 2026-04-08 | 20,267자 | 27개 |
| whdals006 | [Codyssey_E1-1](https://github.com/whdals006/Codyssey_E1-1) | 2026-04-07 | 20,211자 | 6개 |
| Opdata | [codyssey-workstation](https://github.com/Opdata/codyssey-workstation) | 2026-04-08 | 19,310자 | 8개 |
| JungSaeYoung | [codyssey_E1-1](https://github.com/JungSaeYoung/codyssey_E1-1) | 2026-04-04 | 17,817자 | 11개 |
| clae-dev | [ia-codyssey-Docker](https://github.com/clae-dev/ia-codyssey-Docker) | 2026-04-02 | 17,674자 | 18개 |
| coding-monkey-326 | [codyssey-e1-1](https://github.com/coding-monkey-326/codyssey-e1-1) | 2026-03-31 | 17,258자 | 4개 |
| jhj9109 | [codyssey1](https://github.com/jhj9109/codyssey1) | 2026-04-01 | 15,746자 | 27개 |
| 0-hu | [codyssey-e1-1](https://github.com/0-hu/codyssey-e1-1) | 2026-04-06 | 13,870자 | 5개 |
| waz6432 | [CodysseyE1-1](https://github.com/waz6432/CodysseyE1-1) | 2026-04-03 | 12,437자 | 3개 |
| sonjehyun123-maker | [Codyssey-w1-E1](https://github.com/sonjehyun123-maker/Codyssey-w1-E1) | 2026-04-03 | 10,846자 | 4개 |
| kimch0612 | [Codyssey_Week1](https://github.com/kimch0612/Codyssey_Week1) | 2026-03-31 | 7,624자 | 0개 |
| sourcreamsource | [codysseyWeekOne](https://github.com/sourcreamsource/codysseyWeekOne) | 2026-04-08 | 5,289자 | 48개 |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | 2,122자 | 0개 |
| mulloc1 | [codyssey_workstation](https://github.com/mulloc1/codyssey_workstation) | 2026-03-31 | 2,092자 | 16개 |
| dolphin1404 | [Codyssey_E_1_2](https://github.com/dolphin1404/Codyssey_E_1_2) | 2026-04-07 | 2,038자 | 5개 |
| I-nkamanda | [codyssey2026/Problem1_AI_SW_Setup](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem1_AI_SW_Setup) | 2026-04-08 | 1,707자 | 39개 |
| wilderif | [codyssey-e1-1](https://github.com/wilderif/codyssey-e1-1) | 2026-04-03 | 957자 | 32개 |

---

<a id="week-2"></a>
## 2주차 과제

## Codyssey AI/SW 교육 과정 - 2주차 학습 문서

### 1. 미션 개요

이번 주차의 목표는 Python 기초 문법과 객체 지향 프로그래밍 개념을 활용하여 터미널 기반의 퀴즈 게임을 구현하는 것입니다. 더불어 Git과 GitHub를 사용하여 코드 변경 이력을 체계적으로 관리하고 협업의 기본 흐름을 익히는 것을 목표로 합니다. 이 과정을 통해 실무에서 자주 접하는 CLI(Command Line Interface) 애플리케이션 개발 경험과 버전 관리 시스템 활용 능력을 함양하게 됩니다.

### 2. 학습 목표

이 과제를 완료하면 다음 다섯 가지 핵심 개념을 설명할 수 있어야 합니다.

1.  **Python 클래스와 객체**: `Quiz`와 `QuizGame`과 같은 클래스를 정의하고, 이 클래스들을 활용하여 객체를 생성하고 상호작용하는 방법을 이해합니다.
2.  **콘솔 애플리케이션**: `input()`, `print()` 함수 등을 사용하여 사용자와 상호작용하는 터미널 기반 프로그램을 설계하고 구현하는 방법을 익힙니다.
3.  **데이터 지속성**: `state.json` 파일을 활용하여 프로그램 실행 상태(퀴즈 데이터, 최고 점수 등)를 저장하고 불러오는 메커니즘을 이해하고 구현합니다.
4.  **Git & GitHub 워크플로우**: 브랜치 생성, 커밋, 푸시, 풀, 병합 등 Git의 기본적인 명령어와 협업을 위한 GitHub 워크플로우를 이해하고 실제 프로젝트에 적용합니다.
5.  **예외 처리 및 안전 종료**: `try-except` 구문을 사용하여 `KeyboardInterrupt`, `EOFError` 등의 예외를 처리하고, 프로그램이 비정상 종료되는 상황에서도 데이터를 안전하게 저장하는 방법을 배웁니다.

### 3. 기능 요구사항

#### 필수 항목

*   [x] `Quiz` 클래스를 정의하여 퀴즈의 질문, 선택지, 정답, 힌트 등을 저장합니다.
*   [x] `QuizGame` 클래스를 정의하여 게임의 전체 로직 (메뉴 관리, 퀴즈 풀이, 추가, 목록 조회, 점수 확인, 삭제)을 담당하도록 설계합니다.
*   [x] 메인 메뉴를 구성하고, 사용자 입력에 따라 적절한 기능으로 이동하도록 구현합니다.
*   [x] 기본 퀴즈 5개 이상을 포함하여 게임을 시작할 수 있도록 합니다.
*   [x] 퀴즈 풀이 기능을 구현합니다.
    *   [x] 사용자에게 풀고 싶은 문제 수를 선택받습니다.
    *   [x] 선택된 문제 수만큼 퀴즈를 랜덤하게 출제합니다.
    *   [x] 퀴즈 풀이 시 힌트 보기 기능을 제공하고, 힌트 사용 시 점수가 차감되도록 합니다.
    *   [x] 정답/오답 여부를 판별하고 점수를 계산합니다.
*   [x] 퀴즈 추가 기능을 구현합니다.
    *   [x] 사용자로부터 새로운 퀴즈의 질문, 선택지 4개, 정답 번호, 힌트를 입력받아 저장합니다.
*   [x] 퀴즈 목록 조회 기능을 구현하여 현재 저장된 모든 퀴즈를 보여줍니다.
*   [x] 최고 점수 확인 기능을 구현합니다.
*   [x] `state.json` 파일을 사용하여 퀴즈 데이터, 최고 점수, 플레이 기록 등을 저장하고 불러옵니다.
*   [x] `state.json` 파일이 존재하지 않거나 손상되었을 경우, 기본 데이터로 복구하는 로직을 구현합니다.
*   [x] 숫자 입력 시 발생할 수 있는 예외 (빈 입력, 문자열 입력, 범위를 벗어난 숫자 등)를 처리하고 재입력을 유도합니다.
*   [x] `Ctrl+C` (`KeyboardInterrupt`) 또는 `EOFError` 발생 시, 데이터를 안전하게 저장한 후 프로그램을 종료하도록 합니다.
*   [x] Git을 사용하여 브랜치를 생성하고, 해당 브랜치에서 작업한 후 `main` 브랜치로 병합하는 기본적인 Git 워크플로우를 따릅니다.
*   [x] GitHub에 코드를 푸시하고, 원격 저장소와 로컬 저장소의 상태를 일치시킵니다.

#### 보너스 항목

*   [x] 퀴즈 삭제 기능을 구현합니다.
*   [x] 점수 기록 히스토리 저장 및 조회 기능을 구현합니다.
*   [x] 퀴즈 데이터 구조를 딕셔너리에서 객체로 변환하는 `from_dict` 및 객체를 딕셔너리로 변환하는 `to_dict` 메서드를 구현합니다.
*   [x] `uv`와 같은 의존성 관리 도구를 사용하여 가상환경을 설정하고 프로젝트를 관리합니다.
*   [x] 유닛 테스트 코드를 작성하여 `Quiz` 및 `QuizGame` 클래스의 주요 기능을 검증합니다.
*   [x] `with` 문과 컨텍스트 관리자를 활용하여 파일 입출력 등을 안전하게 처리합니다.

### 4. 핵심 기술 스택

| 기술        | 용도                                                                   | 핵심 명령어/개념                                                                                                                                                                                            |
| :---------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Python      | 프로그램 개발 언어                                                     | 클래스 (`class`), 객체, 메서드, 함수, 변수, 자료형 (문자열, 리스트, 딕셔너리), 제어문 (if, for, while), 모듈/패키지, 예외 처리 (`try-except`), 파일 입출력 (`open()`, `json` 모듈)                               |
| Git         | 버전 관리 시스템                                                       | `git init`, `git clone`, `git add`, `git commit`, `git push`, `git pull`, `git branch`, `git checkout`, `git merge`, `git log`, `git remote`                                                                 |
| GitHub      | Git 기반 코드 호스팅 및 협업 플랫폼                                    | Repository 생성, Push/Pull, Pull Request (PR), Issue Tracking (추후 활용)                                                                                                                                |
| JSON        | 데이터 교환 형식                                                       | `json.dump()`, `json.load()`, `json.dumps()`, `json.loads()` (데이터 저장 및 로드)                                                                                                                           |
| `uv` (선택) | Python 의존성 관리 및 가상환경 도구                                    | `uv init`, `uv python pin`, `uv venv`, `uv run` (프로젝트 초기화, Python 버전 고정, 가상환경 생성/활성화, 실행)                                                                                             |
| `unittest` (선택) | Python 내장 유닛 테스트 프레임워크                                     | `unittest.TestCase`, `setUp()`, `tearDown()`, `assertEqual()`, `assertRaises()`, `mock` (테스트 케이스 작성, 설정/해제, 검증, 입력/출력 모킹)                                                              |

### 5. 권장 프로젝트 구조

수강생들의 실제 레포 구조를 종합하여 다음과 같은 프로젝트 구조를 권장합니다.

```text
project_root/
├── .gitignore             # Git 추적에서 제외할 파일/디렉토리 목록
├── README.md              # 프로젝트 설명, 사용법, 기능 등을 담은 문서
├── main.py                # 프로그램의 진입점 (QuizGame 객체 생성 및 실행)
├── requirements.txt       # (uv 사용 시) 프로젝트 의존성 목록
├── pyproject.toml         # (uv 사용 시) 프로젝트 설정 파일
├── src/                   # 소스 코드 디렉토리
│   ├── __init__.py        # src를 Python 패키지로 인식하게 함
│   ├── models/            # 클래스 정의 (모델)
│   │   ├── __init__.py
│   │   ├── quiz.py        # Quiz 클래스 정의
│   │   └── quiz_game.py   # QuizGame 클래스 정의
│   ├── data/              # 기본 데이터 관련 모듈
│   │   ├── __init__.py
│   │   └── default_quizzes.py # 기본 퀴즈 데이터를 생성하는 함수/변수
│   ├── utils/             # 공통 유틸리티 함수
│   │   ├── __init__.py
│   │   └── input_handler.py # 사용자 입력 처리 함수 (get_number_input 등)
│   └── messages.py        # 출력 메시지 관리 (선택 사항)
├── state.json             # 프로그램 실행 상태 저장 파일 (자동 생성)
├── tests/                 # 테스트 코드 디렉토리 (선택 사항)
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── test_quiz.py
│   │   └── test_quiz_game.py
│   └── data/
│       ├── __init__.py
│       └── test_default_quizzes.py
└── docs/                  # 추가 문서, 계획, 인사이트 등
    ├── plan.md
    ├── code_and_json_guide.md
    └── ...
```

### 6. 구현 핵심 포인트

1.  **클래스 설계 및 역할 분담**:
    *   **왜 중요한가**: 복잡한 프로그램을 구조화하고 유지보수성을 높이기 위해 필수적입니다. 각 클래스는 명확한 책임(Single Responsibility Principle)을 가져야 합니다.
    *   **어떻게 접근해야 하는가**: `Quiz` 클래스는 개별 퀴즈의 데이터와 간단한 메서드(예: `display`, `check`)를 담당하도록 합니다. `QuizGame` 클래스는 게임의 전반적인 흐름, 메뉴 관리, 데이터 저장/불러오기, 사용자 상호작용 등 게임 로직 전체를 관리하도록 합니다. `models.py`와 `quiz.py`에 각 클래스를 정의하고, `main.py`에서 `QuizGame` 객체를 생성하여 게임을 시작하는 흐름을 따릅니다.

2.  **`state.json`을 이용한 데이터 영속성**:
    *   **왜 중요한가**: 프로그램이 종료된 후에도 사용자의 진행 상황(퀴즈 목록, 최고 점수 등)이 유지되도록 하여 사용자 경험을 향상시킵니다.
    *   **어떻게 접근해야 하는가**:
        *   **저장**: `QuizGame` 클래스 내에 `save_state()` 메서드를 구현합니다. 이 메서드에서는 현재 메모리에 있는 퀴즈 목록, 최고 점수, 플레이 기록 등을 딕셔너리 형태로 조합하여 `json.dump()`를 사용하여 `state.json` 파일에 기록합니다. `add_quiz`, `delete_quiz`, `play_quiz` 완료 시, 그리고 프로그램 종료 시 이 `save_state()` 메서드를 호출합니다.
        *   **불러오기**: `QuizGame` 객체가 생성될 때 `load_state()` 메서드를 호출합니다. `load_state()`는 `state.json` 파일이 존재하는지 확인하고, 존재하면 `json.load()`로 내용을 읽어옵니다. 읽어온 데이터를 파싱하여 `Quiz` 객체 리스트, 최고 점수, 히스토리 등에 할당합니다. 파일이 없거나 JSON 파싱 오류/구조 오류가 발생하면, `default_quizzes.py`에서 제공하는 기본 데이터로 초기화합니다.

3.  **안전 종료 및 예외 처리**:
    *   **왜 중요한가**: 사용자가 `Ctrl+C` 등을 눌러 예기치 않게 프로그램을 종료하더라도, 현재까지의 중요한 데이터가 손실되지 않도록 보호해야 합니다.
    *   **어떻게 접근해야 하는가**:
        *   `try-except` 블록을 사용하여 사용자 입력을 받거나 중요한 로직을 실행하는 부분을 감쌉니다.
        *   `KeyboardInterrupt`와 `EOFError`를 잡는 `except` 블록을 구현합니다.
        *   이 `except` 블록 안에서 `save_state()` 메서드를 호출하여 데이터를 안전하게 저장합니다.
        *   이후 `sys.exit()` 등을 사용하여 프로그램을 깔끔하게 종료합니다.
        *   입력 검증(`get_number_input` 등) 시에도 `try-except ValueError` 등을 사용하여 숫자로 변환할 수 없는 입력에 대해 안전하게 처리하고 재입력을 유도합니다.

### 7. 트러블슈팅 & 팁

*   **`json.dump()` 시 `TypeError: Object of type Quiz is not JSON serializable` 오류**:
    *   **원인**: Python 객체는 기본적으로 JSON으로 바로 직렬화되지 않습니다.
    *   **해결 방법**: `Quiz` 객체를 딕셔너리로 변환하는 `to_dict()` 메서드를 `Quiz` 클래스에 구현하고, `save_state()`에서 퀴즈 리스트를 순회하며 각 `Quiz` 객체를 `to_dict()`로 변환한 후 JSON으로 저장해야 합니다.
*   **`state.json` 파일이 자동으로 생성/업데이트되지 않아요**:
    *   **원인**: `save_state()` 함수가 적시에 호출되지 않았거나, 파일 쓰기 권한 문제일 수 있습니다.
    *   **확인 방법**: `add_quiz`, `delete_quiz`, `play_quiz` 메소드의 마지막 부분 및 `exit_game` (또는 프로그램 종료 로직)에서 `save_state()`가 제대로 호출되는지, 그리고 `state.json` 파일이 저장되는 디렉토리에 쓰기 권한이 있는지 확인합니다.
*   **Git 브랜치 병합 시 충돌**:
    *   **원인**: 여러 브랜치에서 같은 파일의 같은 부분을 수정했을 때 발생합니다.
    *   **해결 방법**: 충돌이 발생한 파일을 열어 Git이 표시해주는 `<<<<<<<`, `=======`, `>>>>>>>` 마커를 확인하며 어떤 코드를 남길지 결정하여 수정합니다. 수정 후에는 `git add`와 `git commit`으로 병합을 완료해야 합니다.
*   **`uv` 환경 설정 문제**:
    *   **확인 방법**: `uv init .` 명령어로 프로젝트를 초기화했는지, `uv python pin 3.12` 등으로 Python 버전을 고정했는지, `uv venv`로 가상환경을 생성하고 `source .venv/bin/activate` (또는 `.venv\Scripts\activate`)로 활성화했는지 확인합니다. `uv run main.py`로 실행하는 것이 좋습니다.
*   **"ModuleNotFoundError" 발생**:
    *   **원인**: Python이 모듈을 찾지 못하는 경우입니다. `src` 디렉토리에 코드를 모듈화한 경우, `PYTHONPATH` 설정이 잘못되었거나, IDE에서 프로젝트 루트를 제대로 인식하지 못하는 경우가 많습니다.
    *   **해결 방법**: `main.py`에서 `src` 디렉토리의 모듈을 임포트할 때 `from src.models import QuizGame`과 같이 상대 경로가 아닌 절대 경로(패키지 기준)로 임포트해야 합니다. IDE의 Python Interpreter 설정을 확인하거나, 스크립트 실행 시 `PYTHONPATH=. python main.py`와 같이 환경 변수를 설정하여 실행합니다.

### 8. 추가 학습 자료

*   **Python 클래스 심화**:
    *   [Python 공식 튜토리얼 - Classes](https://docs.python.org/ko/3/tutorial/classes.html)
    *   [Real Python - Python Classes and Objects](https://realpython.com/python-classes-objects/)
*   **JSON 다루기**:
    *   [Python 공식 문서 - json 모듈](https://docs.python.org/ko/3/library/json.html)
*   **Git & GitHub**:
    *   [Git 공식 문서](https://git-scm.com/doc)
    *   [GitHub Docs](https://docs.github.com/en/get-started)
    *   [생활코딩 - Git & GitHub](https://opentutorials.org/course/1750)
*   **예외 처리**:
    *   [Python 공식 문서 - Built-in Exceptions](https://docs.python.org/ko/3/library/exceptions.html)
    *   [Real Python - Python Try-Except Blocks](https://realpython.com/python-exceptions/)
*   **Contex Managers (`with` 문)**:
    *   [Python 공식 문서 - 5.1.3. With Statement Context Managers](https://docs.python.org/ko/3/tutorial/compound_stmts.html#with-statement-context-managers)
    *   [Real Python - Python Context Managers and How to Create Them](https://realpython.com/python-with-statement/)
*   **`uv` 의존성 관리 도구**:
    *   [uv 공식 문서](https://astral.sh/uv/)

이 학습 문서를 통해 2주차 과제를 성공적으로 완료하고 Python 프로그래밍 및 Git/GitHub 활용 역량을 한층 더 발전시키시길 바랍니다.

---

### 참고 레포 목록 (23명)

| 수강생 | 레포 | 최종 업데이트 | README 분량 | 파일 수 |
|--------|------|:------------:|:-----------:|:-------:|
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | 12,248자 | 15개 |
| JungSaeYoung | [codyssey_E1-2](https://github.com/JungSaeYoung/codyssey_E1-2) | 2026-04-06 | 9,957자 | 8개 |
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | 8,903자 | 17개 |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | 7,552자 | 12개 |
| yeowon083 | [quiz-game](https://github.com/yeowon083/quiz-game) | 2026-04-06 | 7,195자 | 16개 |
| jhj9109 | [codyssey2](https://github.com/jhj9109/codyssey2) | 2026-04-07 | 6,685자 | 20개 |
| xifoxy-ru | [codyssey_week_02](https://github.com/xifoxy-ru/codyssey_week_02) | 2026-04-08 | 6,631자 | 6개 |
| 0-hu | [codyssey-e1-2](https://github.com/0-hu/codyssey-e1-2) | 2026-04-07 | 5,469자 | 10개 |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-09 | 4,082자 | 13개 |
| coding-monkey-326 | [codyssey-e1-2](https://github.com/coding-monkey-326/codyssey-e1-2) | 2026-04-09 | 4,052자 | 10개 |
| whitecy01 | [codyssey2](https://github.com/whitecy01/codyssey2) | 2026-04-08 | 3,062자 | 13개 |
| wilderif | [codyssey-e1-2](https://github.com/wilderif/codyssey-e1-2) | 2026-04-07 | 2,229자 | 21개 |
| LimJongHan | [Codyssey-E1-2](https://github.com/LimJongHan/Codyssey-E1-2) | 2026-04-08 | 2,187자 | 7개 |
| sourcreamsource | [codysseyWeekTwo](https://github.com/sourcreamsource/codysseyWeekTwo) | 2026-04-09 | 1,882자 | 9개 |
| waz6432 | [CodysseyE1-2](https://github.com/waz6432/CodysseyE1-2) | 2026-04-08 | 1,700자 | 14개 |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | 1,032자 | 14개 |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-06 | 829자 | 2개 |
| Opdata | [codyssey-python-with-git](https://github.com/Opdata/codyssey-python-with-git) | 2026-04-08 | 308자 | 6개 |
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-08 | 158자 | 2개 |
| yacheahobbang | [codyssey-E1-2](https://github.com/yacheahobbang/codyssey-E1-2) | 2026-04-08 | 125자 | 3개 |
| yeowon083 | [python-quiz-game](https://github.com/yeowon083/python-quiz-game) | 2026-04-06 | 101자 | 3개 |
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-08 | 없음 | 39개 |
| whdals006 | [Codyssey_E1-2](https://github.com/whdals006/Codyssey_E1-2) | 2026-04-07 | 없음 | 0개 |

---

<a id="week-3"></a>
## 3주차 과제

## Codyssey 3주차: Mini NPU Simulator 개발 학습 문서

### 1. 미션 개요
이번 주차에서는 3x3 크기의 간단한 NPU(신경망 처리 장치) 시뮬레이터를 개발합니다. 실제 딥러닝 모델의 핵심 연산인 MAC(Multiply-Accumulate) 연산을 직접 구현하며, 이를 통해 패턴을 인식하는 기본적인 원리를 이해하고 실무에서 딥러닝 연산의 중요성을 체감하는 것을 목표로 합니다.

### 2. 학습 목표
이 과제를 완료하면 다음을 설명할 수 있어야 합니다.

*   **MAC 연산의 정의 및 동작 방식:** 두 행렬의 같은 위치 요소끼리 곱한 후 모두 더하는 연산의 원리를 설명할 수 있습니다.
*   **MAC 연산의 실무적 활용:** 이미지 처리(필터링, 컨볼루션) 및 신경망 연산에서 MAC 연산이 왜 중요한지 설명할 수 있습니다.
*   **패턴 인식의 기초:** MAC 연산 점수가 필터와 입력 패턴 간의 유사도를 나타내는 지표가 되는 이유를 설명할 수 있습니다.
*   **라벨 정규화의 필요성 및 구현:** 다양한 형태의 라벨 표기를 일관된 기준으로 통일하는 과정과 그 중요성을 설명할 수 있습니다.
*   **부동소수점 오차 처리:** MAC 연산 결과의 미세한 차이를 동점 처리하기 위한 Epsilon 기반 정책의 필요성과 적용 방법을 설명할 수 있습니다.

### 3. 기능 요구사항

#### 필수 항목

*   [x] **MAC 연산 함수 구현**: 외부 라이브러리 없이 이중 반복문을 사용하여 N x N 2차원 배열의 MAC 연산을 수행하는 함수를 구현합니다.
*   [x] **데이터 구조**: N x N 2차원 배열을 저장하고 읽을 수 있으며, 3x3, 5x5, 13x13, 25x25 크기를 모두 처리할 수 있어야 합니다.
*   [x] **모드 선택 메뉴**: 프로그램 실행 시 사용자 입력 모드(1)와 JSON 파일 분석 모드(2)를 선택할 수 있는 메뉴를 제공합니다.
*   [x] **모드 1: 사용자 입력 (3x3)**
    *   [x] 필터 A (3x3)와 필터 B (3x3)를 사용자로부터 입력받습니다.
    *   [x] 패턴 (3x3)을 사용자로부터 입력받습니다.
    *   [x] 입력 시 행/열 개수 불일치, 숫자 파싱 오류 발생 시 오류 메시지를 출력하고 재입력을 유도합니다. (프로그램 종료 금지)
    *   [x] 입력받은 필터와 패턴으로 MAC 연산을 수행하여 A 점수와 B 점수를 계산합니다.
    *   [x] epsilon (1e-9) 기반 동점 처리 정책을 적용하여 판정 결과를 출력합니다. (A, B, 판정 불가)
    *   [x] 연산 시간(10회 평균, ms 단위)을 측정하여 출력합니다.
*   [x] **모드 2: `data.json` 분석**
    *   [x] `data.json` 파일을 읽어 필터와 패턴 데이터를 로드합니다.
    *   [x] `data.json`의 필터 키(`size_N` 형태)와 패턴 키(`size_N_idx` 형태)를 기반으로 해당 크기의 필터와 패턴을 자동으로 매칭합니다.
    *   [x] 필터와 패턴 크기 불일치 시 오류 처리하고 해당 케이스를 FAIL로 처리합니다. (프로그램 종료 금지)
    *   [x] 각 패턴에 대해 'Cross' 필터 점수와 'X' 필터 점수를 계산합니다.
    *   [x] 계산된 점수를 기반으로 패턴의 판정 결과('Cross', 'X', 'UNDECIDED')를 결정합니다.
    *   [x] 결정된 판정 결과와 `data.json`에 명시된 `expected` 값을 비교하여 PASS/FAIL을 출력합니다.
    *   [x] 전체 테스트 수, 통과 수, 실패 수, 실패 케이스 목록(식별자 및 사유 포함)을 요약하여 출력합니다.
*   [x] **성능 분석**:
    *   [x] 3x3, 5x5, 13x13, 25x25 각 크기에 대해 MAC 연산의 평균 수행 시간(ms, 10회 반복 측정, I/O 시간 제외)을 측정합니다.
    *   [x] 각 크기별 평균 시간과 연산 횟수(N²)를 포함한 성능 분석 표를 출력합니다.
*   [x] **README.md 작성**: 과제 개요, 실행 방법, 구현 요약 (라벨 정규화, MAC 구현 방식, Epsilon 정책 등), 결과 리포트 (실패 원인 분석, 시간 복잡도 분석 등)를 포함합니다.

#### 보너스 항목 (선택)

*   [ ] **1차원 배열 최적화**: 2차원 배열을 1차원 배열로 변환하는 함수와 1차원 기반 MAC 연산 함수를 구현하고, 성능 비교 결과를 출력합니다.
*   [ ] **패턴 생성기**: 크기 N을 입력받아 N x N 크기의 'Cross' 패턴과 'X' 패턴을 자동으로 생성하고, 이를 모드 1 및 성능 분석에 활용할 수 있도록 연동합니다.

### 4. 핵심 기술 스택

| 기술             | 용도                                                                     | 핵심 명령어/개념                                                                                                                                                                 |
| :--------------- | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Python           | 메인 프로그래밍 언어, 로직 구현                                          | `def`, `for`, `while`, `if/elif/else`, `list`, `dict`, `float`, `int`, `try/except`                                                                                             |
| `sys` 모듈       | 프로그램 종료, 명령줄 인수 처리 (과제에서는 주로 사용되지 않음)           | `sys.exit()`                                                                                                                                                                     |
| `json` 모듈      | `data.json` 파일 파싱 및 데이터 로드                                     | `json.load(file_object)`, `json.loads(string_data)`                                                                                                                              |
| `time` 모듈      | 연산 시간 측정 (성능 분석)                                               | `time.time()` (시작/종료 시간 기록)                                                                                                                                              |
| 2차원 배열 (List of Lists) | 필터 및 패턴 데이터 저장                                                 | `matrix[row][col]` 접근, 중첩 반복문 (`for r in range(N): for c in range(N):`)                                                                                                     |
| MAC 연산         | 필터와 패턴 간의 유사도 측정 (핵심 알고리즘)                             | `result += matrix_a[i][j] * matrix_b[i][j]`                                                                                                                                      |
| 라벨 정규화      | 다양한 형태의 라벨(e.g., '+', 'cross', 'x')을 표준화                     | `str.lower()`, `str.replace()`, 조건문 (`if/elif/else`)을 활용한 함수 구현                                                                                                        |
| Epsilon 기반 동점 처리 | 부동소수점 오차를 고려한 점수 비교                                       | `abs(score_a - score_b) < epsilon` (e.g., `epsilon = 1e-9`)                                                                                                                      |

### 5. 권장 프로젝트 구조

수강생들의 GitHub 레포 정보를 바탕으로 다음과 같은 구조를 권장합니다.

```text
Mini_NPU_Simulator/
├── .python-version        # (optional) Python 버전 명시
├── README.md              # 프로젝트 설명, 실행 방법, 구현 요약 등
├── main.py                # 프로그램 진입점, 모드 선택 및 분기 처리
├── mac.py                 # MAC 연산 핵심 로직 (2D, 1D)
├── data_loader.py         # data.json 파일 로드 및 검증, 라벨 정규화
├── mode1.py               # 모드 1: 사용자 입력 처리 및 결과 출력
├── mode2.py               # 모드 2: data.json 분석 및 결과 리포트 생성
├── benchmark.py           # 성능 측정 및 분석 기능
├── data.json              # 필터 및 패턴 데이터 (JSON 형식)
├── pattern_gen.py         # (보너스) 패턴 생성기 구현
└── requirements.txt       # (optional, 외부 라이브러리 사용 시)
```

*   **`main.py`**: 사용자 입력을 받아 모드를 결정하고, 해당 모드의 기능을 수행하는 파일을 호출하는 역할을 합니다.
*   **`mac.py`**: MAC 연산 자체의 계산 로직을 담당합니다. 2차원 배열 MAC, (보너스) 1차원 배열 MAC 등을 포함합니다.
*   **`data_loader.py`**: `data.json` 파일에서 필터와 패턴 데이터를 읽어오는 역할을 합니다. 이 파일 내에서 라벨 정규화 로직을 함께 구현하면 코드의 응집도를 높일 수 있습니다.
*   **`mode1.py` / `mode2.py`**: 각 모드의 사용자 인터페이스 및 비즈니스 로직을 분리하여 관리합니다.
*   **`benchmark.py`**: 성능 측정을 위한 코드만 따로 모아두어 관리의 용이성을 높입니다.

### 6. 구현 핵심 포인트

1.  **MAC 연산 로직의 정확성**:
    *   **왜 중요한가**: MAC 연산은 이 과제의 핵심이며, 이 로직이 틀리면 모든 결과가 잘못됩니다. 행렬의 각 요소에 대해 곱셈 후 누적하는 과정을 정확히 구현해야 합니다.
    *   **어떻게 접근해야 하는가**: `for` 루프를 사용하여 행(`i`)과 열(`j`)을 순회하며 `matrix_a[i][j] * matrix_b[i][j]` 값을 누적 변수에 더하는 방식으로 구현합니다. 외부 라이브러리(NumPy 등) 없이 파이썬 기본 기능만 사용해야 합니다.

2.  **입력 검증 및 재입력 유도**:
    *   **왜 중요한가**: 사용자 입력 오류는 프로그램의 안정성을 해칩니다. 특히 모드 1에서는 사용자가 잘못된 값을 입력했을 때 프로그램이 강제 종료되지 않고, 올바른 값이 입력될 때까지 재시도를 해야 합니다.
    *   **어떻게 접근해야 하는가**: `try-except` 블록을 사용하여 숫자로 변환하는 과정에서 발생할 수 있는 `ValueError`나, 행/열 개수 불일치를 검사하여 `if` 조건문으로 처리합니다. 오류 발생 시 `while` 루프를 사용하여 올바른 입력이 들어올 때까지 해당 입력 부분을 다시 받도록 구현합니다.

3.  **라벨 정규화 일관성**:
    *   **왜 중요한가**: `data.json` 파일의 `expected` 값이나 필터 키(`cross`) 등 다양한 형태의 라벨 표기를 코드 내부에서 일관되게 처리하지 않으면, 비교 로직이 복잡해지고 오류 발생 가능성이 높아집니다.
    *   **어떻게 접근해야 하는가**: `normalize_label(label)`과 같은 별도의 함수를 만들어, 입력받은 라벨을 소문자로 변환하고, 필요한 경우 `replace` 함수 등을 이용해 표준 라벨(예: 'Cross', 'X')로 통일합니다. 이 함수를 `data.json` 로딩 시, 필터 키 처리 시, 그리고 최종 판정 비교 시에 일관되게 호출하여 사용합니다.

4.  **Epsilon 기반 동점 처리**:
    *   **왜 중요한가**: 부동소수점 연산은 미세한 오차를 가질 수 있습니다. 이 때문에 사실상 같은 값임에도 불구하고 `score_a == score_b` 비교가 실패할 수 있습니다. 이를 방지하기 위해 허용 오차(`epsilon`)를 설정하여 점수 차이가 매우 작을 경우 동점으로 처리해야 합니다.
    *   **어떻게 접근해야 하는가**: 두 점수의 차이의 절대값이 미리 정의된 작은 값(예: `1e-9`)보다 작으면 동점으로 간주하도록 `abs(score_a - score_b) < epsilon` 조건을 사용합니다. 동점일 경우 'UNDECIDED' 또는 '판정 불가'로 출력합니다.

### 7. 트러블슈팅 & 팁

*   **`data.json` 파싱 오류**:
    *   **문제**: `json.load()` 시 `JSONDecodeError`가 발생하며 파일 형식이 잘못되었다는 메시지가 나올 수 있습니다.
    *   **해결/팁**:
        *   `data.json` 파일의 모든 괄호(`{`, `}`, `[`, `]`), 쉼표(`,`), 콜론(`:`)이 올바르게 작성되었는지 확인합니다.
        *   문자열 값은 반드시 큰따옴표(`"`)로 감싸야 합니다.
        *   JSON 검증 도구(온라인 JSON validator 등)를 사용하여 파일의 유효성을 미리 검사하는 것이 좋습니다.
        *   중첩된 구조에서 특정 키가 없는 경우 `KeyError`가 발생할 수 있습니다. `data_loader.py`에서 `.get(key)` 메서드를 사용하거나 `try-except KeyError` 블록으로 안전하게 접근합니다.

*   **MAC 연산 시 인덱스 오류 (`IndexError`)**:
    *   **문제**: 행렬의 크기가 일치하지 않거나, 반복문에서 범위를 잘못 설정하여 발생합니다.
    *   **해결/팁**:
        *   사용자 입력 모드(모드 1)에서는 3x3으로 고정되므로 상대적으로 안전하지만, `data.json` 분석 모드(모드 2)에서는 필터와 패턴의 크기가 다를 수 있습니다.
        *   패턴 로드 시 패턴의 크기(N)를 추출하고, 해당 크기에 맞는 필터만 사용하도록 로직을 추가해야 합니다.
        *   `len(matrix)`로 행의 개수를, `len(matrix[0])`으로 열의 개수를 얻을 수 있습니다. MAC 연산 함수 시작 부분에서 두 입력 행렬의 크기가 동일한지 검사하는 로직을 추가하는 것이 좋습니다.

*   **부동소수점 비교 문제**:
    *   **문제**: `score_a == score_b`로 비교했을 때, 미세한 오차 때문에 의도와 다르게 `False`가 나오는 경우.
    *   **해결/팁**: `abs(score_a - score_b) < epsilon` (epsilon은 `1e-9` 등 매우 작은 값)과 같이 오차 범위를 허용하는 방식으로 비교합니다. 동점일 경우 'UNDECIDED' 또는 '판정 불가'로 처리하는 규칙을 명확히 합니다.

*   **성능 측정 시 I/O 시간 포함 문제**:
    *   **문제**: `time.time()`으로 전체 함수 실행 시간을 측정하면 파일 로딩, 결과 출력 등 I/O 시간이 포함되어 순수 연산 시간 측정이 부정확해질 수 있습니다.
    *   **해결/팁**: `benchmark.py` 파일에서 성능 측정은 MAC 연산 함수 호출 구간만 감싸서 측정하도록 합니다. 즉, `mac_2d()` 함수 자체의 시작과 끝 시간을 재는 것이 아니라, `main.py`나 `mode2.py`에서 `mac_2d()`를 호출하는 부분만 `time.time()`으로 감싸서 측정합니다.

*   **라벨 정규화 시 누락**:
    *   **문제**: 'cross'는 'Cross'로, '+'는 'Cross'로, 'x'는 'X'로 정규화하는 규칙을 놓치거나 일부만 구현하는 경우.
    *   **해결/팁**: `data.json`에 명시된 모든 가능한 라벨 표기(`+`, `cross`, `x`)와 내부에서 사용할 표준 라벨(`Cross`, `X`)을 명확히 정의하고, `normalize_label` 함수에서 이 모든 경우를 커버하도록 작성합니다. `README`의 구현 요약 부분에서 라벨 정규화의 중요성을 다시 한번 상기하고, 어떤 규칙이 적용되었는지 명시합니다.

### 8. 추가 학습 자료

*   **MAC 연산 및 CNN 기초**:
    *   [Convolutional Neural Networks (CNNs) for Image Recognition](https://www.coursera.org/learn/convolutional-neural-networks) (Coursera - Deep Learning Specialization): CNN의 핵심인 컨볼루션 연산과 MAC 연산의 관계를 자세히 배울 수 있습니다.
    *   [Why are Matrix Multiplications so Important in Deep Learning?](https://towardsdatascience.com/why-are-matrix-multiplications-so-important-in-deep-learning-181749327f5b): 딥러닝에서 행렬 곱셈(MAC 연산의 집합)의 중요성을 설명하는 글입니다.

*   **Python 데이터 구조 및 알고리즘**:
    *   [Python 2D Lists (Matrices)](https://www.programiz.com/python-programming/list-of-lists): 파이썬에서 2차원 리스트(행렬)를 다루는 기본적인 방법.
    *   [Time Complexity O(N^2)](https://www.geeksforgeeks.org/time-complexity-for-nested-loops-in-python/): 중첩 반복문 (`O(N^2)`)의 시간 복잡도 이해.

*   **JSON 데이터 형식**:
    *   [JSON Tutorial](https://www.w3schools.com/js/js_json_intro.asp): JSON 데이터 형식의 기본 구조 및 파싱 방법.
    *   [Python `json` module documentation](https://docs.python.org/3/library/json.html): 파이썬 표준 라이브러리 `json` 모듈의 사용법.

*   **부동소수점 연산**:
    *   [Floating Point Arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic): 부동소수점 연산의 특징과 한계에 대한 위키백과 설명.

---

### 참고 레포 목록 (4명)

| 수강생 | 레포 | 최종 업데이트 | README 분량 | 파일 수 |
|--------|------|:------------:|:-----------:|:-------:|
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | 10,408자 | 0개 |
| JungSaeYoung | [codyssey_E1-3](https://github.com/JungSaeYoung/codyssey_E1-3) | 2026-04-08 | 4,373자 | 11개 |
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-08 | 없음 | 1개 |
| 0-hu | [codyssey-e1-3](https://github.com/0-hu/codyssey-e1-3) | 2026-04-07 | 없음 | 1개 |

---
