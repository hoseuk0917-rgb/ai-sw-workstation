# Codyssey 과제 수집 보고서

> **수집 일시**: 2026년 04월 09일 15:52 KST  
> **총 수집 과제**: 46건  
> **추적 후보**: 22명

---

## 1주차 과제

### 과제 내용 정리

# Codyssey E1-1 · AI/SW 개발 워크스페이스 구축

실습 목표는 **터미널·Docker·Git**을 사용해 개발 환경을 재현 가능하게 만드는 것이다. 포트 매핑, 바인드 마운트, 명명된 볼륨 등 컨테이너 운영의 핵심을 **명령과 출력으로 직접 검증**한다.

## 이 문서를 읽는 순서

1. **저장소 구조** — 어떤 파일이 무엇인지 파악한다.
2. **체크리스트** — 과제 진행도를 본다.
3. **상세 검증 기록** — 터미널/퍼미션/Docker/Git 순 실습 로그(증빙)이다.
4. **핵심 원리 및 구조 설명** — 디렉터리 기준, 포트·볼륨 재현, 이미지/컨테이너, 권한 숫자, 경로 선택, 인터뷰형 트러블슈팅 순서.

## 목차

- [저장소 구조](#저장소-구조)
- [사전 요구사항 · 환경 스냅샷](#사전-요구사항-및-실행-환경)
- [수행 체크리스트](#수행-체크리스트)
- [상세 검증 기록](#상세-검증-기록)
- [핵심 원리 및 구조 설명](#핵심-원리-및-구조-설명)
- [트러블슈팅](#트러블슈팅)

## 저장소 구조

대략적인 트리는 다음과 같다.

```text
E1-1/
├── README.md              # 기술 문서(실습·트러블슈팅)
├── .gitignore             # Git 추적 제외 규칙
├── test1.txt              # 터미널·chmod 실습 샘플
├── images/
│   ├── image.png          # 커스텀 웹 컨테이너 접속 증빙
│   ├── BindMountTest0.png # 바인드 마운

_*(AI 요약 실패 — 원문 일부)*_

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| I-nkamanda | [codyssey2026/Problem1_AI_SW_Setup](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem1_AI_SW_Setup) | 2026-04-08 | 1,707자 |
| 0-hu | [codyssey-e1-1](https://github.com/0-hu/codyssey-e1-1) | 2026-04-06 | 13,870자 |
| kimch0612 | [Codyssey_Week1](https://github.com/kimch0612/Codyssey_Week1) | 2026-03-31 | 7,624자 |
| JungSaeYoung | [codyssey_E1-1](https://github.com/JungSaeYoung/codyssey_E1-1) | 2026-04-04 | 17,817자 |
| codewhite7777 | [codyssey_E1-3](https://github.com/codewhite7777/codyssey_E1-3) | 2026-04-06 | 2,122자 |
| codewhite7777 | [codyssey_E-1](https://github.com/codewhite7777/codyssey_E-1) | 2026-03-30 | 28,643자 |
| mov-hyun | [e1-1-workstation-setup](https://github.com/mov-hyun/e1-1-workstation-setup) | 2026-04-05 | 28,398자 |
| sonjehyun123-maker | [Codyssey-w1-E1](https://github.com/sonjehyun123-maker/Codyssey-w1-E1) | 2026-04-03 | 10,846자 |
| xifoxy-ru | [codyssey_week_01](https://github.com/xifoxy-ru/codyssey_week_01) | 2026-04-08 | 20,267자 |
| LimJongHan | [Codyssey-E1-1](https://github.com/LimJongHan/Codyssey-E1-1) | 2026-04-03 | 34,992자 |
| sourcreamsource | [codysseyWeekOne](https://github.com/sourcreamsource/codysseyWeekOne) | 2026-04-08 | 5,289자 |
| coding-monkey-326 | [codyssey-e1-1](https://github.com/coding-monkey-326/codyssey-e1-1) | 2026-03-31 | 17,258자 |
| whdals006 | [Codyssey_E1-1](https://github.com/whdals006/Codyssey_E1-1) | 2026-04-07 | 20,211자 |
| dolphin1404 | [Codyssey_E_1_2](https://github.com/dolphin1404/Codyssey_E_1_2) | 2026-04-07 | 2,038자 |
| jhj9109 | [codyssey1](https://github.com/jhj9109/codyssey1) | 2026-04-01 | 15,746자 |
| waz6432 | [CodysseyE1-1](https://github.com/waz6432/CodysseyE1-1) | 2026-04-03 | 12,437자 |
| whitecy01 | [codyssey1](https://github.com/whitecy01/codyssey1) | 2026-04-02 | 21,139자 |
| wilderif | [codyssey-e1-1](https://github.com/wilderif/codyssey-e1-1) | 2026-04-03 | 957자 |

---

## 2주차 과제

### 과제 내용 정리

## 과제 주제
Git과 함께하는 Python 콘솔 퀴즈 게임 구현 및 Git 워크플로우 학습

## 학습 목표
* Python 클래스 기반 객체 지향 프로그래밍 이해
* 사용자 입력 처리 및 예외 처리 기법 학습
* JSON 파일을 이용한 데이터 저장 및 복구 방법 습득
* Git 브랜치 생성, 병합, push/pull을 포함한 협업 워크플로우 적용
* Git을 이용한 코드 변경 이력 관리 방법 숙지

## 주요 내용 요약
터미널 기반 Python 퀴즈 게임을 구현하고, Git 및 GitHub를 사용하여 개발 과정을 관리합니다. 클래스 기반 구조 설계, 메뉴 선택형 퀴즈, 퀴즈 추가/목록/점수 확인 기능, `state.json`을 활용한 데이터 영속성, 예외 처리 및 안전 종료 기능을 포함합니다. Git 브랜치 전략, clone, commit, push/pull 과정을 통해 협업 및 코드 관리 능력을 향상시키는 것을 목표로 합니다.

## 핵심 기술 및 개념
* Python (클래스, 함수, 자료형, 조건문, 반복문)
* Git (init, add, commit, branch, checkout, merge, push, pull, clone, status)
* GitHub
* JSON
* 객체 지향 프로그래밍 (OOP)
* 데이터 영속성
* 예외 처리 (KeyboardInterrupt, EOFError)
* 콘솔 애플리케이션

## 과제 요구사항
* [x] `Quiz`, `QuizGame` 2개 클래스 구성
* [x] 메뉴 출력 및 선택 처리
* [x] 기본 퀴즈 5개 이상 구성
* [x] 퀴즈 풀기 기능 구현
* [x] 퀴즈 추가 기능 구현
* [x] 퀴즈 삭제 기능 구현
* [x] 퀴즈 목록 조회 기능 구현
* [x] 최고 점수 확인 기능 구현
* [x] `state.json` 저장 및 불러오기 구현
* [x] 파일 없음/손상 시 복구 처리 구현
* [x] `KeyboardInterrupt`, `EOFError` 안전 종료 처리
* [x] 브랜치 생성 및 병합 기록 반영
* [x] 별도 디렉토리에서 `git clone` 실행
* [x] 다른 작업 디렉토리에서 commit 후 `push`
* [x] 원래 로컬 저장소에서 변경 이력 반영 확인
* [x] 랜덤 출제 기능 구현
* [x] 문제 수 선택 기능 구현
* [x] 힌트 기능 및 점수 차감 구현
* [x] 점수 기록 히스토리 저장 구현

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| I-nkamanda | [codyssey2026/Problem2_Python_with_git](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem2_Python_with_git) | 2026-04-08 | 158자 |
| 0-hu | [codyssey-e1-2](https://github.com/0-hu/codyssey-e1-2) | 2026-04-07 | 5,469자 |
| kimch0612 | [Codyssey_Week2](https://github.com/kimch0612/Codyssey_Week2) | 2026-04-01 | 12,248자 |
| JungSaeYoung | [codyssey_E1-2](https://github.com/JungSaeYoung/codyssey_E1-2) | 2026-04-06 | 9,957자 |
| codewhite7777 | [codyssey_E-2](https://github.com/codewhite7777/codyssey_E-2) | 2026-04-02 | 1,032자 |
| mov-hyun | [e1-2-python-basics-quiz-game](https://github.com/mov-hyun/e1-2-python-basics-quiz-game) | 2026-04-06 | 829자 |
| sonjehyun123-maker | [Codyssey-w1-E2](https://github.com/sonjehyun123-maker/Codyssey-w1-E2) | 2026-04-09 | 4,082자 |
| xifoxy-ru | [codyssey_week_02](https://github.com/xifoxy-ru/codyssey_week_02) | 2026-04-08 | 6,631자 |
| LimJongHan | [Codyssey-E1-2](https://github.com/LimJongHan/Codyssey-E1-2) | 2026-04-08 | 2,187자 |
| sourcreamsource | [codysseyWeekTwo](https://github.com/sourcreamsource/codysseyWeekTwo) | 2026-04-09 | 1,882자 |
| coding-monkey-326 | [codyssey-e1-2](https://github.com/coding-monkey-326/codyssey-e1-2) | 2026-04-09 | 4,052자 |
| whdals006 | [Codyssey_E1-2](https://github.com/whdals006/Codyssey_E1-2) | 2026-04-07 | 없음 |
| jhj9109 | [codyssey2](https://github.com/jhj9109/codyssey2) | 2026-04-07 | 6,685자 |
| waz6432 | [CodysseyE1-2](https://github.com/waz6432/CodysseyE1-2) | 2026-04-08 | 1,700자 |
| whitecy01 | [codyssey2](https://github.com/whitecy01/codyssey2) | 2026-04-08 | 3,062자 |
| wilderif | [codyssey-e1-2](https://github.com/wilderif/codyssey-e1-2) | 2026-04-07 | 2,229자 |
| yacheahobbang | [codyssey-E1-2](https://github.com/yacheahobbang/codyssey-E1-2) | 2026-04-08 | 125자 |

---

## 3주차 과제

### 과제 내용 정리

## 과제 주제
NPU 시뮬레이터를 통한 MAC 연산 및 패턴 판별 원리 학습

## 학습 목표
*   MAC(Multiply-Accumulate) 연산의 기본 원리 이해
*   패턴 판별 로직 구현 및 성능 분석
*   JSON 데이터 파싱 및 스키마 검증
*   부동소수점 오차 처리 및 동점 판별 전략 학습
*   효율적인 라벨 정규화 로직 설계 및 구현

## 주요 내용 요약
본 과제는 MAC 연산과 패턴 판별 원리를 이해하기 위해 3x3 필터 2개와 패턴을 활용한 NPU 시뮬레이터를 개발하는 것을 목표로 합니다. 사용자 직접 입력 모드와 JSON 파일 분석 모드를 지원하며, 라벨 정규화, 부동소수점 오차를 고려한 동점 처리, 성능 분석 및 결과 리포트 기능을 포함합니다.

## 핵심 기술 및 개념
*   **프로그래밍 언어**: Python
*   **데이터 구조**: 2차원 배열 (list[list[float]]), JSON
*   **알고리즘**: MAC 연산, 반복문, 패턴 매칭, 라벨 정규화, 시간 복잡도(`O(N^2)`)
*   **라이브러리/모듈**: `sys`, `json`, `time`
*   **개념**: NPU (Neural Processing Unit), MAC 연산, 필터, 패턴, 라벨 정규화, 부동소수점 오차, epsilon, 동점 처리, 성능 분석 (평균 시간, 연산 횟수)
*   **명령어**: `python main.py`

## 과제 요구사항
*   [x] 3x3 사용자 입력 모드 구현
*   [x] 행/열 개수 및 숫자 파싱 검증 구현
*   [x] 반복문 기반 MAC 연산 구현
*   [x] epsilon 기반 동점 처리 구현
*   [x] 라벨 정규화(`+`, `cross`, `x` -> `Cross`, `X`) 구현
*   [x] `data.json` 스키마 검증 및 케이스 단위 FAIL 처리 구현
*   [x] 케이스별 PASS/FAIL 출력 구현
*   [x] 성능 분석 표 출력 구현
*   [x] 전체 결과 요약 출력 구현
*   [x] 실제 과제용 `data.json` 데이터 채우기 및 최종 실측 결과 반영

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| I-nkamanda | [codyssey2026/Problem3_Mini_NPU_Simulator](https://github.com/I-nkamanda/codyssey2026/tree/main/Problem3_Mini_NPU_Simulator) | 2026-04-08 | 없음 |
| 0-hu | [codyssey-e1-3](https://github.com/0-hu/codyssey-e1-3) | 2026-04-07 | 없음 |
| kimch0612 | [Codyssey_Week3](https://github.com/kimch0612/Codyssey_Week3) | 2026-04-09 | 10,408자 |
| JungSaeYoung | [codyssey_E1-3](https://github.com/JungSaeYoung/codyssey_E1-3) | 2026-04-08 | 4,373자 |

---

## python주차 과제

### 과제 내용 정리

# 🎯 나만의 퀴즈 게임

Python으로 만든 콘솔 기반 퀴즈 게임입니다.  
터미널에서 퀴즈를 풀고, 새로운 퀴즈를 추가하고, 점수를 기록할 수 있습니다.  
프로그램을 종료해도 데이터가 `state.json` 파일에 저장되어 다음 실행 시 그대로 유지됩니다.

- **GitHub 저장소**: https://github.com/clae-dev/ia-codyssey-Python

---

## 📌 퀴즈 주제 및 선정 이유

**주제: Python 프로그래밍 기초**

Python을 처음 배우면서 학습한 내용을 퀴즈로 만들면 복습 효과가 있다고 생각했습니다.  
변수, 자료형, 함수, 주석 등 기본 문법을 자연스럽게 반복 학습할 수 있도록 구성했습니다.

---

## 🚀 실행 방법

### 요구 사항
- Python 3.10 이상

### 실행
```bash
python main.py
```

외부 라이브러리 설치가 필요 없습니다. Python 표준 라이브러리만 사용합니다.

---

## 📋 기능 목록

| 번호 | 기능 | 설명 |
|------|------|------|
| 1 | 퀴즈 풀기 | 등록된 퀴즈를 랜덤 순서로 출제, 힌트 사용 가능 (감점 적용) |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호, 힌트(선택)를 입력하여 새 퀴즈 등록 |
| 3 | 퀴즈 삭제 | 등록된 퀴즈를 번호로 선택하여 삭제 |
| 4 | 퀴즈 목록 | 등록된 모든 퀴즈의 문제 텍스트를 번호와 함께 표시 |
| 5 | 점수 확인 | 최고 점수와 전체 게임 기록(날짜, 문제 수, 점수) 표시 |
| 6 | 종

_*(AI 요약 실패 — 원문 일부)*_

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| Opdata | [codyssey-python-with-git](https://github.com/Opdata/codyssey-python-with-git) | 2026-04-08 | 308자 |
| clae-dev | [ia-codyssey-Python](https://github.com/clae-dev/ia-codyssey-Python) | 2026-04-08 | 7,552자 |

---

## workstation주차 과제

### 과제 내용 정리

## 1. 프로젝트 개요

누구나 동일한 방식으로 실행/배포/디버그할 수 있는 환경을 구성하기 위해 워크스테이션을 구축한다.</br>
이 과정에서 CLI, Docker, Git/GitHub를 사용한다.
이 미션은 터미널로 디렉토리 권한 정리 / Docker를 설치, 실행, 운영/관리 한다.</br>
커스텀 Docker 이미지 제작, 포트 매핑, 볼륨 영속성 검증까지 CLI 기반으로 전 과정을 수행한다.</br>
이 경험은 이후 리눅스 트러블슈팅, CI/CD 파이프라인, 클라우드 배포/운영 등으로 자연스럽게 확장된다.</br>

---

## 2. 실행 환경

| 항목     | 버전 / 값            |
| -------- | -------------------- |
| OS       | macOS 26.3           |
| Shell    | zsh                  |
| Terminal | 기본 터미널          |
| Docker   | 9.3.1, build c2be9cc |
| Git      | 2.33.0               |

---

## 3. 터미널 조작 로그

```zsh
# cd, pwd, ls -al, mkdir, cp, mv, rm, cat, touch 등

$ cd ..
$ pwd # 현재 작업 중인 디렉토리의 절대 경로를 출력
/Users/jun/Documents/GitHub/codyssey-work/workstation

$ ls -al # 목록 확인(숨김 파일, 디렉토리 포함)
total 16
drwxr-xr-x  4 jun  sta

_*(AI 요약 실패 — 원문 일부)*_

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| Opdata | [codyssey-workstation](https://github.com/Opdata/codyssey-workstation) | 2026-04-08 | 19,310자 |
| mulloc1 | [codyssey_workstation](https://github.com/mulloc1/codyssey_workstation) | 2026-03-31 | 2,092자 |

---

## python_with_npu주차 과제

### 과제 내용 정리

_README 내용 없음_

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| mulloc1 | [codyssey_python_with_npu](https://github.com/mulloc1/codyssey_python_with_npu) | 2026-04-08 | 없음 |

---

## first_python주차 과제

### 과제 내용 정리

# Quiz Game

터미널에서 실행하는 파이썬 객관식 퀴즈 게임입니다. 기본 퀴즈를 불러와 진행하고, 게임 중/추가된 퀴즈와 최고 점수를 `state.json`에 저장합니다.

## 퀴즈 주제와 선정 이유

기본 퀴즈는 파이썬 기초 개념을 확인하는 내용으로 구성되어 있습니다. 예를 들어 `int` 타입, 분기(`if/elif/else`), 길이(`len`), 함수 정의(`def`), 클래스 초기화(`__init__`) 같은 주제를 다뤄서 초보 학습자가 핵심 문법을 빠르게 점검할 수 있도록 했습니다.

## 실행 방법

프로젝트 디렉터리 `first_python`에서 다음을 실행합니다.

```bash
python main.py
```

## 기능 목록

1. 기본 퀴즈 로드 및 시작
2. 퀴즈 풀기(`play_quiz`)
3. 퀴즈 추가(`add_quiz`) 및 상태 저장
4. 퀴즈 목록 출력(`list_quizzes`)
5. 최고 점수 확인(`show_best_score`)
6. 퀴즈 삭제(`delete_quiz`) 및 상태 저장
7. 상태 파일 저장/불러오기(`save_state`, `load_state`)
8. 문제 수 선택 및 랜덤 출제
9. 풀이 중 힌트 보기와 힌트 사용 시 점수 차감
10. 입력 오류 방지(비어 있는 입력, 숫자 범위 등 재입력 처리)

메인 메뉴: 1 퀴즈 풀기, 2 퀴즈 추가, 3 퀴즈 목록, 4 점수 확인, 5 퀴즈 삭제, 6 종료.

## 파일 구조

```text
first_python/
├─ main.py
├─ README.md
├─ .gitignore
├─ src/

_*(AI 요약 실패 — 원문 일부)*_

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| mulloc1 | [codyssey_first_python](https://github.com/mulloc1/codyssey_first_python) | 2026-04-06 | 8,903자 |

---

## docker주차 과제

### 과제 내용 정리

# Docker 기반 개발 환경 구축 실습

## 1. 프로젝트 개요
본 실습에서는 Docker를 활용하여 컨테이너 기반 개발 환경을 구축하였습니다.  
Docker 설치 및 실행 확인, Ubuntu 컨테이너 실행, Dockerfile을 이용한 이미지 생성,  
웹 서버 컨테이너 실행 및 포트 매핑, Bind Mount 실습, Docker Volume 영속성 실습을 진행하였습니다.  
추가로 Docker Compose, 환경 변수 활용, GitHub SSH 키 설정 보너스 과제도 수행하였습니다.  
실습 과정 전체를 GitHub Repository와 README 문서를 통해 정리하였습니다.

Docker를 이용하면 프로그램 실행 환경을 컨테이너로 관리할 수 있으며  
개발 환경을 동일하게 유지할 수 있다는 장점이 있습니다.  
이번 실습을 통해 Docker의 기본 구조와 동작 방식을 이해하는 것을 목표로 하였습니다.

---

## 2. 실행 환경

| 항목 | 내용 |
|------|------|
| OS | Windows 11 |
| Shell / Terminal | PowerShell 7.6.0 |
| Docker | Docker Desktop |
| Git | 2.x |
| Web Server | Nginx (alpine) |
| Language | HTML |

---

## 3. 수행 항목 체크리스트

**필수 항목**
- [x] 터미널 기본 조작 및 디렉토리 구성
- [x] 파일 / 디렉토리 권한 변경 실습
- [x] Docker 설치 및 점검 (`docker --version`, `docker 

_*(AI 요약 실패 — 원문 일부)*_

### 참고 레포

| 수강생 | 레포 | 최종 업데이트 | README 분량 |
|--------|------|:------------:|:-----------:|
| clae-dev | [ia-codyssey-Docker](https://github.com/clae-dev/ia-codyssey-Docker) | 2026-04-02 | 17,674자 |

---
