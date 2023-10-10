"""Texts me the weather everyday."""

import schedule
import time
from twilio.rest import Client
import requests


def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data =response.json()
    return data


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def send_text_messages(body):
    account_sid = "ACf8246d4ae4f0a561e7942e9cf3a8bbb8"
    auth_token = "94f201ccdc4ec34c4058b42090375a76"
    from_phone_number = "+19175127684"
    to_phone_number = "+9103033216"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number

    )

    print("Text message sent!")


def send_weather_update():
    # NY City
    latitude: float = 40.7128
    longitude: float = -74.0060

    weather_data = get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature"]
    relative_humidity = weather_data["hourly"]["relativehumidity_2m"]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

    weather_info = (
        f"Kick the sheets!\n"
        f"The current weather in NY City:\n"
        f"Temperature: {temperature_fahrenheit:.2f} degrees Fahrenheit\n"
        f"Relative Humidity: {relative_humidity}\n"
        f"Wind Speed: {wind_speed} m/s"
        f"Eat more vegetables!"
    )

    send_text_messages(weather_info)

def main():
    # schedule.every().day.at("08:00").do(send_weather_update)
    schedule.every(10).seconds
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()