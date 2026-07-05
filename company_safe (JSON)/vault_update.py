import json

with open("vault.json", "r") as file:
    loaded_data = json.load(file)

    loaded_data["status"] = "unlocked"

with open("vault.json", "w") as file:
        json.dump(loaded_data, file)

print(f"Alarm: The Vault is {loaded_data['status']}!")