import streamlit as st
import time
import random

st.set_page_config(page_title="For You ❤️", layout="centered")

# ---------- PASSWORD ----------
def check_password():
    def password_entered():
        if st.session_state["password"] == "100124":
            st.session_state["authenticated"] = True
        else:
            st.session_state["authenticated"] = False

    if "authenticated" not in st.session_state:
        st.text_input("🔐 Enter the secret password 💖", type="password", key="password", on_change=password_entered)
        return False
    elif not st.session_state["authenticated"]:
        st.text_input("🔐 Enter the secret password 💖", type="password", key="password", on_change=password_entered)
        st.error("Wrong password 🥺")
        return False
    else:
        return True

if not check_password():
    st.stop()

# ---------- PINK UI + HEARTS ----------
st.markdown("""
<style>
body {
    background-color: #fff0f5;
}
.stButton>button {
    background-color: #ff4b6e;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.center {
    text-align: center;
}

/* Floating hearts */
@keyframes float {
  0% { transform: translateY(0px); opacity: 1; }
  100% { transform: translateY(-800px); opacity: 0; }
}

.heart {
  position: fixed;
  bottom: -50px;
  color: #ff4b6e;
  font-size: 24px;
  animation: float 5s linear infinite;
}
</style>

<div class="heart" style="left:10%;">❤️</div>
<div class="heart" style="left:20%; animation-duration:6s;">❤️</div>
<div class="heart" style="left:30%; animation-duration:7s;">❤️</div>
<div class="heart" style="left:40%; animation-duration:5s;">❤️</div>
<div class="heart" style="left:50%; animation-duration:6s;">❤️</div>
<div class="heart" style="left:60%; animation-duration:7s;">❤️</div>
<div class="heart" style="left:70%; animation-duration:5s;">❤️</div>
<div class="heart" style="left:80%; animation-duration:6s;">❤️</div>
<div class="heart" style="left:90%; animation-duration:7s;">❤️</div>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 class='center'>💖 Hey You 💖</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='center'>Only you were meant to see this 🥺</h4>", unsafe_allow_html=True)

# ---------- STEP CONTROL ----------
if "step" not in st.session_state:
    st.session_state.step = 0

# ---------- STEP 1 ----------
if st.session_state.step == 0:
    if st.button("Click Me ❤️"):
        st.session_state.step = 1

# ---------- STEP 2 ----------
elif st.session_state.step == 1:
    st.markdown("<h3 class='center'>Wait... don't rush 🥺</h3>", unsafe_allow_html=True)
    time.sleep(1.5)
    st.markdown("<h3 class='center'>I just wanted to say something...</h3>", unsafe_allow_html=True)
    time.sleep(1.5)

    if st.button("Okay, tell me 💌"):
        st.session_state.step = 2

# ---------- STEP 3 (Typing + Secret) ----------
elif st.session_state.step == 2:
    message = "You make my life so much better just by being in it 💖"

    placeholder = st.empty()
    typed = ""

    for char in message:
        typed += char
        placeholder.markdown(f"<h3 class='center'>{typed}</h3>", unsafe_allow_html=True)
        time.sleep(0.05)

    if st.button("Aww 🥺"):
        st.session_state.step = 3

    if st.button("🤫 Don't click this"):
        st.session_state.step = 99

# ---------- STEP 4 ----------
elif st.session_state.step == 3:
    st.markdown("<h3 class='center'>Do you know why I love you? 💕</h3>", unsafe_allow_html=True)

    reasons = [
        "Because your smile makes everything better 😊",
        "Because you understand me like no one else 🥹",
        "Because you make me laugh even on bad days 😂",
        "Because you are the best part of my life 💖",
        "Because you're YOU ❤️"
    ]

    if st.button("Tell me why 😳"):
        st.success(random.choice(reasons))

    if st.button("Next 👉"):
        st.session_state.step = 4

# ---------- STEP 5 (IMAGES SAME AS BEFORE) ----------
elif st.session_state.step == 4:
    st.markdown("<h3 class='center'>Our Memories 📸</h3>", unsafe_allow_html=True)

    # 👉 SAME SIMPLE FORMAT
    st.image("photo1.jpg")
    st.image("photo2.jpg")
    st.image("photo3.jpg")

    st.markdown("<p class='center'>Every moment with you means everything 💕</p>", unsafe_allow_html=True)

    if st.button("One last thing... 💖"):
        st.session_state.step = 5

# ---------- STEP 6 (SMART NO BUTTON) ----------
elif st.session_state.step == 5:
    st.markdown("<h1 class='center'>Will you always stay with me? 💍💖</h1>", unsafe_allow_html=True)

    if st.button("YES ❤️"):
        st.balloons()
        st.success("I knew it 😭💖 You make me the happiest person!")

    if "no_attempts" not in st.session_state:
        st.session_state.no_attempts = 0

    cols = st.columns(10)
    pos = random.randint(0, 9)

    with cols[pos]:
        if st.button("NO 😡"):
            st.session_state.no_attempts += 1
            st.warning("😤 Wrong choice!")

    if st.session_state.no_attempts == 2:
        st.info("😏 Why are you even trying this?")
    elif st.session_state.no_attempts == 4:
        st.info("😂 Just press YES already!")
    elif st.session_state.no_attempts > 5:
        st.error("NO button disabled. Only love allowed 💖")

# ---------- SECRET PAGE ----------
elif st.session_state.step == 99:
    st.markdown("<h1 class='center'>💌 A Secret Just For You 💌</h1>", unsafe_allow_html=True)

    st.write("If you're here... it means you're really special to me 💖")
    time.sleep(1)

    st.write("I don't say this often but...")
    time.sleep(1)

    st.write("I love you. More than I can explain. 🥺❤️")

    if st.button("Go back 💕"):
        st.session_state.step = 3