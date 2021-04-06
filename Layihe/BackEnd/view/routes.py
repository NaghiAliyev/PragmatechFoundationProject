from flask import Blueprint, render_template, redirect, request

view = Blueprint('view',__name__,template_folder='templates',static_folder='static', static_url_path='/view/static',url_prefix='/')

@view.route("/")
def main_index():
    from app.models import PartnerSlider,HeaderSlider,FinishedProject,MainPagePrinciple,MainPageStatistic
    hSlides = HeaderSlider.query.all()
    mpPrinciples = MainPagePrinciple.query.all()
    mpStatistic = MainPageStatistic.query.get(1)
    partners = PartnerSlider.query.all()
    fProjects = FinishedProject.query.all()
    return render_template('view/index.html',partners=partners, hSlides = hSlides, fProjects = fProjects, principles = mpPrinciples, statistic = mpStatistic)

@view.route("/about")
def main_about():
    from app.models import PartnerSlider,AboutPagePrinciple,AboutPage,AboutPageStatistic
    data = AboutPage.query.get(1)
    partners = PartnerSlider.query.all()
    statistic = AboutPageStatistic.query.all()
    principles = AboutPagePrinciple.query.all()
    return render_template('view/about.html', data = data, partners = partners, principles = principles, statistic = statistic)

@view.route("/services")
def main_services():
    from app.models import Service
    services = Service.query.all()
    return render_template('view/services.html', services = services)

@view.route("/projects/ongoingprojects")
def main_projects_ongoingProjects():
    from app.models import OnGoingProject
    ongProjects = OnGoingProject.query.all()
    return render_template('view/ongoingProjects.html',ongProjects = ongProjects)

@view.route("/projects/ongoingprojects/<slug>")
def main_projects_ongoingProject(slug):
    from app.models import OnGoingProject
    ongProjects = OnGoingProject.query.all()
    for ogp in ongProjects:
        if ogp.slugified_title == slug:
            ongProject = ogp
            featured_image = ongProject.images[0].filename
    return render_template('view/details-ongoingProjects.html', ongProject = ongProject, featured_image = featured_image)

@view.route("/projects/finishedprojects")
def main_projects_finishedProjects():
    from app.models import FinishedProject
    finProjects = FinishedProject.query.all()
    return render_template('view/finishedProjects.html', finProjects = finProjects)

@view.route("/projects/finishedprojects/<slug>")
def main_projects_finishedProject(slug):
    from app.models import FinishedProject
    finProjects = FinishedProject.query.all()
    for fp in finProjects:
        if fp.slugified_title == slug:
            finProject = fp
            featured_image = finProject.images[0].filename
    return render_template('view/details-finishedProjects.html', finProject = finProject, featured_image = featured_image)

@view.route("/products")
def main_products():
    from app.models import Product
    products = Product.query.all()
    return render_template('view/products.html', products = products)

@view.route("/contacts")
def main_contacts():
    from app.models import ContactInformation
    data = ContactInformation.query.get(1)
    return render_template('view/contacts.html', data = data)