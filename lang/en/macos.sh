chmod +x lang/en/macos.sh

echo "I procede to install Spotify"
sleep 1.5
wait
clear
bash <(curl -sSL https://spotx-official.github.io/run.sh) -Bcd --installmac	
