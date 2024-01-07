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


## new function

def fetch_world_bank_data(country_code):
    # World Bank API URL for GDP indicator
    gdp_url = 'http://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/NY.GDP.MKTP.CD?format=json'
    
    # World Bank API URL for health expenditure indicator
    health_expenditure_url = 'http://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/SH.XPD.CHEX.GD.ZS?format=json'
    
    # World Bank API URL for hospital beds per 1000 people indicator
    hospital_beds_url = 'http://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/SH.MED.BEDS.ZS?format=json'
    
    # Replace {COUNTRY_CODE} with the desired country code
    # (e.g., 'US' for the United States, 'IN' for India, etc.)
    
    # Dictionary to store fetched data
    country_data = {}
    
    # Fetch GDP data
    response = requests.get(gdp_url.format(COUNTRY_CODE=country_code))
    if response.status_code == 200:
        gdp_data = response.json()[1]
        latest_gdp = next((x for x in gdp_data if x['value'] is not None), None)
        if latest_gdp:
            country_data['GDP_before_covid'] = latest_gdp['value']
        else:
            country_data['GDP_before_covid'] = None
    
    # Fetch health expenditure data
    response = requests.get(health_expenditure_url.format(COUNTRY_CODE=country_code))
    if response.status_code == 200:
        health_expenditure_data = response.json()[1]
        latest_health_expenditure = next((x for x in health_expenditure_data if x['value'] is not None), None)
        if latest_health_expenditure:
            country_data['Health_expenditure'] = latest_health_expenditure['value']
        else:
            country_data['Health_expenditure'] = None
    
    # Fetch hospital beds data
    response = requests.get(hospital_beds_url.format(COUNTRY_CODE=country_code))
    if response.status_code == 200:
        hospital_beds_data = response.json()[1]
        latest_hospital_beds = next((x for x in hospital_beds_data if x['value'] is not None), None)
        if latest_hospital_beds:
            country_data['Hospital_beds_per_1000'] = latest_hospital_beds['value']
        else:
            country_data['Hospital_beds_per_1000'] = None
    
    return country_data

# Replace 'US' with the desired country code
country_code = 'GH'

# Fetch data for the specified country
country_info = fetch_world_bank_data(country_code)

# Display the retrieved information
print("Information for Country:", country_code)
print("GDP before COVID:", country_info.get('GDP_before_covid'))
print("Health Expenditure:", country_info.get('Health_expenditure'))
print("Hospital Beds per 1000 people:", country_info.get('Hospital_beds_per_1000'))

## NEW FUNCTION

import requests
from pprint import pp

# Define the URL for the COVID-19 News API
url = "https://covid-19-news.p.rapidapi.com/v1/covid"

# Define query parameters for the API request
querystring = {"q":"covid","lang":"en","media":"True"}

# Set the headers including the RapidAPI key and host for authentication
headers = {
	"X-RapidAPI-Key": "d46123fc60msha5c4af93f2cd2a5p1da0dejsn6dae8e8c0828",
	"X-RapidAPI-Host": "covid-19-news.p.rapidapi.com"
}

# Make a GET request to the API with the specified URL, headers, and query parameters
response = requests.get(url, headers=headers, params=querystring)
response = response.json()

#Format on how the display will look like
for articles in response['articles']:
	print("Summary: " + articles['summary'])
	print("Author: " + articles['author'])
	print("Country: " + articles['country'])
	print("Link: " + articles['link'])
	print("Published Date: " + articles['published_date'])

	#Separator for each article
	print("-----------------------------------------------------")
	print("\n")
