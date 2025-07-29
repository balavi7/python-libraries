## Prerequistes
- Make sure your cluster is running (Minikube, kund or EKS)
- Kubectl should be working

In this library, we have two files where one is a basic deployment file in which you spin you an Nginx container with two replicas. The other file is the python script which will list all the pods available across all the namespcaes.

## To run
- `pip3 install kubernetes`  
- `python3 list_all_pods.py`
