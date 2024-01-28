import os
import subprocess
import platform
import sys

def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {script_path}\nError: {e}")

def get_user_choice(options):
    return input(options).strip().lower()

# Set paths
base_folder = 'lang'
en_folder = os.path.join(base_folder, 'en')
it_folder = os.path.join(base_folder, 'it')
script_name = 'linux.py'
script_bash_en = os.path.join(en_folder, 'macos.sh')
script_bash_it = os.path.join(it_folder, 'macos.sh')

# Check macOS
if platform.system() == "Darwin":
    lang_mac = get_user_choice("Running on macOS, what language do you want to use?\n1. English\n2. Italian\n")

    if lang_mac in {"1", "2"}:
        run_script(script_bash_en if lang_mac == "1" else script_bash_it)
    else:
        print("Invalid choice")
        sys.exit()

# Ask language for non-macOS platforms
lang = get_user_choice("Which language do you prefer?\n1. English\n2. Italian\n")
selected_script = os.path.join(en_folder, script_name) if lang == "1" else os.path.join(it_folder, script_name) if lang == "2" else None

if selected_script:
    run_script(selected_script)
else:
    print("Invalid choice")
