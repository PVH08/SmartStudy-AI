import streamlit as st
import google.generativeai as genai

# Lấy API key từ secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Chọn model
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="SmartStudy AI")

st.title("🎓 SmartStudy AI")
st.write("Trợ lý học tập cá nhân hóa cho học sinh")

user_input = st.text_area("Nhập nội dung cần học:")

if st.button("Phân tích"):
    if user_input.strip():
        with st.spinner("Đang xử lý..."):
            try:
                prompt = f"""
Bạn là SmartStudy AI.

Hãy trả lời rõ ràng, dễ hiểu, trình bày đẹp.

Cấu trúc:
1. Giải thích
2. Tóm tắt
3. 3 câu trắc nghiệm (có đáp án)
4. Gợi ý học

Nội dung: {user_input}
"""

                response = model.generate_content(prompt)

                st.success("Kết quả:")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Vui lòng nhập nội dung!")

