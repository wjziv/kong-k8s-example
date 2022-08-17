stop:
	helm uninstall kong

start:
	docker build . -t custom-kong:1.0.0
	minikube image load custom-kong:1.0.0

	helm dep up ./helm/kong
	helm install kong ./helm/kong

	sleep 10
	minikube tunnel
