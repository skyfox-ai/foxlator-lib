#!/bin/bash

echo "$ - installing python interpreter and necessary modules"
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update
sudo apt-get install -y imagemagick

sudo apt-get install -y python3.10 python3.10-distutils python3.10-venv ffmpeg

echo "$ - installing pip"
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

python3.10 -m pip install --upgrade -r ./build-requirements.txt
python3.10 -m install moviepy[optional]
sudo sed -i '/<policy domain="path" rights="none" pattern="@\*"/d' /etc/ImageMagick-6/policy.xml