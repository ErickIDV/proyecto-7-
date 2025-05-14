import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de que el archivo esté en el mismo directorio

# Crear encabezado
st.header('Análisis de datos de vehículos en venta')

# Botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="price", y="odometer", color="condition")
    st.plotly_chart(fig, use_container_width=True)
