start:
	minikube start

clean:
	kubectl delete -f ./artifacts/kong-1.0.0-manifest.yaml

go:
	helm dep up ./helm/kong
	helm package ./helm/kong --destination ./artifacts
	helm template kong ./artifacts/kong-1.0.0.tgz > ./artifacts/kong-1.0.0-manifest.yaml
	kubectl apply -f ./artifacts/kong-1.0.0-manifest.yaml
	sleep 10
	minikube tunnel