import streamlit as st
from logic import *


def load_css():
    with open("style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown('<h1 class="app-title">Calculator</h1>', unsafe_allow_html=True)

st.markdown('<span class="input-wrapper">Enter the first number:</span>', unsafe_allow_html=True)
a= st.number_input("", value=0, key="num1")

st.markdown('<span class="input-wrapper">Enter the second number:</span>', unsafe_allow_html=True)
b= st.number_input("", value=0, key="num2")

st.markdown('<span class="input-wrapper">Select an operator:</span>', unsafe_allow_html=True)
operator = st.selectbox("",["Add","Subtract","Multiply","Divide"])

result = None

def calculate(a,b,operator):
    if operator == "Add":
        result = add(a,b)
        return result
    
    elif operator == "Subtract":
        result = subtract(a,b)
        return result
        
    elif operator == "Multiply":
        result = multiply(a,b)
        return result
    
    elif operator == "Divide":
        result = divide(a,b)
        if result is None:
            st.error("Cannot divide by Zero!")
        return result
            
if st.button("Calculate"):
    result = calculate(a,b,operator)
    if result is not None:
        st.markdown(f"<div class='result'>Result: {result:.2f}</div>", unsafe_allow_html=True)
    else:
        st.error("Invalid Operation")
    
