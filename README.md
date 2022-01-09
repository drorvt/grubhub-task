# demo-flask-app
### Build

```bash
$: docker build -t drorvt/flask_app:1.0
```

## How to run

You need to have all requirements installed.

### Local execution

```
DOCKER="python-app"
HELM_APP="app"

#Clone repository
git clone https://github.com/drorvt/grubhub-task

#Install dependencies locally assuming you have Mac machine and brew installed
#Python 
brew install python
#Pip
sudo easy_install pip
#Flask
pip3 install -r requirements.txt
#Helm 
brew install helm
```

### Run in Docker (meinheld)

```bash
#Make docker build to get image python-app:latest
cd flask-server
docker build -t $DOCKER:latest .
cd ..
echo "BUILD done"
echo "IMAGE $DOCKER:latest listed"
docker container ls
```

### Run in Kubernetes (Helm)
> Be sure to have Helm 3 installed: ([https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)

1) Edit `values.yaml` file in order to setup your environment.


```bash
$ helm install demo-flask-app . -n default

```
