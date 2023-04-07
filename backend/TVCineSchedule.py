import json
import requests
import datetime

class TVCineSchedule():

    def __init__(self):
        self.dic = {}
        self.channels = ["TVC Top", "TVC Emotion", "TVC Edition", "TVC Action"]

    def get_channels(self):
        return self.channels
    
    def convert_name(self, name):
        if name == "tvc+top":
            return "TVC Top"
        elif name == "tvc+emotion":
            return "TVC Emotion"
        elif name == "tvc+edition":
            return "TVC Edition"
        elif name == "tvc+action":
            return "TVC Action"

    def get_all_schedules(self, date):
        if self.dic.get(date) is None:
            self.dic[date] = {}
            channels = ["TVC Top", "TVC Emotion", "TVC Edition", "TVC Action"]
            for channel in channels:
                self.dic[date][channel] = self.get_schedule(date, channel)
        return self.dic[date]

    def get_schedule(self, date, channel):
        if self.dic.get(date) is None or self.dic.get(date).get(channel) is None:

            tvcine=[]
            url = "https://api-tvcine.com/content/emissoes/range?dateStart=" + date + "%2000:00&dateEnd=" + date + "%2023:59&timezone=Europe/Lisbon"
            r = requests.get(url)
            data = r.json()

            #split by channel
            data.sort(key=lambda x: x['canal'])

            #get channel
            for i in range(len(data)):
                for e in data[i]['emissoes']:
                    new_entry = {"programa":e['tituloPT'], "hora": e['horaEmissao'].replace("h",":"), "dia": e['dataEmissao'].split("T")[0]}
                    tvcine.append(new_entry)
                    if self.dic.get(date) is None:
                        self.dic[date] = {}
                    self.dic[date][data[i]['canal']] = tvcine
        return self.dic[date][channel]

