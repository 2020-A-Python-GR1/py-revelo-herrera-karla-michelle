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














