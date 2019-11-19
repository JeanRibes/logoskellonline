import os

from flask import Flask, render_template, Response, url_for

app = Flask(__name__, template_folder="templates")


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/logoskell/<string:prog>')
def render_logoskell(prog):
    with open('figure.logoskell', 'w') as f:
        f.write(prog)
    os.system('./compiler')
    s = "erreur"
    with open('jean.svg') as j:
        s = "".join(j.readlines())
    return Response(s, mimetype='image/svg+xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
