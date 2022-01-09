#!/bin/bash

DOCKER="python-app"
HELM_APP="app"

#Clone repository
git clone https://github.com/drorvt/grubhub-task.git

#Install dependencies locally assuming you have Mac machine and brew installed
#Python 
brew install python
#Pip
sudo easy_install pip
#Flask
pip3 install -r requirements.txt
#Helm 
brew install helm

#Run unit tests to app.py
python app/tests/test.py

#Make docker build to get image python-app:latest
cd flask-server
docker build -t $DOCKER:latest .
cd ..
echo "BUILD done"
echo "IMAGE $DOCKER:latest listed"
docker container ls
