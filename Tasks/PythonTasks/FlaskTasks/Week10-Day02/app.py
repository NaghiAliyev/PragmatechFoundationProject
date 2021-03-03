from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    details = db.Column(db.String(250))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method == 'POST':
        name = request.form['user_name']
        surname = request.form['user_surname']
        email = request.form['user_email']
        detail = request.form['user_details']
        user = User(name=name,surname=surname,email=email,details=detail)
        db.session.add(user)
        db.session.commit()
        return redirect('/users')
    return render_template('new.html')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    userForUpdate = User.query.get(id)
    if request.method == 'POST':
        name = request.form['user_name']
        surname = request.form['user_surname']
        email = request.form['user_email']
        detail = request.form['user_details']
        userForUpdate.name = name
        userForUpdate.surname = surname
        userForUpdate.email = email
        userForUpdate.details = detail
        db.session.commit()
        return redirect('/users')
    return render_template('update.html',user=userForUpdate)

@app.route('/delete/<id>')
def delete(id):
    userForDelete=User.query.get(id)
    db.session.delete(userForDelete)
    db.session.commit()
    return redirect('/users')

@app.route('/details/<id>')
def details(id):
    userForShow=User.query.get(id)
    return render_template('details.html',user=userForShow)

@app.route('/users')
def users():
    allUsers = User.query.all()
    return render_template('users.html',users=allUsers)


if __name__ == "__main__":
    app.run(debug=True)