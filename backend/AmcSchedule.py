import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmcSchedule():
    def __init__(self):
        self.schedule={}

    def get_schedule(self,data):
        if(self.schedule.get(data) is None):
            programacao=[]
            link=f"https://www.amctv.pt/programacao/"
            #Run in headless mode
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            driver = webdriver.Chrome(options=options)
            try:
                driver.get(link)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ren-schedule-items__day")))
                content=driver.page_source
                soup = BeautifulSoup(content, 'html.parser')

                dataNew=data.split("-")[1]+"/"+data.split("-")[2]+"/"+data.split("-")[0]

                scheduleDia=soup.find("div",{"class":"ren-schedule-items__day","data-day":dataNew})

                for i in scheduleDia.find_all("article",{"class":"ren-schedule-item"}):
                    hora=i.find("div",{"class":"ren-schedule-item__time"}).text
                    nome=i.find("div",{"class":"ren-schedule-item__series-name"}).text
                    new_entry = {"programa":nome,"hora":hora,"dia":data}
                    programacao.append(new_entry)
                self.schedule[data]=programacao

            except Exception as e:
                print("Error getting schedule for channel AMC on date "+data,e)
                return []
            
        return self.schedule[data]