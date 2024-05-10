import tkinter as tk
from tkinter import ttk
import requests
import sys
print(sys.path)

def get_weather():
    city = city_entry.get()
    unit = unit_var.get()
    
    if unit == "Celsius":
        unit = "metric"
    else:
        unit = "imperial"
        
    api_key = "493960142acebccb3ba21c30f34bd019"  # Your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != "404":
        temperature_label.config(text=f"Temperature: {data['main']['temp']} °{unit_var.get()[0]}")
        humidity_label.config(text=f"Humidity: {data['main']['humidity']} %")
        wind_speed_label.config(text=f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        temperature_label.config(text="City not found")

root = tk.Tk()
root.title("Weather App")

# Style
root.configure(bg="#f0f0f0")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

city_label = ttk.Label(frame, text="Enter City:")
city_label.grid(row=0, column=0, padx=5, pady=5)

city_entry = ttk.Entry(frame, width=20)
city_entry.grid(row=0, column=1, padx=5, pady=5)

unit_var = tk.StringVar()
unit_var.set("Celsius")
unit_label = ttk.Label(frame, text="Select Unit:")
unit_label.grid(row=1, column=0, padx=5, pady=5)

unit_option = ttk.OptionMenu(frame, unit_var, "Celsius", "Celsius", "Fahrenheit")
unit_option.grid(row=1, column=1, padx=5, pady=5)

weather_button = ttk.Button(frame, text="Show Weather", command=get_weather)
weather_button.grid(row=2, columnspan=2, padx=5, pady=5)

temperature_label = ttk.Label(frame, text="Temperature:")
temperature_label.grid(row=3, columnspan=2, padx=5, pady=5)

humidity_label = ttk.Label(frame, text="Humidity:")
humidity_label.grid(row=4, columnspan=2, padx=5, pady=5)

wind_speed_label = ttk.Label(frame, text="Wind Speed:")
wind_speed_label.grid(row=5, columnspan=2, padx=5, pady=5)

root.mainloop()
