import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de que el archivo esté en el mismo directorio

# Crear encabezado
st.header('Análisis Profesional de Datos de Vehículos en Venta')

# Descripción general del DataFrame
st.subheader('Descripción General del Conjunto de Datos')
st.write('El conjunto de datos contiene información sobre vehículos en venta, incluyendo precio, año del modelo, condición, tipo de combustible, y más.')
st.write(car_data.head())  # Mostrar las primeras filas del DataFrame

# Estadísticas descriptivas
st.subheader('Estadísticas Descriptivas')
st.write('A continuación, se presentan estadísticas descriptivas clave para las columnas numéricas del conjunto de datos:')
st.write(car_data.describe())

# Distribución de precios
st.subheader('Distribución de Precios')
st.write('Visualizamos la distribución de precios para identificar tendencias y valores atípicos.')
price_hist_button = st.button('Construir histograma de precios')

if price_hist_button:
    fig = px.histogram(car_data, x="price", nbins=50, title="Distribución de Precios")
    st.plotly_chart(fig, use_container_width=True)

# Relación entre precio y odómetro
st.subheader('Relación entre Precio y Odómetro')
st.write('Exploramos cómo el precio de los vehículos varía en función del kilometraje.')
scatter_button = st.button('Construir gráfico de dispersión (Precio vs. Odómetro)')

if scatter_button:
    fig = px.scatter(car_data, x="odometer", y="price", color="condition", 
                     title="Relación entre Precio y Odómetro",
                     labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig, use_container_width=True)

# Análisis de la condición del vehículo
st.subheader('Distribución por Condición del Vehículo')
st.write('Analizamos la cantidad de vehículos en cada categoría de condición.')
condition_bar_button = st.button('Construir gráfico de barras (Condición)')

if condition_bar_button:
    condition_counts = car_data['condition'].value_counts().reset_index()
    condition_counts.columns = ['condition', 'count']  # Renombrar columnas
    fig = px.bar(condition_counts, 
                 x='condition', y='count', 
                 title="Distribución por Condición del Vehículo",
                 labels={"condition": "Condición", "count": "Cantidad"})
    st.plotly_chart(fig, use_container_width=True)

# Relación entre cilindros y precio promedio
st.subheader('Relación entre Número de Cilindros y Precio Promedio')
st.write('Examinamos cómo el número de cilindros afecta el precio promedio de los vehículos.')
cylinders_price_button = st.button('Construir gráfico de barras (Cilindros vs. Precio Promedio)')

if cylinders_price_button:
    avg_price_by_cylinders = car_data.groupby('cylinders')['price'].mean().reset_index()
    fig = px.bar(avg_price_by_cylinders, x='cylinders', y='price', 
                 title="Precio Promedio por Número de Cilindros",
                 labels={"cylinders": "Número de Cilindros", "price": "Precio Promedio"})
    st.plotly_chart(fig, use_container_width=True)
