import docker 

client = docker.from_env()
#container = client.containers.run("ubuntu", detach=True)
containers = client.containers.list()
for container in containers:
    print("Container ID:", container.id)
    print("Container Status:", container.status)
    print("container Name:", container.name)
