import streamlit as st
from get_contract import get_source_code

# from model import model
import distutils as _distutil


def main():

    st.title("Smart Contract Prediction")
    st.write("Enter text and select a model to see the prediction result.")

    col1, col2 = st.columns([3, 1])

    with col1:
        contract_hash = st.text_input("Enter text:")

    with col2:
        selected_model = st.selectbox(
            "Select a model:", ["BLSTM", "LSTM", "CNN"]
        )

    if contract_hash.strip() or st.button("Analyse"):
        st.write(get_source_code(contract_hash))


if __name__ == "__main__":
    main()
