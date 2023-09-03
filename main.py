import os, json

# --- SETTINGS ---
language = "de_DE"
path = "C:\Riot Games\League of Legends\LeagueClient.exe"


# --- SAVE SYSTEM ---

# Get the user's Documents folder
documents_folder = os.path.expanduser("~")
config_folder = os.path.join(documents_folder, "Documents", "LEAGUE-LANGUAGE-HELPER")

# Ensure the config folder exists, create it if not
if not os.path.exists(config_folder):
    os.makedirs(config_folder)

# Define the path to the JSON file
json_file_path = os.path.join(config_folder, "config.json")

def save_config(data):
    # Save data to the JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

def load_config():
    # Load data from the JSON file, if it exists
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as json_file:
            return json.load(json_file)
    else:
        return None



def main():
    # state 1 - return screen
    # state 2 - config change
    # state 3 - path creation
    # state 4 - lang creation
    state = 0

    config = load_config()

    if (config):
        try:
            language = config["language"]
            path = config["path"]

            state = 1
        except:
            print("Failed to load config.")
            state = 0

    run = True
    user_input = ""
    state_text = {
        1: f"1 - Start game\n2 - Change config\n\nCurrent config:\n   Language - {language} | Path - {path}",
        2: f"1 - Change path\n2 - Change language",
        3: "Enter path:",
        4: "Enter language (format: en_EN):"
    }
    
    while run:
        if state == 0:
            state = 3

        if state == 1:
            if (user_input == "1"):
                run = False
            
            if (user_input == "2"):
                state = 2
            
            user_input = ""
        
        if state == 2:
            if (user_input == "1"):
                state = 3
            
            if (user_input == "2"):
                state = 4

            user_input = ""

        if state == 3:
            if (user_input != ""):
                path = user_input

                if config:
                    state = 1
                else:
                    state = 4

            user_input = ""

        if state == 4:
            if (user_input != ""):
                language = user_input
            
                state = 1

            user_input = ""


        if not run:
            break

        state_text = {
            1: f"1 - Start game\n2 - Change config\n\nCurrent config:\n   Language - {language} | Path - {path}",
            2: f"1 - Change path\n2 - Change language",
            3: "Enter path:",
            4: "Enter language (format: en_EN):"
        }

        print("\n"*60)
        print("League Language Helper - By Zewenn", "\n"*5)
        print(f'{state_text[state]}\n')
        user_input = input("> ").strip()


    os.system(f'"{path}" --locale={language}')


    config = {
        "language": language,
        "path": path
    }
    save_config(config)

if __name__ == "__main__":
    main()