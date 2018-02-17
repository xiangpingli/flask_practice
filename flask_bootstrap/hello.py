import os
from flask import Flask
from flask import render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db=SQLAlchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')    

    def __repr__(self):
        return '<Role %s>' % self.name


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User> %s' % self.username


@app.route('/test/')
def test():
    return render_template('test.html', current_time=datetime.utcnow())

@app.route('/mysqlquery')
def mysqlquery():
    user_all=User.query.all()
    print user_all
    return render_template('mysqlquery.html', user_all=user_all)

@app.route('/bad/')
def badreq():
    return render_template('bad.html')

@app.route('/user/')
@app.route('/user/<name>')
def user():
    return render_template('user.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            db.session.commit()           
            session['known']= False
        else:
            session['known']=True
        session['name'] = form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'), known=session.get('known', False))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def db_test():
    db.drop_all()
    db.create_all()
    admin_role=Role(name='Admin')
    mod_role=Role(name='Moderator')
    user_role=Role(name='User')
    user_john=User(username='john', role=admin_role)
    user_susan=User(username='susan', role=user_role)
    user_david=User(username='david', role=user_role)
   
    print(admin_role.id) 
    print(mod_role.id)
    print(user_role.id)
     
    db.session.add(admin_role)
    db.session.add(mod_role)
    db.session.add(user_role)
    db.session.add(user_john)
    db.session.add(user_susan)
    db.session.add(user_david)
    
    db.session.commit()

    print(admin_role.id) 
    print(mod_role.id)
    print(user_role.id)

    role_all=[]
    role_all = Role.query.all()
    print("all roles list: %s") %role_all

    user_all=[]
    user_all=User.query.filter_by(role=user_role).all()
    print("all users:%s") %user_all


if __name__ == '__main__':
    db_test()
    manager.run()
    #db_test()
