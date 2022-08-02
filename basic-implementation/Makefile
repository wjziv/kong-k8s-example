start:
	minikube start

clean:
	kubectl delete -f kong-1.0.0-manifest.yaml

go:
	helm dep up ./helm/kong
	helm package ./helm/kong
	helm template kong kong-1.0.0.tgz > kong-1.0.0-manifest.yaml
	kubectl apply -f kong-1.0.0-manifest.yaml
	sleep 10
	minikube tunnel