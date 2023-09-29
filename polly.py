from io import BytesIO

import streamlit as st
import pygame
from gtts import gTTS


def play_audio():
    text = st.session_state.entered_text
    mp3_file = BytesIO()
    tts = gTTS(text=text, lang="en", slow=False)
    tts.write_to_fp(mp3_file)
    mp3_file.seek(0)
    sound = pygame.mixer.Sound(mp3_file)
    sound.play()


if __name__ == "__main__":
    st.title("Text to speech")
    pygame.init()
    pygame.mixer.init()
    text = st.text_area("Enter the speech text", on_change=play_audio, key="entered_text")
