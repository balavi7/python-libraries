from fabric import Connection

conn = Connection(
    host="3.108.237.209", 
    user="ubuntu", 
    connect_kwargs={"key_filename": "/home/.ssh/new_key.pem"}
) 

def setup_nginx():
    print("Update the packages list..")
    conn.run("sudo apt-get update", hide=False)
    print("Install Nginx..")
    conn.run("sudo apt-get install -y nginx", hide=False)
    print("NGINX installed successfully.")

setup_nginx()
# This code connects to a remote host using Fabric and runs a command to get the system name
# and prints the output.
