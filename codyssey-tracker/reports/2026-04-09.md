# Codyssey 과제 수집 보고서

> **수집 일시**: 2026년 04월 09일 14:34 KST  
> **총 수집 과제**: 8건

---

## 1주차 과제

### 과제 내용 정리

## 과제 주제
개발 워크스테이션 구축 및 핵심 기술 실습

## 학습 목표
1.  터미널 기본 명령어 활용 능력 습득
2.  파일 시스템 권한의 개념 이해 및 조작 실습
3.  Docker 기본 개념 이해 및 컨테이너/이미지 관리 능력 함양
4.  Git/GitHub를 활용한 버전 관리 및 협업 기초 다지기
5.  (보너스) Docker Compose를 활용한 다중 컨테이너 관리 및 GitHub SSH 인증 설정

## 주요 내용 요약
본 과제는 터미널 기본 조작, 파일 권한 실습, Docker 기본 기능 점검 및 실습, Git/GitHub 연동을 통해 개발 워크스테이션 환경을 직접 구축하는 것을 목표로 합니다. Dockerfile을 이용한 커스텀 이미지 제작, 포트 매핑, 바인드 마운트, 볼륨을 통한 데이터 영속성 관리 등을 실습합니다. 또한, Docker Compose를 활용한 다중 컨테이너 구성과 GitHub SSH 인증 설정 등의 보너스 항목도 다룹니다.

## 핵심 기술 및 개념
*   **터미널:** `pwd`, `mkdir`, `ls`, `touch`, `cp`, `mv`, `rm`, `chmod`, `stat`, `cat`
*   **파일 권한:** 사용자(u), 그룹(g), 기타(o) 권한 (읽기-r, 쓰기-w, 실행-x), 8진수 권한 표기법 (예: 600, 644, 700)
*   **Docker:** Docker 설치, 데몬, 컨테이너, 이미지, Dockerfile, `docker run`, `docker ps`, `docker images`, `docker build`, `docker stop`, `docker rm`, `docker exec`, `docker logs`, 포트 매핑 (`-p`), 바인드 마운트 (`-v`), 볼륨 (`--mount type=volume`)
*   **Git/GitHub:** Git 설치, `git config`, 원격 저장소 연결, `git init`, `git add`, `git commit`, `git push`, `git pull`, SSH 키 생성 및 등록
*   **Docker Compose:** `docker-compose.yaml`, 다중 컨테이너 오케스트레이션

## 과제 요구사항
- [x] 터미널 기본 조작 및 폴더 구성
- [x] 파일 권한 실습
- [x] Docker 설치 및 기본 점검
- [x] hello-world 컨테이너 실행
- [x] ubuntu 컨테이너 실행 및 내부 명령 확인
- [x] Docker 기본 운영 명령 확인
- [x] Dockerfile 기반 커스텀 이미지 제작
- [x] 포트 매핑 검증
- [x] 바인드 마운트 검증
- [x] 볼륨 영속성 검증
- [x] Git 설정 확인
- [x] GitHub / VS Code 연동 확인
- [x] 트러블슈팅 2건 이상 정리
- [x] **(Bonus)** Docker Compose
- [x] **(Bonus)** GitHub SSH

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| xifoxy-ru | [codyssey_week_01](https://github.com/xifoxy-ru/codyssey_week_01) | 2026-04-08 | 20,267자 |
| LimJongHan | [Codyssey-E1-1](https://github.com/LimJongHan/Codyssey-E1-1) | 2026-04-03 | 34,992자 |
| sourcreamsource | [codysseyWeekOne](https://github.com/sourcreamsource/codysseyWeekOne) | 2026-04-08 | 5,289자 |
| coding-monkey-326 | [codyssey-e1-1](https://github.com/coding-monkey-326/codyssey-e1-1) | 2026-03-31 | 17,258자 |

---

## 2주차 과제

### 과제 내용 정리

## 과제 주제
Git과 함께하는 Python 콘솔 퀴즈 게임 개발

## 학습 목표
* Python 기본 문법을 활용한 콘솔 애플리케이션 개발 능력 향상
* 객체지향 프로그래밍(OOP) 개념을 적용한 클래스 기반 설계 능력 함양
* JSON 파일을 이용한 데이터 지속성(Persistence) 구현 및 데이터 관리 능력 습득
* Git/GitHub를 활용한 효과적인 버전 관리 및 협업 프로세스 이해

## 주요 내용 요약
본 과제는 Python으로 콘솔 기반 퀴즈 게임을 개발하며 Git/GitHub를 활용한 버전 관리를 연습합니다. 사용자는 퀴즈 풀기, 추가, 목록 확인, 점수 확인, 삭제 등의 기능을 이용할 수 있으며, `state.json` 파일을 통해 게임 상태를 저장하고 복구합니다. 객체지향 설계를 위해 `Quiz`와 `QuizGame` 클래스를 사용하고, 문제 순서 랜덤 출제, 힌트 기능 등 보너스 기능 구현을 통해 학습 경험을 확장합니다.

## 핵심 기술 및 개념
*   **프로그래밍 언어:** Python
*   **데이터 저장:** JSON (state.json)
*   **객체지향 프로그래밍 (OOP):** 클래스 (`Quiz`, `QuizGame`), 객체, 속성, 역할 분리
*   **콘솔 입출력:** `input()`, `print()`
*   **파일 처리:** JSON 파일 읽기/쓰기
*   **예외 처리:** `try-except` 블록 (InputError, KeyboardInterrupt, EOFError 등)
*   **버전 관리:** Git (commit, branch, merge), GitHub
*   **기타:** 표준 라이브러리, 메뉴 기반 인터페이스, 데이터 지속성

## 과제 요구사항
*   [ ] 프로그램이 정상 실행되는가?
*   [ ] 메뉴 기능을 통해 모든 항목(퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인, 퀴즈 삭제, 종료)을 접근할 수 있는가?
*   [ ] 퀴즈 풀기 기능이 올바르게 동작하며, 정답/오답 처리가 되는가?
*   [ ] 퀴즈 추가 기능을 통해 새로운 퀴즈를 등록할 수 있는가?
*   [ ] 퀴즈 목록 기능으로 현재 등록된 퀴즈를 확인할 수 있는가?
*   [ ] 최고 점수 확인 기능이 동작하며, 점수 기록 히스토리(보너스)가 저장 및 표시되는가?
*   [ ] 퀴즈 삭제 기능이 정상적으로 동작하며, `state.json` 파일에 반영되는가?
*   [ ] 프로그램 종료 후 재실행 시 `state.json` 파일을 통해 데이터가 유지되는가?
*   [ ] (보너스) 문제 순서 랜덤 출제 기능이 구현되었는가?
*   [ ] (보너스) 퀴즈 풀 때 문제 수를 선택할 수 있는가?
*   [ ] (보너스) 힌트 기능이 구현되었으며, 사용 시 점수 차감이 되는가?
*   [ ] (보너스) 점수 기록 히스토리가 날짜/시간, 푼 문제 수, 점수를 포함하여 저장되는가?
*   [ ] `Quiz` 클래스와 `QuizGame` 클래스를 활용한 객체지향 설계가 적용되었는가?
*   [ ] `state.json` 파일의 예상 데이터 구조와 일치하는가?
*   [ ] Git을 사용하여 기능별로 커밋이 분리되어 있고, 의미 있는 커밋 메시지를 사용했는가?
*   [ ] `main` 브랜치 외 별도의 브랜치에서 개발 후 병합하는 Git 작업 방식이 적용되었는가?
*   [ ] README.md 파일에 프로젝트 설명, 사용법, Git 작업 방식 등이 명확하게 작성되었는가?
*   [ ] `.gitignore` 파일이 설정되어 있는가?
*   [ ] 제시된 파일 구조를 따랐는가?
*   [ ] 예외 처리가 적절하게 구현되어 프로그램의 안정성을 확보했는가?
*   [ ] Python 3.10 이상 환경에서 외부 라이브러리 없이 표준 라이브러리만 사용하여 실행 가능한가?

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| xifoxy-ru | [codyssey_week_02](https://github.com/xifoxy-ru/codyssey_week_02) | 2026-04-08 | 6,631자 |
| LimJongHan | [Codyssey-E1-2](https://github.com/LimJongHan/Codyssey-E1-2) | 2026-04-08 | 2,187자 |
| sourcreamsource | [codysseyWeekTwo](https://github.com/sourcreamsource/codysseyWeekTwo) | 2026-04-09 | 1,882자 |
| coding-monkey-326 | [codyssey-e1-2](https://github.com/coding-monkey-326/codyssey-e1-2) | 2026-04-09 | 4,052자 |

---
