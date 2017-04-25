from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/test/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/bad/')
def badreq():
    return '<h1>bad req!</h1>', 400

if __name__ == '__main__':
    manager.run()
