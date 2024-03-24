import os
import ansible_runner
import re

# get list of changed ansible configuration values
out, err = ansible_runner.get_ansible_config(action='dump',  config_file= os.getcwd() + '/ansible.cfg', only_changed=True)

# get ansible inventory information
out, err = ansible_runner.get_inventory(
    action='list',
    inventories=['./hosts.yml'],
    response_format='json',
)

# get ip address

#print("out: {}".format(out))
#print("err: {}".format(err))
print("\n\n*************************************************************\n")
for group_name in out['all']["children"]:
    if group_name != "ungrouped":
        print(f"Group_name: {group_name}")
        for i in out[group_name]['hosts']:
            print(f"-Name: {i}")
            print(f" -IP: {out['_meta']['hostvars'][i]['ansible_host']}")
        print()
print("*************************************************************")
print('\n')

# Create a runner object and run the command: "ansible all:localhost -m ping"
ansible_runner.interface.run_command("ansible", [
    "-i","./hosts.yml",
    "--private-key", "./secrets/id_rsa",
    "all:localhost",
    "-m", "ping"
])

