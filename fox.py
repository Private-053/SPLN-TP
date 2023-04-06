import datetime
import requests
from bs4 import BeautifulSoup


class Fox():

    def __init__(self):
        self.dic = {}
        self.channels = ["foxcomedy", "fox-crime", "foxlife", "fox-movies", "mundo-fox", "foxtv"]


    def get_fox(self, date, channel):
        if self.dic.get(date) is None or self.dic.get(date).get(channel) is None:

            #remove the - from data
            fox = {}
            data = date.replace("-", "")
            url = "https://www.foxtv.pt/programacao/" + channel + "/" + data + "#day" + data
            print(url)
            r = requests.get(url)
            data = r.text
            #write html
            with open("fox.html", "w") as f:
                f.write(data)

            soup = BeautifulSoup(data, "html.parser")

            
            fox['programa'] = (soup.find_all("div", class_="large-8 medium-8 small-8 column"))
            fox['hora'] = (soup.find_all("div", class_="large-3 medium-3 small-3 column"))
            fox['dia'] = (soup.find_all("li", class_="acilia-schedule-event"))

            

            #clean data
            for i in range(len(fox['programa'])):
                fox['programa'][i] = fox['programa'][i].find("h3").text
                fox['hora'][i] = fox['hora'][i].text
                fox['dia'][i] = fox['dia'][i].get("data-datetime-date").replace("-", "")


            if self.dic.get(date) is None:
                self.dic[date] = {}
            
            self.dic[date][channel] = fox

            #write to file
            with open("fox.txt", "w") as f:
                for i in range(len(fox['programa'])):
                    f.write(fox['programa'][i] + " " + fox['hora'][i]  + " " + fox['dia'][i] + "\n")




        return self.dic
    

if __name__ == "__main__":
    fox = Fox()
    fox.get_fox("2023-04-08", "foxcomedy")