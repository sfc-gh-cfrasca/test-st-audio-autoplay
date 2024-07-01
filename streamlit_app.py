import streamlit as st

#placeholder = st.empty()
#placeholder.audio('timer_sound.mp3', format="audio/mpeg", autoplay=True)

#if st.button("click me"):
#   placeholder.audio('timer_sound.mp3', format="audio/mpeg", autoplay=True)

st.button("click me first")
st.text("audio should autoplay after you click the button")
st.audio('timer_sound.mp3', format="audio/mpeg", autoplay=True)
