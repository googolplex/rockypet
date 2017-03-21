#!/bin/bash
# sudo apt-get -y install build-essential python-dev python-setuptools \
#                      python-numpy python-scipy \
#                      libatlas-dev libatlas3gf-base

sudo pip install cython
git clone "https://github.com/scikit-learn/scikit-learn.git"
cd scikit-learn
make
sudo python setup.py install
