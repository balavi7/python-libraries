import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <env>")
    sys.exit(1)

env = sys.argv[1]
print(f"Deploying to environment: {env}")
# This code checks if an environment argument is provided and prints a message indicating the deployment environment.
