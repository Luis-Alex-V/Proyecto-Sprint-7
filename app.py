import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header('Dashboard de anuncios de venta de coches')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
hist_button = st.button('Construir histograma del odómetro')

if hist_button:
    st.write('Histograma de la variable odometer')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión (odometer vs price)')

if scatter_button:
    st.write('Gráfico de dispersión odometer vs price')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
