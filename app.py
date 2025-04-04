
import streamlit as st
from gtts import gTTS
import os
import uuid

st.set_page_config(page_title="Anbu's AI Assistant", page_icon="🧠")

st.title("🎙️ Talk to Anbu's AI Assistant")
user_input = st.text_input("Type something or ask a question:")

def generate_response(text):
    # You can customize or connect to OpenAI API here
    return f"You said: {text}. I'm still learning to reply smarter!"

if st.button("Talk"):
    if user_input:
        response = generate_response(user_input)
        st.success(response)

        # Convert response to speech
        tts = gTTS(response)
        file_name = f"temp_{uuid.uuid4()}.mp3"
        tts.save(file_name)
        audio_file = open(file_name, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        audio_file.close()
        os.remove(file_name)
    else:
        st.warning("Please enter some text.")
