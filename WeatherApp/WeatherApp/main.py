import tkinter as tk
from tkinter import ttk
import requests

def fetch_weather():
    city = city_entry.get()
    units = units_var.get()

    api_key = '8126dd844cc349d1672531254f616aa7'

    if units == "Celsius":
        units = "metric"
    elif units == "Kelvin":
        units = "standard"
    else:
        units = "imperial"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        result_label.config(
            text=f"Погода в {city}:\n"
                 f"Температура: {temperature}°{units_dict[units]}\n"
                 f"Вологість: {humidity}%\n"
                 f"Швидкість вітру: {wind_speed} м/с"
        )
        print(data)
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

app = tk.Tk()
app.title("Погода в містах світу")

result_label = tk.Label(app, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

city_label = tk.Label(app, text="Введіть місто:")
city_label.pack()
city_entry = tk.Entry(app, font=("Helvetica", 12))
city_entry.pack()

units_label = tk.Label(app, text="Обрати одиниці температури:")
units_label.pack()
units_var = tk.StringVar()
units_var.set("Celsius")  
units_option_menu = ttk.OptionMenu(app, units_var, "Celsius", "Celsius", "Fahrenheit", "Kelvin")
units_option_menu.pack()

fetch_button = tk.Button(app, text="Показати погоду", command=fetch_weather)
fetch_button.pack()

units_dict = {
    "metric": "°C",
    "imperial": "°F",
    "standard": "K",
}

app.mainloop()