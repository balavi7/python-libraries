**This library is mostly used to execute SSH commands remotely, loop over multiple servers, restart services etc.**


## Prerequisites
Install fabric using pip  
`pip3 install fabric`

## About the python script
In this case, this python script will first connect to the remote server using the host and the private key. You need to provide your host IP address, username and path of the private key.
Once connected, it will run the update packages command, and in the next command it will install Nginx.

## To run
`python3 remote_command.py`
