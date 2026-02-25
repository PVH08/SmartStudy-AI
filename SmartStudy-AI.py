import streamlit as st
from openai import OpenAI

# ====== API ======
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ====== UI ======
st.set_page_config(page_title="SmartStudy AI")

st.title("🎓 SmartStudy AI")
st.write("Trợ lý học tập cá nhân hóa cho học sinh")

# ====== CHỌN MÔN ======
subject = st.selectbox(
    "Chọn môn học:",
    ["Toán", "Ngữ văn", "Tiếng Anh", "Lịch sử", "Địa lý", "Khác"]
)

# ====== CHỌN ĐỘ KHÓ ======
level = st.selectbox(
    "Mức độ:",
    ["Dễ", "Trung bình", "Khó"]
)

# ====== INPUT ======
user_input = st.text_area("Nhập nội dung cần học:")

# ====== PHÂN TÍCH ======
if st.button("Phân tích"):
    if user_input.strip() != "":
        with st.spinner("Đang xử lý..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": f"""
Bạn là SmartStudy AI.

Môn học: {subject}
Mức độ: {level}

Hãy trả lời theo cấu trúc:
1. Giải thích dễ hiểu
2. Tóm tắt ngắn
3. 3 câu trắc nghiệm (có đáp án)
4. Gợi ý học hiệu quả
5. Lộ trình học ngắn (3 bước)
"""
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                )

                result = response.choices[0].message.content

                st.success("✅ Kết quả:")
                st.write(result)

                # ====== DOWNLOAD ======
                st.download_button(
                    label="📥 Tải kết quả",
                    data=result,
                    file_name="smartstudy.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error("❌ Lỗi hệ thống hoặc API!")
                st.error(e)
    else:
        st.warning("⚠️ Vui lòng nhập nội dung!")

# ====== CHẤM ĐIỂM ======
st.divider()
st.subheader("📝 Tự kiểm tra")

answer = st.text_area("Nhập câu trả lời của bạn:")

if st.button("Chấm điểm"):
    if answer.strip() != "":
        with st.spinner("Đang chấm..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": """
Bạn là giáo viên.

Hãy:
- Chấm điểm trên thang 10
- Nhận xét ngắn gọn
- Gợi ý cải thiện
"""
                        },
                        {
                            "role": "user",
                            "content": answer
                        }
                    ]
                )

                st.success("📊 Đánh giá:")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error("❌ Lỗi khi chấm điểm!")
                st.error(e)
    else:
        st.warning("⚠️ Nhập câu trả lời trước!")
