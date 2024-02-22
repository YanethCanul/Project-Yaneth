import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Vehicle USA')
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    fig.show()    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_botton= st.button('Construir grafico de dispersion') # crea boton para construir el grafico de dispersion
if scatter_botton: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
    # crear grafico de dispersion
    fig = px.scatter(car_data, x="odometer")
    fig.show() 
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


