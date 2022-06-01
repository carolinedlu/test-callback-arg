import streamlit as st

def callback_fxn(my_text_input):
  st.write("here's the val:")
  st.write(my_text_input)

my_form = st.form("my-form")
st.write("this is my form")
my_form.my_text_input = st.text_input("write something")
my_form.form_submit_button(label='submit stuff', on_click=callback_fxn(my_text_input), args=(my_text_input, ))
