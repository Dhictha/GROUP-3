#PROJECT ON COVID-19
#Retrieving data from the COVID-19 API
from pip._vendor import requests
from pprint import pprint as pp

country = input("Enter the country of your choice: ")
endpoint_url = f"https://disease.sh/v3/covid-19/countries/{country}"
 
response = requests.get(endpoint_url)
print(response.status_code)
 
data = response.json()

pp(data)

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

# Print information about the country
print("Area:", area_value)
print("Population:", Population)
