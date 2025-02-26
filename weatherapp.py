import requests
import os
from bs4 import BeautifulSoup
from tkinter import Label, Tk
from PIL import ImageTk, Image

cwd = os.getcwd()
pictureLoc1 = str(cwd) + "\\cloudy.png"

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_ = "CurrentConditions--location--yub4l").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text
    weatherPred = soup.find("div", class_ = "CurrentConditions--phraseValue---VS-k").text

    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPred)

    temperatureLabel.after(60000, getWeather)
    master.update()
url = "https://weather.com/weather/today/l/73775994a7930975506f2796531c2564e93815bc2ccaafc200f80950408ffa07"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open(pictureLoc1)
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)



locationLabel = Label(master, font = ("Calibri bold", 20), bg = "white")
locationLabel.grid(row = 0, sticky = "N", padx = 100)

temperatureLabel = Label(master, font = ("Calibri bold", 70), bg = "white")
temperatureLabel.grid(row = 1, sticky = "W", padx = 40)

Label(master, image = img, bg = "white").grid(row = 1, sticky = "E")

weatherPredictionLabel = Label(master, font = ("Calibri bold", 15), bg = "white")
weatherPredictionLabel.grid(row = 2, sticky = "W", padx = 40)

getWeather()
master.mainloop()
