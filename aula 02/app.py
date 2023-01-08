from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Index"


def teste():
    return "<p>Testando</p>"


def teste2():
    return "<h1>Testando 2</h1>"

app.add_url_rule("/teste", "teste", teste)
app.add_url_rule("/teste2", "teste2", teste2)

if __name__ == '__main__':
    app.run(debug=True, port="3000")