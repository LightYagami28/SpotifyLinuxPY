import os
import subprocess
import platform

# Set paths
base_folder = 'lang'
en_folder = os.path.join(base_folder, 'en')
it_folder = os.path.join(base_folder, 'it')
script_name = 'linux.py'
script_bash_en = os.path.join(en_folder, 'macos.sh')
script_bash_it = os.path.join(it_folder, 'macos.sh')

# Check macOS
if platform.system() == "Darwin":
    lang_mac = input("Running on macOS, what language do you want to use?\n1. English\n2. Italian\n")
    selected_script = script_bash_en if lang_mac == "1" else script_bash_it if lang_mac == "2" else None

    if selected_script:
        subprocess.run(['bash', selected_script], check=True)
    else:
        print("Not a valid choice")
    exit()

# Ask language for non-macOS platforms
lang = input("Which language do you prefer?\n1. English\n2. Italian\n")
selected_script = os.path.join(en_folder, script_name) if lang == "1" else os.path.join(it_folder, script_name) if lang == "2" else None

if selected_script:
    subprocess.run(['python', selected_script])
else:
    print("Not a valid choice")
