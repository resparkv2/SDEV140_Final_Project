import requests
import os
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import ImageTk, Image

cwd = os.getcwd()
pictureLoc1 = str(cwd) + "\\cloudy.png"

def getFishersWeather():
    url = "https://weather.com/weather/today/l/73775994a7930975506f2796531c2564e93815bc2ccaafc200f80950408ffa07" 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_ = "CurrentConditions--location--yub4l").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text
    weatherPred = soup.find("div", class_ = "CurrentConditions--phraseValue---VS-k").text

    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPred)

    carmelButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.NORMAL)
    fishersButton.config(state = tk.DISABLED)

    temperatureLabel.after(60000, getFishersWeather)
    master.update()

def getCarmelWeather():
    url = "https://weather.com/weather/today/l/e26b2194d6f80bdb4b821313b1cff7352e643869ce69dacfc9bfc10b2dfdd2cb" 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_ = "CurrentConditions--location--yub4l").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text
    weatherPred = soup.find("div", class_ = "CurrentConditions--phraseValue---VS-k").text

    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPred)

    fishersButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.NORMAL)
    carmelButton.config(state = tk.DISABLED)

    temperatureLabel.after(60000, getCarmelWeather)
    master.update()

def getNoblesvilleWeather():
    url = "https://weather.com/weather/today/l/442e2584ec0fb4766e9030444eaa55ed476b6e9a2c58fe62af93040e101b5933" 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_ = "CurrentConditions--location--yub4l").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text
    weatherPred = soup.find("div", class_ = "CurrentConditions--phraseValue---VS-k").text

    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPred)

    fishersButton.config(state = tk.NORMAL)
    carmelButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.DISABLED)

    temperatureLabel.after(60000, getNoblesvilleWeather)
    master.update()

def getIndianapolisWeather():
    url = "https://weather.com/weather/today/l/1fadb5d65825dc7bf21e6e498bc46194118171fedee813143ae33e4e0907114c" 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_ = "CurrentConditions--location--yub4l").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text
    weatherPred = soup.find("div", class_ = "CurrentConditions--phraseValue---VS-k").text

    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPred)

    fishersButton.config(state = tk.NORMAL)
    carmelButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.DISABLED)

    temperatureLabel.after(60000, getIndianapolisWeather)
    master.update()


master = tk.Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open(pictureLoc1)
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

locationLabel = tk.Label(master, font = ("Calibri bold", 20), bg = "white")
locationLabel.grid(row = 0, sticky = "N", padx = 100)

temperatureLabel = tk.Label(master, font = ("Calibri bold", 70), bg = "white")
temperatureLabel.grid(row = 1, sticky = "W", padx = 40)

tk.Label(master, image = img, bg = "white").grid(row = 1, sticky = "E")

weatherPredictionLabel = tk.Label(master, font = ("Calibri bold", 15), bg = "white")
weatherPredictionLabel.grid(row = 2, sticky = "W", padx = 40)

fishersButton = tk.Button(master, text = "Fishers Weather", bg = "white", command = getFishersWeather)
fishersButton.grid(row = 3, column = 0)

carmelButton = tk.Button(master, text = "Carmel Weather", bg = "white", command = getCarmelWeather)
carmelButton.grid(row = 3, column = 1)

noblesvilleButton = tk.Button(master, text = "Noblesville Weather", bg = "White", command = getNoblesvilleWeather)
noblesvilleButton.grid(row = 4, column = 0)

indianapolisButton = tk.Button(master, text = "Indianapolis Weather", bg = "White", command = getIndianapolisWeather)
indianapolisButton.grid(row = 4, column = 1)

master.mainloop()
