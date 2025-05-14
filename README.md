# Proyecto Sprint 7 - Análisis de Datos de Vehículos en Venta

Esta aplicación web y notebook, desarrollados con Streamlit y Python, permiten analizar un conjunto de datos de anuncios de venta de vehículos. Proporciona las siguientes funcionalidades:

## Funcionalidades de la Aplicación Web
- **Histograma interactivo**: Visualiza la distribución de los valores de odómetro.
- **Gráfico de dispersión interactivo**: Muestra la relación entre el precio y el odómetro, categorizado por la condición del vehículo.
- **Gráfico de barras**: Analiza la relación entre el número de cilindros y el precio promedio.

## Funcionalidades del Notebook
- **Descripción general del conjunto de datos**: Muestra las primeras filas y estadísticas descriptivas.
- **Relación entre precio y odómetro**: Gráfico de dispersión para explorar esta relación.
- **Distribución de valores de odómetro**: Histograma para analizar la distribución.
- **Distribución por condición del vehículo**: Gráfico de barras para visualizar la cantidad de vehículos en cada categoría de condición.
- **Relación entre cilindros y precio promedio**: Gráfico de barras para analizar cómo el número de cilindros afecta el precio promedio.

## Cómo ejecutar la aplicación

1. Asegúrate de tener instaladas las dependencias necesarias: `pandas`, `plotly`, y `streamlit`.
2. Ejecuta el comando `streamlit run app.py` desde la terminal para la aplicación web.
3. Abre el archivo `EDA.ipynb` en un entorno compatible con Jupyter para explorar el análisis detallado.

## Estructura del proyecto

- **app.py**: Archivo principal para ejecutar la aplicación Streamlit.
- **EDA.ipynb**: Contiene el análisis exploratorio de datos con visualizaciones adicionales.
- **vehicles_us.csv**: Conjunto de datos utilizado para el análisis.

¡Explora los datos y obtén información valiosa sobre los vehículos en venta!
