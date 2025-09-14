from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI 기초 학습", description="FastAPI 메모장")

class Memo(BaseModel):
    content: str

# 메모 저장소 (메모리)
memos_db = []
next_id = 1

@app.get("/")
async def root():
    return {
        "message": "간단한 메모장 API",
        "endpoints": {
            "GET /memos": "모든 메모 조회",
            "POST /memos": "새 메모 생성",
            "DELETE /memos/{id}": "메모 삭제"
        },
        "docs": "/docs"
    }

@app.get("/memos")
async def get_all_memos():
    return memos_db

@app.post("/memos")
async def create_memo(memo: Memo):
    global next_id
    memo_dict = {"id": next_id, "content": memo.content}
    memos_db.append(memo_dict)
    next_id += 1
    return memo_dict

@app.delete("/memos/{memo_id}")
async def delete_memo(memo_id: int):
    for i, memo in enumerate(memos_db):
        if memo["id"] == memo_id:
            deleted_memo = memos_db.pop(i)
            return {"message": f"메모 {memo_id} 삭제됨", "deleted_memo": deleted_memo}
    return {"error": f"메모 {memo_id}를 찾을 수 없습니다"}
