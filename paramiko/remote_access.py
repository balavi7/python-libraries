import paramiko

hostname = '3.108.237.209'
port = 22
username = 'ubuntu'
key_file = '/home/.ssh/new_key.pem'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, port=port, username=username, key_filename=key_file)

stdin, stdout, stderr = client.exec_command("ls -l")
print(stdout.read().decode())

client.close()
