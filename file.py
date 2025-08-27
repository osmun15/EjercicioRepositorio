#numero = int(input("digita un numero: "))
#print(numero) 


#crear un elemnto con n elementos indicados por el usurio

""" n=int(input("cuantos elementos desea incluir"))
lista = [int(input("ingrese el elemento: ")) for i in range(n)]

print("la lista es: ", lista) """


""" tupla1=(1,2,3)
print(min(tupla1)) """

#ejercicios listas

#ejercicio 6

#Crear una lista con 5 elementos de tipo carácter, una con 3 elementos tipo entero y una tercera que contenga los 8 elementos de las dos primeras. Mostrar en pantalla las 3 listas generadas.

""" # Lista con 5 elementos tipo carácter
lista_caracteres = ['a', 'b', 'c', 'd', 'e']

# Lista con 3 elementos tipo entero
lista_enteros = [1, 2, 3]

# Lista que contiene los 8 elementos de las dos primeras
lista_combinada = lista_caracteres + lista_enteros

# Mostrar en pantalla las listas generadas
print("Lista de caracteres:", lista_caracteres)
print("Lista de enteros:", lista_enteros)
print("Lista combinada:", lista_combinada) """

# 9.  Escribir un programa que pregunte al usuario n números, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

""" # Preguntar cuántos números quiere ingresar
n = int(input("¿Cuántos números desea ingresar? "))

# Crear lista vacía para almacenar los números
numeros = [int(input("Ingrese un número: ")) for i in range(n)]


# Ordenar la lista de menor a mayor
numeros.sort()

# Mostrar la lista ordenada
print("Números ordenados de menor a mayor:")
print(numeros) """

#EJERCICIOS DICCIONARIOS

#ingresada una palabra, generar un diccionario que retorne cada 
# letra de la palabra y su numero de repeticiones en la misma --> mama

""" palabra = input("ingrese su nombre: ")

diccionario={}

for i in palabra:
    if i in diccionario:
        diccionario[i]+=1
    else:
        diccionario[i]=1

print(diccionario) """

#ejercicio estudiantes

""" estudiantes = {
    "ana": 4.5,
    "carlos": 3.5,
    "camilo": 4.9 
}

#crear funciones agregar estudiante nuevo

def agregar(diccionario, nombre, nota):
    diccionario[nombre] = nota
    print(f"Estudiante {nombre} agregado con nota {nota} con exito")


#crear funcion para buscar la nota

def buscar(diccionario, nombre):
    return diccionario.get(nombre, "Estudiante no encontrado.")

def mostrar(diccionario):
    for nombre, nota in diccionario.items():
        print(f"Estudiante: {nombre}, Nota: {nota}")

agregar(estudiantes, "juan", 4.0)

print("nota de ana: ", buscar(estudiantes, "ana"))

mostrar(estudiantes) """


#ejercicio 5 Diccionarios

#Ejercicios

# 5.Agrupar por longitud: Escribe un algoritmo que tome una lista de cadenas como entrada y devuelva 
# un diccionario donde las claves sean las longitudes de las cadenas y los valores sean listas 
# de las cadenas  correspondientes

# Lista de cadenas
cadenas = ["saxofon", "ola", "perro", "gato", "día", "cielo", "sol", "mandarina"]

# Diccionario para agrupar por longitud
agrupadas = {}

for cadena in cadenas:
    longitud = len(cadena)
    
    # Si la cantidad de caracteres de cada palabra dentro de la lista 
    # no esta en el diccionario, la creamos con una lista vacía

    if longitud not in agrupadas:
        agrupadas[longitud] = []
    
    # Agregamos el nombre del elemento a cada lista de la cantida de caracteres correspondiente
    agrupadas[longitud].append(cadena)

# Mostrar resultado
print(agrupadas)
