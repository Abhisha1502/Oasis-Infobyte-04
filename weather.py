import tkinter as tk
from tkinter import messagebox, ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Insert your OpenWeatherMap API key here
API_KEY = "948e10991727e32d0c5a7d261ffa5443"

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def kelvin_to_fahrenheit(kelvin):
    return round((kelvin - 273.15) * 9/5 + 32, 2)

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    unit = unit_var.get()
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = data['weather'][0]['description'].title()
        icon_code = data['weather'][0]['icon']
        temp_k = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        if unit == "Celsius":
            temp = f"{kelvin_to_celsius(temp_k)} °C"
        else:
            temp = f"{kelvin_to_fahrenheit(temp_k)} °F"

        # Update GUI
        weather_label.config(text=f"Condition: {weather}")
        temp_label.config(text=f"Temperature: {temp}")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")

        # Load weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        img_data = icon_response.content
        img = Image.open(BytesIO(img_data))
        icon = ImageTk.PhotoImage(img)
        icon_label.config(image=icon)
        icon_label.image = icon

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"API Request Failed: {e}")
    except KeyError:
        messagebox.showerror("Error", "City not found. Try another city.")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack()

unit_var = tk.StringVar(value="Celsius")
ttk.Combobox(root, textvariable=unit_var, values=["Celsius", "Fahrenheit"]).pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, bg="#3498db", fg="white", font=("Arial", 12)).pack(pady=10)

icon_label = tk.Label(root)
icon_label.pack()

weather_label = tk.Label(root, font=("Arial", 12))
weather_label.pack()

temp_label = tk.Label(root, font=("Arial", 12))
temp_label.pack()

humidity_label = tk.Label(root, font=("Arial", 12))
humidity_label.pack()

wind_label = tk.Label(root, font=("Arial", 12))
wind_label.pack()

root.mainloop()

