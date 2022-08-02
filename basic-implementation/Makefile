start:
	minikube start

clean:
	kubectl delete -f ./artifacts/kong-manifest.yaml

go:
	helm dep up ./helm/kong
	helm template kong ./helm/kong > ./artifacts/kong-manifest.yaml

	kubectl apply -f ./artifacts/kong-manifest.yaml
	sleep 10
	minikube tunnel