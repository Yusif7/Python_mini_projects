import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key='email_form'):
    user_email = st.text_input('Enter your mail...')
    user_message = st.text_area('Enter your message...')

    message = f"""\
Subject:New email from {user_email} 
    
From:{user_email}
{user_message}
"""
    submit = st.form_submit_button('Submit')
    if submit:
        send_email(message)
        st.info('Your mail was sent successfully!')
