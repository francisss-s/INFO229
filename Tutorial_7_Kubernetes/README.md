#Tutorial de kubernetes

####que es Kubernetes?
Kubernetes es una plataforma de código abierto para automatizar la implementación, el escalado y la administración de aplicaciones en contenedores

#### Introduccion
En Kubernetes se utiliza la api API de Kubernetes para describir el estado deseado del clúster: qué aplicaciones u otras cargas de trabajo se quieren ejecutar, qué imagenes de contenedores usan, el número de replicas,etc

Una vez que se especifica el estado deseado, el Plano de Control de Kubernetes realizará las acciones necesarias para que el estado actual del clúster coincida con el estado deseado. Para ello, Kubernetes realiza diferentes tareas de forma automática, como pueden ser: parar o arrancar contenedores, escalar el número de réplicas de una aplicación dada, etc.

### instalar kubernetes
1.- Descargar la última entrega
```
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
```
2.- Habilita los permisos de ejecución del binario kubectl
```
    chmod +x ./kubectl
```

3.- Mueve el binario dentro de tu PATH.
```
    sudo mv ./kubectl /usr/local/bin/kubectl
```

4.- instalar mediente gestor de paquetes
```
    sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2 curl
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
    sudo apt-get update
    sudo apt-get install -y kubectl
```
5.- instalar minikube para manejar los cluster de forma local
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

### primer Miniduke
crearemos un cluster basico
1.- inicia el cluster local
```
minikube start
```
2.- Crear un Deployment
    primero necesitamos saber que un pod es un conjunto de uno o mas contenedores, y que al hacer un deployment verifica el estado del pod y reinicia el contendor si es que este fuera eliminado
    Los Deployments son la manera recomendada de manejar la creación y escalación.

2.1.- Ejecutar el comando kubectl create para crear un Deployment que maneje un Pod. El Pod ejecuta un contenedor basado en la imagen proveida por Docker
```
kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
```
2.2 Ver el Deployment
```
kubectl get deployments
```

2.3 Ver el Pod
```
kubectl get pods
```

2.4 Ver los eventos del clúster
```
kubectl get events
```

3.- Crear un service
Por defecto, el Pod es accedido por su dirección IP interna dentro del clúster de Kubernetes, para hacer que el contenedor hello-node sea accesible desde afuera de la red virtual Kubernetes, se debe exponer el Pod como un Service de Kubernetes.

3.1 Exponer el Pod a la red pública de internet utilizando el comando kubectl expose:
```
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
```
3.2 Ver el Service creado
```
kubectl get services
```
3.3 Ejecutar el comando
```
minikube service hello-node
```

4.- Limpieza

Ahora se puede eliminar los recursos creados en el clúster
```
#para elminiar los servicios creados
kubectl delete service hello-node

#para eliminar los deployments creados
kubectl delete deployment hello-node

#denener la maquna virtual que se creo al principio
minikube stop

#eliminar la maquina virtual
minikube delete

```
