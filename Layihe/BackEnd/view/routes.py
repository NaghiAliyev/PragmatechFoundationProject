from flask import Blueprint, render_template, redirect, request

view = Blueprint('view',__name__,template_folder='templates',static_folder='static', static_url_path='/view/static',url_prefix='/')

@view.route("/")
def index():
    from app.models import PartnerSlider
    partners = PartnerSlider.query.all()
    return render_template('view/index.html',partners=partners)

@view.route("/about")
def main_about():
    return render_template('view/about.html')

@view.route("/services")
def main_services():
    return render_template('view/services.html')

@view.route("/projects")
def main_projects():
    return render_template('view/projects.html')

@view.route("/projects/ongoingprojects")
def main_projects_ongoingProjects():
    return render_template('view/ongoingprojects.html')

@view.route("/projects/finishedprojects")
def main_projects_finishedProjects():
    return render_template('view/finishedprojects.html')

@view.route("/products")
def main_products():
    return render_template('view/products.html')

@view.route("/contacts")
def main_contacts():
    return render_template('view/contacts.html')