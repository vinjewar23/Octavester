import sys
from colorama import Fore, Style
import hashlib
import json
import re
import requests
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from urllib.parse import urlencode

InputNumber = str(input("\033[1;31mEnter mobile number: "))

def formatNumber(InputNumber):
    return re.sub("(?:\+)?(?:[^[0-9]*)", "", InputNumber)

global number
global localNumber
global internationalNumber
global numberCountryCode
global numberCountry

print('\033[1;36m\nRunning local scan...')

FormattedPhoneNumber = "+" + formatNumber(InputNumber)

PhoneNumberObject = phonenumbers.parse(FormattedPhoneNumber, None)


number = phonenumbers.format_number(
        PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace('+', '')
numberCountryCode = phonenumbers.format_number(
        PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
numberCountry = phonenumbers.region_code_for_country_code(
        int(numberCountryCode))

localNumber = phonenumbers.format_number(
            PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace(numberCountryCode, '0')
internationalNumber = phonenumbers.format_number(
            PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

country = geocoder.country_name_for_number(PhoneNumberObject, "en")
location = geocoder.description_for_number(PhoneNumberObject, "en")
carrierName = carrier.name_for_number(PhoneNumberObject, 'en')

print('\nInternational format: {}'.format(internationalNumber))
print('Local format: 0{}'.format(localNumber))
print('Country found: {} ({})'.format(country, numberCountryCode))
print('City/Area: {}'.format(location))
print('Carrier: {}'.format(carrierName))
for timezoneResult in timezone.time_zones_for_number(PhoneNumberObject):
    print('Timezone: {}'.format(timezoneResult))

if phonenumbers.is_possible_number(PhoneNumberObject):
    print('The number is valid and possible.')
else:
    print('The number is valid but might not be possible.')




    
print('\nRunning Numverify.com scan...')

try:
    requestSecret = ''
    resp = requests.get('https://numverify.com/')
    soup = BeautifulSoup(resp.text, "html5lib")
except Exception as e:
    print('Numverify.com is not available')


for tag in soup.find_all("input", type="hidden"):
    if tag['name'] == "scl_request_secret":
        requestSecret = tag['value']
        break

apiKey = hashlib.md5((number + requestSecret).encode('utf-8')).hexdigest()

headers = {
        'Host': 'numverify.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://numverify.com/',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }

response = requests.request(
    "GET", "https://numverify.com/php_helper_scripts/phone_api.php?secret_key={}&number={}".format(apiKey, number), data="", headers=headers)

data = json.loads(response.content.decode('utf-8'))


InternationalNumber = '({}){}'.format(
    data["country_prefix"], data["local_format"])

print(("\nNumber: ({}) {}").format(data["country_prefix"], data["local_format"]))
print(("Country: {} ({})").format(data["country_name"], data["country_code"]))
print(("Location: {}").format(data["location"]))
print(("Carrier: {}").format(data["carrier"]))
print(("Line type: {}").format(data["line_type"]))

if data["line_type"] == 'landline':
    print(("This is most likely a landline, but it can still be a fixed VoIP number."))
elif data["line_type"] == 'mobile':
    print(("This is most likely a mobile number, but it can still be a VoIP number."))

input("\n\033[1;31mPress Enter to exit\n\n\033[0m")
sys.exit()


