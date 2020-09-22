#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:11:35 2020

@author: Karlita
"""

import pandas as pd
import numpy as np
from datetime import date

#  Examen

## 1) Crea un Dataframe de 10 registros y 6 columnas y consigue 
## las 5 primeros y los 5 ultimos registros

arreglo1 = np.random.randint(0, 10, 60).reshape(10,6)
df1 = pd.DataFrame(arreglo1)
cinco_primeros = df1.head()
cinco_ultimos = df1.tail()

## 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con 
## una fecha como indice y con columnas A, B, C, D randomico

arreglo2 = np.random.randint(0,10,24).reshape(6, 4)
columnas = ['A', 'B', 'C', 'D']
indices = [date.today().strftime("%Y-%m-%d"),
           date.today().strftime("%Y-%m-%d"),
           date.today().strftime("%Y-%m-%d"),
           date.today().strftime("%Y-%m-%d"),
           date.today().strftime("%Y-%m-%d"),
           date.today().strftime("%Y-%m-%d")
        ]
df2 = pd.DataFrame(
        arreglo2,
        columns = columnas,
        index = indices
        )

## 4) Crear un Dataframe con 10 registros y 6 columnas y con una 
## propiedad del Dataframe mostrar las columnas, con otro comando 
## mostrar los valores.

arreglo4 = np.random.randint(0,10,60).reshape(10, 6)
df4 = pd.DataFrame(arreglo4)
columnas_df4 = df4.columns.values
valores_df4 = df4.values

## 5) Crear un Dataframe con 10 registros y 6 columnas y con una 
## funcion del Dataframe describir estadisticamente el Dataframe

arreglo5 = np.random.randint(0,10,60).reshape(10, 6)
df5 = pd.DataFrame(arreglo5)
descripcion_df5 = df5.describe()

## 6) Crear un Dataframe con 10 registros y 6 columnas y con una 
## funcion del Dataframe transponer los datos

arreglo6 = np.random.randint(0,10,60).reshape(10, 6)
df6 = pd.DataFrame(arreglo6)
transpuesto_df6 = df6.transpose()

## 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar 
## el dataframe 1 vez por cada columna, ascendente y descendente

arreglo7 = np.random.randint(0,10,60).reshape(10, 6)
df7 = pd.DataFrame(arreglo7)

df7_ascendente = df7.apply(lambda x: x.sort_values().values)
df7_descendente = df7.apply(lambda x: x.sort_values(ascending = False).values)

## 8) Crear un Dataframe con 10 registros y 6 columnas llenas de 
## números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe 
## solo los valores mayores a 7

arreglo8 = np.random.randint(1,10,60).reshape(10, 6)
df8 = pd.DataFrame(arreglo8)

mayores_a_7 = df8 > 7
df8_mayores_7 = df8[mayores_a_7]

## 9) Crear un Dataframe con 10 registros y 6 columnas llenas de 
## números randomicos del 1 al 10 o valores NaN. Luego llenar los 
## valores NaN con 0.

arreglo9 = np.random.randint(1,10,60).reshape(10, 6)
df9 = pd.DataFrame(arreglo9)
mayores_a_3 = df8 > 3
df9_nan = df9[mayores_a_3]
df9_llenos_0 = df9_nan.fillna(0)

## 10) Crear un Dataframe con 10 registros y 6 columnas llenas de 
## números randomicos del 1 al 10 y sacar la media, la mediana, el 
## promedio

arreglo10 = np.random.randint(0,10,60).reshape(10, 6)
df10 = pd.DataFrame(arreglo10)
media_df10 = df10.mean()
mediana_df10 = df10.median()
promedio_df10 = df10.mean()

## 11) Crear un Dataframe con 10 registros y 6 columnas llenas de 
## números randomicos del 1 al 10, luego crear otro dateframe con 10 
## registros y 6 columnas llenas de números randomicos del 1 al 10 y 
## anadirlo al primer Dataframe

arreglo11_1 = np.random.randint(1,10,60).reshape(10, 6)
df11_1 = pd.DataFrame(arreglo11_1)
arreglo11_2 = np.random.randint(1,10,60).reshape(10, 6)
df11_2 = pd.DataFrame(arreglo11_2)
df11_final = df11_1.append(df11_2)

## 12) Crear un Dataframe con 10 registros y 6 columnas llenas de 
## strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 
## y 6 concatenando su texto.

arreglo_string = pd.util.testing.rands_array(3, 60).reshape(10,6)
df12 = pd.DataFrame(arreglo_string)
df12_final = pd.DataFrame(df12[0] + df12[1])
df12_final[1] = df12[2] + df12[3]
df12_final[2] = df12[4] + df12[5]

## 13) Crear un Dataframe con 10 registros y 6 columnas llenas de 
## números randomicos del 1 al 10 enteros, obtener la frecuencia de 
## repeticion de los numeros enteros en cada columna

arreglo13 = np.random.randint(0,10,60).reshape(10, 6)
df13 = pd.DataFrame(arreglo13)
for column in df13.columns:
    print("Columna " + str(column))
    print(df13[column].value_counts())
    
## 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, 
## llenas de números randomicos del 1 al 10 enteros. Crear una nueva 
## columna con el calculo por fila (A * B ) / C

arreglo14 = np.random.randint(1,10,30).reshape(10, 3)
df14 = pd.DataFrame(arreglo14, columns = ['A', 'B', 'C'])
resultados = []
for index in df14.index:
    resultados.append((df14['A'][index] * df14['B'][index]) / df14['C'][index] )
print(resultados)
df14['Resultados'] = resultados






















