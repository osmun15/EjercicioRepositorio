import pandas as pd

#Ejercicio 2 frecuencias


# Lista de edades
edades = [25, 30, 22, 28, 35, 27, 31, 29, 26, 33]

# Crear una serie de pandas
serie_edades = pd.Series(edades)

# Calcular la frecuencia absoluta
frecuencia_abs = serie_edades.value_counts().sort_index()

# Calcular la frecuencia acumulada
frecuencia_acum = frecuencia_abs.cumsum()

# Crear tabla de frecuencias
tabla_frecuencias = pd.DataFrame({
    "Edad": frecuencia_abs.index,
    "Frecuencia": frecuencia_abs.values,
    "Frecuencia Acumulada": frecuencia_acum.values
})

# Mostrar la tabla
print(tabla_frecuencias)
print("\n")