# FastAPI 기초 학습 - 간단한 메모장 (Product Requirements Document)

## 프로젝트 개요
FastAPI를 이해하기 위한 아주 간단한 한줄 메모장 애플리케이션

## 목표
- FastAPI 기본 개념 이해
- 메모 CRUD 작업 구현 (단계별)
- API 문서화 자동 생성 확인
- Pydantic 데이터 검증 학습
- 기본 에러 처리

## 기술 스택
- **Python**: 3.10+
- **FastAPI**: 웹 프레임워크
- **Uvicorn**: ASGI 서버
- **Pydantic**: 데이터 검증

## 구현 기능 (단계별 학습)

### 1. 기본 API 엔드포인트
- `GET /`: 웰컴 메시지 반환

### 2. 메모 API 엔드포인트 (하나씩 추가하며 학습)
- `GET /memos`: 모든 메모 조회
- `POST /memos`: 새 메모 생성
- `GET /memos/{memo_id}`: 특정 메모 조회
- `DELETE /memos/{memo_id}`: 메모 삭제

### 3. 데이터 모델
```python
class Memo(BaseModel):
    content: str  # 메모 내용 (필수)
    # id는 서버에서 자동 생성
```

### 4. 에러 처리
- 404: 메모를 찾을 수 없을 때
- 적절한 HTTP 상태 코드 반환

## 실행 방법

### 1. 환경 설정
```bash
# 프로젝트 디렉토리로 이동
cd 01-fastapi-study

# 의존성 확인 (이미 설치됨)
uv sync
```

### 2. 서버 실행
```bash
uvicorn main:app --reload
```

### 3. API 문서 확인
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 4. API 테스트
브라우저에서 직접 접속하거나 curl, httpx 등을 사용하여 테스트

## 학습 체크리스트

### 기본 개념
- [ ] FastAPI 앱 생성 방법 이해
- [ ] 라우터와 경로 매개변수 이해
- [ ] Pydantic 모델 정의 및 사용
- [ ] 자동 API 문서 생성 확인

### CRUD 작업
- [ ] GET 요청으로 데이터 조회
- [ ] POST 요청으로 데이터 생성
- [ ] PUT 요청으로 데이터 수정
- [ ] DELETE 요청으로 데이터 삭제

### 에러 처리
- [ ] HTTPException 사용법
- [ ] 적절한 HTTP 상태 코드 반환
- [ ] 에러 메시지 커스터마이징

### 추가 학습 (선택사항)
- [ ] 쿼리 매개변수 사용
- [ ] 요청 본문 검증
- [ ] 응답 모델 정의
- [ ] 미들웨어 추가

## 다음 단계
이 프로젝트를 완료한 후:
1. 더 복잡한 데이터베이스 연동 (SQLAlchemy)
2. 인증/인가 구현
3. Streamlit과 연결하여 풀스택 애플리케이션 구축

## 참고 자료
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Pydantic 문서](https://docs.pydantic.dev/)
- [Uvicorn 문서](https://www.uvicorn.org/)