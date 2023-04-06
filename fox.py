import datetime
import requests
from bs4 import BeautifulSoup



#get info trough the URL


#get info from FOX

def get_fox():
    #remove the - from data
    fox = {}
    date = str(get_date()).replace("-", "")
    url = "https://www.foxtv.pt/programacao/foxtv/" + date + "#day" + date
    print(url)
    r = requests.get(url)
    data = r.text
    #write the data to a file
    with open("fox.html", "w") as f:
        f.write(data)
    soup = BeautifulSoup(data, "html.parser")
    #get all the programs and times

    
    fox['programa'] = (soup.find_all("div", class_="large-8 medium-8 small-8 column"))
    fox['hora'] = (soup.find_all("div", class_="large-3 medium-3 small-3 column"))
    
    #clean data
    for i in range(len(fox['programa'])):
        fox['programa'][i] = fox['programa'][i].text
        fox['hora'][i] = fox['hora'][i].text

    #write to file
    with open("fox.txt", "w") as f:
        for i in range(len(fox['programa'])):
            f.write(fox['programa'][i] + " " + fox['hora'][i] + "\n")




    return fox

#get today's date

def get_date():
    today = datetime.date.today()
    return today

get_fox()