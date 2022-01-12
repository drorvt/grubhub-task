from flask import Flask
from flask import request
from flask import jsonify
from requests.utils import default_headers
from kubernetes import client, config, watch
import os


app = Flask(__name__)
@app.route('/')
def index():
    return 'Web App with Python Flask!'
    
@app.route('/pods')
def get_pod():
    #config.load_kube_config()

    config.load_incluster_config()
    v1 = client.CoreV1Api()
    
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    
    return "%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name)

@app.route('/me')
def get_ip():
    #config.load_kube_config()

    config.load_incluster_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s" % (i.status.pod_ip))
    
    return "%s" % (i.status.pod_ip)

@app.route("/health")
def health():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
