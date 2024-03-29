import tkinter as tk
import requests

window_height = 500
window_width = 600


def test_function(entry):
    print("This is a test: ", entry)


# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
    try:
        city_name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']

        menu = '******************** \n'
        result = 'City: %s \nConditions: %s \nTemperature (C°): %s' % (city_name, description, temperature)
        result = menu + result
    except:
        result = 'There was a problem retrieving that information'

    return result


def get_weather(city):
    weather_key = '75c820f8630ffd51e18f9ed9ffd46cf5'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)



window = tk.Tk()
window.title("Weather App v. 0.1 ")

canvas = tk.Canvas(window, height=window_height, width=window_width)
canvas.pack()

background_image = tk.PhotoImage(file='../meteo/icons/landscape.png')
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(window, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(window, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

window.mainloop()
