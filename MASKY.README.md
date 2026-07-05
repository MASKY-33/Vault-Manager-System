# Vault Manager System
This system manages a digital vault using a JSON file as its small database.
It demonstrates all CRUD operations plus a simple menu interface for controlling the vault.

## Features
- Stores vault data (status, code) in vault.json
- Reads the vault status from the JSON file
- Updates the vault status (locked/unlocked)
- Deletes the vault code from the database
- Logs security actions in security.txt
- Menu system for checking or changing the vault state
- Runs until the user types "stop" or chooses option 3

# How to use
Choose an option:
1 → Check the current vault status
2 → Lock or unlock the vault
3 → Exit the system

All changes are saved to vault.json.
Security actions are written to security.txt.


## Learning Purpose
Practice with:
- JSON file handling (read, write, update, delete)
- CRUD operations
- menu‑based systems
- exception‑free file operations
- simple state management
