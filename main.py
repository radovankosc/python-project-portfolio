import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Radovan Kosc")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam massa sapien, pellentesque et maximus sit amet, laoreet quis nulla. Fusce lacus dolor, iaculis in congue id, auctor non mauris. Mauris eget risus vel nisi aliquet convallis. Donec eu tincidunt nibh. Quisque massa augue, faucibus congue tempor nec, fringilla eget eros. Nullam non maximus nulla. Suspendisse posuere justo at turpis imperdiet gravida.
Nulla gravida tincidunt tortor, non scelerisque velit vulputate in. Nulla sit amet libero ligula. Proin at cursus justo. Vivamus mollis nibh vitae dui venenatis, vitae tincidunt leo semper. Sed urna augue, luctus sit amet metus sed, vestibulum laoreet tortor. Cras sollicitudin imperdiet eros et mattis. Nulla molestie rutrum quam at hendrerit. Mauris quis mauris libero. Maecenas pellentesque fermentum porttitor. Sed sit amet quam maximus, suscipit dolor facilisis, mollis tellus. In commodo justo eu cursus iaculis. Nulla ut sollicitudin nibh, at lacinia magna.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
 """
st.text(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

