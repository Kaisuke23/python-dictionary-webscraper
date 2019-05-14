import requests
from bs4 import BeautifulSoup
import subprocess



# This is going to be a python script in where you take a "list of" and then create a dictionary from it
# This was used during a class assignemnt where we were to take a wikipedia page and extrapolate the web content and
# create a dictionary to be used in a dictionary attack

url = 'https://en.wikipedia.org/wiki/List_of_Gundam_manga_and_novels'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
rawData = set()
seen = set()
unique = []

for tableFinder in soup.findAll("i"):
    rawData.add(tableFinder.text.replace("<i>",""))

for x in rawData:
    if x not in seen:
        unique.append(x)
    seen.add(x)
#
file1 = open("gundamDict.txt","a")
for x in unique:
    file1.write(x+"\n")
file1.close();

subprocess.call(["hashcat","--force","--show", "-a", "0", "-m", "0", "gundamHash.hash", "gundamDict.txt"])
