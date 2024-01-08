#!/bin/bash

echo "$ - installing python interpreter and necessary modules"
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update
sudo apt-get install -y python3.10 python3.10-distutils python3.10-venv ffmpeg imagemagick

echo "$ - Checking ImageMagick" 
command -v convert >/dev/null 2>&1 || { echo >&2 "ImageMagick is not installed"; exit 1; }

echo "$ - Configure ImageMagick policy"
sudo cat /etc/ImageMagick-6/policy.xml \
          | sed 's/none/read,write/g' \
          | sudo tee /etc/ImageMagick-6/policy.xml

echo "$ - installing pip"
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

python3.10 -m pip install --upgrade -r ./build-requirements.txt
