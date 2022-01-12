#!/bin/bash

DOCKER="python-app"
HELM_APP="app"

#Clone repository
git clone https://github.com/drorvt/grubhub-task.git

#Install dependencies locally assuming you have Mac machine and brew installed
#Python 
brew install python3
#Pip
sudo easy_install pip3
#Flask
pip3 install -r flask-app/requirements.txt
#Helm 
brew install helm
pip install pick

#Run unit tests to app.py
python app/tests/test.py

#Make docker build to get image python-app:latest
cd flask-app
docker build -t $DOCKER:v6 .
cd ..
echo "BUILD done"
echo "IMAGE $DOCKER:v6 listed"
docker container ls
