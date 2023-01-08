from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route("/hello/<nome>")
def hello(nome=""):
    return f"<h1>Hello {nome}</h1>"


@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID=-1):
    if postID >= 0:
        return f"Blog info {postID}"
    else:
        return f'Blog Todo'
    


@app.route('/blog/<float:postID>')
def blog2(postID=-1):
    if postID >= 0:
        return f"Blog float {postID}"
    else:
        return f'Blog  float Todo'


if __name__ == "__main__":
    app.run(debug=True, port='3000')