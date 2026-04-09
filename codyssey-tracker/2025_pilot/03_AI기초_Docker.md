코디세이 AI 올인원 과정 '단원 5: Docker / 컨테이너 기술' 학습 자료

## 1. 미션 개요

본 단원은 현대 소프트웨어 개발 및 배포의 핵심 기술인 Docker 컨테이너 기술에 대한 심층적인 이해와 실습 능력을 함양하는 것을 목표로 합니다. 가상 머신(VM)과 컨테이너의 근본적인 차이점을 이해하고, Docker 이미지의 계층 구조, 컨테이너 런타임의 역할 및 종류를 학습합니다. 또한, Dockerfile을 사용하여 애플리케이션 이미지를 효율적으로 빌드하고, 포트 매핑, 볼륨 관리, 네트워크 격리 등 컨테이너 운영에 필수적인 개념들을 실습을 통해 익힙니다. 최종적으로 Docker Hub와 같은 컨테이너 레지스트리를 활용하여 이미지를 공유하고 배포하는 과정을 경험함으로써, 실제 서비스 환경에 Docker를 적용할 수 있는 기반 지식을 구축합니다.

## 2. 학습 목표

이 과제를 통해 수강생은 다음을 달성할 수 있습니다:

*   **Docker 기본 개념 이해**: 가상 머신과 컨테이너의 차이점, Docker 이미지와 컨테이너의 관계, 이미지 레이어의 동작 원리를 설명할 수 있습니다.
*   **컨테이너 런타임 이해**: `containerd`, `runc`, `CRI-O` 등 주요 컨테이너 런타임의 역할과 특징을 비교 설명할 수 있습니다.
*   **Docker CLI 활용**: `docker run`, `docker ps`, `docker images`, `docker inspect`, `docker history`, `docker rm`, `docker rmi` 등 핵심 Docker CLI 명령어를 능숙하게 사용할 수 있습니다.
*   **컨테이너 관리 능력**: 컨테이너 이름 지정(`--name`), 포트 매핑(`-p`), 컨테이너 내부 명령어 실행(`docker exec`) 등 컨테이너 생명주기를 관리할 수 있습니다.
*   **Dockerfile 작성 및 최적화**: 애플리케이션을 위한 Dockerfile을 작성하고, `.dockerignore`를 활용하여 이미지 크기를 최적화하며, Gunicorn과 같은 WSGI 서버를 사용하여 프로덕션 환경에 적합한 이미지를 빌드할 수 있습니다.
*   **컨테이너 영속성 및 데이터 관리**: Bind Mount와 Docker Volume의 차이점을 이해하고, 각 기술을 활용하여 컨테이너 데이터를 영속적으로 관리하는 방법을 적용할 수 있습니다.
*   **컨테이너 레지스트리 활용**: Docker Hub에 계정을 생성하고, 로컬 이미지를 태그하여 원격 레지스트리에 푸시(`docker push`)하고 풀(`docker pull`)하는 과정을 수행할 수 있습니다.
*   **운영체제별 Docker 환경 이해**: Linux 컨테이너와 Windows 컨테이너의 차이점을 이해하고, WSL2와 같은 환경의 필요성을 설명할 수 있습니다.
*   **Docker 기반 개발 환경 구축**: Python Flask 애플리케이션을 Docker 컨테이너로 패키징하고 실행하는 전반적인 과정을 수행할 수 있습니다.

## 3. 기능 요구사항

과제에서 구현/수행해야 하는 구체적인 기능이나 작업은 다음과 같습니다.

*   **Docker Desktop 설치 및 기본 동작 확인**:
    *   운영체제에 맞는 Docker Desktop을 설치하고 `docker --version`, `docker info` 명령어로 설치를 확인합니다.
    *   `hello-world` 이미지를 실행하여 Docker의 기본 동작을 검증합니다.
*   **Ubuntu 컨테이너 실습**:
    *   Docker Hub에서 `ubuntu:20.04` 이미지를 검색하고 다운로드합니다.
    *   `ubuntu` 컨테이너를 실행하고 내부에서 파일 생성 및 확인 작업을 수행합니다.
    *   컨테이너 이름 지정(`--name`)의 중요성을 이해하고 실습합니다.
*   **Python Flask 애플리케이션 컨테이너화**:
    *   `python:3` 이미지를 기반으로 Python 개발 환경 컨테이너를 생성합니다.
    *   호스트의 애플리케이션 코드를 컨테이너로 복사하고, 필요한 패키지를 설치합니다.
    *   Flask 애플리케이션을 컨테이너 내에서 실행하고, 호스트 포트와 컨테이너 포트 매핑(`-p`)을 통해 웹 브라우저로 접속을 확인합니다.
    *   실행 중인 컨테이너의 변경 사항을 새로운 이미지로 커밋(`docker commit`)하여 저장합니다.
*   **Dockerfile 작성 및 최적화**:
    *   Flask 애플리케이션을 위한 `Dockerfile`을 작성합니다.
    *   `gunicorn`을 사용하여 프로덕션 환경에 적합한 웹 서버를 구성합니다.
    *   `.dockerignore` 파일을 작성하여 불필요한 파일이 이미지에 포함되지 않도록 설정합니다.
    *   작성된 Dockerfile로 이미지를 빌드하고 실행하여 웹 서비스가 정상 작동하는지 확인합니다.
    *   빌드된 이미지 내부에서 `.dockerignore` 설정이 올바르게 적용되었는지 확인합니다.
*   **컨테이너 데이터 영속성 관리**:
    *   Bind Mount를 사용하여 호스트 파일 시스템과 컨테이너 내부 디렉토리를 연결하고, 호스트에서 파일 변경 시 컨테이너에 실시간 반영되는 것을 확인합니다.
    *   Docker Volume을 생성하고 컨테이너에 연결하여, 컨테이너 삭제 후에도 데이터가 유지되는 것을 확인합니다.
*   **컨테이너 레지스트리 활용**:
    *   Docker Hub 계정을 생성하고 Personal Access Token을 발급받습니다.
    *   로컬에서 빌드한 이미지를 Docker Hub에 로그인 후 태그(`docker tag`)하고 푸시(`docker push`)합니다.
    *   푸시된 이미지를 다른 환경에서 풀(`docker pull`)하여 실행할 수 있음을 이해합니다.
*   **Git 및 GitHub 연동**:
    *   실습 과정에서 생성된 파일들을 Git으로 관리하고 GitHub 원격 저장소에 커밋 및 푸시합니다.

## 4. 핵심 기술 스택

| 카테고리 | 기술/도구 | 설명 |
| :------- | :-------- | :--- |
| **컨테이너 기술** | Docker | 컨테이너 생성, 관리, 배포를 위한 핵심 플랫폼 |
| **컨테이너 런타임** | containerd, runc, CRI-O | 컨테이너 실행 및 격리를 담당하는 저수준 컴포넌트 |
| **운영체제** | Linux (Ubuntu), Windows | 컨테이너 실행 환경 및 호스트 OS |
| **프로그래밍 언어** | Python | Flask 웹 애플리케이션 개발에 사용 |
| **웹 프레임워크** | Flask | 경량 웹 애플리케이션 프레임워크 |
| **WSGI 서버** | Gunicorn | Python 웹 애플리케이션을 위한 WSGI HTTP 서버 |
| **버전 관리** | Git | 소스 코드 버전 관리 시스템 |
| **원격 저장소** | GitHub | Git 저장소 호스팅 및 협업 플랫폼 |
| **컨테이너 레지스트리** | Docker Hub | Docker 이미지 공유 및 저장소 |
| **터미널/쉘** | PowerShell, Bash | 명령어 실행 환경 |

## 5. 권장 프로젝트 구조

본 과제는 `Codyssey` 루트 디렉토리 내에서 진행되며, Docker 관련 파일들은 루트 디렉토리에 위치시키고, 학습 자료 폴더는 별도로 관리하는 것을 권장합니다.

```
Codyssey/
├── app.py                   # Flask 애플리케이션 메인 파일
├── requirements.txt         # Python 패키지 의존성 목록 (flask, gunicorn, gTTS)
├── Dockerfile               # Docker 이미지 빌드 지시 파일
├── .dockerignore            # Docker 빌드 시 제외할 파일/디렉토리 목록
├── .git/                    # Git 버전 관리 메타데이터
├── venv/                    # Python 가상 환경 (선택 사항, .dockerignore에 포함)
├── images/                  # 실습 스크린샷 등 이미지 자료
├── docker-compose.yml       # Docker Compose 설정 파일 (보너스 과제)
├── .env                     # 환경 변수 파일 (보너스 과제)
├── 과정_1/                  # 이전 학습 자료 폴더
├── 과정_5/                  # 현재 단원 학습 자료 폴더
│   ├── 문제_1/
│   ├── 문제_2/
│   ├── ...
│   └── 문제_6/
├── 과정_6/                  # 다음 학습 자료 폴더
└── README.md                # 프로젝트 README 파일
```

**`app/` 디렉토리 활용 (선택 사항):**
만약 웹 서비스 소스 파일만 별도로 관리하고 싶다면, `app/` 디렉토리를 생성하여 `index.html` 또는 `app.py`와 같은 파일을 그 안에 넣고, `Dockerfile`에서 `COPY app/ /usr/share/nginx/html/` 또는 `COPY app/ /app`과 같이 경로를 조정할 수 있습니다. 이 경우 `app.py`는 `app/app.py`가 됩니다.

## 6. 구현 핵심 포인트

### 6.1. 컨테이너 개념 및 런타임 이해

*   **가상머신(VM) vs 컨테이너**:
    *   VM은 하이퍼바이저 위에서 독립적인 OS를 구동하여 강력한 격리를 제공하지만, 오버헤드가 크고 부팅 시간이 오래 걸립니다.
    *   컨테이너는 호스트 OS의 커널을 공유하며 `cgroups`와 `네임스페이스`를 활용하여 프로세스 수준의 격리를 제공합니다. 리소스 사용량이 적고 부팅이 빠릅니다.
    *   **네임스페이스(Namespaces)**: 각 컨테이너가 독립적인 시스템 리소스 뷰(파일 시스템, PID, 네트워크 등)를 갖도록 합니다.
    *   **cgroups**: 컨테이너가 사용할 수 있는 CPU, 메모리, I/O 등의 리소스 사용량을 제한하고 격리합니다.
*   **이미지(Image) vs 컨테이너(Container)**:
    *   **이미지**: 컨테이너를 생성하기 위한 "설계도" 또는 "템플릿"입니다. 불변하며, 파일 시스템 계층 구조와 메타데이터를 포함하는 읽기 전용 스냅샷입니다. `docker build` 명령으로 생성됩니다.
    *   **컨테이너**: 이미지를 기반으로 메모리 위에서 실행되는 "실제 인스턴스"입니다. 이미지 위에 쓰기 가능한 레이어가 추가되어 동작하며, `docker run` 명령으로 생성됩니다.
*   **컨테이너 런타임**: 컨테이너를 실제로 생성, 실행, 중지, 삭제하는 역할을 하는 소프트웨어 컴포넌트입니다.
    *   **`runc`**: OCI(Open Container Initiative) 표준 기반의 저수준 런타임으로, 컨테이너의 생성 및 실행을 담당합니다.
    *   **`containerd`**: CNCF 프로젝트이자 Docker의 핵심 컴포넌트입니다. `runc` 위에 위치하여 이미지 전송, 스토리지 관리, 컨테이너 실행 및 감독 등 고수준 기능을 제공합니다.
    *   **`CRI-O`**: Kubernetes를 위한 경량 런타임으로, Kubernetes CRI(Container Runtime Interface)를 구현하여 `containerd`와 유사한 역할을 수행합니다.

### 6.2. Docker CLI 기본 명령어

Docker의 핵심 기능을 다루는 명령어들을 숙지해야 합니다.

```bash
# Docker 설치 확인
docker --version
docker info

# hello-world 컨테이너 실행
sudo docker run hello-world

# 이미지 목록 확인
sudo docker images

# 컨테이너 목록 확인 (실행 중인 컨테이너만)
sudo docker ps
# 모든 컨테이너 목록 (종료된 컨테이너 포함)
sudo docker ps -a

# 이미지 상세 정보 확인
sudo docker inspect hello-world

# 컨테이너 상세 정보 확인 (컨테이너 ID는 실제 값으로 대체)
sudo docker inspect <컨테이너_ID>
# 예시: 가장 최근 생성된 컨테이너 inspect
sudo docker inspect $(docker ps -a -n 1 -q)

# 이미지 히스토리 확인 (레이어 정보)
sudo docker history hello-world

# 컨테이너 삭제
sudo docker rm <컨테이너_ID_또는_이름>
# 모든 종료된 컨테이너 삭제
sudo docker container prune

# 이미지 삭제
sudo docker rmi <이미지_ID_또는_이름:태그>
```

### 6.3. 컨테이너 이름 관리 (`--name`)

컨테이너에 이름을 지정하면 식별 및 관리가 용이해집니다. 이름을 지정하지 않으면 Docker가 무작위 이름을 할당합니다.

```bash
# 이름 미지정: Docker가 무작위 이름 할당 (예: crazy_wilson)
sudo docker run -it ubuntu:20.04 bash

# 이름 지정: 'my-ubuntu-test' 이름으로 컨테이너 생성
sudo docker run -it --name my-ubuntu-test ubuntu:20.04 bash

# 이름 지정된 컨테이너 재시작 및 진입
sudo docker start -ai my-ubuntu-test
```
*   **이름 미지정 시**: 컨테이너 종료 시 자동 삭제되거나, 재실행 시 새로운 컨테이너가 생성되어 이전 상태가 유지되지 않습니다.
*   **이름 지정 시**: 컨테이너를 정지(`docker stop`) 후에도 `docker start` 또는 `docker exec` 명령으로 재사용 가능하며, 내부에 생성된 파일이나 상태가 유지됩니다.

### 6.4. 포트 매핑 (`-p`) 및 네트워크 격리

컨테이너는 기본적으로 호스트와 격리된 가상 네트워크에서 실행됩니다. 외부에서 컨테이너 내부 서비스에 접근하려면 포트 매핑이 필수적입니다.

```bash
# 호스트의 8080 포트를 컨테이너의 80 포트에 매핑
docker run -it -p 8080:80 --name python-dev python:3 bash
```
*   **컨테이너 포트**: 컨테이너 내부에서 서비스가 리스닝하는 포트 (예: Flask 앱의 `0.0.0.0:80`).
*   **호스트 포트**: 호스트(PC)가 외부로 노출하는 포트. 외부 사용자는 이 포트를 통해 컨테이너 서비스에 접근합니다.
*   **네트워크 격리**: 컨테이너는 Docker 내부의 격리된 가상 네트워크에 존재하며, 호스트 네트워크와 분리되어 있습니다. 포트 매핑은 이 격리된 네트워크와 호스트 네트워크 사이에 "터널"을 생성하는 역할을 합니다.

### 6.5. Dockerfile 작성 및 최적화

Dockerfile은 Docker 이미지를 빌드하기 위한 지시 사항을 담은 텍스트 파일입니다. 효율적인 Dockerfile 작성은 이미지 크기, 빌드 속도, 보안에 큰 영향을 미칩니다.

**예시 Dockerfile (`app.py`와 `requirements.txt`가 루트에 있다고 가정):**

```dockerfile
# 1. 베이스 이미지 지정 (경량화된 Python 이미지 사용)
FROM python:3.10-slim

# 2. 컨테이너 내부 작업 디렉토리 설정
WORKDIR /app

# 3. 호스트의 현재 디렉토리 내용을 컨테이너의 /app 디렉토리로 복사
#    .dockerignore 파일에 의해 제외된 파일은 복사되지 않음
COPY . .

# 4. Python 패키지 설치 (캐시 사용 안 함으로 이미지 크기 최적화)
RUN pip install --no-cache-dir -r requirements.txt

# 5. 컨테이너가 노출할 포트 지정 (문서화 목적)
EXPOSE 80

# 6. 컨테이너 시작 시 실행될 명령어 (Gunicorn 사용)
#    app:app은 app.py 파일 내의 Flask 애플리케이션 객체 이름이 'app'임을 의미
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
```

*   **`FROM`**: 베이스 이미지 지정. `slim` 또는 `alpine` 태그를 사용하여 경량 이미지를 선택하는 것이 좋습니다.
*   **`WORKDIR`**: 이후 명령어가 실행될 컨테이너 내부 작업 디렉토리 설정.
*   **`COPY . .`**: 호스트의 현재 디렉토리(`.`은 Dockerfile이 위치한 디렉토리)의 모든 내용을 컨테이너의 `WORKDIR`(`.`은 `/app`)로 복사합니다. `.dockerignore`에 명시된 파일은 제외됩니다.
*   **`RUN`**: 이미지 빌드 시 실행될 명령어. 각 `RUN` 명령어는 새로운 이미지 레이어를 생성합니다. 여러 명령어를 `&&`로 연결하여 하나의 `RUN` 명령으로 만드는 것이 이미지 레이어 수를 줄여 최적화에 도움이 됩니다.
*   **`EXPOSE`**: 컨테이너가 리스닝할 포트를 문서화합니다. 실제 포트 매핑은 `docker run -p`로 이루어집니다.
*   **`CMD`**: 컨테이너 시작 시 실행될 기본 명령어. `ENTRYPOINT`와 함께 사용될 수 있습니다. 여기서는 Gunicorn을 사용하여 Flask 앱을 실행합니다.

**`.dockerignore`의 역할**:
Docker 이미지 빌드 시 불필요한 파일이나 디렉토리(예: `.git`, `venv`, `__pycache__`, 개발 관련 문서 폴더)가 이미지 빌드 컨텍스트에 포함되지 않도록 필터링합니다. 이는 이미지 크기 축소, 빌드 속도 개선, 민감 정보 제외에 기여합니다.

```dockerignore
.git
.gitignore
.dockerignore
Dockerfile
venv
__pycache__
*.pyc
*.log
# 학습 자료 폴더 제외 (Codyssey 프로젝트 구조에 따라)
과정_1/
과정_5/
과정_6/
```

**Flask와 Gunicorn의 차이**:
*   **Flask 개발 서버**: 단일 스레드로 동작하며 디버깅, 오토리로드 등 개발 편의 기능을 제공합니다. 성능과 안정성이 낮아 개발 환경에 적합합니다.
*   **Gunicorn (WSGI 서버)**: 멀티 워커 프로세스, 비동기 처리, 프로세스 격리 등을 지원하여 높은 성능과 안정성을 제공합니다. 실제 프로덕션 환경 배포에 적합합니다. Nginx와 같은 웹 서버와 함께 사용하면 확장성 있는 구성이 가능합니다.

### 6.6. 컨테이너 데이터 영속성

컨테이너는 기본적으로 임시적이며, 삭제되면 내부 데이터도 함께 사라집니다. 데이터를 영속적으로 유지하기 위해 Bind Mount와 Docker Volume을 사용합니다.

*   **Bind Mount**: 호스트 파일 시스템의 특정 경로를 컨테이너 내부의 특정 경로에 직접 마운트합니다.
    *   **용도**: 개발 중 코드 실시간 반영 (호스트에서 코드 수정 시 컨테이너에 즉시 반영), 호스트의 설정 파일 공유 등.
    *   **명령어**: `-v ${PWD}/app:/usr/share/nginx/html` (현재 디렉토리의 `app` 폴더를 컨테이너의 `/usr/share/nginx/html`에 마운트)
    *   **특징**: 호스트 경로에 의존적이며, 컨테이너 삭제 후에도 호스트 파일은 유지됩니다.
*   **Docker Volume**: Docker가 관리하는 파일 시스템의 특정 영역을 컨테이너에 마운트합니다.
    *   **용도**: 데이터베이스 파일, 로그 파일, 사용자 업로드 파일 등 컨테이너의 생명주기와 독립적으로 유지되어야 하는 영속 데이터 보관.
    *   **명령어**:
        ```bash
        docker volume create mydata # 볼륨 생성
        docker run -d --name vol-test -v mydata:/data ubuntu sleep infinity # 컨테이너에 볼륨 연결
        ```
    *   **특징**: Docker가 저장 위치를 관리하므로 호스트 경로에 구애받지 않으며, 컨테이너 삭제 후에도 볼륨은 별도로 삭제하기 전까지 유지됩니다. 이식성이 높습니다.

### 6.7. 컨테이너 레지스트리 활용 (Docker Hub)

Docker Hub는 Docker 이미지를 저장하고 공유하는 클라우드 기반 레지스트리 서비스입니다.

```bash
# Docker Hub 로그인 (Personal Access Token 사용 권장)
docker login
Username: <DockerHub 사용자명>
Password: <발급받은_토큰>

# 로컬 이미지에 Docker Hub 사용자명/저장소명:태그 형식으로 태그 추가
docker tag david:v1.0 <DockerHub 사용자명>/david:v1.0
# 예시: docker tag david:v1.0 jonghwan159/david:v1.0

# 태그된 이미지를 Docker Hub로 푸시
docker push <DockerHub 사용자명>/david:v1.0
# 예시: docker push jonghwan159/david:v1.0

# (다른 환경에서) 이미지 풀
docker pull <DockerHub 사용자명>/david:v1.0
```
*   **Personal Access Token**: Docker Hub 비밀번호 대신 사용할 수 있는 보안 토큰입니다. 보안 강화를 위해 비밀번호 대신 토큰 사용을 권장합니다.
*   **저장소 생성**: Docker Hub 웹사이트에서 Public 또는 Private 저장소를 생성할 수 있습니다.
*   **태그(`docker tag`)**: 이미지에 새로운 이름과 태그를 부여하여 Docker Hub 저장소 규칙에 맞게 준비합니다.
*   **푸시(`docker push`)**: 로컬 이미지를 원격 레지스트리로 업로드합니다.
*   **풀(`docker pull`)**: 원격 레지스트리에서 이미지를 다운로드합니다.

### 6.8. OS별 Docker 실행 차이 및 WSL2

*   **Linux 컨테이너**: 호스트의 Linux 커널을 공유하여 실행됩니다. 가볍고 빠르며, 대부분의 Docker 사용 사례에 해당합니다.
*   **Windows 컨테이너**: Windows 커널 또는 Hyper-V 기반으로 실행됩니다. .NET Framework, IIS 등 Windows 기반 애플리케이션에 적합합니다. 이미지 크기가 크고 무거운 경향이 있습니다. Docker Desktop에서 "Switch to Windows containers" 옵션으로 전환하여 사용할 수 있습니다.
*   **WSL2 (Windows Subsystem for Linux 2)**: Windows 환경에서 Linux 컨테이너를 효율적으로 실행하기 위한 기술입니다. WSL2는 경량 가상 머신을 사용하여 실제 Linux 커널을 포함하므로, Windows에서 Linux 컨테이너를 거의 네이티브에 가까운 성능으로 실행할 수 있게 합니다. Docker Desktop for Windows는 내부적으로 WSL2를 활용하여 Linux 컨테이너를 구동합니다.

## 7. 트러블슈팅 & 팁

*   **`sudo` 사용**: Linux 환경에서 Docker 명령어를 실행할 때 권한 문제로 `sudo`를 사용해야 할 수 있습니다. `sudo docker ...` 또는 `sudo su -` 후 `docker ...`를 사용합니다. Docker 그룹에 사용자를 추가하여 `sudo` 없이 실행할 수도 있습니다 (`sudo usermod -aG docker $USER && newgrp docker`).
*   **컨테이너 자동 삭제 방지**: `docker run` 명령 시 `-it` 옵션만 사용하고 이름을 지정하지 않으면, 컨테이너 종료 시 자동으로 삭제되거나 재사용이 어렵습니다. `--name` 옵션을 사용하여 이름을 지정하고, `docker start -ai <name>`으로 재진입하는 습관을 들입니다.
*   **포트 충돌**: `docker run -p` 명령 시 호스트 포트가 이미 다른 프로세스에 의해 사용 중이면 에러가 발생합니다. `netstat -ano` (Windows) 또는 `lsof -i :<port>` (Linux) 명령으로 사용 중인 포트를 확인하거나, 다른 호스트 포트를 사용합니다 (예: `-p 8081:80`).
*   **이미지 빌드 실패**: `Dockerfile`의 각 `RUN` 명령어는 새로운 레이어를 생성합니다. 실패 시 이전 레이어까지는 캐시되므로, 실패한 지점부터 디버깅하기 용이합니다. `COPY` 명령 전에 `requirements.txt`만 먼저 복사하여 `pip install`을 실행하면, 코드 변경 시 `pip install` 레이어를 재사용하여 빌드 속도를 높일 수 있습니다.
    ```dockerfile
    # ...
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . . # 나머지 코드 복사
    # ...
    ```
*   **컨테이너 내부 파일 확인**: `docker exec -it <컨테이너_이름> bash` 명령으로 컨테이너 내부에 진입하여 `ls`, `cat` 등으로 파일 시스템을 직접 확인하면 디버깅에 큰 도움이 됩니다. 특히 `.dockerignore`가 제대로 작동했는지 확인하는 데 유용합니다.
*   **로그 확인**: `docker logs <컨테이너_이름>` 명령으로 컨테이너의 표준 출력/오류 로그를 확인하여 애플리케이션 문제를 진단합니다.
*   **리소스 모니터링**: `docker stats` 명령으로 실행 중인 컨테이너의 CPU, 메모리, 네트워크 I/O 사용량을 실시간으로 모니터링할 수 있습니다.
*   **Git 커밋 메시지**: `feat/과정_5/문제_5`와 같이 의미 있는 커밋 메시지 컨벤션을 사용하여 변경 이력을 명확히 합니다.
*   **CNCF Landscape 활용**: 클라우드 네이티브 생태계의 다양한 기술들을 파악하는 데 유용합니다. [https://landscape.cncf.io](https://landscape.cncf.io)

## 8. 추가 학습 자료

*   **Docker 공식 문서**: Docker의 모든 기능과 개념에 대한 가장 정확하고 최신 정보를 제공합니다.
    *   [Docker Get Started](https://docs.docker.com/get-started/)
    *   [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
    *   [Understand images, containers, and storage drivers](https://docs.docker.com/storage/storagedriver/)
    *   [Manage data in Docker](https://docs.docker.com/storage/)
*   **CNCF Landscape**: 클라우드 네이티브 기술 생태계를 시각적으로 탐색할 수 있는 대시보드입니다.
    *   [https://landscape.cncf.io](https://landscape.cncf.io)
*   **Open Container Initiative (OCI)**: 컨테이너 이미지 형식 및 런타임에 대한 표준을 정의합니다.
    *   [https://opencontainers.org/](https://opencontainers.org/)
*   **Gunicorn 공식 문서**: Gunicorn의 설정 및 사용법에 대한 상세 정보를 제공합니다.
    *   [https://gunicorn.org/](https://gunicorn.org/)
*   **WSL2 공식 문서**: Windows에서 Linux 컨테이너를 사용하는 방법에 대한 자세한 정보입니다.
    *   [https://docs.microsoft.com/ko-kr/windows/wsl/](https://docs.microsoft.com/ko-kr/windows/wsl/)