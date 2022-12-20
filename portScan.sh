if  [ $1 ]; then
        ip_address=$1
        for port in $(seq 1 65535); do
                bash -c "echo '' > /dev/tcp/$ip_address/$port" 2>/dev/null && echo -e "${purpleColour}[*] Ports $port ${endColour}-> ${greenColour}OPEN${endColour}"
        done; wait
else
        echo -e "\n${yellowColour}[*]Incorrec use of code ./portScan 'ip_address'${endColour}\n"
fi