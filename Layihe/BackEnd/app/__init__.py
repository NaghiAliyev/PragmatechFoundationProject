from flask import render_template,redirect,request,Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_mail import Mail, Message
from admin.routes import admin_bp
from view.routes import view
from admin import routes
from view import routes

upload_folder = 'view/static/view/uploads'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '!Br_Ba3556!'
app.config['UPLOAD_FOLDER']=upload_folder
migrate=Migrate(app, db, render_as_batch=True)

from app import models

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tikinti.firmasi@gmail.com'
app.config['MAIL_PASSWORD'] = 'TikintiFirmasi_123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.register_blueprint(admin_bp)
app.register_blueprint(view)



