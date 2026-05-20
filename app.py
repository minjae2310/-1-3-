import streamlit as st

# 페이지 설정
st.set_page_config(page_title="스케줄 관리", page_icon="📅")

# 제목
st.title("📅 스케줄 관리")

# 세션 상태 초기화
if "schedules" not in st.session_state:
    st.session_state.schedules = []

# 입력창
schedule = st.text_input("할 일을 입력하세요")

# 추가 버튼
if st.button("추가"):
    if schedule:
        st.session_state.schedules.append(schedule)
        st.success("추가되었습니다!")

# 스케줄 목록 출력
st.subheader("할 일 목록")

if st.session_state.schedules:
    for i, item in enumerate(st.session_state.schedules, start=1):
        st.write(f"{i}. {item}")
else:
    st.write("등록된 스케줄이 없습니다.")
