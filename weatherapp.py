import requests
import os
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import ImageTk, Image

#Changes the picture based on what the predicition says
def changePicture(prediction):

    #Forces all charaters to become lowercase
    tempPrediction = prediction.lower()

    #Determines what is in the temperature label
    #and changes the picture accodingly
    if "watch" in tempPrediction:
        imageLabel.config(image = watchImg, padx = 200)
    elif "rainy" in tempPrediction:
        imageLabel.config(image = rainyImg, padx = 200)
    elif "cloudy" in tempPrediction:
        imageLabel.config(image = cloudyImg, padx = 200)
    elif "showers in vicinity" in tempPrediction:
        imageLabel.config(image = showersInVicinityImg, padx = 200)
    elif "sunny" in tempPrediction:
        imageLabel.config(image = sunnyImg, padx = 200)
    elif "fair" in tempPrediction:
        imageLabel.config(image = fairImg, padx = 200)
    elif "wind" in tempPrediction:
        imageLabel.config(image = windyImg, padx = 200)
    elif "snow" in tempPrediction:
        imageLabel.config(image = snowImg, padx = 200)
    else:
        imageLabel.config(image = errorImg, padx = 200)

def updateTimeLabel():
    timeUrl = "https://www.timeanddate.com/worldclock/"
    timePage = requests.get(timeUrl)
    timeSoup = BeautifulSoup(timePage.content, "html.parser")
    time = timeSoup.find("td", id = "p59", class_ = "rbi").text

    timeLabel.config(text = time)

def updateDateLabel():
    dateUrl = "https://www.timeanddate.com/"
    datePage = requests.get(dateUrl)
    dateSoup = BeautifulSoup(datePage.content, "html.parser")
    date = dateSoup.find("span", id = "ij2").text

    dateLabel.config(text = date)

#Gets the information from the website and updates labels accordingly
def getWebsiteInfoAndUpdateLabels(inUrl):
    page = requests.get(inUrl)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_ = "CurrentConditions--location--yub4l").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text
    weatherPred = soup.find("div", class_ = "CurrentConditions--phraseValue---VS-k").text

    locationLabel.config(text = location)
    temperatureLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPred)
    changePicture(weatherPred)

    updateTimeLabel()
    updateDateLabel()

#Gets the weather for Fishers and updates the labels accordingly
def getFishersWeather():
    url = "https://weather.com/weather/today/l/73775994a7930975506f2796531c2564e93815bc2ccaafc200f80950408ffa07" 
    
    getWebsiteInfoAndUpdateLabels(url)

    #Changes the state of the buttons so that the
    #same one isn't clicked twice in a row
    carmelButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.NORMAL)
    fishersButton.config(state = tk.DISABLED)

    #Updates the window every 60 seconds
    temperatureLabel.after(60000, getFishersWeather)

#Gets the weather for Carmel and updates the labels accordingly
def getCarmelWeather():
    url = "https://weather.com/weather/today/l/e26b2194d6f80bdb4b821313b1cff7352e643869ce69dacfc9bfc10b2dfdd2cb" 
    
    getWebsiteInfoAndUpdateLabels(url)

    #Changes the state of the buttons so that the
    #same one isn't clicked twice in a row
    fishersButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.NORMAL)
    carmelButton.config(state = tk.DISABLED)

    #Updates the window every 60 seconds
    temperatureLabel.after(60000, getCarmelWeather)

#Gets the weather for Noblesville and updates the labels accordingly
def getNoblesvilleWeather():
    url = "https://weather.com/weather/today/l/442e2584ec0fb4766e9030444eaa55ed476b6e9a2c58fe62af93040e101b5933" 
    
    getWebsiteInfoAndUpdateLabels(url)

    #Changes the state of the buttons so that the
    #same one isn't clicked twice in a row
    fishersButton.config(state = tk.NORMAL)
    carmelButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.DISABLED)

    #Updates the window every 60 seconds
    temperatureLabel.after(60000, getNoblesvilleWeather)

#Gets the weather for Indianapolis and updates the labels accordingly
def getIndianapolisWeather():
    url = "https://weather.com/weather/today/l/1fadb5d65825dc7bf21e6e498bc46194118171fedee813143ae33e4e0907114c" 
    
    getWebsiteInfoAndUpdateLabels(url)

    #Changes the state of the buttons so that the
    #same one isn't clicked twice in a row
    fishersButton.config(state = tk.NORMAL)
    carmelButton.config(state = tk.NORMAL)
    noblesvilleButton.config(state = tk.NORMAL)
    indianapolisButton.config(state = tk.DISABLED)

    #Updates the window every 60 seconds
    temperatureLabel.after(60000, getIndianapolisWeather)



#Gets the current working directory
cwd = os.getcwd()

#Sets the image location into a variable for future use
homeImgLoc = str(cwd) + "\\home.png"
cloudyImgLoc = str(cwd) + "\\cloudy.png"
showersInVicinityImgLoc = str(cwd) + "\\showers_in_vicinity.png"
sunnyImgLoc = str(cwd) + "\\sunny.png"
watchImgLoc = str(cwd) + "\\watch.png"
rainyImgLoc = str(cwd) + "\\rainy.png"
errorImgLoc = str(cwd) + "\\error.png"
fairImgLoc = str(cwd) + "\\fair.png"
windyImgLoc = str(cwd) + "\\windy.png"
snowImgLoc = str(cwd) + "\\snow.png"

#Gets the current time
timeUrl = "https://www.timeanddate.com/worldclock/"
timePage = requests.get(timeUrl)
timeSoup = BeautifulSoup(timePage.content, "html.parser")
time = timeSoup.find("td", id = "p59", class_ = "rbi").text

#Gets the current Date
dateUrl = "https://www.timeanddate.com/"
datePage = requests.get(dateUrl)
dateSoup = BeautifulSoup(datePage.content, "html.parser")
date = dateSoup.find("span", id = "ij2").text


#Creates the window
master = tk.Tk()
master.title("Weather App")
master.config(bg = "#90D5FF")

#Opens the deafult image, resizes it, then sets it to homeImg
homeImg = Image.open(homeImgLoc)
homeImg = homeImg.resize((150, 150))
homeImg = ImageTk.PhotoImage(homeImg)

#Opens the cloudy image, resizes it, then sets it to cloudyImg
cloudyImg = Image.open(cloudyImgLoc)
cloudyImg = cloudyImg.resize((150, 150))
cloudyImg = ImageTk.PhotoImage(cloudyImg)

#Opens the showers in vicinity image, resizes it, then sets it to showersInVicinityImg
showersInVicinityImg = Image.open(showersInVicinityImgLoc)
showersInVicinityImg = showersInVicinityImg.resize((150, 150))
showersInVicinityImg = ImageTk.PhotoImage(showersInVicinityImg)

#Opens the sunny image, resizes it, then sets it to sunnyImg
sunnyImg = Image.open(sunnyImgLoc)
sunnyImg = sunnyImg.resize((150, 150))
sunnyImg = ImageTk.PhotoImage(sunnyImg)

#Opens the watch image, resizes it, then sets it to watchImg
watchImg = Image.open(watchImgLoc)
watchImg = watchImg.resize((150, 150))
watchImg = ImageTk.PhotoImage(watchImg)

#Opens the rainy image, resizes it, then sets it to rainyImg
rainyImg = Image.open(rainyImgLoc)
rainyImg = rainyImg.resize((150, 150))
rainyImg = ImageTk.PhotoImage(rainyImg)

#Opens the error image, resizes it, then sets it to errorImg, happens when
#the program doesn't recognize any of the words in the weather prediction
errorImg = Image.open(errorImgLoc)
errorImg = errorImg.resize((150, 150))
errorImg = ImageTk.PhotoImage(errorImg)

#Opens the fair image, resizes it, then sets it to fairImg
fairImg = Image.open(fairImgLoc)
fairImg = fairImg.resize((150, 150))
fairImg = ImageTk.PhotoImage(fairImg)

#Opens the windy image, resizes it, then sets it to windyImg
windyImg = Image.open(windyImgLoc)
windyImg = windyImg.resize((150, 150))
windyImg = ImageTk.PhotoImage(windyImg)

#Opens the snow image, resizes it, then sets it to snowImg
snowImg = Image.open(snowImgLoc)
snowImg = snowImg.resize((150, 150))
snowImg = ImageTk.PhotoImage(snowImg)

#Location of the weather
locationLabel = tk.Label(master, text = "Select Location", font = ("Calibri bold", 20), bg = "#90D5FF")
locationLabel.grid(row = 0, sticky = "N", padx = 100)

#Temperature of location
temperatureLabel = tk.Label(master, font = ("Calibri bold", 70), bg = "#90D5FF")
temperatureLabel.grid(row = 1, sticky = "W", padx = 40)

#Sets the first picture on the window
imageLabel = tk.Label(master, image = homeImg, bg = "#90D5FF")
imageLabel.grid(row = 1, sticky = "N", padx = 200)

#Creates the weather prediction and sets it on the window
weatherPredictionLabel = tk.Label(master, font = ("Calibri bold", 15), bg = "#90D5FF")
weatherPredictionLabel.grid(row = 2, sticky = "W", padx = 40)

#Creates the time label and sets it on the window
timeLabel = tk.Label(master, text = time, font = ("Calibri Bold", 15), bg = "#90D5FF")
timeLabel.grid(row = 0, column = 1, sticky = "E", pady = 30)

#Creates the date label and sets it on the window
dateLabel = tk.Label(master, text = date, font = ("Calibri bold", 20), bg = "#90D5FF")
dateLabel.grid(row = 0, column = 1, sticky = "NE")

#Creates the "Fishers Location" prediction and sets it on the window
fishersButton = tk.Button(master, text = "Fishers Weather", font = ("Calibri bold", 10), bg = "white", command = getFishersWeather)
fishersButton.grid(row = 3, column = 0, sticky = "W")

#Creates the "Carmel Location" prediction and sets it on the window
carmelButton = tk.Button(master, text = "Carmel Weather", font = ("Calibri bold", 10), bg = "white", command = getCarmelWeather)
carmelButton.grid(row = 3, column = 1, sticky = "E")

#Creates the "Noblesville Location" prediction and sets it on the window
noblesvilleButton = tk.Button(master, text = "Noblesville Weather", font = ("Calibri bold", 10), bg = "White", command = getNoblesvilleWeather)
noblesvilleButton.grid(row = 4, column = 0, sticky = "W")

#Creates the "Indianapolis Location" prediction and sets it on the window
indianapolisButton = tk.Button(master, text = "Indianapolis Weather", font = ("Calibri bold", 10), bg = "White", command = getIndianapolisWeather)
indianapolisButton.grid(row = 4, column = 1, sticky = "E")

master.mainloop()