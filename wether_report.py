import requests
from bs4 import BeautifulSoup
from speak import speak
import json
from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests

def Temp():
    # URL of the website
    url = "https://www.accuweather.com/en/in/india-weather"

    # Send a GET request to the URL
    html_page = requests.get(url)

    # Parse the HTML code using BeautifulSoup
    soup = BeautifulSoup(html_page.content, "html.parser")

    # Find the temperature data using the appropriate tag and class name
    temperature = soup.find("div", {"class": "current-temp"})

    # Print the temperature data
    print(temperature)




def temcity():
    city = "Bengaluru"
    response = requests.get(endpoint, params={"q": city, "appid": api_key})
    data = json.loads(response.text)
    speak("Temperature in " + city + ": " + str(data["main"]["temp"]) + "°F")


