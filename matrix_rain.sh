#!/bin/bash
# Matrix Rain Effect - by Razz 😎💻


green="\e[32m"
reset="\e[0m"
cols=$(tput cols)

clear
echo -e "${green}Initializing Matrix rain...${reset}"
sleep 1
clear

while true; do
  for ((i=1; i<=cols; i++)); do
    char=$(tr -dc '01' < /dev/urandom | head -c 1)
    printf "${green}%s${reset}" "$char"
  done
  sleep 0.05
  echo ""
done
