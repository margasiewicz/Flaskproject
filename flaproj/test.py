import requests

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?id=2643743&appid=9f9a3674336f713008ed8a10a57dff18"

    payload = ""
    headers = {
    'x-rapidapi-host': "AccuWeatherstefan-skliarovV1.p.rapidapi.com",
    'x-rapidapi-key': "9f9a3674336f713008ed8a10a57dff18",
    'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url)

    return response
response = get_weather()
print(response)