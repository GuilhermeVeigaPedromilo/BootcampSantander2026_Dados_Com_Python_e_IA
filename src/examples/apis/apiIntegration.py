import requests
import json

url = "https://brasilapi.com.br/api/cambio/v1/"

response = requests.get(url + "moedas", verify= False) # Use verify = false if you have problems of SSL/TLS

data = []

try:
    print("\nCurrently currents (Structure in portuguese):")
    data = response.json()
except response.status_code != 200 as e:
    print(f"\nBad return. Status Code (HTTP): {response.status_code}")
    print("Error: ", e)

for row in data:
    print(row)

currency = input("\nEnter the a currency to search data of the trade it with BRL: ")
date = input("Date to search: ")

newResponse = requests.get(url + f"cotacao/{currency}/{date}", verify=False)
newResponse.json()


print("\nResult: ", )
for row in newResponse:
    print(row)