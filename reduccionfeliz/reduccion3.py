# matriz pivoteada lista para subir al BIGQUERY
# Columnas Features o criterios - Filas Observaciones
# proceso de reduccion de la matriz
# de datos del banco mundial
# para paraguay
# hecho el 2017.3


# elimino las columnas nulas y las filas nulas
# vamos por el paso a paso

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# tomo la matriz antes de pivotear
# y le quito lo mas posible los nan

origen = os.getcwd() + '/matriz_paso2.csv'
csvfile = open(origen, 'r')
# creo el dataframe
# datos_todos = pd.read_csv(csvfile, sep=',')
# ahora descarto las tres primeras filas, que son titulos en la planilla
datos_todos = pd.read_csv(csvfile, sep=',', skiprows=3)

# alli se ven los datos nan (nulos)
# print datos_todos
num_rows = datos_todos.shape[0]
print 'datos todos ' + str(num_rows)
# ahora descarto las tres primeras filas, que son titulos en la planilla
sin_titulos = datos_todos
sintitulos_rows = sin_titulos.shape[0]
print 'datos sin titulos ' + str(sintitulos_rows)
# sin_titulos.to_csv('salida.csv')

# descarto las primeras tres columnas - no son utiles
# Country name, country code, indicator name

sin_columnas1 = sin_titulos.ix[:, 3:]
sin_columnas1_filas = sin_columnas1.shape[0]
print 'datos sin tres columnas ' + str(sin_columnas1_filas)

# elimino el periodo 2016 - aun no esta todo cargado
sin_columnas2016 = sin_columnas1.drop('2016', 1)
# porque este periodo tiene muchos nulos, y hace perder filas en la reduccion
sin_columnas2015 = sin_columnas2016.drop('2015', 1)
# sin_columnas1.drop('2016', axis=1, inplace=True)
# sin_columnas2016.to_csv('salida.csv')


# elimino todas las filas que tienen algun valor nulos
sin_filas_nulas = sin_columnas2015.dropna()

# sin_filas_nulas.drop(sin_filas_nulas.columns[[0, 1, 3]], axis=1)
# elimino la primera columna (index)
# print sin_filas_nulas


# sin columna indice por ahora
sin_filas_nulas.to_csv('sin_filas_columnas_nulas.csv', index=False)

sin_filas_nulas_cuantos = sin_filas_nulas.shape[0]
print 'datos sin filas nulas ' + str(sin_filas_nulas_cuantos)

# print sin_filas_nulas

# counter_nan = datos_todos.isnull().sum()
# print 'counter nan ' + str(counter_nan)

# matriz pivoteada
# queremos las clases en filas y los criterios en columnas

matriz_pivoteada = sin_filas_nulas.set_index('Indicator Code').T
matriz_pivoteada_cuantos = matriz_pivoteada.shape[0]
print 'matriz pivoteada filas ' + str(matriz_pivoteada_cuantos)

matriz_pivoteada.to_csv('matriz_pivoteada.csv')
# En la matriz pivoteada se pueden ver algunas anomalias
# 1960-1983 tiene valores cero en TX.VAL.MRCH.R5.ZS	TX.VAL.MRCH.R4.ZS
# por ahora ignoramos


# obtengo las columnas feature
# x = matriz_pivoteada.ix[:, :-1].values
# print x
# x.to_csv('columnas_feature.csv')
