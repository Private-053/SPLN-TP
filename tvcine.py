import json
import requests
import datetime

class TVCine:

    def __init__(self):
        self.dic = {}
        #self.channels = ["TVC Top", "TVC Emotion", "TVC Edition", "TVC Action"]

    def get_tvcine(self, date, channel):
        if self.dic.get(date) is None:

            tvcine=[]
            url = "https://api-tvcine.com/content/emissoes/range?dateStart=" + date + "%2000:00&dateEnd=" + date + "%2023:59&timezone=Europe/Lisbon"
            r = requests.get(url)
            data = r.json()

            #split by channel
            data.sort(key=lambda x: x['canal'])

            #get channel
            for i in range(len(data)):
                for e in data[i]['emissoes']:
                    new_entry = {"programa": e['tituloPT'], "hora": e['horaEmissao'].replace("h",":"), "dia": e['dataEmissao'].split("T")[0]}
                    tvcine.append(new_entry)
                    if self.dic.get(date) is None:
                        self.dic[date] = {}
                    self.dic[date][data[i]['canal']] = tvcine
        return self.dic[date][channel]
    
if __name__ == "__main__":
    tvcine = TVCine()
    channels = ["TVC Top", "TVC Emotion", "TVC Edition", "TVC Action"]
    print(json.dumps(tvcine.get_tvcine("2023-04-08", channels[0])))

