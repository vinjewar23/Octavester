import sys
import nmap 

ip = input("\033[1;31mEnter the IP address: ")
print('\n')

while(True):
    print("\033[1;36m1. Port Scanning")
    print("2. Version Detection Scan")
    print("99. Exit\033[1;m")

    option = int(input("\033[1;36m\nEnter your option: \033[1;36m"))

    if(option == 1):
        print(""" \033[1;36m
    ┌═════════════════════════════════════════════════════════════════════════════┐
    █                                                                             █
    █                              Port Scanning                                  █ 
    █                                                                             █
    └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
        # initialize the port scanner
        nmScan = nmap.PortScanner()

        # scan for ports in range 21-443
        nmScan.scan(ip)

        # run a loop to print all the found result about the ports
        for host in nmScan.all_hosts():
            print('\033[1;36mHost : %s ' % (host))
            print('State : %s' % nmScan[host].state())
            for proto in nmScan[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
 
                lport = nmScan[host][proto].keys()
                lport=sorted(lport)
            for port in lport:
                print ('port : %s\tstate : %s ' % (port, nmScan[host][proto][port]['state']))
            print('\n \033[1;m')


    elif(option == 2):
        print(""" \033[1;36m
    ┌═════════════════════════════════════════════════════════════════════════════┐
    █                                                                             █
    █                           Version Detection Scan                            █ 
    █                                                                             █
    └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
        # initialize the port scanner
        nmScan = nmap.PortScanner()

        # scan for ports in range 21-443
        nmScan.scan(ip, arguments='-sV')

        # run a loop to print all the found result about the ports
        for host in nmScan.all_hosts():
            print('\033[1;36mHost : %s ' % (host))
            print('State : %s' % nmScan[host].state())
            for proto in nmScan[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
 
                lport = nmScan[host][proto].keys()
                lport=sorted(lport)
            for port in lport:
                print ('port : %s\tstate : %s\tService : %s\tVersion : %s ' % (port, nmScan[host][proto][port]['state'],nmScan[host][proto][port]['name'],nmScan[host][proto][port]['product']))
            print('\n \033[1;m')
        

    elif(option == 99):
        input("\n\033[1;31mPress Enter to exit\n\n\033[0m")
        sys.exit()



