import streamlit as st
import plotly.express as px

st.title('Dashboard de Mudanças Climáticas')

# Gráfico de temperatura
fig = px.line(temp_global, x='Year', y='Temperature', title='Temperatura Global')
st.plotly_chart(fig)

# Filtro por década
decada = st.slider('Selecione a década', 1880, 2020, step=10)
filtered_data = temp_global[temp_global['Year'].between(decada, decada + 10)]
st.write(filtered_data)