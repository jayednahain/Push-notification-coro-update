from plyer import notification
from bs4 import BeautifulSoup
import requests


url = "https://www.worldometers.info/coronavirus/"



def notify(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "coronavirus_gi2_icon.ico",
        timeout =  2,
        app_name = "jayed"
    )

r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
    

data = s.find_all("div",class_="maincounter-number")
print(data)
case = data[0].text.strip()
death = data[1].text.strip()
recovered = data[2].text.strip()

    
notify("Total case",case)
notify("Total death",death)
notify("Total recovered",recovered)
    