import streamlit as st

st.button("Click me!")
st.write("Audio should autoplay after you click the button")
st.caption("Since you need to click somewhere on the page before the browser will auto-play the audio clip")
st.audio('timer_sound.mp3', format="audio/mpeg", autoplay=True)
