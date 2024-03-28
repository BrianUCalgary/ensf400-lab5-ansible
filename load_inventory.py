import ansible_runner

ansible_runner.interface.get_inventory(action="list", inventories=["hosts.yml"], response_format="yaml")

ansible_runner.interface.run_command(executable_cmd="ansible all:localhost -m ping")