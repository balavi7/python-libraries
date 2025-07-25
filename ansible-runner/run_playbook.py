import ansible_runner

result = ansible_runner.run(
    private_data_dir='.',
    playbook='/home/bala_pc/python_libs/ansible-runner/project/playbook.yaml',
    inventory='/home/bala_pc/python_libs/ansible-runner/inventory/hosts',
)

print("Status:", result.status)
print("RC:", result.rc)
print("Stdout:\n", result.stdout.read())

if result.rc != 0:
    print("❌ Playbook failed")
else:
    print("✅ Playbook ran successfully")
