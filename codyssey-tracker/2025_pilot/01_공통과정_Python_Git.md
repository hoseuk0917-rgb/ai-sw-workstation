## 1. 미션 개요

본 단원은 Python 프로그래밍 언어의 기초를 다지고, 웹 개발의 기본 개념인 웹 프레임워크(특히 Flask)를 학습하며, 현대 소프트웨어 개발의 필수 도구인 Git을 활용한 버전 관리 및 협업 역량을 구축하는 데 중점을 둡니다. 총 8개의 주차로 구성되어 있으며, 각 주차는 Python 문법, 웹 애플리케이션 개발, 그리고 Git의 핵심 개념과 고급 활용법을 단계적으로 학습하도록 설계되었습니다. 이를 통해 수강생은 개발 환경 설정부터 실제 웹 애플리케이션 구축, 그리고 효율적인 코드 관리 및 협업 프로세스 이해까지 포괄적인 개발 기초 지식을 습득하게 됩니다.

## 2. 학습 목표

이 과제를 통해 수강생은 다음의 구체적인 학습 목표를 달성해야 합니다.

*   **Python 개발 환경 설정 및 기초 문법 숙달**: Windows Terminal, Python, pip, VS Code 설치 및 설정, Python 기본 문법(함수 정의 등)을 이해하고 활용할 수 있습니다.
*   **Python 웹 프레임워크 기초 이해**: Django, Flask, FastAPI의 특징과 장단점을 비교하고, Flask의 기본 동작 원리(라우팅, 템플릿 렌더링, 확장성)를 이해합니다.
*   **Git 기본 개념 및 명령어 활용**: Git의 버전 관리 시스템 종류(Local, Centralized, Distributed VCS)를 이해하고, `.git` 디렉토리의 역할, `git config`, `git add`, `git commit`, `git status` 등 기본 명령어를 능숙하게 사용할 수 있습니다.
*   **Git 스테이징 영역 및 커밋 개념 이해**: 스테이징 영역의 중요성과 커밋의 역할을 명확히 구분하고, 실제 코드 변경 사항을 효과적으로 관리할 수 있습니다.
*   **Git 고급 버전 관리 전략 이해**: `git reset`과 `git revert`의 차이점 및 사용 시나리오를 이해하고, `git merge`와 `git rebase`의 차이점 및 협업에서의 적절한 브랜치 전략을 수립할 수 있습니다.
*   **Flask 웹 애플리케이션 구축**: Flask를 사용하여 간단한 웹 페이지를 만들고, `0.0.0.0` 및 `127.0.0.1` IP 주소의 의미, 포트 번호의 역할 및 충돌 해결 방안을 이해하여 웹 서버를 운영할 수 있습니다.
*   **알고리즘 기초 이해**: 버블 정렬과 선택 정렬의 원리를 이해하고 비교 분석할 수 있습니다.
*   **문제 해결 능력 및 디버깅**: `Run Without Debugging`과 `Start Debugging`의 차이를 이해하고, Flask 애플리케이션 개발 시 발생할 수 있는 문제(예: 포트 충돌)를 해결할 수 있습니다.

## 3. 기능 요구사항

과제에서 구현/수행해야 하는 구체적인 기능이나 작업은 다음과 같습니다.

*   **개발 환경 설정**:
    *   Windows Terminal, Python (3.8 이상), pip, Visual Studio Code를 설치하고 설정합니다.
    *   Python 환경 변수(Path)를 올바르게 설정하고 `python --version`, `pip --version` 명령어로 확인합니다.
    *   VS Code에 Material Icon Theme 확장을 설치하고 활성화합니다.
*   **Python 기초 프로그래밍**:
    *   Python 인터프리터를 사용하여 "Hello"를 출력합니다.
    *   `my_solution.py` 파일에 `hello()` 함수를 정의하고 "Hello"를 반환하도록 구현합니다.
*   **Flask 웹 프레임워크 학습**:
    *   Flask를 설치하고 `pip show flask` 명령어로 설치를 확인합니다.
    *   Flask를 사용하여 `app.py` 파일을 생성하고 `/` 경로로 접속 시 "Hello, DevOps!"를 반환하는 웹 애플리케이션을 구현합니다.
    *   `app.run(host="0.0.0.0", port=80)`을 사용하여 웹 서버를 실행하고, `0.0.0.0` 및 `127.0.0.1` 접속의 차이점을 설명합니다.
    *   포트 충돌 시 해결 방안을 제시하고, 다른 포트(예: 5001)로 변경하여 실행하는 코드를 작성합니다.
*   **Git 기본 설정 및 활용**:
    *   Git 사용자 정보(`user.name`, `user.email`)를 전역으로 설정합니다.
    *   Windows 환경에서 `core.autocrlf`를 `true`로 설정합니다.
    *   기본 브랜치명을 `main`으로 설정합니다.
    *   기본 에디터를 VS Code로 설정합니다.
    *   `git config --list` 및 `git config --global --edit` 명령어를 사용하여 설정을 확인하고 편집합니다.
    *   `.git` 디렉토리의 역할을 설명하고, 삭제 후 `git status` 명령어를 실행하여 결과를 확인합니다.
*   **Git 버전 관리 실습**:
    *   `sort_calculator.py`와 같은 파일을 생성하고, `git add` 명령어로 스테이징 영역에 추가합니다.
    *   `git commit -m "first commit"` 명령어로 변경 사항을 커밋합니다.
    *   `git status` 명령어를 사용하여 스테이징 및 커밋 후의 상태를 확인합니다.
*   **Git 고급 개념 이해**:
    *   `git reset`과 `git revert`의 차이점을 설명하고, 각각의 사용 시나리오를 제시합니다.
    *   `git merge`와 `git rebase`의 차이점을 설명하고, 협업 환경에서 `merge`를 추천하는 이유를 제시합니다.
*   **알고리즘 학습**:
    *   버블 정렬과 선택 정렬의 정의, 비교 방식, 교환 횟수, 시간 복잡도, 정렬 안정성을 비교 분석하는 표를 작성합니다.
*   **문서 작성**:
    *   Python 웹 프레임워크(Django, Flask, FastAPI) 비교 요약표를 작성합니다.
    *   "배터리가 포함된" 프레임워크, API, ORM 개념을 설명합니다.
    *   `Run Without Debugging`과 `Start Debugging`의 차이점을 설명합니다.

## 4. 핵심 기술 스택

| 카테고리 | 기술/도구 | 설명 |
| :------- | :-------- | :--- |
| **프로그래밍 언어** | Python | 웹 애플리케이션 개발 및 스크립트 작성의 핵심 언어 |
| **웹 프레임워크** | Flask | 경량 웹 애플리케이션 및 REST API 개발 |
| **버전 관리** | Git | 소스 코드 버전 관리 및 협업 |
| **통합 개발 환경 (IDE)** | Visual Studio Code | 코드 작성, 디버깅, 확장 기능 활용 |
| **터미널** | Windows Terminal | 명령줄 인터페이스 (PowerShell, Git Bash) |
| **패키지 관리자** | pip | Python 패키지 설치 및 관리 |
| **운영체제** | Windows | 개발 환경 구축 및 명령어 실행 |
| **개념** | API, ORM | 웹 서비스 및 데이터베이스 연동 이해 |
| **알고리즘** | 버블 정렬, 선택 정렬 | 기본적인 정렬 알고리즘 이해 |

## 5. 권장 프로젝트 구조

본 과정은 여러 주차에 걸쳐 다양한 주제를 다루므로, 각 주제별로 명확하게 구분된 디렉토리 구조를 따르는 것이 학습 및 관리에 효율적입니다.

```
.
├── Codyssey/
│   ├── README.md
│   ├── .git/                                # Git 저장소 (숨김 파일)
│   ├── unit1_python_git/                    # 단원 1 전체 (또는 각 주차별 디렉토리)
│   │   ├── week1_1_flask_hello/             # 1-1: Python 웹 프레임워크 기초
│   │   │   ├── my_solution.py               # Python 함수 예제
│   │   │   ├── python_webframework.md       # 웹 프레임워크 비교 문서
│   │   │   └── task.md                      # 1-1 주차 과제 지시사항
│   │   ├── week1_2_calculator_report/       # 1-2: 거듭제곱 계산기, 리포트 (자료에 없음, 예상)
│   │   │   └── ...
│   │   ├── week1_3_calculator_gtts/         # 1-3: 계산기 v1~v2, gTTS (자료에 없음, 예상)
│   │   │   └── ...
│   │   ├── week1_4_git_directory_sort/      # 1-4: Git 디렉토리 구조, 정렬 알고리즘
│   │   │   ├── git_directory.md             # .git 디렉토리 역할 문서
│   │   │   ├── task.md                      # 1-4 주차 과제 지시사항 (Git 설정)
│   │   │   └── sort_algorithm.py            # 정렬 알고리즘 구현 파일 (예상)
│   │   ├── week1_5_git_staging_commit/      # 1-5: Git Staging과 Commit 개념
│   │   │   ├── staging_vs_commit.md         # 스테이징 vs 커밋 문서
│   │   │   ├── task.md                      # 1-5 주차 과제 지시사항 (정렬 알고리즘 비교)
│   │   │   └── sort_calculator.py           # 정렬 계산기 (예상)
│   │   ├── week1_6_git_reset_revert/        # 1-6: Git Reset vs Revert
│   │   │   └── reset_vs_revert.md           # reset vs revert 문서
│   │   ├── week1_7_flask_webapp/            # 1-7: Flask 웹 앱 구축
│   │   │   ├── app.py                       # Flask 웹 애플리케이션 코드
│   │   │   └── flask_concepts.md            # Flask 관련 개념 문서 (0.0.0.0, 포트 등)
│   │   ├── week1_8_git_merge_rebase/        # 1-8: Git Merge vs Rebase, 브랜치 전략
│   │   │   ├── merge_vs_rebase.md           # merge vs rebase 문서
│   │   │   └── branch_strategy.md           # 브랜치 전략 문서 (예상)
│   │   └── ...
│   └── docs/                                # 공통 문서 또는 최종 정리 문서
│       └── ...
└── .gitignore                               # Git 추적 제외 파일 설정
```

**설명**:

*   `Codyssey/`: 전체 학습 내용을 담는 최상위 디렉토리입니다. Git 저장소로 초기화됩니다.
*   `.git/`: Git이 버전 관리를 위해 사용하는 숨김 디렉토리입니다. 직접 수정하지 않습니다.
*   `unit1_python_git/`: '단원 1: Python 기초 + Git 협업'에 해당하는 모든 자료를 포함합니다.
*   `week1_X_topic/`: 각 주차별 학습 내용을 담는 디렉토리입니다.
    *   `my_solution.py`, `app.py`, `sort_algorithm.py` 등은 실제 구현 코드를 포함합니다.
    *   `python_webframework.md`, `git_directory.md`, `staging_vs_commit.md` 등은 학습 내용을 정리한 마크다운 문서입니다.
    *   `task.md`는 해당 주차의 과제 지시사항을 포함합니다.
*   `docs/`: 전체 과정에서 공통적으로 사용되거나 최종적으로 정리된 문서를 저장할 수 있습니다.
*   `.gitignore`: Git이 추적하지 않을 파일이나 디렉토리를 지정합니다 (예: `.venv/`, `__pycache__/`).

이 구조는 각 주차의 학습 목표와 결과물을 명확히 분리하여 관리하고, Git을 통한 버전 관리를 용이하게 합니다.

## 6. 구현 핵심 포인트

### 6.1. 개발 환경 설정 (1-1)

Windows 환경에서 개발 환경을 효율적으로 구축하는 것이 중요합니다.

*   **Windows Terminal 설치**: `winget`을 사용하여 터미널을 설치합니다. `winget`이 없다면 Windows 업데이트가 필요할 수 있습니다.
    ```powershell
    winget install --id Microsoft.WindowsTerminal -e
    ```
*   **Python 설치**: `Invoke-WebRequest`를 사용하여 Python 설치 파일을 다운로드하고, `/quiet InstallAllUsers=1 PrependPath=1 Include_test=0` 옵션을 통해 자동 설치 및 환경 변수 등록을 수행합니다. `PrependPath=1` 옵션이 중요합니다.
    ```powershell
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe" -OutFile "python-installer.exe"
    Start-Process -FilePath ".\python-installer.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait
    ```
*   **Python 및 pip 경로 확인**: 설치 후 터미널을 재시작하여 환경 변수가 적용되었는지 확인합니다.
    ```powershell
    python --version
    pip --version
    ```
*   **Flask 설치**: Python의 패키지 관리자인 `pip`을 사용하여 Flask를 설치합니다.
    ```powershell
    pip install flask
    pip show flask # 설치 확인
    ```
*   **Visual Studio Code 설치**: `winget`을 사용하여 VS Code를 설치합니다.
    ```powershell
    winget install --id Microsoft.VisualStudioCode -e
    ```
*   **VS Code 확장 설치**: `Material Icon Theme`과 같은 확장은 코드 가독성을 높여줍니다. VS Code 내에서 `Ctrl+Shift+X`로 확장 탭을 열고 검색하여 설치합니다.

### 6.2. Python 기초 및 함수 작성 (1-1)

간단한 Python 코드를 작성하고 실행하는 연습입니다.

*   **Python 인터프리터 사용**:
    ```powershell
    python
    >>> print("Hello")
    Hello
    >>> exit()
    ```
*   **함수 작성 (`my_solution.py`)**:
    ```powershell
    echo "def hello():`n    return 'Hello'" > my_solution.py
    ```
    `type my_solution.py` 명령어로 파일 내용을 확인할 수 있습니다.

### 6.3. Git 초기 설정 및 `.git` 디렉토리 이해 (1-4)

Git을 사용하기 위한 필수 초기 설정과 Git 저장소의 핵심 구조를 이해합니다.

*   **사용자 정보 설정**: 모든 커밋에 기록될 사용자 정보를 설정합니다.
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```
*   **줄바꿈 설정 (Windows)**: Windows와 Unix/Linux 간의 줄바꿈 문자 차이로 인한 문제를 방지합니다.
    ```bash
    git config --global core.autocrlf true
    ```
*   **기본 브랜치명 설정**: Git 2.28 버전부터 기본 브랜치명이 `master`에서 `main`으로 변경되었습니다.
    ```bash
    git config --global init.defaultBranch main
    ```
*   **기본 에디터 설정**: 커밋 메시지 작성 등에 사용될 에디터를 VS Code로 설정합니다.
    ```bash
    git config --global core.editor "code --wait"
    ```
*   **설정 확인**:
    ```bash
    git config --list # 모든 설정 목록 보기
    git config --global --edit # 전역 설정 파일 직접 열기
    ```
*   **`.git` 디렉토리의 역할**: Git 저장소의 모든 메타데이터(커밋 객체, 브랜치 참조, 설정 등)를 포함하는 핵심 디렉토리입니다. 이 디렉토리가 없으면 Git 저장소가 아닙니다.
    ```bash
    # .git 디렉토리 삭제 후 Git 상태 확인 (실험용)
    rm -rf .git
    git status
    # 결과: fatal: not a git repository (Git 저장소가 아님을 확인)
    ```

### 6.4. Git Staging Area와 Commit (1-5)

Git의 핵심 개념인 스테이징 영역과 커밋의 작동 방식을 이해하고 실습합니다.

*   **스테이징 (Staging)**: 변경된 파일을 커밋에 포함할 준비를 하는 단계입니다. `git add` 명령어를 사용합니다.
    ```bash
    # 예시: sort_calculator.py 파일을 스테이징
    git add sort_calculator.py
    git status # 스테이징된 파일 확인
    ```
*   **커밋 (Commit)**: 스테이징 영역에 있는 변경 사항들을 로컬 저장소에 영구적으로 기록하는 작업입니다. 각 커밋은 고유한 해시값을 가지며, 프로젝트의 스냅샷 역할을 합니다.
    ```bash
    git commit -m "Implement initial sorting logic for calculator"
    git status # 커밋 후 상태 확인 (작업 트리가 깨끗해짐)
    ```
    커밋 메시지는 변경 내용을 명확하게 설명해야 합니다.

### 6.5. Git Reset vs Revert (1-6)

버전 이력을 되돌리는 두 가지 주요 방법을 이해하고, 협업 환경에서의 중요성을 파악합니다.

*   **`git reset`**: 특정 커밋 시점으로 브랜치 HEAD를 이동시키고, 그 이후의 커밋 기록을 **삭제**합니다. 주로 개인 작업 브랜치에서 실수한 커밋을 되돌릴 때 사용합니다.
    ```bash
    # 최신 커밋을 취소하고 변경 사항을 워킹 디렉토리에 남김
    git reset HEAD~1
    # 최신 커밋을 취소하고 변경 사항을 스테이징 영역에 남김
    git reset --soft HEAD~1
    # 최신 커밋을 취소하고 변경 사항을 모두 버림 (주의!)
    git reset --hard HEAD~1
    ```
    **주의**: `git reset --hard`는 데이터 손실을 유발할 수 있으므로 신중하게 사용해야 합니다. 특히 이미 원격 저장소에 푸시된 커밋에 대해서는 사용하지 않는 것이 좋습니다.
*   **`git revert`**: 특정 커밋의 변경 사항을 **되돌리는 새로운 커밋**을 생성합니다. 기존 커밋 이력은 그대로 보존되므로, 협업 환경에서 안전하게 변경 사항을 취소할 때 사용합니다.
    ```bash
    # 특정 커밋 (예: abcdef)의 변경 사항을 되돌리는 새 커밋 생성
    git revert abcdef
    ```
    **핵심**: `reset`은 이력을 지우고, `revert`는 이력을 보존하며 되돌립니다.

### 6.6. Flask 웹 앱 구축 및 네트워크 설정 (1-7)

Flask를 사용하여 간단한 웹 애플리케이션을 만들고, 네트워크 관련 개념을 이해합니다.

*   **Flask 애플리케이션 (`app.py`)**:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello_devops():
        return "Hello, DevOps!"

    if __name__ == "__main__":
        # 모든 네트워크 인터페이스에서 접근 가능 (외부에서도 접근 가능)
        # 개발 환경에서만 사용하고, 배포 시에는 보안에 유의해야 함
        app.run(host="0.0.0.0", port=80)
    ```
*   **`0.0.0.0` vs `127.0.0.1`**:
    *   `127.0.0.1` (localhost): 로컬 머신에서만 접근 가능한 IP 주소입니다.
    *   `0.0.0.0`: 모든 네트워크 인터페이스에서 접근 가능하도록 설정합니다. 즉, 동일 네트워크 내 다른 장치나 외부에서도 접근할 수 있습니다.
*   **포트 번호의 의미와 충돌 해결**:
    *   포트 번호는 애플리케이션이 사용하는 네트워크 채널을 정의합니다 (예: HTTP 80, HTTPS 443, Flask 기본 5000).
    *   **포트 충돌 시 해결 방안**:
        1.  **다른 포트 사용**: `app.run(host="0.0.0.0", port=5001)`과 같이 다른 포트 번호를 지정합니다.
        2.  **사용 중인 프로세스 종료**: `lsof -i :<PORT_NUMBER>` (Linux/macOS) 또는 `netstat -ano | findstr :<PORT_NUMBER>` (Windows) 명령어로 해당 포트를 사용하는 프로세스를 찾고, `kill <PID>` (Linux/macOS) 또는 `taskkill /PID <PID> /F` (Windows) 명령어로 종료합니다.
*   **디버깅 모드**:
    *   `Run Without Debugging`: 디버깅 도구 없이 코드를 실행합니다.
    *   `Start Debugging`: 중단점 설정, 변수 추적 등 디버깅 기능을 활성화하여 코드를 실행합니다. 오류 발생 시 문제 추적에 유용합니다.

### 6.7. Git Merge vs Rebase (1-8)

두 가지 브랜치 병합 전략의 차이점과 협업에서의 적절한 사용법을 이해합니다.

*   **`git merge`**: 브랜치들의 이력을 그대로 보존하면서 새로운 병합 커밋을 생성하여 두 브랜치를 합칩니다. 이력이 복잡해질 수 있지만, 변경 이력이 명확하게 남습니다.
    ```bash
    # main 브랜치에서 feature 브랜치를 병합
    git checkout main
    git merge feature
    ```
*   **`git rebase`**: 브랜치의 커밋들을 다른 브랜치의 최신 커밋 위로 "재배치"하여 이력을 선형적으로 만듭니다. 이력이 깔끔해지지만, 기존 커밋 해시가 변경되므로 이미 공유된 브랜치에서는 사용하지 않는 것이 좋습니다.
    ```bash
    # feature 브랜치에서 main 브랜치의 최신 커밋 위로 rebase
    git checkout feature
    git rebase main
    git checkout main
    git merge feature # fast-forward merge 발생
    ```
*   **협업에서의 추천**: **`git merge`**는 이력이 명확하게 남아 누가 어떤 작업을 했는지 추적하기 쉽고, 충돌 발생 시 커뮤니케이션이 용이하므로 협업 환경에서 더 안전하고 권장됩니다. `rebase`는 개인 브랜치에서 작업 이력을 정리할 때 유용합니다.

## 7. 트러블슈팅 & 팁

*   **Python 설치 후 `python` 명령어를 찾을 수 없을 때**:
    *   **해결**: Python 설치 시 "Add Python to PATH" 옵션을 체크했는지 확인합니다. 체크하지 않았다면, Python을 재설치하거나 환경 변수를 수동으로 추가해야 합니다. 설치 후 터미널을 **반드시 재시작**해야 환경 변수가 적용됩니다.
*   **`pip` 명령어를 찾을 수 없을 때**:
    *   **해결**: Python 설치 시 `pip`이 함께 설치되므로, `python` 명령어가 제대로 작동하는지 먼저 확인합니다. `python -m ensurepip --default-pip` 명령어로 `pip`을 재설치할 수 있습니다.
*   **Flask 앱 실행 시 `Address already in use` 오류**:
    *   **원인**: 지정된 포트(기본 5000 또는 80)가 이미 다른 프로세스에 의해 사용 중일 때 발생합니다.
    *   **해결**:
        1.  **다른 포트 사용**: `app.run(port=5001)`과 같이 다른 포트 번호를 지정하여 실행합니다.
        2.  **프로세스 종료**:
            *   **Windows**:
                ```powershell
                netstat -ano | findstr :<PORT_NUMBER> # PID 확인
                taskkill /PID <PID> /F # 프로세스 강제 종료
                ```
            *   **Linux/macOS**:
                ```bash
                lsof -i :<PORT_NUMBER> # PID 확인
                kill <PID> # 프로세스 종료
                ```
*   **Git 설정이 적용되지 않을 때**:
    *   **원인**: `git config` 명령어를 잘못 입력했거나, 전역 설정이 아닌 지역 설정(저장소 내 `.git/config`)에 의해 오버라이드되었을 수 있습니다.
    *   **해결**: `git config --list` 명령어로 현재 적용된 모든 설정을 확인하고, `git config --global --edit` 명령어로 전역 설정 파일을 직접 열어 확인 및 수정합니다.
*   **Git `reset --hard` 사용 시 주의**:
    *   **팁**: `git reset --hard`는 커밋 이력과 워킹 디렉토리의 변경 사항을 모두 삭제하므로, **절대 공유된 브랜치나 중요한 작업에서 사용하지 않아야 합니다.** 개인 작업 브랜치에서만 신중하게 사용하고, 중요한 변경 사항은 미리 백업하거나 `git stash`를 활용하는 것이 좋습니다.
*   **Git `rebase` 사용 시 주의**:
    *   **팁**: `git rebase`는 커밋 이력을 재작성하므로, 이미 원격 저장소에 푸시되어 다른 사람과 공유된 브랜치에서는 사용하지 않는 것이 좋습니다. 공유된 브랜치에서 `rebase`를 사용하면 다른 팀원들의 이력과 충돌을 일으킬 수 있습니다.
*   **VS Code에서 Python 인터프리터 설정**:
    *   **팁**: VS Code에서 Python 파일을 열었을 때, 하단 상태 바에 현재 선택된 Python 인터프리터가 표시됩니다. 클릭하여 올바른 Python 버전(예: `python 3.12.3`)을 선택해야 합니다. 가상 환경을 사용하는 경우 해당 가상 환경의 인터프리터를 선택합니다.
*   **Markdown 작성 팁**:
    *   **팁**: VS Code에서 Markdown 파일을 작성할 때, `Ctrl+Shift+V`를 누르면 실시간 미리보기를 통해 작성 내용을 확인할 수 있습니다. 표, 코드 블록 등 마크다운 문법을 정확히 사용하는 연습을 합니다.

## 8. 추가 학습 자료

*   **Python 공식 문서**:
    *   [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
    *   [The Python Standard Library](https://docs.python.org/3/library/index.html)
*   **Flask 공식 문서**:
    *   [Flask Documentation](https://flask.palletsprojects.com/en/latest/)
    *   [Quickstart](https://flask.palletsprojects.com/en/latest/quickstart/)
*   **Git 공식 문서**:
    *   [Pro Git Book (한국어)](https://git-scm.com/book/ko/v2)
    *   [Git Reference](https://git-scm.com/docs)
*   **Visual Studio Code 공식 문서**:
    *   [VS Code Documentation](https://code.visualstudio.com/docs)
    *   [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
*   **Windows Terminal 공식 문서**:
    *   [Windows Terminal Documentation](https://learn.microsoft.com/ko-kr/windows/terminal/)
*   **winget 사용법**:
    *   [winget 사용 가이드](https://learn.microsoft.com/ko-kr/windows/package-manager/winget/)
*   **알고리즘 시각화**:
    *   [Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms) (버블 정렬, 선택 정렬 등 시각화 자료)
*   **API 개념**:
    *   [MDN Web Docs: Introduction to Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
*   **ORM 개념**:
    *   [Wikipedia: Object-relational mapping](https://en.wikipedia.org/wiki/Object-relational_mapping)