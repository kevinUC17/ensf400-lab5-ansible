import ansible_runner
import requests

# Write your answer here by modifying or extending the sample code below

with open("./secrets/id_rsa", "r") as f:
    ssh_key = f.read()
    
r = ansible_runner.run(private_data_dir=".", playbook='./hello.yml', inventory='./hosts.yml', ssh_key=ssh_key)


url = "http://0.0.0.0"
print("\nChecking for Server Response...")
for i in range(10):
    response = requests.get(url)
    if response.status_code == 200:
        print("Response:", response.text)
    else:
        print("Failed to connect to the server.")
print("Ending Program...")