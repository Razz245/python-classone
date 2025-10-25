#!/bin/bash
# Matrix Hacker Animation - by Razz 😎💻

clear
green="\e[32m"
white="\e[97m"
reset="\e[0m"

cols=$(tput cols)
lines=$(tput lines)

echo -e "${white}Initializing Matrix environment...${reset}"
sleep 1
clear

while true; do
  for i in $(seq 1 $cols); do
    rand=$((RANDOM % 2))
    if (( rand == 0 )); then
      echo -ne "${green}$(tr -dc '01' < /dev/urandom | head -c 1)${reset}"
    else
      echo -ne " "
    fi
  done
  echo
  sleep 0.02
done
