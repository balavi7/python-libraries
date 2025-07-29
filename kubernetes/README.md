## Prerequistes
- Make sure your Cluster is Running (Minikube, kind or EKS)
- Kubectl should be working

In this library, we have two files where one is a basic deployment file in which you spin you an Nginx container with two replicas. This is a YAML file just in case if you need to check additional custom pods to be listed then you can deploy the same. The other file is the python script which will list all the pods available across all the namespcaes.

## To run
- `pip3 install kubernetes`  
- `python3 list_all_pods.py`
