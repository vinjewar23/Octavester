import os 
import sys

#check if running as root
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] Octavester must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")


print("""

 / _ \  ___| |_ __ ___   _____  ___| |_ ___ _ __ 
| | | |/ __| __/ _` \ \ / / _ \/ __| __/ _ \ '__|
| |_| | (__| || (_| |\ V /  __/\__ \ ||  __/ |   
 \___/ \___|\__\__,_| \_/ \___||___/\__\___|_| 

""")

#functions
print("\033[1;91m1. Mobile Number Information")
print("2. Email Information")
print("3. IP Geolocation")
print("4. Location Graber")
print("5. Subdomain Finder")
print("6. DNS Lookup")
print("7. IP Scanner")
print("8. Encrypt & Decrypt text")
print("0. Exit \033[1;m")

option = (input("\033[1;34m \nEnter your choice: \033[1;94m"))

if(option == "0"):
    sys.exit()


elif(option == "1"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                          Mobile Number Information                          █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("python phonenoinfo.py")


elif(option == "2"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                              Email Information                              █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("python emailinfo.py")


elif(option == "3"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                               IP GeoLocation                                █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("python IPGEO.py")


elif(option == "4"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                             Location Graber                                 █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("cd location && ./location.py")


elif(option == "5"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                             Subdomain Finder                                █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("python subdomain.py")


elif(option == "6"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                               DNS LOOKUP                                    █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("python dns_lookup.py ")


elif(option == "7"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                               IP SCANNER                                    █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("python ipscanner.py ")

elif(option == "8"):
    print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════════════════┐
█                                                                             █
█                             Encrypt & Decrypt                               █ 
█                                                                             █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
    command = os.system("python vigenere.py ")
