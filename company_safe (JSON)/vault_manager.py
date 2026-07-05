import json


while True:
    print("\n--- Vault Manager System ---")
    choice = input("Choose: 1. Check status, 2. Lock/Unlock, 3 = Stop: ")


    if choice == "3" or choice.lower() == "stop":
        print("Bye!")
        break


    elif choice == "1":
        with open("vault.json", "r") as file:
            loaded_data = json.load(file)
            
        print(f"Current state: {loaded_data['status']}")

        with open("security.txt", "a") as file:
            file.write("Vault has been successfully controlled. \n")
    

    elif choice == "2":
        new_status = input("Give in the new status (locked/unlocked): ").lower()

        with open("vault.json", "r") as file:
            loaded_data = json.load(file)

            loaded_data["status"] = new_status

        with open("vault.json", "w") as file:
            json.dump(loaded_data, file)
            
            
        print("Database successfully updated!")