#!/usr/local/bin/bash

cd $IKS_BASE_DIR
source venv/bin/activate
#python src/python/iks.py $IKS_MENU_DIR $@
python src/python/iks.py $@
