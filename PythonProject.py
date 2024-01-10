#PROJECT ON GLOBAL PANDEMIC (COVID19) TRACKING APP
##RETRIEVING HEALTH(COVID) RELATED NEWS FROM THE NEWS API
from pip._vendor import requests
from pprint import pp

# URL for the COVID-19 News API
url = "https://covid-19-news.p.rapidapi.com/v1/covid"

# Query parameters for the API request
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

#Print GEOGRAPHICAL information of a country from REST API
#Prompt user for the name of the country
country = input("Enter the country of your choice: ")

# Construct the API endpoint for the given country
endpoint = f"https://restcountries.com/v3.1/name/{country}?fullText=true"

# Make the GET request to the API
response = requests.get(endpoint)

# Print the HTTP status code received from the API
print(response.status_code)

# Parse the JSON response data
data = response.json()

# Extract specific information from the response data
continent = data[0]['continents']
area_value = data[0]['area']
Population = data[0]['population']
Capital = data[0]['capital']
Timezone = data[0]['timezones']
Languages = data[0]['languages']
Currencies = data[0]['currencies']
unMember = data[0]['unMember']
print()

# Print information about the country
print(f"{country} is located in {continent}. It has an area of {area_value} and {Population} number of people. \nThe capital of {country} is {Capital} and their timezone is {Timezone}. \nThey speak these languages {Languages} and their currency is {Currencies}.")
print("Is UN Member: ", unMember)

# Construct the API endpoint for COVID-19 data by country
endpoint1 = f"https://disease.sh/v3/covid-19/countries/{country}"
response = requests.get(endpoint1)

if response.status_code == 200:
    data = response.json()
    #Extract necessaary information
    cases = data['cases']
    deaths = data['deaths']
    recovered = data['recovered']
    population = data['population']
    tests = data['tests']
    #Calculate tested positive and negative cases
    tested_positive = cases
    tested_negative = tests - cases
    population_left_after_covid = population - deaths
    print()
    #Print information about the country's population, deaths, population left after COVID(affected&un-affected) and tested positive & negative
    print(f"{country} has a total population of {population} people.")
    print(f"Out of the {population} people, {tested_positive} tested positive for COVID-19 and {tested_negative} tested negative.")
    print(f"Fortunately, some people survived COVID-19, but the number of people who couldn't survive were {deaths}. Thats very unfortunate!")
    print(f"Population left after COVID: {population_left_after_covid}")
else:
    print("Failed to fetch data for the country. Please check the country name or try again later.")
print()

#Pretty print the updated data dictionary
#Print if you want more COVID related info for the country
pp(data)
print() 
#Retrieving data from the WORLD BANK API
#Function to fetch data from the World Bank API
def fetch_world_bank_data(country_code):
    # World Bank API URL for GDP indicator
    gdp_url = 'http://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/NY.GDP.MKTP.CD?format=json'
    
    # World Bank API URL for health expenditure indicator
    health_expenditure_url = 'http://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/SH.XPD.CHEX.GD.ZS?format=json'
    
    # World Bank API URL for hospital beds per 1000 people indicator
    hospital_beds_url = 'http://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/SH.MED.BEDS.ZS?format=json'

    
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

# Enter the country code e.g('NG' for Nigeria, 'KE' for Kenya)
country_code = input("Enter the country code: ")

# Fetch data for the specified country
country_info = fetch_world_bank_data(country_code)

# Display the retrieved information
print("Information for Country:", country_code)
print("GDP before COVID:", country_info.get('GDP_before_covid'))
print("Health Expenditure:", country_info.get('Health_expenditure'))
print("Hospital Beds per 1000 people:", country_info.get('Hospital_beds_per_1000'))

#TOP 10 AFFECTED COUNTRIES
# Construct the endpoint URL for all countries
all_countries_endpoint = "https://disease.sh/v3/covid-19/countries"

# Make the GET request
response = requests.get(all_countries_endpoint)

# Check the response status code
if response.status_code == 200:
    # Parse the response data for all countries
    all_countries_data = response.json()

    # Sort the countries by deaths in descending order
    top_10_countries = sorted(all_countries_data, key=lambda x: x.get("deaths", 0), reverse=True)[:10]

    # Print the top 10 countries
    print("Top 10 countries by deaths:")
    for country in top_10_countries:
        print(f"{country['country']}: {country['deaths']}")
else:
    print(f"Failed to retrieve data for all countries. Status code: {response.status_code}")


