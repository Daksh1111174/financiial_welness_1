import streamlit as st
from services.auth import init_db, register_user, login_user

st.set_page_config(page_title="Financial Wellness Buddy", layout="wide")

# Glass UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color: white;
}
</style>
""", unsafe_allow_html=True)

init_db()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔐 Login")

    option = st.selectbox("Select", ["Login", "Register"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Register":
        if st.button("Register"):
            if register_user(username, password):
                st.success("Registered Successfully")
            else:
                st.error("User Exists")

    if option == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Credentials")

else:
    st.title("💰 Financial Wellness Buddy")
    st.sidebar.success("Logged In")
    st.write("Use sidebar to navigate pages.")
