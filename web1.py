import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="I'm Sorry, Tusai ❤️", layout="centered")

# ---- BACKGROUND STYLE ----
page_bg = """
<style>
body {
    background: linear-gradient(135deg, #ffe6e6, #ffe0f0, #e6f7ff);
    font-family: 'Segoe UI', sans-serif;
}
.big-title {
    font-size: 45px;
    color: #ff4d6d;
    text-align: center;
    margin-top: 40px;
}
.sub-text {
    font-size: 20px;
    color: #555;
    text-align: center;
    margin-bottom: 10px;
}
.button-style {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}
.stButton > button {
    background-color: #ff4d6d;
    color: white;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 12px;
    border: none;
    transition: 0.3s;
}
.stButton > button:hover {
    background-color: #e60039;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- CONTENT ----
st.markdown('<div class="big-title">Hey Tusai... 🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">This is not just a webpage...</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">It’s a piece of my heart built just for you.</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">I know I’ve hurt you, and I’m truly sorry...</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">But my love for you has never faded, not even for a second.</div>', unsafe_allow_html=True)

# Optional image (uncomment and use your own image path if needed)
image = Image.open("tusai.jpg")
 st.image(image, caption="For You ❤️", use_column_width=True)

# ---- FINAL MESSAGE BUTTON ----
if st.button("Tap to See My Final Words 💌"):
    st.markdown("---")
    st.markdown('<div class="sub-text"><b>Tusai, amar jibon e tui ekta upohar...</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Jodi vul kori thaki, khoma kore de...</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Karon amar bhalobasha aaj o toke niyei...</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">I love you. Forever. Unconditionally. ❤️</div>', unsafe_allow_html=True)
