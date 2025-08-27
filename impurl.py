import pandas as pd

""" #crear variable con la url
url="http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#definir el nombre de las columnas
col_names=["sepal_length", "sepal_width", "petal_length", "petal_width", "especies"]

df_iris = pd.read_csv(url, names=col_names)

#mostrar las primeras filas del dataframe
print(df_iris.head()) """

#crear un fichero de texto con la tabla de multiplicar de un numero del 1 al 10
n=int(input('digite un numero del 1 al 10 para generar la tabla'))
nombre_fichero='tabla' + str(n)+ '.txt'
f=open(nombre_fichero,'w')
for i in range(1,11):
    f.write(str(n)+ 'x' + str(i) +'=' + str(n*i) +'\n')
f.close()
