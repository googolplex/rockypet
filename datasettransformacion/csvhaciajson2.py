import csv
import json
import pandas as pd

# version pandas

# en modo local porque no tengo buen internet
csvfile = open('/home/xoldfusion/Descargas/machinelearning2017/cristhianrepo/tensor/datasetLab/cuantas_fotos.csv', 'r')

# para que se pueda emplear desde dentro del jupyter
# url = 'https://raw.githubusercontent.com/cristhianrey/tensor/master/datasetLab/cuantas_fotos_raw.csv'

# ejemplo ov = pd.read_csv("path/to/file.txt", sep='\t', header=None)
# ejemplo Cov.columns = ["Sequence", "Start", "End", "Coverage"]

datos = pd.read_csv(csvfile, sep='\t',names=["fecha","hora"])
jsonfile = open('/home/xoldfusion/Descargas/machinelearning2017/cristhianrepo/tensor/datasetLab/cuantas_fotos_raw.json', 'w')
# para sacar directo al new line delimited json del dataframe
salida = datos.to_json(orient='records').replace('},{','} \n{').replace('[{','{').replace('}]','}')
with jsonfile as f:
    f.write(salida)
print salida
