#! /bin/bash
set -e
echo "Setting up deps"

sudo apt-get update

sudo apt-get install python3-pip

# ensure we have pyenv so we can install a valid version of python.
curl https://pyenv.run | bash
echo "pyenv init - | source" > ~/.config/fish/config.fish
pyenv init - | source

# make sure we have pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

# make sure we have ssl
pip install pip --upgrade
pip install pyopenssl --upgrade



# install 3.10
pyenv install 3.10

pyenv global 3.10


# ensure that we have docker
curl https://get.docker.com | bash
sudo groupadd docker
sudo usermod -aG docker $USER

# package deps
pip install poetry 
poetry install

