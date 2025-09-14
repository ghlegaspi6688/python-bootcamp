import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

if response.status_code == 200:
    data = response.json()
    print(data['rates']['PHP'])

else:
    print("Failed. Server said:", response.status_code)
# Get the latest conversion rate from USD to PHP
print()
