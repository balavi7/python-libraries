import docker

client = docker.from_env()
containers = client.containers.run("nginx", detach=True, name="my_nginx", ports={'80/tcp': 9000})
print ("STarted Container", containers.name)
print("Container ID:", containers.id)
print("Container Status:", containers.status)

