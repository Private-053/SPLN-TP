import requests
from bs4 import BeautifulSoup


class AxnSchedule():
    def __init__(self):
        self.schedule={}

    def get_schedule(self,data,channel):
        if(self.schedule.get(data) is None):
            programacao=[]
            link=f"https://www.axn.pt/wp-admin/admin-ajax.php"
            dia=data.split("-")[2]
            mes=data.split("-")[1]
            ano=data.split("-")[0]
            payload = {"action":"get_tv_guide_items", "day":dia, "month":mes, "year":ano, "channel":channel}
            session = requests.Session()
            r = session.post(link, data=payload)
            html=r.json()["html"]
            soup = BeautifulSoup(html, 'html.parser')

            for i in soup.find_all("li",{"class":"axn-guide-list-item"}):
                hora=i.find("span",{"class":"hour"}).text
                nome=i.find("div",{"class":"content"}).find("h2",{"class":"title"}).text
                new_entry = {"programa":nome,"hora":hora,"dia":data}
                programacao.append(new_entry)
            self.schedule[data]=programacao
        return self.schedule[data]