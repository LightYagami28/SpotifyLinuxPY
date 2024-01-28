chmod +x lang/en/macos.sh

echo "Proceeding to install Spotify..."
sleep 1.5
clear

# Run SpotX installation script
bash <(curl -sSL https://spotx-official.github.io/run.sh) -Bcd --installmac
