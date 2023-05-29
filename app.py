import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('proj_nb.pkl', 'rb')) 

def predict_note_authentication(N,P,K,temperature,humidity,ph,rainfall):
  output= model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
  
    if prediction==['apple']:
        output='Apple'
    if prediction==['banana']:
        output='Banana'
    if prediction==['blackgram']:
        output='Blackgram'
    if prediction==['chickpea']:
        output='chickpea'
    if prediction==['coconut']:
        output='coconut'
    if prediction==['coffee']:
        output='coffee'
    if prediction==['cotton']:
        output='cotton'
    if prediction==['grapes']:
        output='grapes'
    if prediction==['jute']:
        output='jute'
    if prediction==['kidneybeans']:
        output='kidneybeans'
    if prediction==['lentil']:
        output='lentil'
    if prediction==['maize']:
        output='maize'
    if prediction==['mango']:
        output='mango'
    if prediction==['mothbeans']:
        output='mothbeans'
    if prediction==['mungbean']:
        output='mungbean'
    if prediction==['muskmelon']:
        output='muskmelon'
    if prediction==['orange']:
        output='orange'
    if prediction==['papaya']:
        output='papaya'
    if prediction==['pigeonpeas']:
        output='pigeonpeas'
    if prediction==['pomegranate']:
        output='pomegranate'
    if prediction==['rice']:
        output='rice'
    
    else:
        output='watermelon'
  print(output)
  return output

def main():
    
    html_temp = """
   <div class="" style="background-color:red;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Crop Selector")
    N = st.number_input("Enter Your Soil Nitrogen value",1,100)
P = st.number_input("Enter Your Soil Phosphorus value",1,100)
K = st.number_input("Enter Your Soil Potassium value",1,100)
temperature = st.number_input("Enter Your Soil Nitrogen value",1,100)
humidity= st.number_input("Enter Humidity",1,100)
ph = st.number_input("Enter pH value",3,7)
rainfall= st.number_input("Enter Rainfall amount",100,200)
    
    result=""
    if st.button("Predict"):
      result=predict_note_authentication(N,P,K,temperature,humidity,ph,rainfall)
      st.success('You should grow: {}'.format(result))
      
    if st.button("About"):
      st.header("Developed by ABHISHEK KUMAR SINGH")
      st.subheader("Student , Department of Computer Engineering")
    html_temp = """
    <div class="" style="background-color:green;" >
    <div class="clearfix">           
    <div class="col-md-12">
    <center><p style="font-size:20px;color:white;margin-top:10px;">SVM & RANDOM FOREST CLASSIFICATION</p></center> 
    </div>
    </div>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
if __name__=='__main__':
  main()
