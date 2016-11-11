import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#We are opening our html file, and we use 'w' to write the html
f = open("index.html", 'w')

url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Turns the extracted html script into a string
webPage = soup.prettify()

#Replaces everything that needed to be replaced
webPage = webPage.replace("student", "AMAZING student")
webPage = webPage.replace("students", "AMAZING students")
webPage = webPage.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "media\pic.jpg")
webPage = webPage.replace("logo2.png", "media\logo.png")

#This writes the html file that was created above with the webpage and the changes made
f.write(webPage)

