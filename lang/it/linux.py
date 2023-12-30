import time
import os
import subprocess
import sys
import platform
import flatpak

# Package lists
package_names = ['git', 'zip', 'unzip', 'flatpak']
package_names_gentoo = ['dev-vcs/git', 'app-arch/unzip', 'app-arch/zip', 'flatpak']
package_names_nixos = ['nixpkgs.git', 'nixpkgs.unzip', 'nixpkgs.zip', 'nixpkgs.flatpak']

#link
command = "bash <(curl -sSL https://spotx-official.github.io/run.sh) -cd"

# Check distro
print("Procedo a controllare che distro stai usando")
time.sleep(1.5)
os.system('clear')

# Clear screen function
def clear_screen():
    os.system('clear')

# Check Wi-Fi status and decide whether to proceed
def is_wifi_active():
    system = platform.system()

    if system == "Linux":
        try:
            result = subprocess.run(['nmcli', 'radio', 'wifi'], capture_output=True, text=True, check=True)
            return result.stdout.strip() == 'enabled'
        except subprocess.CalledProcessError as e:
            print(f"Errore nel controllare il wifi: {e}")
            return False
    else:
        print("Il controllo del wifi è supportato solo su linux.")

if not is_wifi_active():
    print("Il Wifi non è attivo. Assicurati il wifi sia collegato e funzionante, poi riprova.")
    sys.exit(1)  # Exit the script with exit code 1 (error)

# Logic to check distro with package manager
def install_packages(package_manager, package_names):
    try:
        subprocess.run(['sudo', package_manager, '--yes'] + package_names, check=True)
        print(f"I pacchetti {', '.join(package_names)} sono stati installati con successo.")
        clear_screen()
        print("Procedo a installare Spotify")
        time.sleep(1.5)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'installazione dei pacchetti: {e}")

#install spotify 
def install_flatpak_package(application_id):
    # Create a Flatpak installation reference
    installation = flatpak.Installation(system=True)

    # Check if the package is already installed
    if installation.exists(application_id):
        print(f"Questo pacchetto di flatpak '{application_id}' è già installato.")
    else:
        # Install the Flatpak package
        installation.install_user(application_id)
        print(f"Il pacchetto '{application_id}' è stato con successo installato.")

os.system('clear')
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Errore nel eseguire il comando: {e}")

install_flatpak_package("com.spotify.Client")
# Call functions with package lists
install_packages('apt', package_names)
install_packages('pacman', package_names)
install_packages('dnf', package_names)
install_packages('zypper', package_names)
install_packages('yum', package_names)
install_packages('emerge', package_names_gentoo)
install_packages('xbps-install', package_names)
install_packages('nix-env', package_names_nixos)