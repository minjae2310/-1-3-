import streamlit as st
import random

st.set_page_config(
    page_title="벌칙 룰렛",
    page_icon="🎯",
    layout="centered"
)

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "home"

if "history" not in st.session_state:
    st.session_state.history = []

# 기본 벌칙
default_penalties = [
    "노래 한 소절 부르기",
    "물 한 컵 마시기",
    "애교 하기",
    "팔굽혀펴기 5개",
    "춤 10초 추기",
    "친구 칭찬하기",
    "웃긴 표정 짓기",
    "간식 하나 사주기"
]

# 홈 화면
if st.session_state.page == "home":
    st.title("🎯 벌칙 룰렛")
    st.write("친구들과 재미있게 즐길 수 있는 간단한 벌칙 룰렛입니다!")

    st.markdown("---")

    if st.button("📖 사용 설명 보기", use_container_width=True):
        st.session_state.page = "guide"
        st.rerun()

    if st.button("🎲 바로 시작하기", use_container_width=True):
        st.session_state.page = "roulette"
        st.rerun()

# 설명 페이지
elif st.session_state.page == "guide":
    st.title("📖 사용 설명")

    st.info("""
1. 기본 벌칙이 준비되어 있습니다.
2. 원하는 벌칙을 직접 추가할 수 있습니다.
3. '룰렛 돌리기' 버튼을 누르면 랜덤으로 벌칙이 선택됩니다.
4. 최근 결과는 아래에 기록됩니다.
""")

    if st.button("🏠 메인으로"):
        st.session_state.page = "home"
        st.rerun()

# 룰렛 페이지
elif st.session_state.page == "roulette":
    st.title("🎯 벌칙 룰렛")

    st.subheader("벌칙 목록")

    custom_text = st.text_area(
        "추가할 벌칙 입력 (한 줄에 하나씩)",
        placeholder="예시\n노래 부르기\n춤 추기"
    )

    penalties = default_penalties.copy()

    try:
        if custom_text.strip():
            extra = [
                item.strip()
                for item in custom_text.split("\n")
                if item.strip()
            ]
            penalties.extend(extra)
    except Exception:
        st.warning("벌칙을 불러오는 중 오류가 발생했습니다.")

    st.write(f"총 {len(penalties)}개의 벌칙")

    with st.expander("현재 벌칙 보기"):
        for idx, item in enumerate(penalties, start=1):
            st.write(f"{idx}. {item}")

    st.markdown("---")

    if st.button("🎲 룰렛 돌리기", use_container_width=True):
        try:
            result = random.choice(penalties)

            st.success(f"당첨 벌칙: **{result}**")

            st.session_state.history.insert(0, result)

            if len(st.session_state.history) > 10:
                st.session_state.history = st.session_state.history[:10]

        except Exception:
            st.error("룰렛 실행 중 오류가 발생했습니다.")

    st.markdown("---")

    st.subheader("📝 최근 결과")

    if st.session_state.history:
        for i, item in enumerate(st.session_state.history, start=1):
            st.write(f"{i}. {item}")
    else:
        st.caption("아직 결과가 없습니다.")

    st.markdown("---")

    if st.button("🏠 메인으로 이동"):
        st.session_state.page = "home"
        st.rerun()
