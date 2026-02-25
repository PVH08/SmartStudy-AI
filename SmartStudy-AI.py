import streamlit as st
import requests

st.set_page_config(page_title="SmartStudy AI")

st.title("🎓 SmartStudy AI (Free Version)")
st.write("Trợ lý học tập miễn phí 100%")

user_input = st.text_area("Nhập nội dung cần học:")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

def ask_ai(prompt):
    response = requests.post(API_URL, json={"inputs": prompt})
    result = response.json()

    if isinstance(result, list):
        return result[0]["generated_text"]
    return "Lỗi AI, thử lại sau!"

if st.button("Phân tích"):
    if user_input:
        with st.spinner("Đang xử lý..."):

            prompt = f"""
Bạn là SmartStudy AI.

Hãy trả lời theo cấu trúc:
1. Giải thích dễ hiểu
2. Tóm tắt ngắn
3. 3 câu trắc nghiệm (có đáp án)
4. Gợi ý cách học

Nội dung: {user_input}
"""

            result = ask_ai(prompt)

            st.write(result)
