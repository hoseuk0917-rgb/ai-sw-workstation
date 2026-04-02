# AI/SW 개발 워크스테이션 구축

## 1. 프로젝트 개요

상세 명령어 정리는 [명령어 모음.md](./명령어%20모음.md)에 별도로 정리했다.

### 목적
- PowerShell 기반 터미널 조작 익히기
- Git 저장소 초기화 및 GitHub 원격 저장소 연동 익히기
- Docker Desktop 설치 및 Docker CLI 점검하기
- `hello-world`, `ubuntu` 컨테이너 실행으로 기본 동작 확인하기
- `nginx:alpine` 기반 커스텀 이미지 빌드 및 포트 매핑 확인하기
- 바인드 마운트와 Docker 볼륨 영속성을 직접 검증하기

### 이번 과제에서 확인한 핵심 개념
- PowerShell 파일/폴더 조작
- Git 로컬 저장소와 GitHub 원격 저장소 연동
- Docker 이미지와 컨테이너의 차이
- 포트 매핑, 바인드 마운트, 볼륨의 차이
- WSL 환경에서의 파일 권한 실습

---

## 2. 실행 환경

- OS: Windows
- Shell: PowerShell 5.1
- Git: `git version 2.51.2.windows.1`
- Docker: `Docker version 29.3.1, build c2be9cc`
- 작업 경로: `D:\코디세이\ai-sw-workstation`

---

## 3. 수행 체크리스트

- [x] 작업 폴더 생성
- [x] README 및 로그 파일 생성
- [x] Git 저장소 초기화
- [x] GitHub 원격 저장소 연결
- [x] 초기 커밋 및 push
- [x] 권한 실습
- [x] Docker 설치 확인
- [x] Docker 기본 운영 명령 수행
- [x] `hello-world` 실행
- [x] `ubuntu` 컨테이너 실행
- [x] Dockerfile 기반 커스텀 이미지 제작
- [x] 포트 매핑 접속 확인
- [x] 바인드 마운트 반영 확인
- [x] Docker 볼륨 영속성 확인
- [x] GitHub/VSCode 연동 증거 정리

---

## 4. 터미널 조작 로그

### 4-1. 작업 폴더 생성 및 구조 확인

#### 목적
- 과제용 기본 폴더 구조 만들기
- 작업 위치와 파일 구조 확인하기

#### 실행 명령
```powershell
Set-Location 'D:\코디세이'
New-Item -ItemType Directory -Force -Path '.\ai-sw-workstation' | Out-Null
Set-Location '.\ai-sw-workstation'
New-Item -ItemType Directory -Force -Path '.\app','.\logs','.\screenshots' | Out-Null
New-Item -ItemType File -Force -Path '.\README.md','.\logs\terminal.md','.\logs\docker.md' | Out-Null
Get-ChildItem -Force
Get-Location
tree /F
```

#### 확인 내용
- `ai-sw-workstation` 작업 폴더 생성
- `app`, `logs`, `screenshots` 폴더 생성
- `README.md`, `terminal.md`, `docker.md` 생성
- 현재 위치와 폴더 구조 확인

---

### 4-2. PowerShell 기본 조작 실습

#### 목적
- 파일/폴더 생성, 읽기, 복사, 이름 변경, 이동, 삭제 흐름 익히기

#### 실행 명령
```powershell
Set-Location 'D:\코디세이\ai-sw-workstation'

New-Item -ItemType Directory -Force -Path '.\cli_lab' | Out-Null
Set-Location '.\cli_lab'

Get-Location
Get-ChildItem -Force

New-Item -ItemType Directory -Force -Path '.\dir_a','.\dir_b' | Out-Null
New-Item -ItemType File -Force -Path '.\note.txt','.\empty.txt' | Out-Null

'sample line' | Set-Content '.\note.txt'
Get-Content '.\note.txt'

Copy-Item '.\note.txt' '.\dir_a\note-copy.txt'
Rename-Item '.\dir_a\note-copy.txt' 'note-renamed.txt'
Move-Item '.\dir_a\note-renamed.txt' '.\dir_b\'

Remove-Item '.\empty.txt'
Get-ChildItem -Recurse -Force

Set-Location '..'
```

#### 확인 내용
- 현재 위치와 파일 목록 확인
- 디렉토리와 파일 생성
- 파일 내용 기록 및 재확인
- 복사, 이름 변경, 이동, 삭제 수행
- 최종 폴더 구조 확인

---

## 5. 권한 실습

### 5-1. 실습 배경
- Windows `D:` 드라이브(`/mnt/d/...`)에서는 권한 변경 결과가 기대한 형태로 바로 보이지 않았다.
- 제출용 권한 실습은 WSL 홈 디렉토리에서 별도로 수행했다.

### 5-2. 목적
- 파일과 디렉토리 권한 변경 전/후 비교
- `chmod 755`, `chmod 644` 의미 확인

### 5-3. 실행 명령
```powershell
wsl -d Ubuntu-22.04 -- bash -lc "
rm -rf ~/perm_lab &&
mkdir -p ~/perm_lab/dir_a &&
touch ~/perm_lab/file_a.txt &&
echo 'sample' > ~/perm_lab/file_a.txt &&
echo '--- before ---' &&
ls -ld ~/perm_lab/dir_a &&
ls -l ~/perm_lab/file_a.txt &&
chmod 755 ~/perm_lab/dir_a &&
chmod 644 ~/perm_lab/file_a.txt &&
echo '--- after ---' &&
ls -ld ~/perm_lab/dir_a &&
ls -l ~/perm_lab/file_a.txt
"
```

### 5-4. 확인 내용
- 디렉토리 1개와 파일 1개 생성
- 권한 변경 전/후 비교
- 디렉토리 `755`, 파일 `644` 설정 확인

### 5-5. 권한 해석
- `r` = 읽기
- `w` = 쓰기
- `x` = 실행
- `755` = 소유자(rwx), 그룹(rx), 기타 사용자(rx)
- `644` = 소유자(rw), 그룹(r), 기타 사용자(r)

---

## 6. Docker 설치 및 점검

### 6-1. 설치 전 확인

#### 목적
- Docker CLI가 설치되어 있는지 먼저 점검

#### 실행 명령
```powershell
docker --version
docker info
where.exe docker
Get-Command docker -ErrorAction SilentlyContinue
```

#### 확인 내용
- 초기에는 `docker` 명령이 인식되지 않았다.
- `where.exe docker` 결과가 없었다.
- Docker CLI가 설치되지 않았거나 PATH에 등록되지 않은 상태로 판단했다.

---

### 6-2. WinGet 복구 및 Docker Desktop 설치 시작

#### 목적
- `winget` 인식 문제 해결
- Docker Desktop 설치 실행

#### 실행 명령
```powershell
Get-AppxPackage Microsoft.DesktopAppInstaller | Select-Object Name, Version, InstallLocation
Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
$env:PATH += ";$env:LOCALAPPDATA\Microsoft\WindowsApps"
where.exe winget
Get-Command winget -ErrorAction SilentlyContinue
winget --version
winget install -e --id Docker.DockerDesktop
```

#### 확인 내용
- App Installer 존재 확인
- App Installer 재등록 후 PATH 갱신
- `winget` 정상 인식 확인
- Docker Desktop 설치 시작

---

### 6-3. Docker Desktop 수동 실행 및 설치 후 확인

#### 목적
- Docker Desktop 실행 파일 존재 여부 확인
- Docker CLI 동작 여부 확인

#### 실행 명령
```powershell
Test-Path 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
Test-Path 'C:\Program Files\Docker\Docker\resources\bin\docker.exe'
Get-ChildItem 'C:\Program Files\Docker\Docker\resources\bin' -ErrorAction SilentlyContinue | Select-Object Name
Start-Process 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
$env:Path += ';C:\Program Files\Docker\Docker\resources\bin'
where.exe docker
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' --version
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' info
```

#### 확인 내용
- Docker Desktop 실행 파일 존재 확인
- Docker CLI 실행 파일 존재 확인
- Docker Desktop 수동 실행
- `docker --version` 정상 출력
- `docker info`에서 Client/Server 정보 확인

---

## 7. Docker 기본 운영 명령

### 7-1. hello-world 실행 및 기본 운영 확인

#### 목적
- Docker 설치와 엔진 동작 여부 빠르게 확인

#### 실행 명령
```powershell
$env:Path += ';C:\Program Files\Docker\Docker\resources\bin'
docker run --name hello-test hello-world
docker images
docker ps -a
docker logs hello-test
docker rm hello-test
docker stats --no-stream
```

#### 확인 내용
- `hello-world` 실행 성공
- 이미지 목록 확인
- 컨테이너 상태 확인
- 실행 로그 확인
- 테스트 컨테이너 삭제
- `docker stats --no-stream`으로 리소스 상태 1회 확인

---

## 8. 컨테이너 실행 실습

### 8-1. ubuntu 컨테이너 실행 및 내부 명령 수행

#### 목적
- 실행 중인 컨테이너 내부에서 명령 실행하기
- `run`과 `exec` 차이 이해하기

#### 실행 명령
```powershell
$env:Path += ';C:\Program Files\Docker\Docker\resources\bin'
docker run -dit --name ubuntu-test ubuntu bash
docker exec ubuntu-test bash -lc "ls / && echo hello-from-ubuntu"
docker ps -a
docker logs ubuntu-test
docker rm -f ubuntu-test
```

#### 확인 내용
- `ubuntu` 컨테이너 백그라운드 실행
- `docker exec`로 내부 명령 실행
- 컨테이너 상태 확인
- 실습 후 컨테이너 삭제

#### 관찰 내용
- `docker run -it ubuntu bash` : 즉시 컨테이너 내부 셸 진입
- `docker run -dit ...` : 백그라운드 유지 후 `docker exec`로 명령 실행
- `exec` : 실행 중인 컨테이너 안에서 새 명령 수행

---

## 9. Dockerfile 기반 커스텀 이미지

### 9-1. 목적
- `nginx:alpine` 기반 커스텀 정적 웹 서버 이미지 만들기

### 9-2. 베이스 이미지
- `nginx:alpine`

### 9-3. 선택 이유
- 공식 이미지
- 구조가 단순함
- 정적 HTML 테스트에 적합
- 이후 포트 매핑, 바인드 마운트, 볼륨 실습으로 확장 가능

### 9-4. 생성 파일

#### `app/index.html`
```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>AI/SW 개발 워크스테이션</title>
</head>
<body>
  <h1>Hello from my custom nginx container</h1>
  <p>과제용 정적 웹 서버가 정상 실행 중입니다.</p>
  <p>Port mapping test: localhost:8080</p>
</body>
</html>
```

#### `Dockerfile`
```dockerfile
FROM nginx:alpine
LABEL org.opencontainers.image.title="my-custom-nginx"
LABEL org.opencontainers.image.description="AI/SW 개발 워크스테이션 과제용 정적 웹 서버"
COPY app/ /usr/share/nginx/html/
```

### 9-5. 빌드 및 실행 명령
```powershell
docker build -t my-web:1.0 .
docker run -d -p 8080:80 --name my-web my-web:1.0
docker ps
curl http://localhost:8080
```

### 9-6. 확인 내용
- `my-web:1.0` 이미지 빌드 성공
- `my-web` 컨테이너 실행 성공
- `8080:80` 포트 매핑 확인
- `curl http://localhost:8080` 응답 확인

---

## 10. 포트 매핑 접속 증거

### 10-1. 목적
- 호스트 포트와 컨테이너 내부 포트 연결 검증

### 10-2. 실행 명령
```powershell
docker run -d -p 8080:80 --name my-web my-web:1.0
docker ps
curl http://localhost:8080
```

### 10-3. 확인 내용
- `docker ps`에서 `0.0.0.0:8080->80/tcp` 확인
- `curl http://localhost:8080` 실행 시 HTML 응답 확인

### 10-4. 응답 예시
```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>AI/SW 개발 워크스테이션</title>
</head>
<body>
  <h1>Hello from my custom nginx container</h1>
  <p>과제용 정적 웹 서버가 정상 실행 중입니다.</p>
  <p>Port mapping test: localhost:8080</p>
</body>
</html>
```

### 10-5. 해석
- 호스트 포트: `8080`
- 컨테이너 내부 포트: `80`
- `http://localhost:8080` 접속 시 컨테이너 내부 nginx 웹 서버로 연결됨

---

## 11. 바인드 마운트 반영

### 11-1. 목적
- 호스트의 `app` 폴더를 컨테이너 내부 웹 루트에 직접 연결
- 파일 수정 시 재빌드 없이 즉시 반영되는지 확인

### 11-2. 실행 명령
```powershell
docker run -d -p 8081:80 --name my-web-bind -v ${PWD}\app:/usr/share/nginx/html nginx:alpine
curl http://localhost:8081
```

### 11-3. 초기 응답
```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>AI/SW 개발 워크스테이션</title>
</head>
<body>
  <h1>Hello from my custom nginx container</h1>
  <p>과제용 정적 웹 서버가 정상 실행 중입니다.</p>
  <p>Port mapping test: localhost:8080</p>
</body>
</html>
```

### 11-4. 수정한 `app/index.html`
```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Bind Mount Test</title>
</head>
<body>
  <h1>Bind Mount Updated</h1>
  <p>호스트에서 수정한 파일이 즉시 반영되었습니다.</p>
</body>
</html>
```

### 11-5. 수정 후 확인 명령
```powershell
curl http://localhost:8081
docker ps
```

### 11-6. 수정 후 응답
```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Bind Mount Test</title>
</head>
<body>
  <h1>Bind Mount Updated</h1>
  <p>호스트에서 수정한 파일이 즉시 반영되었습니다.</p>
</body>
</html>
```

### 11-7. 확인 내용
- `my-web-bind` 컨테이너가 `8081:80`으로 실행됨
- 호스트 파일 수정 후 즉시 응답 변경 확인
- 바인드 마운트를 통해 호스트 변경이 컨테이너 내부에 바로 반영됨을 확인

---

## 12. Docker 볼륨 영속성

### 12-1. 목적
- Docker 볼륨 생성
- 컨테이너 삭제 후 데이터 유지 여부 확인

### 12-2. 실행 명령
```powershell
docker volume create mydata
docker run -d --name vol-test -v mydata:/data ubuntu sleep infinity
docker exec vol-test bash -lc "echo hi > /data/hello.txt && cat /data/hello.txt"
docker rm -f vol-test
docker run -d --name vol-test2 -v mydata:/data ubuntu sleep infinity
docker exec vol-test2 bash -lc "cat /data/hello.txt"
docker rm -f vol-test2
docker volume ls
docker volume inspect mydata
```

### 12-3. 확인 내용
- `mydata` 볼륨 생성
- 첫 번째 컨테이너에서 `/data/hello.txt` 파일 생성
- 컨테이너 삭제 후 두 번째 컨테이너에서 동일 파일 재확인
- `hi`가 그대로 출력되어 영속성 확인
- `docker volume ls`, `docker volume inspect mydata`로 볼륨 상태 확인

### 12-4. 해석
- 바인드 마운트 = 호스트 특정 폴더 직접 연결
- 볼륨 = Docker가 관리하는 별도 저장공간
- 이번 실습에서는 볼륨을 사용해 컨테이너 삭제 후 데이터 유지 여부를 검증함

---

## 13. Git 설정 및 GitHub 연동

### 13-1. 로컬 저장소 초기화 및 원격 저장소 연결
```powershell
Set-Location 'D:\코디세이\ai-sw-workstation'
git init
git config user.name "고호석"
git config user.email "hoseok0917@gmail.com"
git branch -M main
git add .
git commit -m "init: start ai-sw-workstation"
git remote add origin https://github.com/hoseuk0917-rgb/ai-sw-workstation.git
git push -u origin main
git remote -v
git status
```

### 13-2. 확인 내용
- 로컬 Git 저장소 초기화
- GitHub 원격 저장소 연결
- 첫 커밋 생성 및 `main` 브랜치 push 완료
- `git status`에서 working tree clean 상태 확인

### 13-3. VS Code / GitHub 확인
- VS Code에서 저장소가 Source Control에 정상 인식되는 것을 확인했다.
- GitHub 원격 저장소 연결은 `git remote -v` 및 `git push` 성공으로 확인했다.
- 증거 이미지 파일명: `screenshots/vscode-github.png`

---

## 14. 트러블슈팅

### 14-1. `winget` 명령이 인식되지 않는 문제

#### 문제
- PowerShell에서 `winget --version` 실행 시 명령을 찾을 수 없었다.

#### 원인 가설
- App Installer는 설치되어 있으나 현재 세션에서 등록 또는 PATH 반영이 되지 않았을 가능성

#### 확인 명령
```powershell
Get-AppxPackage Microsoft.DesktopAppInstaller | Select-Object Name, Version, InstallLocation
where.exe winget
Get-Command winget -ErrorAction SilentlyContinue
```

#### 해결 명령
```powershell
Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
$env:PATH += ";$env:LOCALAPPDATA\Microsoft\WindowsApps"
winget --version
```

#### 결과
- `where.exe winget`에서 실행 경로 확인
- `winget --version` 정상 출력
- 이후 Docker Desktop 설치 명령 실행 가능

---

### 14-2. Docker Desktop 설치 후 `docker` 명령이 바로 인식되지 않는 문제

#### 문제
- Docker Desktop 설치 후 같은 PowerShell 세션에서 `docker` 명령이 바로 인식되지 않았다.

#### 원인 가설
- Docker Desktop 초기 실행 미완료
- CLI 경로가 현재 세션 PATH에 미반영

#### 확인 명령
```powershell
Test-Path 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
Test-Path 'C:\Program Files\Docker\Docker\resources\bin\docker.exe'
where.exe docker
```

#### 해결 명령
```powershell
Start-Process 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
$env:Path += ';C:\Program Files\Docker\Docker\resources\bin'
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' --version
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' info
```

#### 결과
- Docker Desktop과 Docker CLI 파일 존재 확인
- Docker Desktop 수동 실행
- PATH 반영 후 `docker --version`, `docker info` 정상 동작

---

### 14-3. `/mnt/d` 경로에서 chmod 결과가 바로 보이지 않는 문제

#### 문제
- WSL에서 `/mnt/d/코디세이/ai-sw-workstation` 경로를 사용해 `chmod`를 실행했지만 전후 출력이 동일하게 보였다.

#### 확인 명령
```powershell
wsl -d Ubuntu-22.04 -- bash -lc "
cd /mnt/d/코디세이/ai-sw-workstation &&
mkdir -p perm_lab/dir_a &&
touch perm_lab/file_a.txt &&
echo 'sample' > perm_lab/file_a.txt &&
echo '--- before ---' &&
ls -ld perm_lab/dir_a &&
ls -l perm_lab/file_a.txt &&
chmod 755 perm_lab/dir_a &&
chmod 644 perm_lab/file_a.txt &&
echo '--- after ---' &&
ls -ld perm_lab/dir_a &&
ls -l perm_lab/file_a.txt
"
```

#### 결과
- 권한 표기가 전후 동일하게 보였다.

#### 대응
- 제출용 권한 실습은 `/mnt/d` 대신 WSL 홈 디렉토리(`~/perm_lab`)에서 다시 수행했다.
- 해당 결과를 최종 권한 실습 증거로 사용했다.