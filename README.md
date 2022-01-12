# demo-flask-app
### Build

```bash
$: docker build -t flaskapp .
$: docker images
$: docker tag <imageid> drorvt/flaskapp
$: docker push drorvt/flaskapp
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
### verify route working 

```bash
$: kubectl --namespace default port-forward svc/appflask-k8-helm  32077:5000
$: Open in Browser :
"http://localhost:32077/pods"
"http://localhost:32077/me"
"http://localhost:32077/health"
"http://localhost:32077/"

```
