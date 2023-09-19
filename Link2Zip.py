# This will not run on online IDE
import requests
from bs4 import BeautifulSoup
import os

URL = input("Enter URL: ")
r = requests.get(URL)

if(URL[-1] != "/"):
    URL = URL + "/"

list = URL.replace("%20", " ").split("/")
name = list[len(list) - 2]

# If this line causes an error, run 'pip install html5lib' or install html5lib
soup = BeautifulSoup(r.content, "html5lib")

f = open("Link2Zip.txt", "w", encoding = "utf-8")
f.write(soup.prettify())
f.close()

f = open("Link2Zip.txt", "r", encoding = "utf-8")

path = os.path.join(os.getcwd(), name)
if not os.path.exists(path):
    os.mkdir(path)

while True:
    # Get next line from file
    line = f.readline()

    # End of file is reached
    if line.find("</html>") != -1:
        break
    
    # Finds and parses names of games to create zip files
    elif line.find("title=\"") != -1:
        line = f.readline().replace("&amp;", "&")
        open(name + "/" + line[8:-1], "w").close()

f.close()
if os.path.exists("Link2Zip.txt"):
    os.remove("Link2Zip.txt")
