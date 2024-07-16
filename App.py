from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Website for Emoji - https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage",page_icon=":ninja:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

# --------- Loading assets

lottie_coding=load_lottieurl("https://lottie.host/d1749d0c-d3df-4d44-95ff-2c878401d479/UrdXpEL7jp.json")
img_lottie_animation=Image.open("D:\Study,Courses\Python 100 days of code\My-website-using-Streamlit\images/thumbnail1.png")


#------Header Section--------
with st.container():
    st.subheader("Hi,I am Vipul :ninja:")
    st.title(" Python Developer From Pune,India")
    st.write("I am a budding coder diving deep into the world of Python and exploring its vast potential.")
    st.write("[Learn More > ](https://github.com/vipulsharma17)")


#------what i do-------------
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
                - I create content for YouTube, featuring fun vlogs and occasionally insightful videos.
                - I am currently undertaking a 100-day code challenge and sharing my progress on Twitter.
                - I document my coding journey and practice on GitHub, showcasing my growth and projects.

                If this sounds interesting to you, consider subscribing and turning on the notifications, so you dont miss any content.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@VipulSharma07)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# ---- PROJECTS ----
        
with st.container():
    st.write("---")
    st.header("My Vlogs")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("A Day in my life")
        st.write(
            """
            - One of those videos where i show that i can code lol
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/3BYaPkiw27I?feature=shared)")


# ---- CONTACT ----
        
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/vipulsharmaa07@gmail.com" method="POST">
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