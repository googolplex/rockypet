#!/bin/bash
# hecho para mi pc de escritorio
# el 2017/03
rm *.*~
cp *.sh rockypet/bashfeliz
cd rockypet
git add -A
git commit -a -m "instalo t-sne en la pc"
git push -u origin master
