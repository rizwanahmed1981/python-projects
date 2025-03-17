import streamlit as st
import pandas as pd

st.title("BMI CALCULATOR")

height = st.slider("Enter Your Hieight (in cm): ", 100, 250, 175)
weight = st.slider("Enter your height (in kg): ", 40, 200, 70)

if st.button("Calculate BMI"):
    bmi = weight / ((height/ 100)** 2)
    if bmi <18.5 :
        st.write(f"<p style='background-color: white; color:blue; font-size: 24px; padding: 10px; border-radius:5px; text-align:center;'>Your BMI is {bmi:.2f}</p>", unsafe_allow_html=True)
        st.warning("- Underweight: BMI les than 18.5")
    elif bmi > 18.5 and bmi < 24.9 :
        st.write(f"<p style='background-color: white; color:blue; font-size: 24px; padding: 10px; border-radius:5px; text-align:center;'>Your BMI is {bmi:.2f}</p>", unsafe_allow_html=True)        
        st.success("- Normal weight: BMI les between 18.5 and 24.9")
    elif bmi >= 25 and bmi <= 29.9:
        st.write(f"<p style='background-color: white; color:blue; font-size: 24px; padding: 10px; border-radius:5px; text-align:center;'>Your BMI is {bmi:.2f}</p>", unsafe_allow_html=True)
        st.warning("- Overweight: BMI between 25 and 29.9")
    elif bmi >= 30:
        st.write(f"<p style='background-color: white; color:blue; font-size: 24px; padding: 10px; border-radius:5px; text-align:center;'>Your BMI is {bmi:.2f}</p>", unsafe_allow_html=True)
        st.markdown('<p style="color:white; font-size:24px; background-color:red; padding:10px; border-radius:5px; ">- Obasity: BMI 30 or greater</p>', unsafe_allow_html=True)


    
