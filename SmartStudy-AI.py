import streamlit as st
import google.generativeai as genai

# ====== API KEY ======
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

# ====== UI ======
st.set_page_config(page_title="SmartStudy AI")

st.title("🎓 SmartStudy AI")
st.write("Trợ lý học tập cá nhân hóa cho học sinh (Gemini)")

# ====== INPUT ======
user_input = st.text_area("Nhập nội dung cần học:")

# ====== XỬ LÝ ======
if st.button("Phân tích"):
    if user_input:
        with st.spinner("Đang xử lý..."):
            try:
                prompt = f"""
Bạn là SmartStudy AI.

Hãy trả lời theo cấu trúc:
1. Giải thích
2. Tóm tắt
3. Câu hỏi trắc nghiệm (có đáp án)
4. Gợi ý học

Nội dung: {user_input}
"""

                response = model.generate_content(prompt)

                result = response.text

                st.success("Kết quả:")
                st.write(result)

            except Exception as e:
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Vui lòng nhập nội dung!")
