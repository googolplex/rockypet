import csv
import json
import pandas as pd
import subprocess

# version pandas + sftp
# 20170321a intento leer directo desde el server SFTP
# 20170321a porque tengo problemas con el GOOGLE DRIVE + MULTCLOUD, no lee bien desde alli

# ejemplo con sftp
# no lo hago con python porque gnu linux resuelve mejor este problema

bashCommand = "./traer_csvfeliz.sh"
salida = subprocess.check_output(['bash', '-c', bashCommand])
print salida
# para que se pueda emplear desde dentro del jupyter
# url = 'https://raw.githubusercontent.com/cristhianrey/tensor/master/datasetLab/cuantas_fotos.csv'
csvfile = open('./cuantas_fotos.csv', 'r')

# otra forma de agregarle nombres de columnas
# ejemplo ov = pd.read_csv("path/to/file.txt", sep='\t', header=None)
# ejemplo Cov.columns = ["Sequence", "Start", "End", "Coverage"]
# datos = pd.read_csv(csvfile, sep='\t', names=["fecha", "hora"])

datos = pd.read_csv(csvfile, sep='\t', names=["fecha", "hora"])
jsonfile = open(
    '/home/xoldfusion/Descargas/machinelearning2017/cristhianrepo/tensor/datasetLab/cuantas_fotos_raw.json', 'w')
# para sacar directo al new line delimited json del dataframe
salida = datos.to_json(orient='records').replace(
    '},{', '} \n{').replace('[{', '{').replace('}]', '}')
with jsonfile as f:
    f.write(salida)
# print salida
