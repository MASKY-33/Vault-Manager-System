import json

with open("vault.json", "r") as file:
    loaded_data = json.load(file)

    del loaded_data["code"]

with open("vault.json", "w") as file:
    json.dump(loaded_data, file)

print("The 'code' is successfully deleted from the file.")