import streamlit as st
import requests
st.title("1 : HTTP Rest")
st.title("User Profile Microservice by Fraz")

user_id = st.text_input("Enter User ID:")
if st.button("Get User Profile"):
    response = requests.get(f'http://127.0.0.1:5000/user/{user_id}')
    if response.status_code == 200:
        user_profile = response.json()
        st.write("Username:", user_profile["username"])
        st.write("Email:", user_profile["email"])
    else:
        st.write("User not found")
