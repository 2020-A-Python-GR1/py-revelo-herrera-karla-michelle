#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:47:30 2020

@author: dev-16
"""

import pandas as pd
import os

path = './data/artwork_data.csv'


df1 = pd.read_csv(path,nrows = 10)

# definir columnas

columnas = ['id', 'artist','title',
            'medium', 'year', 
            'acquisitionYear', 'height',
            'width', 'units']

df2 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas)

# colocar como index los valores de la columna id
df3 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas,
        index_col = 'id')

path_guardado = './data/artwork_data.csv'

df3.to_pickle(path_guardado)