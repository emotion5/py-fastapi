from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="FastAPI 기초 학습", description="FastAPI 기본 기능 학습을 위한 API")

class Item(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "FastAPI 기초 학습 프로젝트에 오신 걸 환영합니다!"}
