import streamlit as st
import httpx
import json

# 페이지 설정
st.set_page_config(
    page_title="간단한 메모장",
    page_icon="",
    layout="centered"
)

# API 베이스 URL - 환경에 따라 동적 설정
import os

# Render.com 배포시에는 localhost:8000으로 FastAPI 접근
if "onrender.com" in os.environ.get("RENDER_EXTERNAL_URL", ""):
    API_BASE = "http://localhost:8000"
else:
    # 로컬 개발 환경
    API_BASE = "http://localhost:8000"

# 커스텀 CSS로 회색조 미니멀 디자인
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #4a4a4a;
        font-weight: 300;
        margin-bottom: 2rem;
    }
    .memo-card {
        background: #f8f9fa;
        border-left: 4px solid #6c757d;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .memo-content {
        color: #495057;
        margin: 0;
    }
    .memo-id {
        color: #6c757d;
        font-size: 0.8rem;
        margin-top: 0.5rem;
    }
    .stButton > button {
        background-color: #6c757d;
        color: white;
        border: none;
        padding: 0.25rem 0.75rem;
        font-size: 0.875rem;
    }
    .stButton > button:hover {
        background-color: #545b62;
    }

    /* 입력 필드 직각 처리 */
    .stTextInput > div > div > input {
        border-radius: 0;
    }

    /* 입력 필드 컨테이너 직각 처리 */
    .stTextInput > div > div {
        border-radius: 0;
    }

    /* 폼 제출 버튼 직각 처리 */
    .stFormSubmitButton > button {
        border-radius: 0;
    }

    /* 폼 전체 컨테이너 직각 처리 */
    .stForm {
        border-radius: 0;
    }

    /* 폼 내부 컨테이너 직각 처리 */
    .stForm > div {
        border-radius: 0;
    }
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<h1 class="main-header">간단 메모</h1>', unsafe_allow_html=True)

# FastAPI 연결 확인
def check_api_connection():
    try:
        response = httpx.get(f"{API_BASE}/")
        return response.status_code == 200
    except:
        return False

if not check_api_connection():
    st.error("⚠️ FastAPI 서버에 연결할 수 없습니다. `uvicorn main:app --reload` 를 실행해주세요.")
    st.stop()

# 메모 추가 섹션
st.markdown("### ")
with st.form("memo_form"):
    memo_content = st.text_input("메모 내용", placeholder="메모를 입력하세요...", label_visibility="collapsed")
    submit_button = st.form_submit_button("메모 추가")

    if submit_button and memo_content.strip():
        try:
            response = httpx.post(
                f"{API_BASE}/memos",
                json={"content": memo_content.strip()}
            )
            if response.status_code == 200:
                st.success("메모가 추가되었습니다!")
                st.rerun()
            else:
                st.error("메모 추가 중 오류가 발생했습니다.")
        except Exception as e:
            st.error(f"연결 오류: {e}")

# 메모 목록 조회
st.markdown("### 메모 목록")

try:
    response = httpx.get(f"{API_BASE}/memos")
    if response.status_code == 200:
        memos = response.json()

        if not memos:
            st.markdown("*아직 메모가 없습니다.*")
        else:
            for memo in reversed(memos):  # 최신 메모를 위에 표시
                with st.container():
                    col1, col2 = st.columns([4, 1])

                    with col1:
                        st.markdown(f"""
                        <div class="memo-card">
                            <p class="memo-content">{memo['content']}</p>
                            <p class="memo-id">ID: {memo['id']}</p>
                        </div>
                        """, unsafe_allow_html=True)

                    with col2:
                        if st.button("삭제", key=f"delete_{memo['id']}", type="secondary"):
                            try:
                                delete_response = httpx.delete(f"{API_BASE}/memos/{memo['id']}")
                                if delete_response.status_code == 200:
                                    st.success("메모가 삭제되었습니다!")
                                    st.rerun()
                                else:
                                    st.error("삭제 중 오류가 발생했습니다.")
                            except Exception as e:
                                st.error(f"삭제 오류: {e}")
    else:
        st.error("메모를 불러올 수 없습니다.")

except Exception as e:
    st.error(f"서버 연결 오류: {e}")

# 하단 정보
st.markdown("---")
st.markdown("*간단 메모리 메모장*")