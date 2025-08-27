import pandas as pd

""" #1 crear el diccionario

datos={
    "nombre": ["Juan", "Ana", "Pedro", "Maria"],
    "edad": [28, 22, 35, 30],
    "ciudad":["medellin","bogota","cali","medellin"],
    "salario":[1500000,2000000,1800000,2500000]
}


# 2 convertirlo a un DataFrame
dFrame=pd.DataFrame(datos)

#3 imprimir datos
print("DataFrame")
print(dFrame)

#4 filtrar empleados con sueldos mayores a 1.500.5000
print("empleados con salario superior a $1.500.000")
print(dFrame["salario"]> 1500000)


#5 muestra el promedio del total de los sueldos
print("promedio de sueldos")
promedioSueldo= dFrame["salario"].mean()
print(f"promedio: {promedioSueldo}")


#6 promedio de sueldos por ciudad
print("promedio total de sueldos por ciudad")
print(dFrame.groupby("ciudad")["salario"].mean())


#7 ordenar por edad
print("datos ordenados por edad")
print(dFrame.sort_values(by="edad")) """


# 6. Indexación y selección: 5. Selecciona la columna "edad" de un DataFrame.  6. Selecciona las filas donde la edad sea mayor a 30.


datos = {
    "nombre": ["Ana", "Luis", "Pedro", "Marta", "Sofía"],
    "edad": [25, 35, 40, 28, 32],
    "ciudad": ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]
}

# Convertir el diccionario a un DataFrame
datadframe = pd.DataFrame(datos)

# seleccionar la columna edad
print("La edad de los empleados:")
print(datadframe["edad"])

# seleccionar las filas donde la edad sea mayor a 30
print("los empleados mayores a 30 son:")
print(datadframe[datadframe["edad"] > 30])