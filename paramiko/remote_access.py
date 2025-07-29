import paramiko

hostname = '13.233.98.222'
port = 22
username = 'ubuntu'
key_file = '/Downloads/new_key.pem'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, port=port, username=username, key_filename=key_file)

stdin, stdout, stderr = client.exec_command("ls -l")
print(stdout.read().decode())

client.close()
