import streamlit as st
from predict import prediction
from explore import explore_page



def main():

    choice = st.sidebar.selectbox("Predict or Explore:",("Predict" , "Explore"))
    st.sidebar.image('airbnb.png')

    if choice == 'Predict':
        prediction()
    else :
        explore_page()


if __name__ == '__main__':
    main()