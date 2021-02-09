from flask import Flask, render_template
from screener import Screener

tabela = Screener()
stats = tabela.getData()
app = Flask(__name__)
print(stats.to_html())


@app.route('/')
def renderStats():
    return render_template('stats.html', data=stats.to_html(classes="table table-hover table-striped"))


if __name__ == '__main__':
    app.run()
