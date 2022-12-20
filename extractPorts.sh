echo -e "\n${purpleColour}[*] Extracting information...${endColour}\n"
	ip_address=$(cat $1 | grep -oP "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" | sort -u) 
	open_ports=$(cat $1 | grep -oP "\d{1,5}/[open/tcp]" | awk '{print $1}' FS="/" | xargs | tr " " ",") 
	echo -e "\t${blueColour}[*] IP Address: ${endColour}${yellowColour}$ip_address${endColour}"
	echo -e "\t${blueColour}[*] Ports Open: ${endColour}${yellowColour}$open_ports${endColour}\n"
	echo $open_ports | tr -d '\n' | xclip -sel clip
	echo -e "${turquoiseColour}[*] Ports has been copied to clipboard${endColour}\n"