import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Radovan Kosc")
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam massa sapien, pellentesque et maximus sit amet, laoreet quis nulla. Fusce lacus dolor, iaculis in congue id, auctor non mauris. Mauris eget risus vel nisi aliquet convallis. Donec eu tincidunt nibh. Quisque massa augue, faucibus congue tempor nec, fringilla eget eros. Nullam non maximus nulla. Suspendisse posuere justo at turpis imperdiet gravida.
Nulla gravida tincidunt tortor, non scelerisque velit vulputate in. Nulla sit amet libero ligula. Proin at cursus justo. Vivamus mollis nibh vitae dui venenatis, vitae tincidunt leo semper. Sed urna augue, luctus sit amet metus sed, vestibulum laoreet tortor. Cras sollicitudin imperdiet eros et mattis. Nulla molestie rutrum quam at hendrerit. Mauris quis mauris libero. Maecenas pellentesque fermentum porttitor. Sed sit amet quam maximus, suscipit dolor facilisis, mollis tellus. In commodo justo eu cursus iaculis. Nulla ut sollicitudin nibh, at lacinia magna.
    """
    st.info(content)