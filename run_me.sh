#!/usr/local/bin/bash

cd $IKS_BASE_DIR
# source .venv/bin/activate
#python src/python/iks.py $IKS_MENU_DIR $@
#poetry run python3 src/python/iks.py $@
python3 iks/iks.py $@
