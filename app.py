import os
import time

from flask import Flask, render_template

from screener import Screener

from apscheduler.schedulers.blocking import BlockingScheduler

os.environ['TZ'] = 'Poland'
time.tzset()

sched = BlockingScheduler()


@sched.scheduled_job('cron', id='my_job_id', seconds=10)
def getData():
    czas = time.strftime('%d/%m/%Y -- %H:%M:%S')
    tabela = Screener()
    stats = tabela.getData()
    return [stats, czas]


app = Flask(__name__)


@app.route('/')
def renderStats():
    return render_template('stats.html', data=getData()[0].to_html(classes="table table-hover table-striped"),
                           time=getData()[1])


if __name__ == '__main__':
    app.run()
