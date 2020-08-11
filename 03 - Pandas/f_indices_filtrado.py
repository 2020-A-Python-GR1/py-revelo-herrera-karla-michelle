#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:34:15 2020

@author: dev-16
"""

import pandas as pd

path_guardado = "/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas))

print(artistas.size)

# Filtrar obras de blake

blake = df['artist'] == 'Blake, William' # serie
print (blake.value_counts())
df_blake = df[blake] #dataframe

