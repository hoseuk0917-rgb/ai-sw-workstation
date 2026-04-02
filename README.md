# AI/SW 개발 워크스테이션 구축

## 1. 프로젝트 개요

상세 명령어 정리는 [명령어 모음.md](./명령어%20모음.md)에 별도로 정리했다.

이 프로젝트는 터미널(CLI), Docker, Git/GitHub를 활용하여 AI/SW 개발 워크스테이션을 구축하고, 실행 환경 재현, 컨테이너 실행, 포트 매핑, 마운트/볼륨, 버전관리 흐름을 직접 검증하는 것을 목표로 한다.

특히 다음 내용을 직접 손으로 수행하고 결과를 확인하는 데 중점을 두었다.

- PowerShell 기반 기본 파일/폴더 조작
- Git 저장소 초기화 및 GitHub 원격 저장소 연동
- Docker Desktop 설치 및 Docker CLI 점검
- hello-world, ubuntu 컨테이너 실행
- 이후 Dockerfile 기반 웹 서버 컨테이너, 포트 매핑, 바인드 마운트, 볼륨 영속성까지 확장 예정

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
- [ ] 권한 실습
- [x] Docker 설치 확인
- [x] Docker 기본 운영 명령 수행
- [x] hello-world 실행
- [x] ubuntu 컨테이너 실행
- [x] Dockerfile 기반 커스텀 이미지 제작
- [x] 포트 매핑 접속 확인
- [x] 바인드 마운트 반영 확인
- [x] Docker 볼륨 영속성 확인
- [ ] GitHub/VSCode 연동 증거 정리

---

## 4. 터미널 조작 로그

### 4-1. 작업 폴더 생성 및 구조 확인

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

확인 결과:
- 과제용 작업 폴더를 생성했다.
- `app`, `logs`, `screenshots` 폴더와 기본 파일을 만들었다.
- 현재 작업 위치와 폴더 구조를 확인했다.

### 4-2. PowerShell 기본 조작 실습

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

확인 결과:
- 현재 위치와 파일 목록을 확인했다.
- 디렉토리와 파일을 생성했다.
- 파일 내용을 기록하고 다시 읽어 보았다.
- 파일 복사, 이름 변경, 이동, 삭제를 수행했다.
- 최종 폴더 구조를 재확인했다.

---

## 5. 권한 실습

### 파일/디렉토리 권한 변경 전후 비교

Windows의 `D:` 드라이브 경로(`/mnt/d/...`)에서는 권한 변경 결과가 기대한 형태로 바로 보이지 않아, WSL 홈 디렉토리에서 별도로 실습했다.

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

확인 결과:
- WSL(Ubuntu) 홈 디렉토리에서 권한 실습을 수행했다.
- 디렉토리 1개와 파일 1개를 만든 뒤 권한 변경 전/후를 비교했다.
- 디렉토리는 `755`, 파일은 `644`로 설정해 권한 표기 차이를 확인했다.

권한 해석:
- `r` = 읽기
- `w` = 쓰기
- `x` = 실행
- `755` = 소유자(rwx), 그룹(rx), 기타 사용자(rx)
- `644` = 소유자(rw), 그룹(r), 기타 사용자(r)

---

## 6. Docker 설치 및 점검

### 6-1. Docker 설치 전 확인

```powershell
docker --version
docker info
where.exe docker
Get-Command docker -ErrorAction SilentlyContinue
```

확인 결과:
- 초기에 `docker` 명령이 인식되지 않았다.
- `where.exe docker` 결과가 없었다.
- Docker CLI가 설치되지 않았거나 PATH에 등록되지 않은 상태로 판단했다.

### 6-2. WinGet 복구 및 Docker Desktop 설치 시작

```powershell
Get-AppxPackage Microsoft.DesktopAppInstaller | Select-Object Name, Version, InstallLocation
Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
$env:PATH += ";$env:LOCALAPPDATA\Microsoft\WindowsApps"
where.exe winget
Get-Command winget -ErrorAction SilentlyContinue
winget --version
winget install -e --id Docker.DockerDesktop
```

확인 결과:
- App Installer 존재를 확인했다.
- App Installer 재등록 후 현재 세션 PATH를 갱신했다.
- `winget` 명령이 정상 인식되는 것을 확인했다.
- `winget install -e --id Docker.DockerDesktop`로 Docker Desktop 설치를 시작했다.

### 6-3. Docker Desktop 수동 실행 및 설치 후 확인

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

확인 결과:
- Docker Desktop 실행 파일과 Docker CLI 파일 존재를 확인했다.
- Docker Desktop을 수동으로 실행했다.
- Docker CLI 경로가 확인되었다.
- `docker --version`이 정상 출력되었다.
- `docker info`에서 Client와 Server 정보가 모두 출력되어 Docker 엔진이 동작 중임을 확인했다.

---

## 7. Docker 기본 운영 명령

### hello-world 실행 및 기본 운영 명령

```powershell
$env:Path += ';C:\Program Files\Docker\Docker\resources\bin'
docker run --name hello-test hello-world
docker images
docker ps -a
docker logs hello-test
docker rm hello-test
docker stats --no-stream
```

확인 결과:
- `hello-world` 컨테이너 실행에 성공했다.
- `docker images`로 이미지 목록을 확인했다.
- `docker ps -a`로 컨테이너 상태를 확인했다.
- `docker logs hello-test`로 실행 로그를 확인했다.
- 실습 후 테스트 컨테이너를 삭제했다.
- `docker stats --no-stream`으로 리소스 상태를 1회 확인했다.

---

## 8. 컨테이너 실행 실습

### ubuntu 컨테이너 실행 및 내부 명령 수행

```powershell
$env:Path += ';C:\Program Files\Docker\Docker\resources\bin'
docker run -dit --name ubuntu-test ubuntu bash
docker exec ubuntu-test bash -lc "ls / && echo hello-from-ubuntu"
docker ps -a
docker logs ubuntu-test
docker rm -f ubuntu-test
```

확인 결과:
- `ubuntu` 컨테이너를 백그라운드로 실행했다.
- `docker exec`로 컨테이너 내부에 명령을 실행했다.
- 컨테이너 목록과 상태를 확인했다.
- `docker logs ubuntu-test`는 별도 출력이 없었다.
- 실습 후 컨테이너를 삭제했다.

추가 정리:
- `docker run -it ubuntu bash`는 즉시 컨테이너 내부 셸로 진입하는 방식이다.
- `docker run -dit ...`는 백그라운드에서 컨테이너를 유지한 뒤, `docker exec`로 내부 명령을 수행하는 방식이다.
- `exec`는 실행 중인 컨테이너 안에 새 명령을 넣는 개념이다.

---

## 9. Dockerfile 기반 커스텀 이미지

### nginx 기반 정적 웹 서버 이미지 제작
이번 실습에서는 `nginx:alpine` 이미지를 베이스로 사용해 정적 웹 서버 이미지를 제작했다.

선택 이유:
- 공식 웹 서버 이미지라 구조가 단순하다.
- 정적 HTML 파일을 복사해 바로 동작을 확인할 수 있다.
- 이후 포트 매핑, 바인드 마운트, 볼륨 실습으로 확장하기 쉽다.

생성 파일:

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

빌드 및 실행 명령:
```powershell
docker build -t my-web:1.0 .
docker run -d -p 8080:80 --name my-web my-web:1.0
docker ps
curl http://localhost:8080
```

확인 결과:
- `nginx:alpine` 기반 커스텀 이미지를 성공적으로 빌드했다.
- `my-web:1.0` 이미지를 컨테이너로 실행했다.
- 호스트 8080 포트를 컨테이너 80 포트에 연결했다.
- `docker ps`에서 `0.0.0.0:8080->80/tcp` 포트 매핑을 확인했다.
- `curl http://localhost:8080`으로 HTML 응답을 확인했다.

---

## 10. 포트 매핑 접속 증거

포트 매핑 실행 명령:
```powershell
docker run -d -p 8080:80 --name my-web my-web:1.0
docker ps
curl http://localhost:8080
```

확인 결과:
- 컨테이너 `my-web`이 실행되었다.
- `docker ps`에서 `0.0.0.0:8080->80/tcp`가 표시되었다.
- `curl http://localhost:8080` 실행 시 아래 HTML 응답이 반환되었다.

응답 확인:
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

설명:
- 포트 매핑은 호스트 포트와 컨테이너 내부 포트를 연결하는 기능이다.
- 이번 실습에서는 호스트 `8080` 포트와 컨테이너 `80` 포트를 연결했다.
- 따라서 로컬 PC에서 `http://localhost:8080`으로 접속했을 때 컨테이너 내부 nginx 웹 서버에 도달할 수 있었다.

---

## 11. 바인드 마운트 반영

이번 실습에서는 호스트의 `app` 폴더를 컨테이너 내부 `/usr/share/nginx/html`에 바인드 마운트했다.

실행 명령:
```powershell
docker run -d -p 8081:80 --name my-web-bind -v ${PWD}\app:/usr/share/nginx/html nginx:alpine
curl http://localhost:8081
```

초기 응답:
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

그 다음 호스트 파일을 아래처럼 수정했다.

수정한 `app/index.html`:
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

수정 후 확인 명령:
```powershell
curl http://localhost:8081
docker ps
```

수정 후 응답:
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

확인 결과:
- `my-web-bind` 컨테이너가 `8081:80`으로 실행되었다.
- 호스트에서 `app/index.html`을 수정한 뒤 컨테이너를 다시 빌드하지 않아도 응답이 즉시 바뀌었다.
- 즉, 바인드 마운트를 통해 호스트 파일 변경이 컨테이너 내부에 바로 반영됨을 확인했다.

---

## 12. Docker 볼륨 영속성

이번 실습에서는 Docker 볼륨을 생성하고, 컨테이너를 삭제한 후에도 데이터가 유지되는지 확인했다.

실행 명령:
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

확인 결과:
- `mydata`라는 Docker 볼륨을 생성했다.
- 첫 번째 컨테이너 `vol-test`에서 `/data/hello.txt` 파일을 만들고 내용 `hi`를 기록했다.
- `vol-test` 컨테이너를 삭제한 뒤, 같은 볼륨을 연결한 `vol-test2` 컨테이너를 다시 실행했다.
- 두 번째 컨테이너에서 `cat /data/hello.txt`를 실행했을 때 동일하게 `hi`가 출력되었다.
- 즉, 컨테이너는 삭제되어도 볼륨 데이터는 유지됨을 확인했다.

볼륨 확인:
- `docker volume ls`에서 `mydata` 볼륨이 존재하는 것을 확인했다.
- `docker volume inspect mydata`로 볼륨의 세부 정보를 확인했다.

설명:
- 바인드 마운트는 호스트의 특정 폴더를 그대로 연결하는 방식이다.
- 볼륨은 Docker가 관리하는 별도 저장 공간이다.
- 이번 실습에서는 볼륨을 사용해 컨테이너 삭제 후에도 데이터가 유지되는 영속성을 검증했다.
---

## 13. Git 설정 및 GitHub 연동

### 로컬 저장소 초기화 및 원격 저장소 연결

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

확인 결과:
- 로컬 Git 저장소를 초기화했다.
- GitHub 원격 저장소와 연결했다.
- 첫 커밋을 생성하고 `main` 브랜치로 push를 완료했다.
- `git status`에서 working tree clean 상태를 확인했다.

---

## 14. 트러블슈팅

### 1) `winget` 명령이 인식되지 않는 문제

문제:
- PowerShell에서 `winget --version` 실행 시 명령을 찾을 수 없다는 오류가 발생했다.

원인 가설:
- App Installer는 설치되어 있으나 현재 세션에서 등록 또는 PATH 반영이 되지 않았을 가능성이 있었다.

확인:
```powershell
Get-AppxPackage Microsoft.DesktopAppInstaller | Select-Object Name, Version, InstallLocation
where.exe winget
Get-Command winget -ErrorAction SilentlyContinue
```

해결:
```powershell
Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
$env:PATH += ";$env:LOCALAPPDATA\Microsoft\WindowsApps"
winget --version
```

결과:
- `where.exe winget`에서 실행 경로가 확인되었다.
- `winget --version`이 정상 출력되었다.
- 이후 Docker Desktop 설치 명령을 실행할 수 있었다.

### 2) Docker Desktop 설치 후 `docker` 명령이 바로 인식되지 않는 문제

문제:
- Docker Desktop 설치 후 같은 PowerShell 세션에서 `docker` 명령이 바로 인식되지 않았다.

원인 가설:
- Docker Desktop 초기 실행이 완료되지 않았거나 CLI 경로가 현재 세션 PATH에 반영되지 않았을 가능성이 있었다.

확인:
```powershell
Test-Path 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
Test-Path 'C:\Program Files\Docker\Docker\resources\bin\docker.exe'
where.exe docker
```

해결:
```powershell
Start-Process 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
$env:Path += ';C:\Program Files\Docker\Docker\resources\bin'
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' --version
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' info
```

결과:
- Docker Desktop과 Docker CLI 파일 존재를 확인했다.
- Docker Desktop을 수동으로 실행했다.
- PATH 반영 후 `docker --version`, `docker info`가 정상 동작했다.

### 3) `/mnt/d` 경로에서 chmod 결과가 바로 보이지 않는 문제

문제:
- WSL에서 `/mnt/d/코디세이/ai-sw-workstation` 경로를 사용해 `chmod`를 실행했지만, 전후 출력이 동일하게 보였다.

확인:
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

결과:
- 권한 표기가 전후 동일하게 보였다.

대응:
- 제출용 권한 실습은 `/mnt/d` 대신 WSL 홈 디렉토리(`~/perm_lab`)에서 다시 수행했다.
- 그 결과를 권한 실습 증거로 사용했다.

