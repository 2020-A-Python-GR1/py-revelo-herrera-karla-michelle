#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:08:37 2020

@author: dev-16
"""

import pandas as pd
import os

path = "/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/03 - Pandas/data/artwork_data.csv"


df1 = pd.read_csv(
    path,
    nrows=10,
    )

columnas = ['id', 'artist', 'title',
            'medium', 'year',
            'acquisitionYear', 'height',
            'width', 'units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')



path_guardado = "/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/03 - Pandas/data/artwork_data.pickle"
# artwork_data.pickle

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)

