import streamlit as st
import pandas

# Make all object in page full page mode
st.set_page_config(layout='wide')
# Create two perpendicularly columns
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title('Yusif Osmanov')
    content = (
        """
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        There is some important information about me and my life, please read this inforation if you want to know who am i.
        """
        'Thank you for your attentions!')
    st.info(content)

st.write('Below you can find some of the apps i have built in Python. Feel free to contact me!')

# Method for reading csv files
df = pandas.read_csv('data.csv', sep=';')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Separate title by 2 parts first 10 on left second 10 on the right, and add all content with columns to our portfolio site
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source code]({row['url']})")
