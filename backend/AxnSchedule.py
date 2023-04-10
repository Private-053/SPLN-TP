import requests
from bs4 import BeautifulSoup
import json


class AxnSchedule():
    def __init__(self):
        self.schedule={}
        self.channels=["AXN","AXN WHITE","AXN MOVIES"]

    def get_channels(self):
        return self.channels
    
    def convert_name(self, name):
        if name == "axn":
            return "AXN"
        elif name == "axn+white":
            return "AXN WHITE"
        elif name == "axn+movies":
            return "AXN MOVIES"

    def get_all_schedules(self,date):
        schedule={}
        for i in self.channels:
            schedule[i]=self.get_schedule(date,i)
        return schedule

    def get_schedule(self,date,channel):
        if(self.schedule.get(date) is None or self.schedule.get(date).get(channel) is None):
            programacao=[]
            link=f"https://www.axn.pt/wp-admin/admin-ajax.php"
            dia=date.split("-")[2]
            mes=date.split("-")[1]
            ano=date.split("-")[0]
            payload = {"action":"get_tv_guide_items", "day":dia, "month":mes, "year":ano, "channel":channel}
            session = requests.Session()
            r = session.post(link, data=payload)
            try:
                if r.json()["html"] is None:
                    print("Error getting schedule for channel "+channel+" on date "+date)
                    return []
                
                html=r.json()["html"]
                soup = BeautifulSoup(html, 'html.parser')
                for i in soup.find_all("li",{"class":"axn-guide-list-item"}):
                    hora=i.find("span",{"class":"hour"}).text[-5:]
                    nome=i.find("div",{"class":"content"}).find("h2",{"class":"title"}).text
                    new_entry = {"programa":nome,"hora":hora,"dia":date}
                    programacao.append(new_entry)
                if self.schedule.get(date) is None:
                    self.schedule[date]={}
                self.schedule[date][channel]=programacao
            except:
                print("Error getting schedule for channel "+channel+" on date "+date)
                return []
            
        return self.schedule[date][channel]