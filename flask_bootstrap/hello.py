from flask import Flask
from flask import render_template
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/test/')
def test():
    return render_template('test.html')

@app.route('/bad/')
def badreq():
    return render_template('bad.html')

@app.route('/user/')
@app.route('/user/<name>')
def user():
    return render_template('user.html')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    manager.run()
