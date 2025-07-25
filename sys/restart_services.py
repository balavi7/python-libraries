# restart_service.py
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python restart_service.py <service-name>")
    sys.exit(1)

service = sys.argv[1]
print(f"Restarting {service}...")
os.system(f"sudo systemctl restart {service}")
# This script restarts a specified service using systemctl.
