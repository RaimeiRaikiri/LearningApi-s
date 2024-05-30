import requests

# Fetches quotes from api
response = requests.get("https://type.fit/api/quotes")

# Checks if the fetch went smoothly
if response.status_code == 200:
    # Converts data to dictionary
    quotes =  response.json()
    
    
