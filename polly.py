import streamlit as st
import base64
from gtts import gTTS


if __name__ == "__main__":
    st.title("Text to speech")
    text = st.text_area("Enter the speech text", key="entered_text")#on_change=play_converted_speech, key="entered_text")
    if text:
        text = st.session_state.entered_text
        speech = next(gTTS(text=text, lang="en", slow=False).stream())
        audio_base64 = base64.b64encode(speech).decode('utf-8')
        audio_tag = f'<audio autoplay="true" src="data:audio/wav;base64,{audio_base64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)


