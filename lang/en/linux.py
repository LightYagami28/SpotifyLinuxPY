import time
import os
import subprocess

print("I’ll check what distro you’re using")
time.sleep(1.5)
os.system('clear')

import subprocess

def install_packages_with_apt(package_names):
    try:
        subprocess.run(['sudo', 'apt', 'install', '-y'] + package_names, check=True)
        print(f"I pacchetti {', '.join(package_names)} sono stati installati con successo.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'installazione dei pacchetti: {e}")

# Lista di pacchetti da installare
packages_to_install_apt = ['git', 'zip', 'unzip', 'curl', 'flatpak']
packages_to_install_pacman = ['git', 'zip', 'unzip', 'curl', 'flatpak']
packages_to_install_dnf = ['git', 'zip', 'unzip', 'curl', 'flatpak']
packages_to_install_yum = ['git', 'zip', 'unzip', 'curl', 'flatpak']
packages_to_install_xbps = ['git', 'zip', 'unzip', 'curl', 'flatpak']
packages_to_install_zypper = ['git', 'zip', 'unzip', 'curl', 'flatpak']
packages_to_install_emerge = ['git', 'zip', 'unzip', 'curl', 'flatpak']
packages_to_install_nix = ['nixos.git', 'nixos.zip', 'nixos.unzip', 'nixos.curl', 'nixos.flatpak']

# Chiamare la funzione con la lista di pacchetti
install_packages_with_apt(packages_to_install_apt)

