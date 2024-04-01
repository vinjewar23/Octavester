import requests
import sys

ip_address = input("\033[1;31mEnter the IP address: ")
response = requests.get(f'http://ip-api.com/json/{ip_address}').json()


print('\033[1;36m\nTarget: ', response['query'])
print('IP: ', response['query'])
print('ASN: ', response['as'])
print('City: ', response['city'])
print('Country: ', response['country'])
print('Country Code: ', response['countryCode'])
print('ISP: ', response['isp'])
print('Latitude: ', str(response['lat']))
print('Longtitude: ', str(response['lon']))
print('Organization: ', response['org'])
print('Region Code: ', response['region'])
print('Region Name: ', response['regionName'])
print('Timezone: ', response['timezone'])
print('Zip Code: ', response['zip'])
print('Google Maps: ', 'http://www.google.com/maps/place/{0},{1}/@{0},{1},16z'.format(response['lat'], response['lon']))

input("\n\033[1;31mPress Enter exit\n\033[0m")
sys.exit()
