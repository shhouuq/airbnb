import streamlit as st
import numpy as np 
import pickle
import pandas as pd


def load_pipeline():
    filename = 'pipeline_train.pkl'
    loaded_pipeline = pickle.load(open(filename , 'rb'))

    return loaded_pipeline



def transform(x) : 

    data = load_pipeline()
    transformer = data['transformation']
    transformed_data = transformer.transform(x)
    return transformed_data 


def clustering(data):
    pipe = load_pipeline()
    model = pipe['clustering']
    cluster = model.predict(data.values) + 1
    return cluster

def predict(features) :
    pipe = load_pipeline()
    prediction = pipe['regression'].predict(features.reshape(1,18))
    return prediction


def prediction():


    st.title('Airbnb price prediction in Riyadh!')

    st.write('**Kindly fill the needed information to predict:**')
    
    st.write("**In which governorator is the Airbnb located ?**")
    option_gov = st.selectbox(
    "",
    ("Riyadh", "Ammariyah", "Diriyah" , "Zilfi" , "Sulaymaniyah"),
    index=None,
    placeholder="Select governorator...",
)

    st.markdown("")
    st.markdown("")

    st.write("**Kindly specify latitude and longitude:**")

    lat = st.slider('Latitude' , 24.00001 , 24.99000 , 24.780)
    lng = st.slider('Longitude' , 46.00001 , 46.99000 , 46.628)

    st.markdown("")
    st.markdown("")


    st.write('**How is the cancel policy ?**')
    option_policy = st.selectbox(
    "",
    ("Cancel Flexible", "Cancel Moderate", "Cancel strict with 14 days grace period" , "Cancel strict with other grace period" ),
    index=None,
    placeholder="Select Policy...",
)
    
    st.markdown("")
    st.markdown("")
    




    
    st.markdown("")
    st.markdown("")


    st.write('**Does the Airbnb have wide hallways?**')
    option_wide= st.selectbox(
    "",
    ("Yes",  "No" ),
    index=None,
    placeholder="Select Y/N...",  key = 50
)

    st.markdown("")
    st.markdown("")

    st.write('**Is breakfast provided?**')
    option_break= st.selectbox(
    "",
    ("Yes",  "No" ),
    index=None,
    placeholder="Select Y/N...",  key = 17
)

    st.markdown("")
    st.markdown("")






    st.write('**Is WIFI provided?**')
    option_wifi= st.selectbox(
    "",
    ("Yes",  "No" ),
    index=None,
    placeholder="Select Y/N...",  key = 24
)
    

    st.markdown("")
    st.markdown("")


    st.write('**Is there a GYM?**')
    option_gym= st.selectbox(
    "",
    ("Yes",  "No" ),
    index=None,
    placeholder="Select Y/N...",  key = 26
)




    st.markdown("")
    st.markdown("")

    st.write('**How many Reviews did the place get ?**')
    reviews = st.slider('' , 0 , 400 , 5)

    st.markdown("")
    st.markdown("")
    


    
    



    st.write("**How many nights would you stay?**")
    nights = st.slider('' , 1 , 100 , 10)

    st.markdown("")
    st.markdown("")
    

    st.write('**How many persons ?**')
    persons = st.slider('' , 1 , 15 , 2)


    st.markdown("")
    st.markdown("")
    

    st.write('**How many bathrooms ?**')
    baths = st.slider('' , 1 , 10 , 2)


    ok = st.button('Predict night price')


    if ok:
        clst = pd.DataFrame({'lat' : [lat] , 'lng' : [lng]})
        cluster = clustering(clst)

        cancel = None
        if option_policy == 'Flexible':
            cancel = 'CANCEL_FLEXIBLE'
        elif option_policy == "Cancel Moderate":
            cancel = 'CANCEL_MODERATE'
        elif option_break == "Cancel strict with 14 days grace period":
            cancel = 'CANCEL_STRICT_14_WITH_GRACE_PERIOD'
        else:
            cancel = 'CANCEL_BETTER_STRICT_WITH_GRACE_PERIOD'

        data_dict = {
             'governorates' : option_gov ,
             'persons' : persons,
             'cluster' : cluster ,
             'reviewsCount' : reviews,
             'stayed_nights' : nights ,
             'cancelPolicy' :  cancel, 
             'Wide_hallways' : 1.0 if option_wide=='Yes' else 0.0,
             'bathrooms' : baths, 
             'Gym' : 1.0 if option_gym=='Yes' else 0.0,
             'Wifi': 1.0 if option_wifi=='Yes' else 0.0,
             'Breakfast' : 1.0 if option_break=='Yes' else 0.0 

         }

        data = pd.DataFrame(data_dict)

        X = transform(data)

        prediction = predict(X)
        st.write(f"The estimated price for one night is ${prediction[0]:.2f}")

