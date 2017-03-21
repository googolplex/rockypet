import csv
import json
import urllib2

# para que sea compatible con el upload de google
# para que se pueda emplear desde dentro del jupyter
# url = 'https://raw.githubusercontent.com/cristhianrey/tensor/master/datasetLab/cuantas_fotos_dia_hh_cantidad.csv'

url = 'https://raw.githubusercontent.com/cristhianrey/tensor/master/datasetLab/cuantas_fotos_raw.csv'
response = urllib2.urlopen(url)

csv.register_dialect('nublado', delimiter='\t', quoting=csv.QUOTE_NONE)
# csvfile = open('/home/xoldfusion/Descargas/machinelearning2017/cristhianrepo/tensor/datasetLab/cuantas_fotos_raw.csv', 'r')
jsonfile = open('/home/xoldfusion/Descargas/machinelearning2017/cristhianrepo/tensor/datasetLab/cuantas_fotos_raw.json', 'w')

fieldnames = ("fecha","hora")
# reader = csv.DictReader(csvfile, fieldnames,dialect='nublado')
reader = csv.DictReader(response, fieldnames,dialect='nublado')
for row in reader:
    json.dump(row,jsonfile)
    jsonfile.write('\n')

#    salida = json.dumps([row for row in reader])
#  jsonfile.write('\n')
