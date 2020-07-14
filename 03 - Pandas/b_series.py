#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

"""
Created on Tue Jul 14 07:58:46 2020

@author: dev-16
"""

#b_series.py



lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)
series_d = pd.Series(
        [True,
         False,
         12,
         12.12,
         "Karlita",
         None,
         (1),
         [2],
         {"nombre" : "Karlita"}
         ])

lista_ciudades = [
        "Ambato",
        "Cuenca",
        "Loja",
        "Quito"]
serie_ciudades = pd.Series(
        lista_ciudades,
        index = [
                "A",
                "C",
                "L",
                "Q"])
valores_ciudad = {
        "Ibarra" : 9500,
        "Guayaquil" : 10000,
        "Cuenca": 7000,
        "Quito" : 8000,
        "Loja" : 3000
        }
series_valor_ciudad = pd.Series(valores_ciudad)

# Ciudades menores a 5000

ciudades_menor_5K = series_valor_ciudad < 5000

print(type(series_valor_ciudad))
print(type(ciudades_menor_5K))
print(ciudades_menor_5K)

s5 = series_valor_ciudad[ciudades_menor_5K]

# Ciudades con 10% más

series_valor_ciudad = series_valor_ciudad * 1.1
series_valor_ciudad["Quito"] = series_valor_ciudad["Quito"] - 50








