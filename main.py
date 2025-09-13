import streamlit as st
from app import get_few_shot_db_chain

st.title("BrandStore Assistant👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)