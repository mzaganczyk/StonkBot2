from flask import Flask, render_template
from screener import Screener
from datetime import datetime

tabela = Screener()
stats = tabela.getData()
app = Flask(__name__)
print(stats.to_html())
czas = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


@app.route('/')
def renderStats():
    return render_template('stats.html', data=stats.to_html(classes="table table-hover table-striped"), time=czas)


if __name__ == '__main__':
    app.run()
