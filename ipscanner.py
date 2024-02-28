import os 
import sys

ip = input("\033[31mEnter the IP address: \033[31m")

while(True):
    print("\033[1;91m1. Port Scanning")
    print("2. Version Detection Scan")
    print("3. Vulnerability Scan")
    print("99. Exit\033[1;m")

    option = int(input("\033[36m\nEnter your option: \033[1;m"))

    if(option == 1):
        print(""" \033[1;33m
    ┌═════════════════════════════════════════════════════════════════════════════┐
    █                                                                             █
    █                              Port Scanning                                  █ 
    █                                                                             █
    └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
        command = os.system("nmap "+ip)



    elif(option == 2):
        print(""" \033[1;36m
    ┌═════════════════════════════════════════════════════════════════════════════┐
    █                                                                             █
    █                           Version Detection Scan                            █ 
    █                                                                             █
    └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
        command = os.system("nmap -sV "+ ip)

        

    elif(option == 3):
        print(""" \033[1;36m
    ┌═════════════════════════════════════════════════════════════════════════════┐
    █                                                                             █
    █                             Vulnerability Scan                              █ 
    █                                                                             █
    └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
        command = os.system("nmap -sV -sC "+ ip)

    elif(option == 99):
        input("\n\033[33mPress Enter to exit\n\n\033[0m")
        sys.exit()



