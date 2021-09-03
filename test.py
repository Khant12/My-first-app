import streamlit as st
import numpy as np
import pandas as pd
import time,datetime

now = datetime.date.today()

st.write(f"Today is {now}")


st.title('Am I Human Too?')
from PIL import Image
image = Image.open('./photo/images.jpeg')

st.image(image, caption= '')



def greeting():

    if st.button('Do you know me?'):
        st.write('Haha.. let\'t find out..（‐＾▽＾‐）')
    else:
        st.write('Hello Stranger \﻿ (•◡•) /')
greeting()


st.warning('This app is just for fun!')
def information():


    name = st.text_input('Enter your name')
    if name != "":
        st.write('Ok',name,'....Let\'s move to next quizz..')

    
    options = st.slider('Can you guees my age?', 0, 130, 25)
    if options == 16:
        st.write('Yes you are brillant...How did you know my age?')
    elif options > 16:
        st.write('Try think...I am a little bit younger..')
    elif options < 16:
        st.write('Do you think I am a kid!..')
    
information()



options = st.multiselect(
     'What are my favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue','Black', 'DarkBlue'])

if "Blue" in options:
    st.write('I also like blue..I mean dark blue and sky blue')
elif "Yellow" in options:
    st.write('I don\'t like too much yellow')
elif "Red" in options:
    st.write("This is my second favourite one!.. ;>")
elif "DarkBlue" in options or "Black" in options:
    st.write("Yay....This is my favorite one ᕙ(`▿´)ᕗ")
elif "Green" in options:
    st.write('I don\'t like green but I like dark green ')



submitted = st.button("Submit")
if submitted:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    
    with st.spinner('Wait for it...'):
        time.sleep(5)
        st.balloons()
        st.success('Yay..See you next time')
        


