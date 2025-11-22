# Workbench Webserver v2

## Introduction

This is the webserver made for the jarransworkbench.com site
This version is made to host different projects on subdomains
This version is also built on Flask

## Infrastucture

### AWS
This is meant to run on an AWS lightsail instance
The keypair for SSH access to the instance should be stored as PersonalServerKey.pem
After making the lightsail instance, assign it a static IP

## Deployment
Use the deploy.py script to deploy the server both locally (for testing) and remotely
```
./deploy.py local
```