import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

st.set_page_config(page_title="SmartStudy AI")

st.title("🎓 SmartStudy AI")
st.write("Trợ lý học tập cá nhân hóa cho học sinh")

user_input = st.text_area("Nhập nội dung cần học:")

if st.button("Phân tích"):
    if user_input:
        with st.spinner("Đang xử lý..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": """
Bạn là SmartStudy AI.

Hãy trả lời theo cấu trúc:
1. Giải thích
2. Tóm tắt
3. Câu hỏi trắc nghiệm (có đáp án)
4. Gợi ý học
"""},

                    {"role": "user", "content": user_input}
                ]
            )

            result = response.choices[0].message.content
            st.write(result)