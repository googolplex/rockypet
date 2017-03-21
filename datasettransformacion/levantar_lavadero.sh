#!/bin/bash
# para levantar datos al bigquery lavadero
# 2017.3.21a
# requiere el google client:w


# gcloud auth login
# gcloud config set project lavadero-1469906906353

bq load --replace --source_format=CSV --encoding="UTF-8" --field_delimiter="\t" lavadero-1469906906353:tesis2016_roque_dennis.cuantas_fotos ./cuantas_fotos.csv  ./esquemafeliz.txt
# para ver cuantas filas quedaron
bq show lavadero-1469906906353:tesis2016_roque_dennis.cuantas_fotos
