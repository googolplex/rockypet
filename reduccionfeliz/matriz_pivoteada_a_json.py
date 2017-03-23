import csv
import json
import pandas as pd
import subprocess

# version pandas + sftp
# llevo al JSON la matriz pivoteada, eso me evita definir a
# mano el esquema en el bigquery
csvfile = open('./matriz_pivoteada.csv', 'r')

# otra forma de agregarle nombres de columnas
# ejemplo ov = pd.read_csv("path/to/file.txt", sep='\t', header=None)
# ejemplo Cov.columns = ["Sequence", "Start", "End", "Coverage"]
# datos = pd.read_csv(csvfile, sep='\t', names=["fecha", "hora"])

datos = pd.read_csv(csvfile, sep=';', decimal=',')

# cambio los nombres de columnas para que sea compatible con el BIGQUERY
datos.rename(columns=lambda x: x.replace('.', '_'), inplace=True)
# datos.rename(columns=lambda x: x.replace(',', '","'), inplace=True)


jsonfile = open('matriz_pivoteada.json', 'w')
# para sacar directo al new line delimited json del dataframe
salida = datos.to_json(orient='records').replace(
    '},{', '} \n{').replace('[{', '{').replace('}]', '}')
with jsonfile as f:
    f.write(salida)

datos.to_csv('matriz_pivoteada_bigquery_ok.csv', index=False, sep=';', decimal='.')
# print salida
