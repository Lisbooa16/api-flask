from flask import Flask, request
import json

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['POST', 'GET'])
def index():
    # print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps(t1['nome'])

if __name__ == '__main__':
    app.run(debug=True, port='3000')



"""   
        Explicação do method do REQUEST : FORM



"""