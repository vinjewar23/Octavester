import requests
 
# function for scanning subdomains
def domain_scanner(domain_name,sub_domain_names):
    print('-----------Scanner Started-----------')
    print('----------Subdomains found:----------')

    for subdomain in sub_domain_names:
       
        # making url by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"
         
        # using try catch block to avoid crash of
        # the program
        try:  
            requests.get(url) 
            # is valid then printing the url
            print(f'[+] {url}')
             
        # if url is invalid then pass it
        except requests.ConnectionError:
            pass
    print('\n')
    print('----Scanning Finished----')
    print('-----Scanner Stopped-----')
 
# main function
if __name__ == '__main__':
   
    # inputting the domain name
    domain_name = input("Enter the Domain Name:")
    print('\n')
 
    # opening the subdomain text file
    with open('subdomains.txt','r') as file:
       
        # reading the file
        name = file.read()
         
        # using splitlines() function storing the 
        # list of splitted strings
        sub_domain = name.splitlines()
         
    domain_scanner(domain_name,sub_domain)
