# Kong Gateway on k8s

This project deploys Kong as a reverse-proxy gateway on minikube.

It services a single backend application, an [echo-server](https://github.com/Ealenn/Echo-Server).

## Requirements

- helm v3
- minikube

## Instructions

While `cd`'d into this directory...

Run `minikube start` to start a new cluster.

Install the kong implementation with  `make start`.

Make requests to the Kong gateway through `localhost:80`.

The echo-server is found at `localhost/echo`.

When finished, clean up everything with `make stop`.

Kill the cluster with `minikube stop`.
