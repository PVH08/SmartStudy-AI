import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="SmartStudy AI")

st.title("🎓 SmartStudy AI")
st.write("Trợ lý học tập cá nhân hóa cho học sinh")

# ====== PHÂN TÍCH ======
user_input = st.text_area("Nhập nội dung cần học:")

if st.button("Phân tích"):
    if user_input:
        with st.spinner("Đang xử lý..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": """Bạn là SmartStudy AI.

Hãy trả lời theo cấu trúc:
1. Giải thích
2. Tóm tắt
3. Câu hỏi trắc nghiệm (có đáp án)
4. Gợi ý học
"""
                        },
                        {"role": "user", "content": user_input}
                    ]
                )

                result = response.choices[0].message.content
                st.success("Kết quả:")
                st.write(result)

            except Exception as e:
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Vui lòng nhập nội dung!")

# ====== TẠO BÀI TẬP ======
st.divider()
st.subheader("📝 Tạo bài tập")

exercise_input = st.text_area("Nhập nội dung để tạo bài tập:")

if st.button("Tạo bài tập"):
    if exercise_input:
        with st.spinner("Đang tạo bài tập..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": """Bạn là giáo viên.

Hãy tạo:
- 5 câu trắc nghiệm
- 2 câu tự luận
- Có đáp án ở cuối
"""
                        },
                        {"role": "user", "content": exercise_input}
                    ]
                )

                exercise = response.choices[0].message.content

                st.success("Bài tập:")
                st.write(exercise)

                # ====== NÚT TẢI ======
                st.download_button(
                    label="📥 Tải bài tập",
                    data=exercise,
                    file_name="baitap.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Vui lòng nhập nội dung!")
