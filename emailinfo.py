
import requests
import sys
import json

email = input("\033[1;31mEnter the target mail address: ")
response = requests.get(f'https://emailrep.io/{email}')
response_json = json.loads(response.text)

print('\033[1;36m\nTarget: ', response_json['email'])
print('Suspicious: ', response_json['suspicious'])
print('Has response_jsonutation: ', response_json['reputation'])
print('Is blacklisted: ', response_json['details']['blacklisted'])
print('Has a malicious activity: ', response_json['details']['malicious_activity'])
print('Has a recent malicious activity: ', response_json['details']['malicious_activity_recent'])
print('Credentials leaked: ', response_json['details']['credentials_leaked'])
print('Is on a data breach: ', (response_json['details']['data_breach']))
print('Domain exists: ', (response_json['details']['domain_exists']))
print('Is a new domain: ', response_json['details']['new_domain'])
print('Is spam: ', response_json['details']['spam'])
print('Free provider: ', response_json['details']['free_provider'])
print('Temporary address: ', response_json['details']['disposable'])
print('Deliverable: ', response_json['details']['deliverable'])
print('Valid MX: ', response_json['details']['valid_mx'])
print('Primary Mail Exchanger: ', response_json['details']['primary_mx'])
print('Spoofable: ', response_json['details']['spoofable'])


input("\n\033[1;31mPress Enter to exit\n\n\033[0m")
sys.exit()
