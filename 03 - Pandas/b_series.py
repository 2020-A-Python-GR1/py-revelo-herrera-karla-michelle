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

#Utilizando otras librerias
svc_cuadrado = np.square(series_valor_ciudad)

#Añadiendo un valor a una serie
ciudades_uno = pd.Series({
        "Montañita" : 300,
        "Guayaquil" : 10000,
        "Quito" : 2000})

ciudades_dos = pd.Series({
        "Loja" : 300,
        "Guayaquil" : 10000})

ciudades_uno["Loja"] = 0

print(ciudades_uno + ciudades_dos)

#Añadir y concatenar series

ciudades_add = ciudades_uno.add(ciudades_dos)

ciud_concat = pd.concat([
        ciudades_uno,
        ciudades_dos])

ciudad_concat_verify = pd.concat([
        ciudades_uno,
        ciudades_dos],
        verify_integrity = False)

ciud_append_verify = ciudades_uno.append(
        ciudades_dos,
        verify_integrity = False)

# Min y max
print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

# Funciones estadisticas
print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))

#Ordenar valores

print(ciudades_uno.sort_values(
        ascending = False).head(2))

print(ciudades_uno.sort_values().tail(2))

#Ejercicio
# Con los valores se hará lo siguiente:
# 0 - 1000 -> 5%
# 1001 - 5000 -> 10%
# 5001 - 20000 -> 15%

def calcular(valor_serie):
    if(valor_serie <= 1000):
        return valor_serie * 1.05
    if(valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.10
    if(valor_serie > 5000):
        return valor_serie * 1.15

ciudad_calculada = ciudades_uno.map(calcular)

#if else
# Cuando no aplica la condicion

resultado = ciudades_uno.where(ciudades_uno < 1000,
                               ciudades_uno * 1.05)

series_numeros = pd.Series(['1.0', '2', -3])

print(pd.to_numeric(series_numeros))

# ‘integer’, ‘signed’, ‘unsigned’, ‘float’
print(pd.to_numeric(series_numeros, downcast = 'integer'))


series_numeros_err = pd.Series(['no tiene', '1.0', '2', -3])

# Tipos de errores
# ignore, coerce, raise (default)
# print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerce'))








































































