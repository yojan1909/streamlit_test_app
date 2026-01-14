import streamlit as st 
st.title(" Hello Streamlit") 
st.write("Streamlit is working successfully!") 
name = st.text_input("Enter your name:") 
if name:
    st.success(f"Welcome, {name} ")
    number = st.slider("Choose a number", 0, 100, 50)
    st.write("You selected:", number) 
st.button("Click Me")
