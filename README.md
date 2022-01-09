# demo-flask-app
### Build

```bash
$: docker build -t drorvt/flask_app:1.0
```

## How to run

You need to have all requirements installed.

##Run automated deployment script

Run the deployment script, automation.sh. For this you need to run the following command:


```bash
$ chmod +x automation.sh
$ ./automation.sh
```

### Run in Kubernetes (Helm)
> Be sure to have Helm 3 installed: ([https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)

1) Edit `values.yaml` file in order to setup your environment.


```bash
$ helm install demo-flask-app . -n default

```
### Run github action ci :
```bash
### install EKS :
goto actions press on terraform and run workflows

### deploy helm app :
goto actions press on HELM and run workflows
```
