import flask
import AxnSchedule
import AmcSchedule
import HollywoodSchedule
from datetime import date

app = flask.Flask(__name__)

axn = AxnSchedule.AxnSchedule()
amc = AmcSchedule.AmcSchedule()
hollywood = HollywoodSchedule.HollywoodSchedule()

@app.route('/')
def index():
    schedule={}
    today=date.today().strftime("%Y-%m-%d")
    schedule["axn"]=axn.get_all_schedules(today)
    schedule["amc"]=amc.get_schedule(today)
    schedule["hollywood"]=hollywood.get_schedule(today)
    return flask.jsonify(schedule)

if __name__ == '__main__':
    app.run()