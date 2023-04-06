import requests
import datetime

class TVCine:

    def __init__(self):
        self.dic = {}
        #self.channels = ["TVC Top", "TVC Emotion", "TVC Edition", "TVC Action"]

    def get_tvcine(self, date, channels):
        if self.dic.get(date) is None:

            tvcine = {}
            tvcine['programa'] = []
            tvcine['hora'] = []
            tvcine['dia'] = []
            url = "https://api-tvcine.com/content/emissoes/range?dateStart=" + date + "%2000:00&dateEnd=" + date + "%2023:59&timezone=Europe/Lisbon"
            print(url)
            r = requests.get(url)
            data = r.json()
            

            #split by channel
            data.sort(key=lambda x: x['canal'])

                #write in file
            with open("tvcine.json", "w") as f:
                f.write(str(data))

            #get channel
            for i in range(len(data)):
                if data[i]['canal'] in channels:
                    for e in data[i]['emissoes']:
                        tvcine['programa'].append(e['tituloPT'])
                        tvcine['hora'].append(e['horaEmissao'].replace("h", "."))
                        tvcine['dia'].append(e['dataEmissao'].split("T")[0])
                        if self.dic.get(date) is None:
                            self.dic[date] = {}
                        self.dic[date][data[i]['canal']] = tvcine

            #write to file
            with open("tvcine.txt", "w") as f:
                for i in range(len(tvcine['programa'])):
                    f.write(tvcine['programa'][i] + " " + tvcine['hora'][i]  + " " + tvcine['dia'][i] + "\n")


        return self.dic
    
if __name__ == "__main__":
    tvcine = TVCine()
    channels = ["TVC Top", "TVC Emotion", "TVC Edition", "TVC Action"]
    tvcine.get_tvcine("2023-04-08", channels)



