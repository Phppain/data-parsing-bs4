"""get_weather.py"""

import requests
from bs4 import BeautifulSoup

def get_weather_with_split(url):
    response = requests.get(url)
    html = response.text
    start = html.split('class="DailyContent')
    start2 = start[5].split('dir="ltr">')
    weather = start2[-1].split('<span')
    return weather[0]

def get_weather_with_bs4(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('index.html', 'w') as f:
        f.write(response.text)
    span = soup.find_all('span', {"class": "DailyContent--temp--1s3a7", "dir": "ltr"})
    weather = span[0].get_text()
    return weather

if __name__ == "__main__":
    url = "https://weather.com/weather/tenday/l/Astana+Kazakhstan?canonicalCityId=0bb785ac3ae4aaeb7e158822878142002426b317e0ef09021e2553aa99be357e"
    weather = get_weather_with_split(url)
    print(f"Температура в Астане: {weather}ºF")

    weather = get_weather_with_bs4(url)
    print(f"Температура в Астане: {weather}F")
