# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "AF": "Afghanistan",
    "AU": "Australia",
    "SG": "Singapore",
    "SO": "Somalia",
    "RU": "Russian Federation",
    "NP": "Nepal",
}

# TODO: Print the country for the given country code
# TODO: # If the key is not found, print Unknown
country_code = input("Enter country code: ")
print(country_codes.get(country_code, "Unknown"))
# TODO: Print all codes
# TODO: Print all countries
for countryco1 in country_codes.values():
    print(countryco1)
for countryco2 in country_codes.keys():
    print(countryco2)
for countryco3 in country_codes.items():
    print(countryco3)
