from flask import render_template,redirect,request,Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
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


app.register_blueprint(admin_bp)
app.register_blueprint(view)



