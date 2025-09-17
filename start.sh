#!/bin/bash

# Render.com 배포용 시작 스크립트
# FastAPI와 Streamlit을 동시에 실행

# 환경 변수 설정
export MAIN_HOST=${HOST:-0.0.0.0}
export MAIN_PORT=${PORT:-8501}
export FASTAPI_PORT=8000

echo "Starting FastAPI server on $MAIN_HOST:$FASTAPI_PORT"
echo "Starting Streamlit server on $MAIN_HOST:$MAIN_PORT (main port)"

# FastAPI 서버를 백그라운드에서 시작 (고정 포트 8000)
uvicorn main:app --host $MAIN_HOST --port $FASTAPI_PORT &

# 잠시 대기 (FastAPI 서버가 시작될 시간)
sleep 5

# Streamlit 서버 시작 (메인 포트에서 실행)
streamlit run streamlit_app.py \
  --server.port $MAIN_PORT \
  --server.address $MAIN_HOST \
  --server.headless true \
  --server.enableCORS false \
  --server.enableXsrfProtection false