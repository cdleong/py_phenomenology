#!/bin/bash

#conda update conda
#conda clean --all
#conda update --all

ENV_NAME="py_phenom_env"
#conda env remove -n "$ENV_NAME" 
conda env update --file py_phenom_env.yml 
#conda create -y --name "$ENV_NAME" python=3.6.6

#conda install -y -n "$ENV_NAME" geopandas xlrd
