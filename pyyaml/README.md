**Pyyaml is a Python library which basically lets you read YAML files and write into YAML files. In short it can validate or update existing YAMLs before applying, also it can be used in automating CI/CD pipeline configs.**

## Prerequisites
- Install pyyaml  
`pip3 install pyyaml`
- A running pod  
`kubectl apply -f pod.yaml`

## About the script
**In this script you will need to provide the location of the YAML file which needs to be read and once executed the output is given in a JSON format**

## To run
`python read_write_yaml.py`
