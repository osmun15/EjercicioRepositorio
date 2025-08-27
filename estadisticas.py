import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Título del dashboard
st.title('Mi Primer Dashboard en Streamlit')
# Texto introductorio
st.write('Este es un dashboard sencillo creado con Streamlit.')
# Datos de ejemplo
data = {'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    'Ventas': [100, 150, 120, 180, 140]}
df = pd.DataFrame(data)
# Mostrar los datos como una tabla
st.subheader('Tabla de Ventas')
st.dataframe(df)
# Crear un gráfico de barras con Matplotlib
st.subheader('Gráfico de Ventas Mensuales')
fig, ax = plt.subplots()
ax.bar(df['Mes'], df['Ventas'])
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas')
st.pyplot(fig)