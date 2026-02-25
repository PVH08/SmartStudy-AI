import streamlit as st
import google.generativeai as genai

# Cấu hình API KEY
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("❌ Chưa cấu hình GEMINI_API_KEY trong secrets.toml")
    st.stop()

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.set_page_config(page_title="SmartStudy AI", page_icon="🎓")
st.title("🎓 SmartStudy AI")
st.caption("Trợ lý học tập cá nhân hóa cho học sinh")

# Input
user_input = st.text_area("📚 Nhập nội dung cần học:", height=150)

# Button
if st.button("🚀 Phân tích"):
    if not user_input.strip():
        st.warning("⚠️ Vui lòng nhập nội dung!")
    else:
        with st.spinner("⏳ Đang xử lý..."):
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

                # 🔥 FIX lỗi Gemini trả về None
                if not response.text:
                    st.error("❌ Không nhận được phản hồi từ AI")
                else:
                    st.success("✅ Kết quả:")
                    st.markdown(response.text)

            except Exception as e:
                st.error(f"❌ Lỗi hệ thống: {e}")
