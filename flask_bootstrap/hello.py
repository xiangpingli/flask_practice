from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/test/')
def index():
    return render_template('test.html')

@app.route('/user/')
@app.route('/user/<name>')
def user():
    return render_template('user.html')

@app.route('/bad/')
def badreq():
    return render_template('bad.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=5000,
            debug=True)
