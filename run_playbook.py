import ansible_runner
import os

os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')

ansible_runner.interface.run(private_data_dir='./', playbook="hello.yml")