# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

#Here lies a comment for extra credit
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

f = open("index.html", 'w')

url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

webPage = soup.prettify()
webPage = webPage.replace("student", "AMAZING students")
webPage = webPage.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "https://scontent-ort2-1.xx.fbcdn.net/v/t1.0-0/p206x206/14141962_10153874492878359_3419118872454018419_n.jpg?oh=48b3ae049106348e65a16dfed3075466&oe=58961321")

f.write(webPage)

