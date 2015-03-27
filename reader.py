import requests
from PIL import Image
from bs4 import BeautifulSoup

def writeToFile(fileName, text):
    fd = open(fileName, 'a')
    fd.write(text)
    fd.close()

URL = "http://mangafox.me/manga/toukyou_esp/v11/c048/1.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text)
writeToFile("temp",page.text)

print soup