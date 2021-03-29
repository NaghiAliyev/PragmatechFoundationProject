from flask import Blueprint, render_template, redirect, request
from werkzeug.utils import secure_filename
import os


admin_bp = Blueprint('admin',__name__,template_folder='templates',static_folder='static', static_url_path='admin/static',url_prefix='/admin')

@admin_bp.route("/")
def admin_index():
    return render_template('admin/index.html')
photo_index=0

@admin_bp.route("/main-page")
def main_page():
    return render_template('admin/main-page.html')

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
        global photo_index
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['title'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        photo_index+=1
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
    from app import db
    from app.models import HeaderSlider
    hSlideForDelete = HeaderSlider.query.get(id)
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
        global photo_index
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['title'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        photo_index+=1
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
        global photo_index
        file = request.files['img']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['name'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        photo_index+=1
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
        global photo_index
        file = request.files['img']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['name'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        photo_index+=1
        name = request.form['name']
        partnerForUpdate.name = name
        partnerForUpdate.img = newName
        db.session.commit()
        return redirect('/admin/partners')
    return render_template('admin/update_partner.html',partner=partnerForUpdate)


# ------------------------------

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
        global photo_index
        file = request.files['img']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['name'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        photo_index+=1
        db.session.add(
            MainPagePrinciple(
                title=request.form['title'],
                desc=request.form['desc'],
                img=newName
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
        global photo_index
        file = request.files['img']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['name'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        photo_index+=1
        title = request.form['title']
        desc = request.form['desc']
        mpPrincipleForUpdate.title = title
        mpPrincipleForUpdate.desc = desc
        mpPrincipleForUpdate.img = newName
        db.session.commit()
        return redirect('/admin/mpprinciples')
    return render_template('admin/update_main_page_principle.html',mpPrinciple=mpPrincipleForUpdate)

@admin_bp.route("/about", methods=["POST", "GET"])
def index_about():
    from app.models import AboutPage
    from app import db
    if request.method == "POST":
        # file = request.files['img']
        # filename = secure_filename(file.filename)
        # newName = f"photo_{request.form['name'][0:3]}.{filename.split('.')[-1]}"
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))        
        db.session.add(
            AboutPage(
                title = request.form['title'],
                desc = request.form['desc']
                # img = newName
            )
        )
        db.session.commit()
        return redirect('/admin/about/show')
    return render_template('admin/about.html')

@admin_bp.route("/about/show")
def show_about():
    from app.models import AboutPage
    datas = AboutPage.query.all()
    return render_template('admin/aboutshow.html',datas=datas)

# Finished Project Routes
# Finished Projects Index Page
@admin_bp.route("/projects/finished_projects")
def index_finished_projects():
    from app.models import FinishedProject
    fProjects = FinishedProject.query.all()
    return render_template('admin/finished_projects.html', fProjects = fProjects)

# Selected Finished Project Index Page
@admin_bp.route("/projects/finished_projects/<fProject_slugified_title>")
def show_finished_project(fProject_slugified_title):
    from app.models import FinishedProject
    fProjects = FinishedProject.query.all()
    for fp in fProjects:
        if fp.slugified_title == fProject_slugified_title:
            fProject = fp
    return render_template('admin/finished_project.html',fProject = fProject)

# Add Finished Project
@admin_bp.route("/projects/finished_projects/add", methods=["GET", "POST"])
def add_finished_project():
    from app.models import FinishedProject
    from app import db,app
    from app.tools import slugify
    if request.method == "POST":
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_fproject_{slugify(request.form['title'],to_lower=True)}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        db.session.add(
            FinishedProject(
                title = request.form['title'],
                start_time =request.form['start_time'],
                finish_time = request.form['finish_time'],
                area = request.form['area'],
                cost = request.form['cost'],
                location = request.form['location'],
                description = request.form['description'],
                slugified_title = slugify(request.form['title'],to_lower=True),

                image = newName
            )
        )
        db.session.commit()
        return redirect('/admin/projects/finished_projects')
    return render_template('admin/add_finished_project.html')

# Delete Finished Project
# Update Finished Project

