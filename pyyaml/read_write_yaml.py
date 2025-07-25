import yaml
with open('/home/bala_pc/python_libs/pyyaml/pod.yaml', 'r') as file:
    pod_data = yaml.safe_load(file)
print(pod_data)
# This code reads a YAML file containing pod configuration and prints the parsed data.