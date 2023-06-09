import datetime
import json
import requests
from bs4 import BeautifulSoup


class FoxSchedule():

    def __init__(self):
        self.dic = {}
        self.channels = ["foxcomedy", "fox-crime", "foxlife", "fox-movies", "mundo-fox", "foxtv"]

    def get_channels(self):
        return self.channels
    
    def get_all_schedules(self, date):
        if self.dic.get(date) is None:
            self.dic[date] = {}
            channels = ["foxcomedy", "fox-crime", "foxlife", "fox-movies", "mundo-fox", "foxtv"]
            for channel in channels:
                self.dic[date][channel] = self.get_schedule(date, channel)
        return self.dic[date]

    def get_schedule(self, date, channel):
        if self.dic.get(date) is None or self.dic.get(date).get(channel) is None:

            data = date.replace("-", "")
            
            url = "https://www.foxtv.pt/programacao/" + channel + "/" + data + "#day" + data
            r = requests.get(url)
            data = r.text

            soup = BeautifulSoup(data, "html.parser")

            
            programas = (soup.find_all("div", class_="large-8 medium-8 small-8 column"))
            horas = (soup.find_all("div", class_="large-3 medium-3 small-3 column"))
            dias = (soup.find_all("li", class_="acilia-schedule-event"))

            programacao = []

            #clean data
            for i in range(len(programas)):
                dataEntry=dias[i].get("data-datetime-date")
                if dataEntry == date:
                    new_entry = {"programa": programas[i].find("h3").text, "hora": horas[i].text.replace(".",":")[-5:], "dia": dataEntry}
                    programacao.append(new_entry)

            if self.dic.get(date) is None:
                self.dic[date] = {}
            
            self.dic[date][channel] = programacao
        return self.dic[date][channel]