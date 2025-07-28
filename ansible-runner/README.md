# Prerequisites

- Install the library using pip  
`pip3 install ansible-runner`
- Ansible runner expects a standard folder strcuture  
my-project/  
├── inventory/  
│   └── hosts  
├── project/  
│   └── playbook.yml  
├── env/  
│   └── envvars  
├── run_playbook.py

- To execute the file  
`python3 run_playbook.py`

- If the SSH and host settings are correct, you should see the following:  
  Connect to the server  
  Update the Cache  
  Install and start Nginx  

**Replace IP address, Ansible user, Ansible_ssh_private_key, playbook and inventory according to your actual path**
