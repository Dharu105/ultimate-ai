# app.py

import streamlit as st
import tempfile
import base64
from agents.chat import chat_response
from agents.pdf import pdf_qa
from agents.image import image_recognition

# PAGE CONFIG
st.set_page_config(
    page_title="Ultimate AI",
    layout="wide"
)

# LOAD CSS
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- LOGO ---------------- #

with open("assets/logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""
    <div class="logo-wrapper">
        <img src="data:image/png;base64,{encoded}">
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">
        Ultimate AI
    </div>

    <div class="purple-line"></div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="mode-title">
        Select Mode
    </div>
    """, unsafe_allow_html=True)

    mode = st.radio(
        "",
        [
            "💬 Chatbot",
            "📄 PDF Search",
            "🖼️ Image Recognition"
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # THINK
    st.markdown("""
    <div class="feature-card think-card">
        <div class="card-head">✨ Think</div>
        <div class="card-sub">Understand deeply</div>
    </div>
    """, unsafe_allow_html=True)

    # ASK
    st.markdown("""
    <div class="feature-card ask-card">
        <div class="card-head">❓ Ask</div>
        <div class="card-sub">Ask anything</div>
    </div>
    """, unsafe_allow_html=True)

    # SOLVE
    st.markdown("""
    <div class="feature-card solve-card">
        <div class="card-head">⚡ Solve</div>
        <div class="card-sub">Get solutions</div>
    </div>
    """, unsafe_allow_html=True)

    # EVOLVE
    st.markdown("""
    <div class="feature-card evolve-card">
        <div class="card-head">🚀 Evolve</div>
        <div class="card-sub">Grow every day</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MAIN CENTER ---------------- #

st.markdown("""
<div class="main-center">

<h1>
👋 Hello! How can I help you today?
</h1>

<p>
Ask me anything, upload a PDF or image,
and let's get started.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- CHATBOT ---------------- #

if mode == "💬 Chatbot":

    user_input = st.chat_input(
        "Ask anything..."
    )

    if user_input:

        with st.chat_message("user"):
            st.write(user_input)

        response = chat_response(user_input)

        with st.chat_message("assistant"):
            st.write(response)

# ---------------- PDF SEARCH ---------------- #

elif mode == "📄 PDF Search":

    pdf_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf_file:

        question = st.text_input(
            "Ask question from PDF"
        )

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(pdf_file.read())

            temp_pdf = tmp.name

        if question:

            answer = pdf_qa(
                temp_pdf,
                question
            )

            st.success(answer)

# ---------------- IMAGE RECOGNITION ---------------- #

elif mode == "🖼️ Image Recognition":

    image_file = st.file_uploader(
        "Upload Image",
        type=["png","jpg","jpeg"]
    )

    if image_file:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ) as tmp:

            tmp.write(image_file.read())

            temp_image = tmp.name

        st.image(image_file)

        result = image_recognition(temp_image)

        st.write(result)