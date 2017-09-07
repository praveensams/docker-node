from flask import Flask
import re
import docker

app = Flask(__name__)

@app.route('/')
def hello_world():
    l=[]
    client = docker.from_env()
    for i in client.containers.list():
        d=str(i).lstrip('<Container:').rstrip(">")
        l.append(d)

    return "%s"%str(l)

@app.route('/test')
def hello():
    l=[]
    client = docker.from_env()
    for i in client.containers.list():
        d=str(i).lstrip('<Container:').rstrip(">")
        l.append(d)

    return "%s"%str(l)

@app.route('/upload',methods=='POST')
def hell():
    l=[]
    client = docker.from_env()
    for i in client.containers.list():
        d=str(i).lstrip('<Container:').rstrip(">")
        l.append(d)
    return "%s"%str(l)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
