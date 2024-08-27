import streamlit as st
import main

api_key = "redacted"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
main.get_picture(url)
description = main.get_description(url)
header = main.get_title(url)

st.title(header)
st.image("image.jpg")
st.write(description)


