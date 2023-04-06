import requests
import datetime


def get_tvcine(channels):
    tvcine = {}
    tvcine['programa'] = []
    tvcine['hora'] = []
    tvcine['dia'] = []
    semana = get_date() + datetime.timedelta(days=7)
    semana = str(semana)
    date = str(get_date())
    url = "https://api-tvcine.com/content/emissoes/range?dateStart=" + date + "%2000:00&dateEnd=" + semana + "%2023:59&timezone=Europe/Lisbon"
    print(url)
    r = requests.get(url)
    data = r.json()
    


    #split by channel
    data.sort(key=lambda x: x['canal'])


        #write in file
    with open("tvcine.json", "w") as f:
        f.write(str(data))

    #get channel
    print(len(data))
    for i in range(len(data)):
        if data[i]['canal'] in channels:
            for e in data[i]['emissoes']:
                tvcine['programa'].append(e['tituloPT'])
                tvcine['hora'].append(e['horaEmissao'].replace("h", "."))
                tvcine['dia'].append(e['dataEmissao'].split("T")[0])


    #write to file
    with open("tvcine.txt", "w") as f:
        for i in range(len(tvcine['programa'])):
            f.write(tvcine['programa'][i] + " " + tvcine['hora'][i]  + " " + tvcine['dia'][i] + "\n")




def get_date():
    today = datetime.date.today()
    return today


get_tvcine(("TVC Emotion", "TVC Action", "TVC Edition", "TVC Top"))