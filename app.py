import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("MY LANGUAGE")
input_test = st.text_input("provide your text input here", 'Hello I am Masroor')


button_clicked = st.button("Click to get Language")
if button_clicked:
	st.text("This Language is: "+Lrdetect_Model.predict([input_test]))
