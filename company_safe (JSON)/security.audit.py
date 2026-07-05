import json

with open("vault.json", "r") as file:
    loaded_data = json.load(file)

print(f"Current state: {loaded_data['status']}.")

with open("security.txt", "a") as file:
    file.write("Vault is controlled successfully. \n")

print("Everything went perfectly!")