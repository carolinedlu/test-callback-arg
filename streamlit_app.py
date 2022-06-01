import streamlit as st

def callback_fxn():
  st.write("here's the val:")
  if my_text_input:
    st.write(my_text_input)

my_form = st.form("my-form")
st.write("this is my form")
my_text_input = my_form.text_input("write something")
my_form.form_submit_button(label='submit stuff', on_click=callback_fxn)
