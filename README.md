# InvisibleMan
Hide your Ass by changing Public IP and userAgents in every 10 seconds - CYBERSECURITY

# ABOUT
Hackers hide their IP address so they can evade detection from security admins or security system logs, such as firewalls and Intrusion Detection Systems. Every time we send information out on the Internet from our computers, each packet contains an IP header, which stores the source IP address. That IP address can be logged depending on what we’re connecting to on the other side; therefore, it’s important that the IP address is obfuscated.

Maybe this will be among of challanges that can help you out to advice your organization to buy High standard security detection systems.
This peace of code will help you to archieve your dreams by forcing Tor to change IP in every request sent in 10 sec, so you will get public IP and fake user Agents in every 10 sec with out dropping a connection.
ENJOY
@Auxgrep

# DISCLAIMER
The information provided here is for educational purposes only. I am in no way responsible for any misuse of the information provided. All the information here is meant to provide the reader with the knowledge to defend against hackers and prevent the attacks.

# SETUP
1.sudo git clone https://github.com/AuxGrep/InvisibleMan
2.sudo chmod +x setup.sh
3.cd InvisibleMan

# RUN
```sudo python3 control_server.py ```

# TEST A SCAN 
use proxychains, your connection will pass to your established control_server for IP and Fake_userAgent assgnment
``` sudo proxychains nmap <host> -p 80 ``` or ```ssh -l root <serverIp> ``` or ```proxychains firefox https://google.com ``` 
