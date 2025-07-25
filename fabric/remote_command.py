from fabric import Connection

conn = Connection(
    host="13.127.179.12", 
    user="ubuntu", 
    connect_kwargs={"key_filename": "/mnt/d/Users/91966/Downloads/new_key.pem"}
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