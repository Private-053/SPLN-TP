import json
import requests
import datetime

class TVCineSchedule():

    def __init__(self):
        self.dic = {}
        self.channels = ["TVC Top", "TVC Emotion", "TVC Edition", "TVC Action"]

    def get_channels(self):
        return self.channels

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

            if data is None:
                return []

            #split by channel
            data.sort(key=lambda x: x['canal'])

            #get channel
            for canalDict in data:
                if canalDict['canal'] == channel:
                    for e in canalDict['emissoes']:
                        hora=e['horaEmissao'].replace("h",":")[-5:]
                        if len(hora) == 4:
                            hora = "0" + hora
                        new_entry = {"programa":e['tituloPT'], "hora": hora, "dia": e['dataEmissao'].split("T")[0]}
                        tvcine.append(new_entry)
                        if self.dic.get(date) is None:
                            self.dic[date] = {}
                        self.dic[date][channel] = tvcine
        return self.dic[date][channel]