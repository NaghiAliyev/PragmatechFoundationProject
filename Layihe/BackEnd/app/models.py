from app import db

class HeaderSlider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    image = db.Column(db.String(100))
    read_more_url=db.Column(db.String(100))

class PartnerSlider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    img = db.Column(db.String(100))

class FinishedProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    start_time = db.Column(db.String(100))
    finish_time = db.Column(db.String(100))
    area = db.Column(db.String(100))
    cost = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.Text)
    images = db.relationship('FinishedProjectImage', backref='project', lazy=True)
    slugified_title = db.Column(db.String(100))

class FinishedProjectImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    project_id = db.Column(db.Integer, db.ForeignKey('finished_project.id'), nullable=False)

class OnGoingProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    start_time = db.Column(db.String(100))
    progress = db.Column(db.String(50))
    location = db.Column(db.String(100))
    images = db.relationship('OnGoingProjectImage', backref='project', lazy=True)
    slugified_title = db.Column(db.String(100))

class OnGoingProjectImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    project_id = db.Column(db.Integer, db.ForeignKey('on_going_project.id'), nullable=False)

class MainPageStatistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    static_value = db.Column(db.String(100))
    image = db.Column(db.String(100))

class MainPagePrinciple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(100))

class AboutPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(100))

class AboutPagePrinciple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(100))

class AboutPageStatistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    image = db.Column(db.String(100))

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(100))

class ContactInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(100))
    e_mail = db.Column(db.String(100))
    working_time = db.Column(db.String(100))
    location = db.Column(db.String(100))
    gm_location = db.Column(db.String(100))