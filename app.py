import os
import time

from flask import Flask, render_template

from screener import Screener

from apscheduler.schedulers.background import BackgroundScheduler

os.environ['TZ'] = 'Poland'


def getData():
    czas = time.strftime('%d/%m/%Y -- %H:%M:%S')
    tabela = Screener()
    stats = tabela.getData()
    return [stats, czas]


scheduler = BackgroundScheduler()
scheduler.add_job(func=getData, trigger="interval", seconds=10)
scheduler.start()

app = Flask(__name__)


@app.route('/')
def renderStats():
    return render_template('stats.html', data=getData()[0].to_html(classes="table table-hover table-striped"),
                           time=getData()[1])


if __name__ == '__main__':
    app.run()
