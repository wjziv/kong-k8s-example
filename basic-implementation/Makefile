stop:
	helm uninstall kong

start:
	helm dep up ./helm/kong
	helm install kong ./helm/kong

	sleep 10
	minikube tunnel
