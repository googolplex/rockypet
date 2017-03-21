#!/bin/bash
# hecho para mi pc de escritorio
# el 2017/03
rm *.*~
cp *.sh rockypet/
cd rockypet
git add -A
git commit -a -m "inicio del proyecto rockypet"
git push -u origin master
