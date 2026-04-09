# Term-Project: PopPins II (어딧세이)

> 레포: [poppins](https://github.com/I-nkamanda/poppins), [termproj_plans](https://github.com/I-nkamanda/termproj_plans)

---

## 1. 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 프로젝트명 | PopPins II (어딧세이) |
| 유형 | AI 기반 PBL(Problem-Based Learning) 생성 플랫폼 |
| AI 모델 | Gemini 2.5 Flash / Gemini 2.0 Flash Exp |
| 벡터 DB | FAISS with Semantic Chunking (LangChain) |
| 백엔드 | FastAPI (uvicorn) |
| 프론트엔드 | React (Vite) |
| 데스크탑 앱 | Tauri 기반 Standalone 앱 |
| 작성자 | 이진걸 |

---

## 2. 핵심 기능

PopPins II는 Python PDF 교재를 벡터 DB에 저장하여 AI hallucination을 방지하고, LMS에 부착 가능한 PBL 모듈로 설계되었습니다.

**학습 주제 입력**: AI와 대화를 통해 학습 주제를 구체화합니다.

**AI 기반 PBL 생성**: RAG(Retrieval-Augmented Generation)로 교재 기반 학습 자료를 생성합니다.

**4가지 AI 생성기**: 커리큘럼 생성기, 개념 설명 생성기, 실습 과제 생성기, 퀴즈 생성기를 제공합니다.

**객관식/주관식 퀴즈**: 챕터별 5개 객관식 + 3개 주관식 문제를 자동 생성하고, AI가 채점합니다.

**대시보드**: 최근 학습 코스를 한눈에 볼 수 있는 대시보드를 제공합니다.

**다운로드**: 챕터별 콘텐츠를 다운로드할 수 있습니다.

---

## 3. 기술 스택

| 계층 | 기술 |
|------|------|
| AI/LLM | Google Gemini 2.5 Flash, Gemini 2.0 Flash Exp |
| RAG | LangChain + FAISS (Semantic Chunking) |
| 백엔드 | FastAPI + uvicorn |
| 프론트엔드 | React + Vite |
| 데스크탑 | Tauri (Rust 기반 경량 앱) |
| 데이터 | PDF 파싱, 벡터 임베딩 |

---

## 4. 기획 문서 목록

[termproj_plans](https://github.com/I-nkamanda/termproj_plans) 레포에 다음 기획 문서가 포함되어 있습니다.

| 문서 | 내용 |
|------|------|
| `pop_pins_ii_prd.md` | Product Requirement Document (v1.4.2) |
| `pop_pins_ii_architecture.md` | 시스템 아키텍처 |
| `pop_pins_ii_erd.md` | ERD (데이터베이스 설계) |
| `pop_pins_ii_ia_diagram.md` | 정보 아키텍처 다이어그램 |
| `pop_pins_ii_sequence_diagram.md` | 시퀀스 다이어그램 |
| `pop_pins_ii_user_diagram.md` | 사용자 다이어그램 |
| `pop_pins_ii_wireframe.md` | 와이어프레임 |
| `pop_pins_ii_test_strategy.md` | 테스트 전략 |
| `pop_pins_ii_test_data.md` | 테스트 데이터 |
| `pop_pins_ii_takeaways.md` | 회고/교훈 |
| `pop_pins_ii_planning_document.md` | 기획 문서 |
| `텀 프로젝트 제안_이진걸.pptx` | 프로젝트 제안 발표 자료 |

---

## 5. 참고 가치

이 텀프로젝트는 다음과 같은 점에서 참고 가치가 높습니다.

**기획 문서 완성도**: PRD, ERD, 와이어프레임, 시퀀스 다이어그램 등 실무 수준의 기획 문서가 모두 공개되어 있습니다.

**RAG 구현 사례**: Gemini + FAISS + LangChain을 활용한 실제 RAG 파이프라인 구현 코드를 참고할 수 있습니다.

**풀스택 구성**: FastAPI(백엔드) + React(프론트엔드) + Tauri(데스크탑) 3계층 아키텍처의 실제 구현 사례입니다.
