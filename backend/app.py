from flask import Flask, request, jsonify
import AmcSchedule
import AxnSchedule
import FoxSchedule
import HollywoodSchedule
import TVCineSchedule
import Imdb
from datetime import date
import urllib.parse as parse

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

amc = AmcSchedule.AmcSchedule()
axn = AxnSchedule.AxnSchedule()
fox = FoxSchedule.FoxSchedule()
hollywood = HollywoodSchedule.HollywoodSchedule()
tvcine = TVCineSchedule.TVCineSchedule()
imdb = Imdb.MyIMDB()

@app.route('/')
def index():
    schedule={}

    dia=request.args.get('date')
    if dia is None:
        dia=date.today().strftime("%Y-%m-%d")

    schedule.update(axn.get_all_schedules(dia))
    schedule["amc"]=amc.get_schedule(dia)
    schedule.update(fox.get_all_schedules(dia))
    schedule["hollywood"]=hollywood.get_schedule(dia)
    schedule.update(tvcine.get_all_schedules(dia))

    scheduleNew=[]

    for key in schedule:
        for entry in schedule[key]:
            entry["canal"]=key
            scheduleNew.append(entry)

    #Sort by hora
    scheduleNew.sort(key=lambda x: x["hora"])

    return jsonify(scheduleNew)

@app.route('/canal/<channel>')
def get_channel(channel):
    schedule=[]
    
    dia=request.args.get('date')
    if dia is None:
        dia=date.today().strftime("%Y-%m-%d")

    if channel == "amc":
        schedule=amc.get_schedule(dia)
    elif channel in axn.get_channels():
        schedule=axn.get_schedule(dia,channel)
    elif channel in fox.get_channels():
        schedule=fox.get_schedule(dia,channel)
    elif channel == "hollywood":
        schedule=hollywood.get_schedule(dia)
    elif channel in tvcine.get_channels():
        schedule=tvcine.get_schedule(dia,channel)

    schedule.sort(key=lambda x: x["hora"])

    return jsonify(schedule)

@app.route('/rating/<titulo>')
def get_titulo(titulo):
    rating = imdb.getRatting(titulo)
    return rating


if __name__ == '__main__':
    app.run()