import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

def translate_text(text, destination):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=destination)
    return translation.text

def convert_to_audio(text, language):
    tts = gTTS(text, lang=language)
    audio_file = 'translation_audio.mp3'
    tts.save(audio_file)
    return audio_file

# Streamlit app
st.title("Language Translator")

# Input text
input_text = st.text_area("Enter English text:")

# Translation language selection
destination_language = st.selectbox("Select Destination Language:", ['Hindi', 'Telugu'])

# Translate and generate audio
if st.button("Translate"):
    if destination_language == 'Hindi':
        translated_text = translate_text(input_text, 'hi')
        audio_file = convert_to_audio(translated_text, 'hi')
    else:
        translated_text = translate_text(input_text, 'te')
        audio_file = convert_to_audio(translated_text, 'te')

    st.success(f"Translated Text ({destination_language}): {translated_text}")

    # Play audio
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')

    # Remove audio file
    os.remove(audio_file)
