import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="리뷰 작성 앱",
    page_icon="⭐",
    layout="wide"
)

st.title("⭐ 리뷰 작성 & 관리 앱")
st.caption("상품, 서비스, 맛집, 영화 등 다양한 리뷰를 기록해보세요.")

# 세션 상태 초기화
if "reviews" not in st.session_state:
    st.session_state.reviews = []

# 사이드바
st.sidebar.header("📊 요약 정보")

review_count = len(st.session_state.reviews)

if review_count > 0:
    avg_rating = round(
        sum(r["별점"] for r in st.session_state.reviews) / review_count,
        2
    )
else:
    avg_rating = 0

st.sidebar.metric("총 리뷰 수", review_count)
st.sidebar.metric("평균 별점", avg_rating)

tab1, tab2, tab3 = st.tabs([
    "✍ 리뷰 작성",
    "📋 리뷰 목록",
    "📈 통계"
])

# -------------------------
# 리뷰 작성
# -------------------------
with tab1:
    st.subheader("리뷰 작성")

    with st.form("review_form"):

        target = st.text_input(
            "리뷰 대상",
            placeholder="예: 스타벅스, 아이폰 17, 범죄도시"
        )

        category = st.selectbox(
            "카테고리",
            [
                "맛집",
                "카페",
                "상품",
                "서비스",
                "영화",
                "도서",
                "기타"
            ]
        )

        rating = st.slider(
            "별점",
            min_value=1,
            max_value=5,
            value=5
        )

        review_text = st.text_area(
            "리뷰 내용",
            placeholder="리뷰를 작성해주세요."
        )

        submitted = st.form_submit_button("리뷰 저장")

        if submitted:
            try:
                if not target.strip():
                    st.error("리뷰 대상을 입력해주세요.")
                elif not review_text.strip():
                    st.error("리뷰 내용을 입력해주세요.")
                else:
                    st.session_state.reviews.append(
                        {
                            "작성일시": datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S"
                            ),
                            "카테고리": category,
                            "리뷰대상": target,
                            "별점": rating,
                            "리뷰내용": review_text
                        }
                    )

                    st.success("리뷰가 저장되었습니다.")
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")

# -------------------------
# 리뷰 목록
# -------------------------
with tab2:
    st.subheader("리뷰 목록")

    if not st.session_state.reviews:
        st.info("작성된 리뷰가 없습니다.")
    else:
        df = pd.DataFrame(st.session_state.reviews)

        st.dataframe(
            df.iloc[::-1],
            use_container_width=True
        )

        csv = df.to_csv(
            index=False,
            encoding="utf-8-sig"
        ).encode("utf-8-sig")

        st.download_button(
            label="📥 CSV 다운로드",
            data=csv,
            file_name="reviews.csv",
            mime="text/csv"
        )

# -------------------------
# 통계
# -------------------------
with tab3:
    st.subheader("리뷰 통계")

    if not st.session_state.reviews:
        st.info("통계를 표시할 리뷰가 없습니다.")
    else:
        df = pd.DataFrame(st.session_state.reviews)

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "평균 별점",
                round(df["별점"].mean(), 2)
            )

        with col2:
            st.metric(
                "총 리뷰 수",
                len(df)
            )

        st.markdown("### 카테고리별 리뷰 수")

        category_count = (
            df["카테고리"]
            .value_counts()
            .reset_index()
        )

        category_count.columns = [
            "카테고리",
            "리뷰 수"
        ]

        st.bar_chart(
            category_count.set_index("카테고리")
        )

# 하단 안내
st.divider()
st.caption(
    "작성된 데이터는 현재 세션 동안만 유지됩니다."
)
