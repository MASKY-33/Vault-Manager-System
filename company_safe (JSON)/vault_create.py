import json

company_safe = {"status" : "locked", "code" : 9942}

with open("vault.json", "w") as file:

    json.dump(company_safe, file)

print("Features successfully saved in the database!")