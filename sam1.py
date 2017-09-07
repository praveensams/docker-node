from flask import Flask
import re
import docker
l=[]

client = docker.from_env()
for i in client.containers.list():
	d=str(i).lstrip('<Container:').rstrip(">")
	l.append(d)

print str(l)
	
	
