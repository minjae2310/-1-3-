import streamlit as st
import json
import os

USERS_FILE = "users.json"

st.set_page_config(
    page_title="벌칙 룰렛",
    page_icon="🎯",
    layout="centered"
)


def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def register(username, password):
    users = load_users()

    if username in users:
        return False

    users[username] = password
    save_users(users)
    return True


def login(username, password):
    users = load_users()
    return username in users and users[username] == password


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


if not st.session_state.logged_in:

    st.title("🎯 벌칙 룰렛")

    tab1, tab2 = st.tabs(["로그인", "회원가입"])

    with tab1:
        st.subheader("로그인")

        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")

        if st.button("로그인"):
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호가 올바르지 않습니다.")

    with tab2:
        st.subheader("회원가입")

        new_username = st.text_input("새 아이디")
        new_password = st.text_input("새 비밀번호", type="password")

        if st.button("회원가입"):
            if register(new_username, new_password):
                st.success("회원가입이 완료되었습니다.")
            else:
                st.error("이미 존재하는 아이디입니다.")

else:
    st.title("🎯 벌칙 룰렛")
    st.success(f"{st.session_state.username}님 환영합니다!")

    if st.button("로그아웃"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
