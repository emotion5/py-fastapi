# 간단한 메모장 - FastAPI + Streamlit

FastAPI를 학습하기 위한 간단한 메모장 애플리케이션입니다.

## 기능
- 메모 추가
- 메모 목록 조회
- 메모 삭제
- 회색조 미니멀 디자인

## 실행 방법

### 1. 의존성 설치
```bash
uv sync
```

### 2. 서버 실행 (두 개의 터미널 필요)

**터미널 1: FastAPI 백엔드 서버**
```bash
uvicorn main:app --reload
```
- 포트: 8000
- API 문서: http://localhost:8000/docs

**터미널 2: Streamlit 프론트엔드**
```bash
streamlit run streamlit_app.py
```
- 포트: 8501
- 메인 접속: http://localhost:8501

### 3. 사용법
1. 브라우저에서 http://localhost:8501 접속
2. 메모 입력 후 "메모 추가" 버튼 클릭
3. 목록에서 메모 확인 및 삭제

## 구조
```
FastAPI (백엔드) ←→ Streamlit (프론트엔드) ←→ 사용자
```

- **FastAPI**: REST API 제공 (메모 CRUD)
- **Streamlit**: 웹 UI 제공 (httpx로 API 호출)
- 사용자는 Streamlit에만 접속하면 됩니다