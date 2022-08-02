# Kong Gateway on k8s

This project deploys Kong as a reverse-proxy gateway on minikube.

It services a single backend application, an [echo-server](https://github.com/Ealenn/Echo-Server).

## Requirements

- kubectl
- helm v3
- minikube

## Instructions

While `cd`'d into this directory...

Run `make go`.

Make requests to the Kong gateway through `localhost:80`.

The echo-server is found at `localhost/echo`.

When finished, clean up with `make clean`
