from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Collins Micheal Webdevelopment", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
# Use LocaL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jjsrh4we.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
st.subheader("Hi I am collins micheal :wave:")
st.title("A web developer from nigeria")
st.write ("I am a student with knowledge of web developing and desiging. also teaches some course on cybersecurities")
st.write ("Passionate about creating a website that will be efficient for human use in the nearest future")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            i'm a web developer
            - A web designer
            - aslo educates people on cybersecurities
            """
        )
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
            
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
        with text_column:
            st.subheader("Developing is fun!")
            st.write(
                """
                Developing is fun with Collins Micheal Webdevelopment
                """
            )
            st.markdown("Looking forward to work for you!")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("My Aim")
        st.write(
            """
            Always Available For you
            """
        )
        st.markdown("Phone Number: 09130448907. you can alternatively get in touch with me by sending me a mail down below")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/alaricmartins584@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">    
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()    

        
        