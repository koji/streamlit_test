import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('layout')

# add sidebar
st.sidebar.write('interactive widgets in sidebar')

selectbox_items = ['apple', 'banana', 'orange']
option = st.sidebar.selectbox(
    'which fruit do you like?',
    selectbox_items,
)

'you like', option, ', right?'

# input textbox
my_input = st.sidebar.text_input('tell me your name')
'hello', my_input, '!!!'


# slider
condition = st.sidebar.slider('How are you today?', 0, 100, 50)

'You are', condition, '%, today lol'


# two columns
st.write('two-column layout')
left_column, right_column = st.beta_columns(2)

is_button_pressed = left_column.button('click me')

if is_button_pressed:
    right_column.write('you pressed the button!')


# expander

expander = st.beta_expander('Do you like python?')
expander.write('yes!')


# progressbar
st.write('progressbar')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(i+1)
    time.sleep(0.1)
    bar.progress(i+1)

st.write('Done!!')
