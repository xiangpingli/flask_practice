from flask import Flask
from flask.ext.script import Manager
from flask import render_template

app = Flask(__name__)
manager = Manager(app)

@app.route('/test/')
def index():
    return render_template('test.html')

@app.route('/bad/')
def badreq():
    return render_template('bad.html')

if __name__ == '__main__':
    manager.run()
