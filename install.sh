#!/bin/bash

pip3 install -r requirements.txt

python3 ./install/create_infrastructure.py
python3 ./install/install_aws.py
python3 ./install/adding_crontab.py
python3 ./install/create_folder_paths.py