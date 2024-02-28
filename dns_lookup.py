import dns.resolver
import sys

domain=input("Enter a domain name: ") 

# Finding A record 
result = dns.resolver.resolve(domain, 'A') 
# Printing record 
for val in result: 
    print('A Record : ', val.to_text())


# Finding A record 
result = dns.resolver.resolve(domain, 'A')   
# Printing record 
for val in result: 
    print('A Record : ', val.to_text())


result = dns.resolver.resolve(domain, 'NS') 
# Printing record 
for val in result: 
    print('NS Record : ', val.to_text()) 


result = dns.resolver.resolve(domain, 'MX') 
# Printing record 
for val in result: 
    print('MX Record : ', val.to_text())

result = dns.resolver.resolve(domain, 'SOA') 
# Printing record 
for val in result: 
    print('SOA Record : ', val.to_text()) 


result = dns.resolver.resolve(domain, 'TXT')   
# Printing record 
for val in result: 
    print('TXT Record : ', val.to_text())

input("\n\033[33mPress Enter to exit\n\n\033[0m")
sys.exit()

