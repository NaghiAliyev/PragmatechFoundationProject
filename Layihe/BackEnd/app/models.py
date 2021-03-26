from app import db

class HeaderSlider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))
    read_more_url=db.Column(db.String(100))

class PartnerSlider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    img = db.Column(db.String(100))

class FinishedProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    start_time = db.Column(db.String(100))
    finis_time = db.Column(db.String(100))
    area = db.Column(db.String(100))
    cost = db.Column(db.String(100))
    location = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))

class OnGoingProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    start_time = db.Column(db.String(100))
    location = db.Column(db.String(100))
    img = db.Column(db.String(100))

class MainPageStatistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))

class MainPagePrinciple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))

class AboutPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))

class AboutPagePrinciple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))

class AboutPageStatistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc_title = db.Column(db.String(100))
    desc_content = db.Column(db.String(100))
    img = db.Column(db.String(100))

class ContactInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(100))
    e_mail = db.Column(db.String(100))
    working_time = db.Column(db.String(100))
    location = db.Column(db.String(100))