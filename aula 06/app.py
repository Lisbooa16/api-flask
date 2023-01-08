from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder='static')

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        return dumps(request.form) # ou request.form['nome']
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port='3000')



"""   
        Explicação do method do REQUEST : FORM



"""