import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components




def explore_page():

    df = pd.read_csv('filtered_df.csv')
    st.title("Explore Riyadh's Airbnbs")

    days = df.stayed_nights.value_counts().sort_index()
    fig = px.bar(
    days,
    x = days.index ,
    y = days.values ,
    labels = {'stayed_nights' : 'Stayed nights' , 'y' : 'Frequency'} ,
    title = 'Frequency of days did people stayed in Airbnbs' ,
    color_discrete_sequence = ['rgb(57,105,172)'] ,
)
    st.plotly_chart(fig, use_container_width=True)
    

    cancelation = df[['property_id' , 'cancelPolicy']].drop_duplicates().cancelPolicy.value_counts().reset_index()
    fig = px.bar(cancelation, y=cancelation['count'], x=cancelation['cancelPolicy'], text_auto='.2s',
             title="Frequency of Cancel policy for Airbnbs",
             labels = {
                 'count' : 'Frequency' ,
                 'cancelPolicy' : 'Cancel Policy'
             } ,
             color_discrete_sequence = ['rgba(186, 83, 122, 1)'])

    st.plotly_chart(fig, use_container_width=True)


    months_total = df.groupby(
    ['check_in',
    'property_type']
    ).agg({
    'total':'sum' ,
    }).reset_index()

    fig = px.line(
    months_total ,
    x = months_total.check_in,
    y = months_total.total,
    markers = True ,
    color = 'property_type' ,
    title = 'Monthly trend property type wise' ,
    labels = {
        'check_in' : 'Check in Month' ,
        'total' : 'Total Revenue',
        'property_type' : 'Property type'
    }
)
    
    st.plotly_chart(fig, use_container_width=True)



    districts = df['district'].value_counts()

    districts = df[['district','property_id']].drop_duplicates()['district'].value_counts().reset_index()

    fig = px.bar(districts, y=districts['count'], x=districts['district'], text_auto='.s',
                title="Districts of Airbnb",
                color_discrete_sequence = px.colors.qualitative.Set2[0:1],
                labels = {
                    'y' : 'Frequency' ,
                    'district' : 'District'
                })
    
    st.plotly_chart(fig, use_container_width=True)


    Governorates = df[['property_id','governorates']].drop_duplicates()['governorates'].value_counts()
    fig = px.pie(Governorates, values=Governorates.values, names=Governorates.index, title='Governorates of Airbnb')

    st.plotly_chart(fig, use_container_width=True)

    types = df[['property_id','property_type']].drop_duplicates()['property_type'].value_counts()
    fig = px.bar(types, y=types.values, x=types.index, text_auto='.s',
             title="Airbnb Property types:  ",
             color =types.index ,
             color_discrete_sequence = px.colors.qualitative.Pastel[2:19] ,
             labels = {
                 'y' : 'Frequency' ,
                 'property_type' : 'Property type'
             } )

    st.plotly_chart(fig, use_container_width=True)


    persons = df[['property_type','governorates','persons']].drop_duplicates().groupby(['property_type','governorates']).agg(
    {'persons' : pd.Series.median ,
      }
    ).reset_index()

    persons['persons'] = persons['persons'].apply(lambda x : int(x))

    fig = px.bar(
                persons ,
                x="persons",
                y="property_type",
                orientation='h',
                color = "governorates",
                title="Average persons in each airbnb type per Governorates  " ,
                labels = {
                    'property_type' : 'Property type' ,
                    'governorates' : 'Governorates'

                }

                )
    
    st.plotly_chart(fig, use_container_width=True)


    st.write("**Clustered Airbnbs around Riyadh**")
    map_html = open("clustering_map.html", 'r', encoding='utf-8')
    map = map_html.read()
    with st.container():
         components.html(map,width=700, height=500)