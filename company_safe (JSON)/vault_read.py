import json

with open("vault.json", "r") as file:

    loaded_data = json.load(file)

print(f"The Vault is {loaded_data['status']}.")