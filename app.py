from flask import Flask, render_template
from screener import Screener
import time, os

os.environ['TZ'] = 'Poland'
time.tzset()
czas = time.strftime('%d/%m/%Y %H:%M:%S')

tabela = Screener()

stats = tabela.getData()
app = Flask(__name__)


@app.route('/')
def renderStats():
    return render_template('stats.html', data=stats.to_html(classes="table table-hover table-striped"), time=czas)


if __name__ == '__main__':
    app.run()
