chmod +x lang/it/macos.sh

echo "Installing Homebrew and Spotify..."
sleep 1.5
wait
clear
bash <(curl -sSL https://spotx-official.github.io/run.sh) -Bcd --installmac
