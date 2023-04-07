import requests

class HollywoodSchedule():
    def __init__(self):
        self.schedule={}

    def get_schedule(self,data):
        if(self.schedule.get(data) is None):
            programacao=[]
            link=f"https://canalhollywood.pt/wp-admin/admin-ajax.php?action=get_movies_range&start={data}&end={data}"
            r = requests.get(link)
            lista = r.json()["movies"][data]
            if lista is None:
                return []
            for i in lista:
                new_entry = {"programa":i["title"],"hora":i["date"].split(" ")[1][:5],"dia":data}
                programacao.append(new_entry)
            self.schedule[data]=programacao
        return self.schedule[data]