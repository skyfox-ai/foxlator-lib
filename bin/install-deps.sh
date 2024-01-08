#!/bin/bash

echo "$ - installing python interpreter and necessary modules"
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update
sudo apt-get install -y python3.10 python3.10-distutils python3.10-venv ffmpeg

echo "$ - fixing ImageMagick detection bug"
mkdir -p /tmp/distr && \
    cd /tmp/distr && \
    wget https://download.imagemagick.org/ImageMagick/download/releases/ImageMagick-7.0.11-2.tar.xz && \
    tar xvf ImageMagick-7.0.11-2.tar.xz && \
    cd ImageMagick-7.0.11-2 && \
    ./configure --enable-shared=yes --disable-static --without-perl && \
    make && \
    make install && \
    ldconfig /usr/local/lib && \
    cd /tmp && \
    rm -rf distr

echo "$ - installing pip"
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

python3.10 -m pip install --upgrade -r ./build-requirements.txt

