# AI/SW 개발 워크스테이션 구축

## 1. 프로젝트 개요
이 프로젝트는 터미널(CLI), Docker, Git/GitHub를 활용하여 AI/SW 개발 워크스테이션을 구축하고, 실행 환경 재현, 컨테이너 실행, 포트 매핑, 마운트/볼륨, 버전관리 흐름을 직접 검증하는 것을 목표로 한다.

## 2. 실행 환경
- OS: Windows
- Shell: PowerShell 5.1
- Git: git version 2.51.2.windows.1
- Docker: Docker version 29.3.1, build c2be9cc
- 작업 경로: D:\코디세이\ai-sw-workstation

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
- [ ] Dockerfile 기반 커스텀 이미지 제작
- [ ] 포트 매핑 접속 확인
- [ ] 바인드 마운트 반영 확인
- [ ] Docker 볼륨 영속성 확인
- [ ] GitHub/VSCode 연동 증거 정리

## 4. 터미널 조작 로그
### 작업 폴더 생성 및 구조 확인
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

## 5. 권한 실습
- 아직 수행 전

## 6. Docker 설치 및 점검
### Docker 설치 전 확인
```powershell
docker --version
docker info
where.exe docker
Get-Command docker -ErrorAction SilentlyContinue
```

확인 결과:
- `docker` 명령이 인식되지 않았다.
- `where.exe docker` 결과가 없었다.
- Docker CLI가 아직 설치되지 않았거나 PATH에 등록되지 않은 상태로 판단했다.

### WinGet 복구 및 Docker Desktop 설치 시작
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

### Docker Desktop 수동 실행 및 설치 후 확인
```powershell
Test-Path 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
Test-Path 'C:\Program Files\Docker\Docker\resources\bin\docker.exe'
Get-ChildItem 'C:\Program Files\Docker\Docker\resources\bin' -ErrorAction SilentlyContinue | Select-Object Name
Start-Process 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\dotnet\;C:\Program Files\Amazon\AWSCLIV2\;C:\Users\hoseu\bin;C:\Python314;C:\Python314\Scripts;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\Git\bin;C:\Windows\Sys;C:\Users\hoseu\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\hoseu\.lmstudio\bin;C:\Users\hoseu\AppData\Roaming\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WinGet\Links;C:\Users\hoseu\AppData\Local\Programs\Python\Python313;C:\Users\hoseu\AppData\Local\Programs\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WindowsApps;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin += ';C:\Program Files\Docker\Docker\resources\bin'
where.exe docker
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' --version
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' info
```

확인 결과:
- Docker Desktop 실행 파일과 docker CLI 파일 존재를 확인했다.
- Docker Desktop을 수동으로 실행했다.
- Docker CLI 경로가 확인되었다.
- `docker --version`이 정상 출력되었다.
- `docker info`에서 Client와 Server 정보가 모두 출력되어 Docker 엔진이 동작 중임을 확인했다.

## 7. Docker 기본 운영 명령
### hello-world 실행 및 기본 운영 명령
```powershell
C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\dotnet\;C:\Program Files\Amazon\AWSCLIV2\;C:\Users\hoseu\bin;C:\Python314;C:\Python314\Scripts;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\Git\bin;C:\Windows\Sys;C:\Users\hoseu\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\hoseu\.lmstudio\bin;C:\Users\hoseu\AppData\Roaming\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WinGet\Links;C:\Users\hoseu\AppData\Local\Programs\Python\Python313;C:\Users\hoseu\AppData\Local\Programs\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WindowsApps;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin += ';C:\Program Files\Docker\Docker\resources\bin'
docker run --name hello-test hello-world
docker images
docker ps -a
docker logs hello-test
docker rm hello-test
```

확인 결과:
- `hello-world` 컨테이너 실행에 성공했다.
- `docker images`로 이미지 목록을 확인했다.
- `docker ps -a`로 컨테이너 상태를 확인했다.
- `docker logs hello-test`로 실행 로그를 확인했다.
- 실습 후 테스트 컨테이너를 삭제했다.

## 8. 컨테이너 실행 실습
### ubuntu 컨테이너 실행 및 내부 명령 수행
```powershell
C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\dotnet\;C:\Program Files\Amazon\AWSCLIV2\;C:\Users\hoseu\bin;C:\Python314;C:\Python314\Scripts;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\Git\bin;C:\Windows\Sys;C:\Users\hoseu\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\hoseu\.lmstudio\bin;C:\Users\hoseu\AppData\Roaming\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WinGet\Links;C:\Users\hoseu\AppData\Local\Programs\Python\Python313;C:\Users\hoseu\AppData\Local\Programs\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WindowsApps;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin += ';C:\Program Files\Docker\Docker\resources\bin'
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

## 9. Dockerfile 기반 커스텀 이미지
- 추후 작성 예정

## 10. 포트 매핑 접속 증거
- 추후 작성 예정

## 11. 바인드 마운트 반영
- 추후 작성 예정

## 12. Docker 볼륨 영속성
- 추후 작성 예정

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
C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\dotnet\;C:\Program Files\Amazon\AWSCLIV2\;C:\Users\hoseu\bin;C:\Python314;C:\Python314\Scripts;C:\Windows\System32;C:\Windows;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files\nodejs;C:\src\flutter\bin;C:\Program Files\Git\cmd;C:\Program Files\Git\bin;C:\Windows\Sys;C:\Users\hoseu\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\hoseu\.lmstudio\bin;C:\Users\hoseu\AppData\Roaming\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WinGet\Links;C:\Users\hoseu\AppData\Local\Programs\Python\Python313;C:\Users\hoseu\AppData\Local\Programs\Python\Python313\Scripts;C:\Users\hoseu\AppData\Local\Microsoft\WindowsApps;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Docker\Docker\resources\bin += ';C:\Program Files\Docker\Docker\resources\bin'
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' --version
& 'C:\Program Files\Docker\Docker\resources\bin\docker.exe' info
```

결과:
- Docker Desktop과 docker CLI 파일 존재를 확인했다.
- Docker Desktop을 수동으로 실행했다.
- PATH 반영 후 `docker --version`, `docker info`가 정상 동작했다.
