from flask import Flask, request, abort, redirect, url_for
import json

app = Flask(__name__, static_folder='static')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['pass'] == 'admin':
            return redirect(url_for('sucesso'), code=302)
        else:
            abort(401)
    else:
        abort(403)


@app.route('/sucesso')
def sucesso():
    return 'sucesso'


if __name__ == '__main__':
    app.run(debug=True, port='3000')



"""   
        Explicação do method do REQUEST : FORM



"""