## 1. 미션 개요

'PopPins II (어딧세이)' 프로젝트는 Google Gemini AI 모델을 활용하여 개인 맞춤형 학습 콘텐츠를 생성하는 AI 기반 교육 플랫폼입니다. 사용자가 학습 주제, 난이도, 챕터 수 등의 조건을 입력하면, AI가 해당 조건에 맞춰 개념 설명, 실습 과제, 객관식 및 주관식 퀴즈를 포함하는 커리큘럼을 동적으로 생성합니다. 이 프로젝트는 단순한 콘텐츠 생성에서 나아가, RAG(Retrieval-Augmented Generation) 기술을 도입하여 외부 지식(Python 교재 PDF)을 활용함으로써 AI 답변의 정확성과 신뢰성을 높였습니다.

최종 목표는 사용자가 자신의 학습 속도와 스타일에 맞춰 최적화된 학습 경험을 제공하고, AI가 생성한 콘텐츠를 통해 효과적인 자기 주도 학습을 지원하는 것입니다. 프로젝트는 백엔드(FastAPI), 프론트엔드(React), 그리고 RAG 벡터 데이터베이스 생성 도구로 구성되어 있으며, 데스크탑 애플리케이션(Tauri)으로의 확장 가능성까지 고려하여 설계되었습니다.

## 2. 학습 목표

이 프로젝트를 통해 수강생은 다음과 같은 핵심 역량을 습득하고 기술적 이해를 심화할 수 있습니다.

1.  **AI 모델 활용 및 통합**:
    *   Google Gemini API(Flash/Pro)를 백엔드 서비스에 통합하고, 다양한 프롬프트 엔지니어링 기법을 적용하여 고품질의 학습 콘텐츠(개념, 실습, 퀴즈)를 생성하는 방법을 학습합니다.
    *   AI 모델의 응답을 파싱하고 구조화된 데이터로 변환하는 기술(JSON 파싱, Pydantic 모델 활용)을 익힙니다.

2.  **RAG(Retrieval-Augmented Generation) 시스템 구축**:
    *   LangChain 프레임워크를 사용하여 외부 문서(PDF)에서 정보를 검색하고 AI 모델의 답변을 보강하는 RAG 파이프라인을 구축하는 방법을 이해합니다.
    *   `Semantic Chunking`과 같은 고급 청킹 기법을 적용하여 벡터 데이터베이스의 검색 정확도를 향상시키는 방법을 실습합니다.
    *   FAISS와 같은 벡터 데이터베이스를 구축하고 관리하는 방법을 학습합니다.
    *   임베딩 모델(Gemini, OpenAI)의 선택과 활용법을 익힙니다.

3.  **웹 서비스 개발 (백엔드)**:
    *   FastAPI 프레임워크를 사용하여 RESTful API를 설계하고 구현하는 능력을 강화합니다.
    *   비동기 프로그래밍(async/await)을 활용하여 AI API 호출과 같은 I/O 바운드 작업을 효율적으로 처리하는 방법을 학습합니다.
    *   SQLite와 SQLAlchemy ORM을 사용하여 데이터 영속성(Persistence)을 구현하고, 학습 이력 및 사용자 피드백을 관리하는 방법을 익힙니다.
    *   환경 변수 관리(`python-dotenv`), 로깅(`logging`), 의존성 관리(`pipenv` 또는 `venv`) 등 프로덕션 환경에 준하는 백엔드 개발 모범 사례를 적용합니다.

4.  **웹 서비스 개발 (프론트엔드)**:
    *   React 프레임워크와 Vite를 사용하여 사용자 친화적인 웹 인터페이스를 구축하는 방법을 학습합니다.
    *   백엔드 API와 통신하여 데이터를 비동기적으로 가져오고 화면에 렌더링하는 방법을 실습합니다.
    *   라우팅(React Router), 상태 관리, 컴포넌트 기반 UI 개발 등 최신 프론트엔드 개발 기법을 적용합니다.
    *   마크다운 렌더링, 코드 블록 강조 등 동적으로 생성된 콘텐츠를 효과적으로 표시하는 방법을 구현합니다.

5.  **DevOps 및 배포 준비**:
    *   `.env` 파일을 통한 환경 변수 관리, `.gitignore`를 통한 민감 정보 보호 등 보안 및 설정 관리의 중요성을 이해합니다.
    *   Git LFS를 활용하여 대용량 파일(벡터 DB)을 효율적으로 관리하는 방법을 학습합니다.
    *   테스트 코드(`pytest`)를 작성하여 애플리케이션의 안정성과 신뢰성을 확보하는 방법을 익힙니다.
    *   Docker를 활용한 컨테이너화 및 CI/CD 파이프라인 구축의 기초를 이해하고, 데스크탑 앱(Tauri)으로의 확장 가능성을 탐구합니다.

6.  **문제 해결 및 디버깅**:
    *   AI 모델의 응답 실패, API 키 오류, RAG 관련 문제 등 실제 개발 과정에서 발생할 수 있는 다양한 문제 상황을 진단하고 해결하는 능력을 배양합니다.
    *   효율적인 로깅 및 에러 핸들링 전략을 수립합니다.

## 3. 기능 요구사항

PopPins II 프로젝트는 사용자에게 개인화된 학습 경험을 제공하기 위해 다음과 같은 핵심 기능들을 요구합니다.

### 3.1. 핵심 기능

*   **AI 기반 학습 콘텐츠 생성**:
    *   사용자가 입력한 `학습 주제`, `난이도`, `챕터 수`, `학습 목표`에 따라 맞춤형 커리큘럼을 생성합니다.
    *   각 챕터는 `개념 설명`, `실습 과제`, `객관식 퀴즈`, `주관식 심화 학습`으로 구성됩니다.
    *   생성된 콘텐츠는 마크다운 형식으로 제공되며, 코드 블록이 올바르게 렌더링되어야 합니다.
*   **RAG(Retrieval-Augmented Generation) 시스템**:
    *   외부 PDF 교재(예: Python 교재)를 기반으로 벡터 데이터베이스를 구축하고, AI 모델이 답변을 생성할 때 해당 데이터베이스에서 관련 정보를 검색하여 활용합니다.
    *   `Semantic Chunking` 기법을 적용하여 검색 정확도를 극대화합니다.
    *   RAG 기능의 활성화/비활성화 및 벡터 DB 경로를 환경 변수로 제어할 수 있어야 합니다.
*   **데이터 영속성 및 학습 이력 관리**:
    *   생성된 모든 코스, 챕터, 퀴즈 결과, 사용자 피드백은 SQLite 데이터베이스에 저장되어야 합니다.
    *   사용자는 이전에 생성했던 코스를 대시보드에서 확인하고 다시 접근할 수 있어야 합니다.
    *   각 코스와 챕터는 고유한 URL을 가지며 직접 접근이 가능해야 합니다.
*   **사용자 피드백 및 적응형 학습**:
    *   챕터별 사용자 평점(1-5점) 및 코멘트를 저장하는 기능을 제공합니다.
    *   객관식 퀴즈에 대한 즉각적인 피드백(정답/오답) 및 점수를 제공합니다.
    *   주관식 심화 학습 문제에 대해 AI 기반 채점 및 모범 답안을 제공합니다.
    *   (향후 확장) 사용자 피드백과 퀴즈 성적을 기반으로 다음 콘텐츠를 개인화하여 생성하는 적응형 학습 시스템의 기반을 마련합니다.
*   **콘텐츠 다운로드**:
    *   생성된 챕터 콘텐츠를 마크다운 파일(`.md`) 또는 SCORM 패키지(`.zip`) 형태로 다운로드할 수 있어야 합니다.
    *   다운로드 파일명은 챕터 번호와 제목을 포함하여 정규화되어야 합니다.

### 3.2. 기술적 요구사항

*   **백엔드**:
    *   **프레임워크**: FastAPI를 사용하여 RESTful API를 구현합니다.
    *   **AI 통합**: Google Gemini API(gemini-2.5-flash, gemini-1.5-pro)를 사용합니다.
    *   **데이터베이스**: SQLite를 사용하여 학습 이력, 코스, 챕터, 피드백 등을 저장합니다. SQLAlchemy ORM을 활용합니다.
    *   **RAG**: LangChain을 사용하여 벡터 데이터베이스(FAISS)를 구축하고 관리합니다.
    *   **환경 변수**: `python-dotenv`를 사용하여 `.env` 파일에서 환경 변수를 로드합니다.
    *   **로깅**: `logging` 모듈을 사용하여 애플리케이션 로그를 기록합니다.
    *   **테스트**: `pytest`를 사용하여 단위 및 통합 테스트를 작성합니다.
*   **프론트엔드**:
    *   **프레임워크**: React를 사용하여 SPA(Single Page Application)를 구현합니다.
    *   **빌드 도구**: Vite를 사용하여 빠른 개발 환경을 구축합니다.
    *   **상태 관리**: (명시되지 않았으나) React의 Context API 또는 Redux/Zustand와 같은 라이브러리를 활용하여 전역 상태를 관리합니다.
    *   **UI/UX**: 사용자 친화적인 인터페이스를 제공하며, 마크다운 렌더링 라이브러리(예: `react-markdown`, `remark-gfm`)를 사용하여 콘텐츠를 표시합니다.
    *   **API 통신**: `fetch` API 또는 `axios`를 사용하여 백엔드와 비동기 통신합니다.
*   **RAG 벡터 DB 생성 도구**:
    *   Python 스크립트로 구현되며, PDF 파일을 읽어 `Semantic Chunking`을 수행하고 FAISS 벡터 DB를 생성합니다.
    *   `langchain-experimental`, `pypdf`, `tiktoken` 등의 라이브러리를 활용합니다.
*   **배포 및 관리**:
    *   `.gitignore`를 통해 민감 정보(API 키, `.env` 파일)가 Git에 커밋되지 않도록 관리합니다.
    *   Git LFS를 사용하여 대용량 벡터 DB 파일을 효율적으로 관리합니다.
    *   (선택 사항) Tauri를 사용하여 데스크탑 애플리케이션으로 패키징할 수 있는 구조를 제공합니다.

### 3.3. 비기능 요구사항

*   **성능**: AI 응답 시간은 챕터당 10-30초 이내를 목표로 합니다. 비동기 처리 및 효율적인 RAG 구현을 통해 성능을 최적화합니다.
*   **확장성**: 서비스 계층 분리, 모듈화된 아키텍처를 통해 향후 기능 추가 및 확장이 용이해야 합니다.
*   **안정성**: AI API 호출 실패, 네트워크 오류 등 예외 상황에 대한 견고한 에러 핸들링을 제공합니다. 콘텐츠 생성 실패 시 재시도 메커니즘을 고려합니다.
*   **보안**: API 키와 같은 민감 정보는 환경 변수로 관리하며, Git에 노출되지 않도록 합니다.
*   **사용성**: 직관적인 UI/UX를 제공하여 비전공자도 쉽게 사용할 수 있도록 합니다.

## 4. 핵심 기술 스택

PopPins II 프로젝트는 현대적인 웹 개발 및 AI 기술 스택을 활용하여 구축되었습니다. 각 구성 요소는 특정 목적을 위해 선택되었으며, 상호 보완적으로 작동하여 강력하고 유연한 시스템을 형성합니다.

### 4.1. 백엔드 (FastAPI)

*   **Python 3.8+**: 프로젝트의 주 언어. 간결하고 강력한 문법, 풍부한 라이브러리 생태계.
*   **FastAPI**: 고성능 웹 프레임워크. 비동기 처리(`async/await`)를 기본 지원하여 AI API 호출과 같은 I/O 바운드 작업에 효율적입니다. 자동 API 문서(Swagger UI, ReDoc) 생성 기능은 개발 편의성을 높입니다.
    *   **Pydantic**: 데이터 유효성 검사 및 직렬화/역직렬화에 사용됩니다. API 요청 및 응답 모델을 정의하여 데이터 일관성을 보장합니다.
*   **Uvicorn**: ASGI(Asynchronous Server Gateway Interface) 서버. FastAPI 애플리케이션을 실행하는 데 사용됩니다.
*   **Google Gemini API**: Google의 최신 대규모 언어 모델(LLM)인 Gemini 2.5 Flash 및 Gemini 1.5 Pro를 활용하여 학습 콘텐츠를 생성합니다.
    *   `google-generativeai` 라이브러리를 통해 API와 연동합니다.
*   **LangChain**: LLM 기반 애플리케이션 개발을 위한 프레임워크. RAG 파이프라인 구축, 프롬프트 관리, 체인 구성 등에 활용됩니다.
    *   `langchain-google-genai`: Gemini 모델과의 연동을 위한 LangChain 통합 모듈.
    *   `langchain-community`: 다양한 컴포넌트(문서 로더, 벡터스토어 등) 제공.
    *   `langchain-experimental`: `SemanticChunker`와 같은 실험적인 기능 활용.
*   **FAISS (Facebook AI Similarity Search)**: 효율적인 유사성 검색을 위한 라이브러리. RAG 시스템의 벡터 데이터베이스로 사용됩니다.
*   **SQLAlchemy**: Python SQL 툴킷 및 ORM(Object Relational Mapper). SQLite 데이터베이스와의 상호작용을 추상화하여 데이터 영속성을 구현합니다.
    *   **SQLite**: 가볍고 파일 기반의 관계형 데이터베이스. 개발 및 소규모 배포에 적합하며, 프로젝트의 학습 이력 및 코스 데이터를 저장하는 데 사용됩니다.
*   **python-dotenv**: `.env` 파일에서 환경 변수를 로드하여 민감 정보(API 키) 및 설정 값을 안전하게 관리합니다.
*   **logging**: Python 표준 로깅 라이브러리. 애플리케이션의 동작 상태, 에러, 디버그 정보를 기록합니다.
*   **pytest**: Python 테스트 프레임워크. 백엔드 API 엔드포인트 및 유틸리티 함수의 단위/통합 테스트를 작성하는 데 사용됩니다.
*   **pypdf**: PDF 파일을 파싱하고 텍스트를 추출하는 데 사용됩니다. RAG 벡터 DB 생성 과정에서 PDF 문서를 처리합니다.
*   **tiktoken**: OpenAI에서 개발한 토큰화 라이브러리. 텍스트의 토큰 수를 계산하여 LLM의 토큰 제한을 관리하는 데 활용될 수 있습니다.

### 4.2. 프론트엔드 (React)

*   **Node.js 18+**: JavaScript 런타임 환경. 프론트엔드 개발 도구 및 패키지 관리에 사용됩니다.
*   **React**: 선언적이고 컴포넌트 기반의 UI 라이브러리. 사용자 인터페이스를 구축하는 데 사용됩니다.
*   **Vite**: 차세대 프론트엔드 빌드 도구. 빠른 개발 서버와 최적화된 번들링을 제공하여 개발 생산성을 높입니다.
*   **TypeScript**: JavaScript의 상위 집합. 정적 타입 검사를 통해 코드의 안정성과 유지보수성을 향상시킵니다.
*   **Tailwind CSS (추정)**: 유틸리티 우선 CSS 프레임워크. 빠르고 유연하게 UI 스타일링을 할 수 있습니다. (과제 자료에 명시되지는 않았으나, 현대적인 React 프로젝트에서 흔히 사용됨)
*   **React Router**: 클라이언트 측 라우팅을 구현하여 SPA에서 여러 페이지를 관리합니다.
*   **react-markdown**: 마크다운 형식의 텍스트를 HTML로 렌더링하는 React 컴포넌트. AI가 생성한 콘텐츠를 웹 페이지에 표시하는 데 사용됩니다.
    *   **remark-gfm**: GitHub Flavored Markdown(GFM)을 지원하기 위한 `react-markdown` 플러그인. 테이블, 체크박스 등 GFM 문법을 올바르게 렌더링합니다.
    *   **rehype-highlight**: 코드 블록에 구문 강조(syntax highlighting)를 적용하는 `react-markdown` 플러그인.
*   **Axios / Fetch API**: 백엔드 API와 비동기 통신을 수행하여 데이터를 주고받습니다.

### 4.3. 기타 도구 및 기술

*   **Git**: 버전 관리 시스템. 소스 코드 변경 이력을 추적하고 협업을 용이하게 합니다.
*   **Git LFS (Large File Storage)**: 대용량 파일(예: FAISS 벡터 DB 파일)을 Git 저장소에서 효율적으로 관리하기 위한 확장 기능.
*   **Tauri**: Rust 기반의 크로스 플랫폼 데스크탑 애플리케이션 프레임워크. 웹 기술(HTML, CSS, JavaScript)로 데스크탑 앱을 빌드할 수 있게 하여, `standalone` 버전 구현에 사용됩니다.
*   **Docker / Docker Compose (향후 확장)**: 애플리케이션을 컨테이너화하여 일관된 개발 및 배포 환경을 제공합니다. (과제 자료에 언급되었으나, 직접적인 구현은 아님)

이러한 기술 스택의 조합은 PopPins II 프로젝트가 강력한 AI 기능을 제공하면서도, 현대적인 웹 애플리케이션의 요구사항을 충족하고, 향후 확장 및 유지보수가 용이하도록 설계되었음을 보여줍니다.

## 5. 권장 프로젝트 구조

PopPins II 프로젝트는 백엔드, 프론트엔드, RAG 벡터 DB 생성 도구 및 기타 지원 파일들로 구성된 모놀리식 저장소(monorepo) 형태를 취하고 있습니다. 효율적인 개발, 관리 및 배포를 위해 다음과 같은 프로젝트 구조를 권장합니다.

```
Pop-pins2/
├── .git/                       # Git 버전 관리 관련 파일
├── .github/                    # GitHub Actions 등 CI/CD 설정 (선택 사항)
├── .gitignore                  # Git 추적에서 제외할 파일/폴더 목록
├── .env.example                # 환경 변수 예시 파일 (Git에 커밋)
├── app/                        # 백엔드 서비스 (FastAPI)
│   ├── __init__.py             # Python 패키지 초기화
│   ├── main.py                 # FastAPI 애플리케이션 진입점 및 API 라우터
│   ├── models/                 # Pydantic 및 SQLAlchemy 모델 정의
│   │   ├── __init__.py
│   │   ├── database.py         # SQLAlchemy 엔진, 세션, Base 정의
│   │   ├── schemas.py          # Pydantic 요청/응답 스키마
│   │   └── crud.py             # 데이터베이스 CRUD 작업 함수
│   ├── services/               # 비즈니스 로직 및 외부 서비스 연동
│   │   ├── __init__.py
│   │   ├── generator.py        # 핵심 콘텐츠 생성 로직 (Gemini, RAG 통합)
│   │   ├── rag_service.py      # RAG 관련 로직 (벡터 DB 로드, 검색)
│   │   └── db_service.py       # 데이터베이스 관련 비즈니스 로직
│   ├── routers/                # API 엔드포인트 라우터 (모듈화)
│   │   ├── __init__.py
│   │   ├── course.py           # 코스 생성 및 관리 API
│   │   ├── chapter.py          # 챕터 콘텐츠 생성 및 관리 API
│   │   ├── feedback.py         # 피드백 API
│   │   └── health.py           # 헬스 체크 API
│   ├── core/                   # 핵심 유틸리티 및 설정
│   │   ├── __init__.py
│   │   ├── config.py           # 환경 변수 로드 및 애플리케이션 설정
│   │   └── logger.py           # 로깅 설정
│   ├── tests/                  # 백엔드 테스트 코드
│   │   ├── __init__.py
│   │   ├── conftest.py         # pytest fixtures
│   │   ├── test_api_endpoints.py # API 엔드포인트 테스트
│   │   └── test_generator.py   # generator 서비스 로직 테스트
│   ├── static/                 # 정적 파일 (SCORM 패키지 템플릿 등)
│   ├── templates/              # Jinja2 템플릿 (필요시)
│   ├── .env.example            # 백엔드 전용 환경 변수 예시
│   ├── requirements.txt        # 백엔드 Python 의존성 목록
│   ├── API_REFERENCE.md        # 백엔드 API 문서
│   └── CHANGELOG.md            # 백엔드 변경 이력
├── frontend/                   # 프론트엔드 서비스 (React + Vite)
│   ├── public/                 # 정적 자산 (index.html, favicon 등)
│   ├── src/                    # 소스 코드
│   │   ├── assets/             # 이미지, 아이콘 등 정적 자산
│   │   ├── components/         # 재사용 가능한 UI 컴포넌트
│   │   │   ├── common/         # 범용 컴포넌트 (버튼, 모달 등)
│   │   │   └── specific/       # 특정 페이지/기능 관련 컴포넌트
│   │   ├── contexts/           # React Context API (전역 상태 관리)
│   │   ├── hooks/              # 커스텀 React Hooks
│   │   ├── pages/              # 라우팅되는 페이지 컴포넌트
│   │   │   ├── Dashboard.tsx
│   │   │   ├── CourseDetail.tsx
│   │   │   └── ChapterView.tsx
│   │   ├── services/           # 백엔드 API 호출 로직
│   │   │   └── api.ts          # API 클라이언트
│   │   ├── styles/             # 전역 스타일 및 CSS 변수
│   │   ├── utils/              # 유틸리티 함수
│   │   ├── App.tsx             # 메인 애플리케이션 컴포넌트
│   │   ├── main.tsx            # 애플리케이션 진입점
│   │   └── vite-env.d.ts       # Vite 환경 변수 타입 정의
│   ├── .env.example            # 프론트엔드 전용 환경 변수 예시
│   ├── package.json            # Node.js 패키지 의존성 및 스크립트
│   ├── tsconfig.json           # TypeScript 설정
│   └── README.md               # 프론트엔드 README
├── RAG vector generator/       # RAG 벡터 DB 생성 도구
│   ├── pdfs/                   # 학습에 사용될 PDF 원본 파일 저장소
│   ├── vector_db/              # 생성된 벡터 DB 저장소 (Git LFS 관리)
│   │   └── python_textbook_gemini_db_semantic/ # 실제 DB 파일들
│   ├── python_textbook_rag_generator.py # 벡터 DB 생성 스크립트
│   ├── requirements.txt        # RAG 생성기 Python 의존성
│   └── README.md               # RAG 생성기 README
├── standalone/                 # Tauri 기반 데스크탑 앱 (선택 사항)
│   ├── src-tauri/              # Rust 백엔드 (Tauri 코어)
│   ├── frontend/               # Tauri 앱에 포함될 웹 프론트엔드 (복사본 또는 빌드 결과)
│   ├── app/                    # Tauri 앱에 포함될 백엔드 (복사본 또는 빌드 결과)
│   ├── vector_db/              # Tauri 앱에 포함될 벡터 DB (복사본)
│   └── README.md               # Standalone 앱 README
├── venv/                       # Python 가상 환경 (Git 추적 제외)
├── node_modules/               # Node.js 패키지 (Git 추적 제외)
├── manual.md                   # 비전공자용 사용자 설명서
├── dev_summary.md              # 개발 요약 및 진행 상황
├── README.md                   # 프로젝트 메인 README
├── README_SETUP.md             # 새 리포지토리 설정 가이드
├── README_TESTS.md             # 테스트 가이드
└── cleanup_for_new_repo.ps1    # 정리 스크립트 (Windows PowerShell)
```

### 구조 설명:

*   **루트 디렉토리**: 프로젝트의 전반적인 설정 파일, README, 가이드 문서, 그리고 주요 서브 프로젝트(app, frontend, RAG generator)를 포함합니다.
*   **`app/`**: FastAPI 백엔드 애플리케이션의 모든 코드를 포함합니다. `services` 디렉토리에 비즈니스 로직을, `models`에 데이터 모델을, `routers`에 API 엔드포인트를 분리하여 모듈성을 높입니다. `core`는 전역 설정 및 유틸리티를 담습니다.
*   **`frontend/`**: React 프론트엔드 애플리케이션의 모든 코드를 포함합니다. `src` 내부에 컴포넌트, 페이지, 서비스, 유틸리티 등을 기능별로 분리하여 관리합니다.
*   **`RAG vector generator/`**: RAG 기능을 위한 벡터 데이터베이스를 생성하는 독립적인 Python 스크립트와 관련 리소스(PDFs, 생성된 DB)를 포함합니다.
*   **`standalone/`**: Tauri를 사용하여 데스크탑 애플리케이션을 빌드하기 위한 구조를 제공합니다. 이는 웹 애플리케이션의 백엔드와 프론트엔드를 통합하여 독립적으로 실행 가능한 형태로 만듭니다.
*   **`python_textbook_gemini_db_semantic/`**: RAG 생성기에서 생성된 실제 벡터 데이터베이스 파일들이 저장되는 위치입니다. 이 폴더는 Git LFS로 관리되어야 합니다.
*   **문서 파일**: `README.md`, `manual.md`, `dev_summary.md` 등 프로젝트의 다양한 측면을 설명하는 문서들을 루트에 배치하여 접근성을 높입니다.
*   **환경 설정 파일**: `.gitignore`, `.env.example` 등은 프로젝트의 보안과 이식성을 위해 필수적입니다.

이러한 구조는 각 구성 요소의 독립성을 유지하면서도, 전체 프로젝트의 일관성과 관리 용이성을 보장합니다.

## 6. 구현 핵심 포인트

PopPins II 프로젝트의 성공적인 구현을 위해 다음 핵심 포인트들을 고려해야 합니다. 각 포인트는 기술적 도전과제를 해결하고 프로젝트의 목표를 달성하는 데 중요한 역할을 합니다.

### 6.1. AI 콘텐츠 생성 및 프롬프트 엔지니어링

*   **다단계 프롬프트 설계**: 단일 프롬프트로 모든 콘텐츠를 생성하기보다, 커리큘럼 개요, 챕터 제목, 개념, 실습, 퀴즈 등 각 단계별로 최적화된 프롬프트를 설계합니다.
    *   `ContentGenerator` 클래스 내부에 각 콘텐츠 유형(개념, 실습, 퀴즈)에 대한 전용 프롬프트 템플릿을 정의하고 관리합니다.
    *   예시: `generate_course_outline_prompt`, `generate_concept_prompt`, `generate_exercise_prompt`, `generate_quiz_prompt`.
*   **JSON 형식 강제 및 파싱**: AI 모델이 구조화된 JSON 응답을 반환하도록 프롬프트에 명시적으로 지시하고, 응답을 안전하게 파싱하는 로직을 구현합니다.
    *   `clean_json_response`와 같은 유틸리티 함수를 사용하여 AI 응답에서 불필요한 마크다운 블록(` ```json `)을 제거하고 JSON 파싱 오류를 처리합니다.
    *   Pydantic 모델을 사용하여 파싱된 데이터의 유효성을 검사하고 타입 안정성을 확보합니다.
*   **콘텐츠 품질 제어**:
    *   `temperature`, `top_p`, `top_k` 등 Gemini API의 파라미터를 조정하여 생성되는 콘텐츠의 창의성과 일관성을 제어합니다.
    *   `max_output_tokens`를 적절히 설정하여 응답 길이를 조절합니다.
*   **재생성 메커니즘**: AI 응답 실패 또는 품질 저하 시, 사용자에게 콘텐츠 재생성 옵션을 제공하고, 백엔드에서 캐시를 무시하고 재시도하는 로직을 구현합니다 (`force_refresh` 파라미터).

### 6.2. RAG(Retrieval-Augmented Generation) 시스템 구현

*   **Semantic Chunking**: `langchain-experimental`의 `SemanticChunker`를 사용하여 PDF 문서를 의미론적 경계에 따라 분할합니다. 이는 고정 크기 청킹보다 관련성 높은 청크를 검색하는 데 유리합니다.
    *   **구현 예시**:
        ```python
        from langchain_experimental.text_splitter import SemanticChunker
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        
        # ... (PDF 로드 및 텍스트 추출)
        
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
        text_splitter = SemanticChunker(embeddings, breakpoint_threshold_type="percentile")
        docs = text_splitter.create_documents([full_text])
        ```
*   **벡터 데이터베이스 구축 및 관리**:
    *   FAISS를 사용하여 임베딩된 청크를 저장하고 효율적인 유사성 검색을 수행합니다.
    *   `RAG vector generator` 스크립트를 통해 PDF 파일을 처리하고 벡터 DB를 생성하는 파이프라인을 구축합니다.
    *   `Git LFS`를 사용하여 생성된 대용량 FAISS 인덱스 파일을 Git 저장소에서 관리합니다.
*   **RAG 통합 로직**:
    *   `rag_service.py`와 같은 모듈에서 벡터 DB 로드, 쿼리 임베딩, 유사성 검색, 검색된 문서 필터링 등의 RAG 관련 로직을 캡슐화합니다.
    *   `ContentGenerator`는 사용자 쿼리를 기반으로 `rag_service`를 호출하여 관련 문서를 검색하고, 이를 AI 프롬프트에 `[RAG Context]`로 주입하여 답변을 보강합니다.
    *   **환경 변수 제어**: `USE_RAG`, `VECTOR_DB_PATH`, `VECTOR_DB_EMBEDDING_MODEL` 환경 변수를 통해 RAG 기능의 활성화 여부와 설정값을 동적으로 제어합니다.

### 6.3. 데이터 영속성 및 ORM 활용

*   **SQLAlchemy ORM**: `app/models/database.py`에 SQLAlchemy 엔진, 세션, `Base`를 설정하고, `app/models/schemas.py`에 `Course`, `Chapter`, `Feedback`, `GenerationLog` 등의 ORM 모델을 정의합니다.
*   **CRUD 작업**: `app/models/crud.py`에 데이터베이스와의 상호작용을 위한 CRUD(Create, Read, Update, Delete) 함수를 구현합니다.
*   **의존성 주입**: FastAPI의 의존성 주입 시스템을 활용하여 각 API 엔드포인트에 데이터베이스 세션을 주입하고, 요청 처리 후 세션을 자동으로 닫도록 합니다.
    *   **예시**:
        ```python
        from fastapi import Depends
        from sqlalchemy.orm import Session
        from app.models.database import get_db
        
        @router.post("/generate-course")
        async def generate_course_api(request: CourseRequest, db: Session = Depends(get_db)):
            # ... db 세션을 사용하여 데이터 저장
        ```
*   **학습 이력 및 대시보드**: `GenerationLog` 모델을 사용하여 모든 AI 생성 요청의 메타데이터(주제, 모델, 지연 시간 등)를 기록하고, 이를 기반으로 대시보드에서 최근 학습 코스 목록을 제공합니다.

### 6.4. 환경 변수 관리 및 보안

*   **`.env` 파일 사용**: `python-dotenv` 라이브러리를 사용하여 `GEMINI_API_KEY`, `PORT`, `USE_RAG` 등 민감 정보 및 설정 값을 `.env` 파일에서 로드합니다.
*   **`.gitignore` 설정**: `.env` 파일이 Git 저장소에 커밋되지 않도록 `.gitignore`에 명시적으로 추가합니다.
    *   **체크리스트 활용**: `poppins/.gitignore_check.md`에 제시된 명령어를 활용하여 `.env` 파일이 올바르게 무시되고 있는지 정기적으로 확인합니다.
*   **`.env.example` 제공**: 필요한 환경 변수 목록과 예시 값을 담은 `.env.example` 파일을 제공하여 다른 개발자가 쉽게 환경을 설정할 수 있도록 합니다.

### 6.5. 비동기 프로그래밍 및 성능 최적화

*   **`async/await`**: FastAPI는 비동기 프레임워크이므로, AI API 호출(`gemini.generate_content`), RAG 검색, 데이터베이스 I/O 등 시간이 오래 걸리는 작업에 `async/await`를 적극적으로 활용하여 논블로킹(non-blocking) 방식으로 처리하고 애플리케이션의 응답성을 높입니다.
*   **병렬 처리**: 여러 챕터 콘텐츠를 동시에 생성해야 하는 경우, `asyncio.gather` 등을 사용하여 AI 호출을 병렬로 실행함으로써 전체 응답 시간을 단축할 수 있습니다.
*   **캐싱 전략**: (선택 사항) 동일한 요청에 대한 AI 응답을 캐싱하여 불필요한 API 호출을 줄이고 응답 속도를 향상시킬 수 있습니다. (현재 프로젝트에서는 `force_refresh`를 통해 캐시 무시 기능이 구현됨)

### 6.6. 프론트엔드 UI/UX 및 마크다운 렌더링

*   **컴포넌트 기반 개발**: React의 컴포넌트 아키텍처를 활용하여 재사용 가능한 UI 컴포넌트를 구축하고, 페이지별로 컴포넌트를 조합하여 UI를 구성합니다.
*   **마크다운 렌더링**: `react-markdown`, `remark-gfm`, `rehype-highlight` 라이브러리를 사용하여 AI가 생성한 마크다운 콘텐츠를 웹 페이지에 올바르게 렌더링하고, 코드 블록에 구문 강조를 적용합니다.
*   **반응형 디자인**: 다양한 디바이스(데스크탑, 모바일)에서 일관된 사용자 경험을 제공하도록 반응형 웹 디자인을 적용합니다.
*   **사용자 피드백**: 로딩 스피너, 에러 메시지, 성공 알림 등 사용자에게 현재 시스템 상태에 대한 명확한 피드백을 제공하여 사용성을 높입니다.

이러한 핵심 포인트들을 충실히 구현함으로써 PopPins II 프로젝트는 강력하고 안정적인 AI 기반 학습 플랫폼으로 기능할 수 있습니다.

## 7. 트러블슈팅 & 팁

PopPins II 프로젝트를 개발하고 운영하는 과정에서 발생할 수 있는 일반적인 문제들과 이를 해결하기 위한 팁 및 모범 사례를 제시합니다.

### 7.1. 환경 설정 및 실행 관련 문제

*   **문제**: `GEMINI_API_KEY`가 설정되지 않았거나 잘못되어 AI 모델 초기화 실패.
    *   **해결**:
        1.  `app/.env` 파일이 프로젝트 루트 디렉토리(또는 `app` 디렉토리)에 올바르게 생성되었는지 확인합니다.
        2.  `.env` 파일 내 `GEMINI_API_KEY=your_actual_api_key_here` 형식으로 유효한 API 키가 입력되었는지 확인합니다. `your_actual_api_key_here` 같은 플레이스홀더 값은 사용할 수 없습니다.
        3.  API 키가 20자 이상인지, 공백이나 특수문자가 포함되지 않았는지 확인합니다.
        4.  터미널에서 `echo $GEMINI_API_KEY` (Linux/macOS) 또는 `$env:GEMINI_API_KEY` (Windows PowerShell) 명령어로 환경 변수가 제대로 로드되었는지 확인합니다.
        5.  Google AI Studio에서 API 키가 활성화되어 있고, 할당량 제한에 도달하지 않았는지 확인합니다.
*   **문제**: 백엔드 서버가 시작되지 않거나 프론트엔드에서 백엔드 API에 연결할 수 없음.
    *   **해결**:
        1.  백엔