#!/bin/bash

# Render.com 배포용 시작 스크립트
# FastAPI와 Streamlit을 동시에 실행

# 환경 변수 설정
export FASTAPI_HOST=${HOST:-0.0.0.0}
export FASTAPI_PORT=${PORT:-8000}
export STREAMLIT_PORT=$((FASTAPI_PORT + 1))

echo "Starting FastAPI server on $FASTAPI_HOST:$FASTAPI_PORT"
echo "Starting Streamlit server on $FASTAPI_HOST:$STREAMLIT_PORT"

# FastAPI 서버를 백그라운드에서 시작
uvicorn main:app --host $FASTAPI_HOST --port $FASTAPI_PORT &

# 잠시 대기 (FastAPI 서버가 시작될 시간)
sleep 3

# Streamlit 서버 시작 (포그라운드에서 실행)
streamlit run streamlit_app.py \
  --server.port $STREAMLIT_PORT \
  --server.address $FASTAPI_HOST \
  --server.headless true \
  --server.enableCORS false \
  --server.enableXsrfProtection false