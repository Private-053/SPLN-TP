import json
import requests

class AmcSchedule():
    def __init__(self):
        self.schedule={}

    def get_schedule(self,data):
        if(self.schedule.get(data) is None):
            programacao=[]
            link=f"https://www.amctv.pt/wp/wp-admin/admin-ajax.php"
            payload = {"action":"schedule-epg", "start-date":data, "days":1, "tz":"Europe/Lisbon", "channel":"AMC Portugal", "show-title":None, "security":"9a0bf10486"}
            session = requests.Session()
            r = session.post(link, data=payload)
            schedule=r.json()["schedule"][data]
            for i in schedule:
                new_entry = {"programa":i["title"],"hora":i["runtime"],"dia":data}
                programacao.append(new_entry)
            self.schedule[data]=programacao
        return self.schedule[data]