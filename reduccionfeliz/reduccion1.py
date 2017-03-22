# estudio la matriz de ejemplo de siraj Raval
# reescrito para practicar por GOOGOL PLEX
# el 2017.03

import sys
import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.manifold import TSNE


print (sys.executable)
print (sys.version)
origen = os.getcwd() + '/rogerrepo/rockypet/reduccionfeliz/pml-training.csv'
print origen


csvfile = open(origen, 'r')
datos_todos = pd.read_csv(csvfile, sep=',')
num_rows = datos_todos.shape[0]
print 'filas ' + str(num_rows)
counter_nan = datos_todos.isnull().sum()
# print son las columnas con valores nulos
# print "contador nulos"
# print counter_nan
counter_without_nan = counter_nan[counter_nan == 0]
# print "contador sin nulos"
# son las columnas que no tienen valores nulos
# print counter_without_nan
datos_sin_nulos = datos_todos[counter_without_nan.keys()]
# print datos_sin_nulos
# elimino las columnas que no hacen nada
dataframe_all = datos_sin_nulos.ix[:, 7:]
# print dataframe_all
# obtengo los nombres de las columnas
columns = dataframe_all.columns
# print columns
# obtengo las columnas feature y escalo

x = dataframe_all.ix[:, :-1].values
# print x
standard_scaler = StandardScaler()
x_std = standard_scaler.fit_transform(x)

# print x_std

# obtengo las etiquetas de clase, que estan en la ultima columna todas las filas

y = dataframe_all.ix[:, -1].values
# print y
# obtengo los valores unicos de las clases
class_labels = np.unique(y)
# print class_labels
# convierto las etiquetas en numeros
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
# print y

# parto los datos en dos conjuntos
# el de prueba y el de entrenamiento

test_percentage = 0.1
x_train, x_test, y_train, y_test = train_test_split(
    x_std, y, test_size=test_percentage, random_state=0)

# le aplico el t-sne
# t-distributed Stochastic Neighbor Embedding (t-SNE) visualization

tsne = TSNE(n_components=2, random_state=0)
x_test_2d = tsne.fit_transform(x_test)

markers = ('s', 'd', 'o', '^', 'v')
# hago hashes con los colores
color_map = {0: 'red', 1: 'blue', 2: 'lightgreen', 3: 'purple', 4: 'cyan'}
plt.figure()
# print np.unique(y_test)
# print enumerate(np.unique(y_test))

for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_test == cl, 0], y=x_test_2d[
                y_test == cl, 1], c=color_map[idx], marker=markers[idx], label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()
