echo "Restarting port " $1

ufw deny $1
ufw allow $1