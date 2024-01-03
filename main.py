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