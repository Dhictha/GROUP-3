# Import necessary modules
from pip._vendor import requests
from pprint import pprint as pp

# Prompt user for the name of the country
name = input("Enter the name of the country: ")

# Construct the API endpoint for the given country
endpoint = f"https://restcountries.com/v3.1/name/{name}?fullText=true"

# Make the GET request to the API
response = requests.get(endpoint)

# Print the HTTP status code received from the API
print(response.status_code)

# Parse the JSON response data
data = response.json()

# Extract specific information from the response data
area_value = data[0]['area']
Population = data[0]['population']
Continent = data[0]['continents']
Languages = data[0]['languages']
Capital = data[0]['capital']
Timezone = data[0]['timezones']
Currencies = data[0]['currencies']
unMember = data[0]['unMember']

# Print information about the country
print("Area:", area_value)
print("Population:", Population)
print("Continent: ", Continent)
print("Languages: ", Languages)
print("Capital :", Capital)
print("Timezone: ", Timezone)
print("Currency :", Currencies)
print("Is UN Member: ", unMember)
