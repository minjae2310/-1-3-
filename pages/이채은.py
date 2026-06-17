import streamlit as st
import random
import time

st.set_page_config(
    page_title="교실 벌칙 룰렛",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 교실 벌칙 룰렛")
st.markdown("재미있게 사용하고 서로 배려하는 벌칙을 선택하세요!")

# 기본 벌칙
default_penalties = [
    "노래 한 소절 부르기 🎤",
    "웃긴 표정 하기 😆",
    "팔굽혀펴기 5회 💪",
    "칭찬 3개 말하기 👍",
    "동물 소리 내기 🐶",
    "애교 한 번 하기 😊",
    "박수 치며 자기소개 👏",
    "물 한 컵 마시기 🥤"
]

# 세션 상태 초기화
if "penalties" not in st.session_state:
    st.session_state.penalties = default_penalties.copy()

if "result" not in st.session_state:
    st.session_state.result = ""

st.divider()

# 벌칙 추가
st.subheader("➕ 벌칙 추가")

new_penalty = st.text_input("새 벌칙 입력")

col1, col2 = st.columns(2)

with col1:
    if st.button("추가"):
        text = new_penalty.strip()

        if text:
            if text not in st.session_state.penalties:
                st.session_state.penalties.append(text)
                st.success("벌칙이 추가되었습니다.")
            else:
                st.warning("이미 존재하는 벌칙입니다.")
        else:
            st.warning("벌칙 내용을 입력하세요.")

with col2:
    if st.button("기본값 복원"):
        st.session_state.penalties = default_penalties.copy()
        st.session_state.result = ""
        st.success("기본 벌칙으로 복원되었습니다.")

st.divider()

# 현재 벌칙 목록
st.subheader("📋 현재 벌칙 목록")

if st.session_state.penalties:
    for i, item in enumerate(st.session_state.penalties, start=1):
        st.write(f"{i}. {item}")
else:
    st.info("등록된 벌칙이 없습니다.")

st.divider()

# 벌칙 삭제
st.subheader("🗑️ 벌칙 삭제")

if st.session_state.penalties:
    delete_item = st.selectbox(
        "삭제할 벌칙 선택",
        st.session_state.penalties
    )

    if st.button("선택 벌칙 삭제"):
        try:
            st.session_state.penalties.remove(delete_item)
            st.success("삭제되었습니다.")
        except ValueError:
            st.error("삭제 중 오류가 발생했습니다.")

st.divider()

# 룰렛 영역
st.subheader("🎡 룰렛 돌리기")

display_area = st.empty()

if st.button("룰렛 시작!"):
    if not st.session_state.penalties:
        st.error("벌칙이 하나 이상 필요합니다.")
    else:
        for _ in range(20):
            temp = random.choice(st.session_state.penalties)
            display_area.markdown(
                f"## 🎲 {temp}"
            )
            time.sleep(0.08)

        winner = random.choice(st.session_state.penalties)
        st.session_state.result = winner

        display_area.markdown(
            f"""
            # 🎉 당첨!
            ## {winner}
            """
        )

# 결과 표시
if st.session_state.result:
    st.divider()
    st.subheader("🏆 최종 결과")
    st.success(st.session_state.result)
