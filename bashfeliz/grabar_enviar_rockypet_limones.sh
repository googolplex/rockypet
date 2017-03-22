#!/bin/bash
# hecho para mi pc de escritorio
# el 2017/03
rm *.*~
cp *.sh rockypet/bashfeliz
cd rockypet
git add -A
git commit -a -m "matriz pivoteada lista para el bigquery"
git push -u origin master
