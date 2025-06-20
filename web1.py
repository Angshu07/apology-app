from PIL import Image
import streamlit as st

# Page config
st.set_page_config(page_title="Sorry Tela ❤️", page_icon="🌹", layout="centered")

# Session state to manage navigation
if 'step' not in st.session_state:
    st.session_state.step = 1

# Rose-themed background with animation
bg_css = """
<style>
body {
    background-image: url("https://i.pinimg.com/originals/3b/67/8b/3b678b8d6a1cd6e5c2a7d26c302f3f5e.gif");
    background-size: cover;
    background-attachment: fixed;
}
.boxer {
    background-color: black;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin-top: 20px;
    font-weight: bold;
    font-size: 18px;
}
</style>
"""
st.markdown(bg_css, unsafe_allow_html=True)

# STEP 1 - Welcome Page
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align: center; color: #ff3399;'>Welcome to my heart, not just a webpage.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Thikache suru kora jak </h3>", unsafe_allow_html=True)
    st.markdown("<div class='boxer'> Thikache tep to amake dekhi ,umm ha madam tomakei bolchi tepo,ei lekha tar niche badike</div>", unsafe_allow_html=True)
    if st.button("yes,tepo abar amake_tepo-(double tap please)"):
        st.session_state.step = 2

# STEP 2 - Show photo and text
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center;'>Hi Tollygonger Tela</h2>", unsafe_allow_html=True)
    image = Image.open("tusai_photo.jpg")  # Use your own photo here
    st.image(image, caption="You're truly special for me ...btw u're looking damn gorgeous ..janish to tor choto smile tate etotai mughdho....baki bojanor moto i've no wrods ..it's beautiful ", use_column_width=True)
    st.markdown("#### Ekta kane kane kotha bolbo... O tui to sunte parbina - dekhte to parbi 😉")
    if st.button("Aree bhalo kore tep to amake(double tap please )"):
        st.session_state.step = 3

# STEP 3 - Motivational Compliments
elif st.session_state.step == 3:
    st.markdown("### 🌸I just want to say --")
    st.success("""
Being with you makes me want to be a better person — not out of pressure, but out of love. You've taught me how to balance love with life — 
our boundaries, our goals, our imperfections, and even the hard moments. I truly don’t want to lose you… not for anything.  
 You're one of the best decisions I’ve ever made,litrally I’m very proud to have you & felt so much lucky becuz of after all of this u accept me.Honestly from bottom of my heart i'm really really- truly sorry Tusai ❤️ ...come to me-baby....i missed you ,missed u so much..
    """)
    st.markdown("#### Ekta kotha bolbo — jante chas to tep to niche 👇")
    if st.button(" jore tep to amake,ekbari tippi nahole lege jabe hehe(double tap please)"):
        st.session_state.step = 4

# STEP 4 - Moner Kotha
elif st.session_state.step == 4:
    st.markdown("### 💌 just ektu kotha  ---")
    st.info("""
First of all I'm really sorry... seriously mon theke bolchi re😞😞...amr khub kharap lagche..tokhon orom bhabe react jemon kora uchit hoyni...temoni toke orom sonano bhulbhal senseless jinisgulo Amar bola uchit hoyni ..... ami sottie bolchi.....abhiman kore achis amar opore ami jani... onekkichui bolbi it's ok..becuz ami dosh korechi bolbi. But extra reactions er jonne I'm really really sorry...amar ogulo bola uchit hoyni(ami tor opor etokhon dhore rag korte parina 3din hoye gelo kotha bolchisna please i'm sorry)..ami tor sathe amader moddhe je choto bisoy ta jhamela hoyehche seta niye ami call e kotha bolte chai openly toke bolte chai....r tor kotha sunte chai......amar kharap legeche je ekta choto  bisoy etota boro houwar kotha na but hoyeche tai ektu over react kore feli ...so ami tor sathe kotha bolte chai ja hoyehce sob kichur jonne sorry re but ami kotha bolbo tor sathe call e please.....
.. please khoma kore de ar amar sathe jeta mainly bola uchit seta niye kotha boli.....raag ta side e rekhe ayna amar kache....amar ekta choto prochestaa i don't know tor  pochonodo hbe ki hbe na ami janina 😞👉🏻👈🏻 ...but I'm sorry 😭
    """)
    if st.button(" last time tep akbar amake please jore tippi amake 💘 (double tap please)"):
        st.session_state.step = 5

# STEP 5 - Final Romantic Message
elif st.session_state.step == 5:
    st.markdown("<h2 style='text-align: center; color:#cc0052;'>I love u Tela 😭<br>I don't wanna lose u konobhabei na <br>I'm really really really sorry,ektu kotha bolbo tor sathe , please ........................tor Jontu.</h2>", unsafe_allow_html=True)

