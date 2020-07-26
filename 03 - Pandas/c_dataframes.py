#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:50:25 2020

@author: dev-16
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

# operaciones con la serie

s1 = df1[0]
s2 = df1[1]
s3 = df1[2]
df1[3] = s1
df1[4] = s1 * s2

# nombres a las columnas
datos_fisicos_uno = pd.DataFrame(
        arr_pand,
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'Edad (anios)'])

# nombres a las filas
datos_fisicos_dos = pd.DataFrame(
        arr_pand,
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'Edad (anios)'],
        index = [
                'Karlita',
                'Michelle'])

# definir indices y columnas

df1.index = ['Karlita','Revelo']
df1.index = ['Karoline','Cecilia']
df1.columns = ['A','B','C','D','E']


