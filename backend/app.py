from flask import Flask, request, jsonify
import AmcSchedule
import AxnSchedule
import FoxSchedule
import HollywoodSchedule
import TVCineSchedule
from datetime import date
import urllib.parse as parse

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

amc = AmcSchedule.AmcSchedule()
axn = AxnSchedule.AxnSchedule()
fox = FoxSchedule.FoxSchedule()
hollywood = HollywoodSchedule.HollywoodSchedule()
tvcine = TVCineSchedule.TVCineSchedule()

@app.route('/')
def index():
    schedule={}

    dia=request.args.get('date')
    if dia is None:
        dia=date.today().strftime("%Y-%m-%d")

    schedule["axn"]=axn.get_all_schedules(dia)
    schedule["amc"]=amc.get_schedule(dia)
    schedule["fox"]=fox.get_all_schedules(dia)
    schedule["hollywood"]=hollywood.get_schedule(dia)
    schedule["tvcine"]=tvcine.get_all_schedules(dia)

    return jsonify(schedule)

@app.route('/canal/<channel>')
def get_channel(channel):
    schedule=[]
    
    dia=request.args.get('date')
    if dia is None:
        dia=date.today().strftime("%Y-%m-%d")

    if channel == "amc":
        schedule=amc.get_schedule(dia)
    elif channel in [parse.quote_plus(entry.lower()) for entry in axn.get_channels()]:
        schedule=axn.get_schedule(dia,axn.convert_name(channel))
    elif channel in [parse.quote_plus(entry.lower().replace("-","+")) for entry in fox.get_channels()]:
        schedule=fox.get_schedule(dia,fox.convert_name(channel))
    elif channel == "hollywood":
        schedule=hollywood.get_schedule(dia)
    elif channel in [parse.quote_plus(entry.lower()) for entry in tvcine.get_channels()]:
        schedule=tvcine.get_schedule(dia,tvcine.convert_name(channel))

    return jsonify(schedule)


if __name__ == '__main__':
    app.run()