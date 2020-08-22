#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:52 2020

@author: dev-16
"""

import pandas as pd

path_guardado = "/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

# loc: Para obtener un registro, filtrado horizontal
filtrado_horizontal = df.loc[1035] # Devuelve la serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index)

# filtrado vertical
serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index)

#primero = df.loc[1035, 'artist']

# Filtrado por índice

df_1035 = df[df.index == 1035]
segundo = df.loc[1035] #Por indice
segundo = df.loc[[1035,1036]] #Por arreglo de indices
segundo = df.loc[3:5] #Por intervalo de indices
segundo = df.loc[df.index == 1035] #Por arreglo de True y False

segundo = df.loc[1035, 'artist'] #1 indice
segundo = df.loc[1035, ['artist', 'medium']] #varios indices

# iloc

tercero = df.loc[0] #Por indice
tercero = df.loc[[0,1]] #Por arreglo de indices
tercero = df.loc[0:10] #Por intervalo de indices
tercero = df.loc[df.index == 1035] #Por arreglo de True y False

#######


datos={
       "nota 1":{
           "Pepito":7,
           "Juanit:":8,
           "Maria":9           
           },
       "nota 2":{
           "Pepito":7,
           "Juanit:":8,
           "Maria":9           
           },
       "disciplina":{
           "Pepito":4,
           "Juanit:":9,
           "Maria":2             
           }
       
       }

notas=pd.DataFrame(datos)

condicion_nota = notas["nota 1"]>7
condicion_nota_dos = notas["nota 2"]>7
condicion_diciplina = notas["disciplina"]>7

mayores_siete= notas.loc[condicion_nota,["nota 1"]]

pasaron=notas.loc[condicion_nota][condicion_diciplina][condicion_nota_dos]


notas.loc["Maria","disciplina"]=7

notas.loc[:,"disciplina"]=7


########## Promedio de las 3 notas (nota1 + nota 2 + disc)/3


promedio = (notas["nota 1"]+notas["nota 2"]+notas["disciplina"])/3













