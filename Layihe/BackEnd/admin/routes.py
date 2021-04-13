from flask import Blueprint, render_template, redirect, request
from werkzeug.utils import secure_filename
from app.tools import slugify
import os


admin_bp = Blueprint('admin',__name__,template_folder='templates',static_folder='static', static_url_path='admin/static',url_prefix='/admin')

@admin_bp.route("/")
def admin_index():
    return render_template('admin/index.html')


# Header Slider routes
# Header Slider index
@admin_bp.route('/header_slider')
def index_header_slider():
    from app.models import HeaderSlider
    headerSlider = HeaderSlider.query.all()
    return render_template('admin/header_slider.html',hSlides=headerSlider)

# Add Header Slide
@admin_bp.route("/header_slider/add", methods=['GET', 'POST'])
def add_header_slider():
    from app import db,app
    from app.models import HeaderSlider
    if request.method == "POST":
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        db.session.add(
            HeaderSlider(
                title=request.form['title'],
                description=request.form['description'],
                image=newName
            )
        )
        db.session.commit()
        return redirect('/admin/header_slider')
    return render_template('admin/add_header_slide.html')

# Delete Header Slide
@admin_bp.route("/header_slider/delete/<id>")
def delete_header_slider(id):
    from app import db,app
    from app.models import HeaderSlider
    hSlideForDelete = HeaderSlider.query.get(id)
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],hSlideForDelete.image)) # upload file-dan silmek ucun 
    db.session.delete(hSlideForDelete)
    db.session.commit()
    return redirect('/admin/header_slider')

# Update Header Slide
@admin_bp.route("/header_slider/update/<id>", methods=['GET', 'POST'])
def update_header_slider(id):
    from app import db,app
    from app.models import HeaderSlider
    hSlideForUpdate = HeaderSlider.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], hSlideForUpdate.image)) # upload file-dan silmek ucun 

        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        title = request.form['title']
        description = request.form['description']
        hSlideForUpdate.title = title
        hSlideForUpdate.description = description
        hSlideForUpdate.image = newName
        db.session.commit()
        return redirect('/admin/header_slider')
    return render_template('admin/update_header_slide.html',hSlide=hSlideForUpdate)

# Partners routes
# Partners index
@admin_bp.route('/partners')
def index_partner():
    from app.models import PartnerSlider
    partnerSlider = PartnerSlider.query.all()
    return render_template('admin/partners.html',partners=partnerSlider)

# Add Partner
@admin_bp.route("/partners/add", methods=['GET', 'POST'])
def add_partner():
    from app import db,app
    from app.models import PartnerSlider
    if request.method == "POST":
        
        file = request.files['img']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['name'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        db.session.add(
            PartnerSlider(
                name=request.form['name'],
                img=newName
            )
        )
        db.session.commit()
        return redirect('/admin/partners')
    return render_template('admin/add_partner.html')

# Delete Partner
@admin_bp.route("/partners/delete/<id>")
def delete_partner(id):
    from app import db
    from app.models import PartnerSlider
    partnerForDelete = PartnerSlider.query.get(id)
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],partnerForDelete.img)) # upload file-dan silmek ucun 
    db.session.delete(partnerForDelete)
    db.session.commit()
    return redirect('/admin/partners')

# Update Partner
@admin_bp.route("/partners/update/<id>", methods=['GET', 'POST'])
def update_partner(id):
    from app import db,app
    from app.models import PartnerSlider
    partnerForUpdate = PartnerSlider.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],partnerForUpdate.img)) # upload file-dan silmek ucun 

        file = request.files['img']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['name'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        name = request.form['name']
        partnerForUpdate.name = name
        partnerForUpdate.img = newName
        db.session.commit()
        return redirect('/admin/partners')
    return render_template('admin/update_partner.html',partner=partnerForUpdate)

# MainPagePrinciples routes
# MainPagePrinciples index
@admin_bp.route('/mpprinciples')
def index_main_page_principle():
    from app.models import MainPagePrinciple
    mpPrinciples = MainPagePrinciple.query.all()
    return render_template('admin/main_page_principle.html',mpPrinciples=mpPrinciples)

# Add MainPagePrinciple
@admin_bp.route("/mpprinciples/add", methods=['GET', 'POST'])
def add_main_page_principle():
    from app import db,app
    from app.models import MainPagePrinciple
    if request.method == "POST":
        
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        db.session.add(
            MainPagePrinciple(
                title=request.form['title'],
                description=request.form['description'],
                image=newName
            )
        )
        db.session.commit()
        return redirect('/admin/mpprinciples')
    return render_template('admin/add_main_page_principle.html')

# Delete MainPagePrinciple
@admin_bp.route("/mpprinciples/delete/<id>")
def delete_main_page_principle(id):
    from app import db
    from app.models import MainPagePrinciple
    mpPrincipleForDelete = MainPagePrinciple.query.get(id)
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],mpPrincipleForDelete.image)) # upload file-dan silmek ucun 
    db.session.delete(mpPrincipleForDelete)
    db.session.commit()
    return redirect('/admin/mpprinciples')

# Update MainPagePrinciple
@admin_bp.route("/mpprinciples/update/<id>", methods=['GET', 'POST'])
def update_main_page_principle(id):
    from app import db,app
    from app.models import MainPagePrinciple
    mpPrincipleForUpdate = MainPagePrinciple.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],mpPrincipleForUpdate.image)) # upload file-dan silmek ucun 

        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'])}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        title = request.form['title']
        description = request.form['description']
        mpPrincipleForUpdate.title = title
        mpPrincipleForUpdate.description = description
        mpPrincipleForUpdate.image = newName
        db.session.commit()
        return redirect('/admin/mpprinciples')
    return render_template('admin/update_main_page_principle.html',mpPrinciple=mpPrincipleForUpdate)

# MainPageStatistic routes
# MainPageStatistic index
@admin_bp.route('/mpstatistic')
def index_main_page_statistic():
    from app.models import MainPageStatistic
    mpStatistic = MainPageStatistic.query.get(1)
    return render_template('admin/main_page_statistic.html',mpStatistic=mpStatistic)

# Update MainPageStatistic
@admin_bp.route("/mpstatistic/update/<id>", methods=['GET', 'POST'])
def update_main_page_statistic(id):
    from app import db,app
    from app.models import MainPageStatistic
    mpStatisticForUpdate = MainPageStatistic.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],mpStatisticForUpdate.image)) # upload file-dan silmek ucun 

        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        title = request.form['title']
        description = request.form['description']
        static_value = request.form['static_value']
        mpStatisticForUpdate.title = title
        mpStatisticForUpdate.description = description
        mpStatisticForUpdate.static_value = static_value
        mpStatisticForUpdate.image = newName
        db.session.commit()
        return redirect('/admin/mpstatistic')
    return render_template('admin/update_main_page_statistic.html',mpStatistic=mpStatisticForUpdate)

# ---------------------------------------------
# About Page Routes
# About Page Index
@admin_bp.route('/about')
def index_about_page():
    from app.models import AboutPage
    data = AboutPage.query.get(1)
    return render_template('admin/about_page.html',data=data)

# Update About Page data
@admin_bp.route("/about/update/<id>", methods=['GET', 'POST'])
def update_about_page(id):
    from app import db,app
    from app.models import AboutPage
    data = AboutPage.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],data.image)) # upload file-dan silmek ucun 

        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        title = request.form['title']
        description = request.form['description']
        data.title = title
        data.description = description
        data.image = newName
        db.session.commit()
        return redirect('/admin/about')
    return render_template('admin/update_about_page_data.html',data = data)

# About Page Principles
@admin_bp.route('/about/principles')
def index_about_page_principles():
    from app.models import AboutPagePrinciple
    principles = AboutPagePrinciple.query.all()
    return render_template('admin/about_page_principles.html', principles=principles)

# Update About Page Principle
@admin_bp.route("/about/principles/update/<id>", methods=['GET', 'POST'])
def update_about_page_principle(id):
    from app import db,app
    from app.models import AboutPagePrinciple
    principleForUpdate = AboutPagePrinciple.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],principleForUpdate.image)) # upload file-dan silmek ucun 

        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        title = request.form['title']
        description = request.form['description']
        principleForUpdate.title = title
        principleForUpdate.description = description
        principleForUpdate.image = newName
        db.session.commit()
        return redirect('/admin/about/principles')
    return render_template('admin/update_about_page_principle.html', principle = principleForUpdate)

# About Page Statistic 
@admin_bp.route("/about/statistic")
def index_about_page_statistic():
    from app.models import AboutPageStatistic
    statistic = AboutPageStatistic.query.all()
    return render_template('admin/about_page_statistic.html')

# ---------------------------------------------

# Finished Project Routes
# Finished Projects Index Page
@admin_bp.route("/projects/finished_projects")
def index_finished_projects():
    from app.models import FinishedProject
    fProjects = FinishedProject.query.all()
    return render_template('admin/finished_projects.html', fProjects = fProjects)

# Add Finished Project
@admin_bp.route("/projects/finished_projects/add", methods=["GET", "POST"])
def add_finished_project():
    from app.models import FinishedProject,FinishedProjectImage
    from app import db,app
    from app.tools import slugify
    if request.method == "POST":
        fProject = FinishedProject(
                title = request.form['title'],
                start_time =request.form['start_time'],
                finish_time = request.form['finish_time'],
                area = request.form['area'],
                cost = request.form['cost'],
                location = request.form['location'],
                description = request.form['description'],
                slugified_title = slugify(request.form['title'],to_lower=True)
            )
        db.session.add(fProject)
        db.session.commit()
        files = request.files.getlist('images[]')
        counter = 0
        for file in files:
            if file:
                file_name = secure_filename(file.filename)
                newName = f"photo_fproject_{slugify(request.form['title'],to_lower=True)}_{counter}.{file_name.split('.')[-1]}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
                db.session.add(
                    FinishedProjectImage(
                        filename = newName,
                        project = fProject
                    )
                )
                db.session.commit()
                counter+=1
        return redirect('/admin/projects/finished_projects')
    return render_template('admin/add_finished_project.html')

# Delete Finished Project
@admin_bp.route("/projects/finished_projects/delete/<id>")
def delete_finished_project(id):
    from app import db,app
    from app.models import FinishedProject,FinishedProjectImage
    fProjectForDelete = FinishedProject.query.get(id)
    for image in fProjectForDelete.images:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],image.filename)) # upload file-dan silmek ucun 
        db.session.delete(image) # db-dan silmek ucun 
        db.session.commit()
    db.session.delete(fProjectForDelete)
    db.session.commit()
    return redirect('/admin/projects/finished_projects')

# Update Finished Project
@admin_bp.route("/projects/finished_projects/update/<id>", methods=["GET", "POST"])
def update_finished_project(id):
    from app import db,app
    from app.models import FinishedProject,FinishedProjectImage
    from app.tools import slugify
    fProjectForUpdate = FinishedProject.query.get(id)
    if request.method == "POST":
        
        for image in fProjectForUpdate.images:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'],image.filename)) # upload file-dan silmek ucun 
            db.session.delete(image) # db-dan silmek ucun 
            db.session.commit()
       
        title = request.form['title']
        description = request.form['description']
        start_time = request.form['start_time']
        finish_time = request.form['finish_time']
        area = request.form['area']
        cost = request.form['cost']
        location = request.form['location']
        slugified_title = slugify(request.form['title'],to_lower=True)
        fProjectForUpdate.title = title
        fProjectForUpdate.description = description
        fProjectForUpdate.start_time = start_time
        fProjectForUpdate.finish_time = finish_time
        fProjectForUpdate.area = area
        fProjectForUpdate.cost = cost
        fProjectForUpdate.location = location
        fProjectForUpdate.slugified_title = slugified_title

        files = request.files.getlist('images[]')
        counter = 0
        for file in files:
            if file:
                file_name = secure_filename(file.filename)
                newName = f"photo_fproject_{slugify(request.form['title'],to_lower=True)}_{counter}.{file_name.split('.')[-1]}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
                db.session.add(
                    FinishedProjectImage(
                        filename = newName,
                        project = fProjectForUpdate
                    )
                )
                db.session.commit()
                counter+=1

        db.session.commit()
        return redirect('/admin/projects/finished_projects')
    return render_template('admin/update_finished_project.html',project=fProjectForUpdate)


# On Going Project Routes
# On Going Projects Index Page
@admin_bp.route("/projects/ongoing_projects")
def index_ongoing_projects():
    from app.models import OnGoingProject
    ogProjects = OnGoingProject.query.all()
    return render_template('admin/ongoing_projects.html', ogProjects = ogProjects)

# Add On Going Project
@admin_bp.route("/projects/ongoing_projects/add", methods=["GET", "POST"])
def add_ongoing_project():
    from app.models import OnGoingProject,OnGoingProjectImage
    from app import db,app
    from app.tools import slugify
    if request.method == "POST":
        ogProject = OnGoingProject(
                title = request.form['title'],
                start_time =request.form['start_time'],
                location = request.form['location'],
                description = request.form['description'],
                progress = request.form['progress'],
                slugified_title = slugify(request.form['title'],to_lower=True)
            )
        db.session.add(ogProject)
        db.session.commit()

        files = request.files.getlist('images[]')
        counter = 0
        for file in files:
            if file:
                file_name = secure_filename(file.filename)
                newName = f"photo_ogproject_{slugify(request.form['title'],to_lower=True)}_{counter}.{file_name.split('.')[-1]}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
                db.session.add(
                    OnGoingProjectImage(
                        filename = newName,
                        project = ogProject
                    )
                )
                db.session.commit()
                counter+=1
        return redirect('/admin/projects/ongoing_projects')
    return render_template('admin/add_ongoing_project.html')

# Delete On Going Project
@admin_bp.route("/projects/ongoing_projects/delete/<id>")
def delete_ongoing_project(id):
    from app.models import OnGoingProject, OnGoingProjectImage
    from app import db,app
    ogProjectsForDelete = OnGoingProject.query.get(id)
    for image in ogProjectsForDelete.images:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],image.filename)) # upload file-dan silmek ucun 
        db.session.delete(image) # db-dan silmek ucun 
        db.session.commit()
    db.session.delete(ogProjectsForDelete)
    db.session.commit()
    return redirect('/admin/projects/ongoing_projects')

# Update On Going Project
@admin_bp.route("/projects/ongoing_projects/update/<id>", methods=["GET", "POST"])
def update_ongoing_project(id):
    from app import db,app
    from app.models import OnGoingProject,OnGoingProjectImage
    from app.tools import slugify
    ogProjectForUpdate = OnGoingProject.query.get(id)
    if request.method == "POST":
        
        for image in ogProjectForUpdate.images:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'],image.filename)) # upload file-dan silmek ucun 
            db.session.delete(image) # db-dan silmek ucun 
            db.session.commit()
        
        title = request.form['title']
        description = request.form['description']
        start_time = request.form['start_time']
        progress = request.form['progress']
        location = request.form['location']
        slugified_title = slugify(request.form['title'],to_lower=True)
        ogProjectForUpdate.title = title
        ogProjectForUpdate.description = description
        ogProjectForUpdate.start_time = start_time
        ogProjectForUpdate.progress = progress
        ogProjectForUpdate.location = location
        ogProjectForUpdate.slugified_title = slugified_title

        files = request.files.getlist('images[]')
        counter = 0
        for file in files:
            if file:
                file_name = secure_filename(file.filename)
                newName = f"photo_ogproject_{slugify(request.form['title'],to_lower=True)}_{counter}.{file_name.split('.')[-1]}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
                db.session.add(
                    OnGoingProjectImage(
                        filename = newName,
                        project = ogProjectForUpdate
                    )
                )
                db.session.commit()
                counter+=1

        db.session.commit()
        return redirect('/admin/projects/ongoing_projects')
    return render_template('admin/update_ongoing_project.html', project=ogProjectForUpdate)

# # ---------------
# @admin_bp.route('/testing')
# def testing():
#     return render_template('admin/testing.html')
# # --------------------

# Services Page Routes
# Services Page Index
@admin_bp.route('/services')
def index_services_page():
    from app.models import Service
    services = Service.query.all()
    return render_template('admin/services_page.html',services=services)

# Add Service
@admin_bp.route("/services/add", methods=['GET', 'POST'])
def add_service():
    from app import db,app
    from app.models import Service
    if request.method == "POST":
        
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        db.session.add(
            Service(
                title = request.form['title'],
                description = request.form['description'],
                image = newName
            )
        )
        db.session.commit()
        return redirect('/admin/services')
    return render_template('admin/add_service.html')

# Delete Service
@admin_bp.route("/services/delete/<id>")
def delete_service(id):
    from app.models import Service
    from app import db
    serviceForDelete = Service.query.get(id)
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],serviceForDelete.image)) # upload file-dan silmek ucun 
    db.session.delete(serviceForDelete)
    db.session.commit()
    return redirect('/admin/services')

# Update Service
@admin_bp.route("/services/update/<id>", methods=['GET', 'POST'])
def update_service(id):
    from app import db,app
    from app.models import Service
    serviceForUpdate = Service.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],serviceForUpdate.image)) # upload file-dan silmek ucun 

        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        title = request.form['title']
        description = request.form['description']
        serviceForUpdate.title = title
        serviceForUpdate.description = description
        serviceForUpdate.image = newName
        db.session.commit()
        return redirect('/admin/services')
    return render_template('admin/update_service.html', service = serviceForUpdate)

# Products Page Routes
# Products Page Index
@admin_bp.route('/products')
def index_products_page():
    from app.models import Product
    products = Product.query.all()
    return render_template('admin/products_page.html',products=products)

# Add Product
@admin_bp.route("/products/add", methods=['GET', 'POST'])
def add_product():
    from app import db,app
    from app.models import Product
    if request.method == "POST":
        
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        db.session.add(
            Product(
                title = request.form['title'],
                description = request.form['description'],
                image = newName
            )
        )
        db.session.commit()
        return redirect('/admin/products')
    return render_template('admin/add_product.html')

# Delete Product
@admin_bp.route("/products/delete/<id>")
def delete_product(id):
    from app.models import Product
    from app import db
    productForDelete = Product.query.get(id)
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],productForDelete.image)) # upload file-dan silmek ucun 
    db.session.delete(productForDelete)
    db.session.commit()
    return redirect('/admin/products')

# Update Product
@admin_bp.route("/products/update/<id>", methods=['GET', 'POST'])
def update_product(id):
    from app import db,app
    from app.models import Product
    productForUpdate = Product.query.get(id)
    if request.method == "POST":
        
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],productForUpdate.image)) # upload file-dan silmek ucun 

        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        
        title = request.form['title']
        description = request.form['description']
        productForUpdate.title = title
        productForUpdate.description = description
        productForUpdate.image = newName
        db.session.commit()
        return redirect('/admin/products')
    return render_template('admin/update_product.html', product = productForUpdate)


# Contact Page Routes
# Contact Data
@admin_bp.route("/contact")
def index_contact_page():
    from app.models import ContactInformation
    data = ContactInformation.query.get(1)
    return render_template('admin/contact_page.html', data = data)

# Update Contact data
@admin_bp.route("/contact/update/<id>", methods=['GET', 'POST'])
def update_contact(id):
    from app import db,app
    from app.models import ContactInformation
    contactForUpdate = ContactInformation.query.get(id)
    if request.method == "POST":
        telephone = request.form['telephone']
        e_mail = request.form['e_mail']
        working_time = request.form['working_time']
        location = request.form['location']
        gm_location = request.form['gm_location']
        contactForUpdate.telephone = telephone
        contactForUpdate.e_mail = e_mail
        contactForUpdate.working_time = working_time
        contactForUpdate.location = location
        contactForUpdate.gm_location = gm_location.split('"')[1]
        db.session.commit()
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],contactForUpdate.image)) # upload file-dan silmek ucun 

        return redirect('/admin/contact')
    return render_template('admin/update_contact.html', data = contactForUpdate)

# Messages Routes

@admin_bp.route("/messages")
def index_messages():
    from app.models import UserMessage
    messages = UserMessage.query.all()
    return render_template('admin/messages.html')

# @admin_bp.route("/messages/add")
