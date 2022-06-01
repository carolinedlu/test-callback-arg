import streamlit as st

def callback_fxn(my_text_input):
  st.write("here's the val:")
  st.write(my_text_input)

with st.form():
  st.write("this is my form")
  my_text_input = st.text_input("write something")
  submit = st.form_submit_button(label='submit stuff', on_click=callback_fxn(), args=(my_text_input, ))
