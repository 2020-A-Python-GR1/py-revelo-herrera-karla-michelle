#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:09:36 2020

@author: dev-16
"""

import numpy as np
import pandas as pd
import os
import xlsxwriter


path_guardado = "/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)
sub_df = df.iloc[49980:50519, :].copy()

num_artistas = sub_df['artist'].value_counts()
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

workbook = xlsxwriter.Workbook('grafico.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Artista')
worksheet.write('B1', 'Num. obras')

for i in range(num_artistas.size):
    worksheet.write(f'A{i + 2}', artistas[i])
    worksheet.write(f'B{i + 2}', num_artistas[artistas[i]])

chart = workbook.add_chart({'type': 'pie'})

chart.add_series({
    'name': 'Artistas y sus obras',
    'categories': '=Sheet1!$A$2:$A$12'.format(len(num_artistas.index)+1),
    'values': '=Sheet1!$B$2:$B$12'.format(len(num_artistas.index)+1),    
    }) 


chart.set_title({'name': 'Artistas y sus obras'})
chart.set_style(26)
worksheet.insert_chart('D2', chart, {'x_offset': 25, 'y_offset': 10})


workbook.close()