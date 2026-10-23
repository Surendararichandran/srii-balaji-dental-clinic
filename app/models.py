from datetime import datetime
from app import db

class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(40), default='bi-heart-pulse')
    image = db.Column(db.String(255), default='https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=1200&q=80')

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150))
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.id'))
    appointment_date = db.Column(db.String(20), nullable=False)
    appointment_time = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    treatment = db.relationship('Treatment')

class Enquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150))
    subject = db.Column(db.String(180), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    excerpt = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(100), default='Srii Balaji Dental Clinic Team')

TREATMENTS = [
('Root Canal Treatment','root-canal','Save damaged or infected teeth using advanced and comfortable root canal treatment.','bi-bandaid'),
('Dental Implants','dental-implants','Permanent and natural-looking replacement solutions for missing teeth.','bi-shield-plus'),
('Braces & Orthodontics','braces','Correct teeth alignment and improve your smile with modern orthodontic treatments.','bi-grid-3x3-gap'),
('Invisalign / Clear Aligners','invisalign','Straighten your teeth discreetly using transparent removable aligners.','bi-stars'),
('Teeth Whitening','teeth-whitening','Professional teeth whitening treatment for a brighter and more confident smile.','bi-brightness-high'),
('Dental Filling','dental-filling','Restore damaged or decayed teeth using durable and aesthetic dental fillings.','bi-droplet-half'),
('Teeth Cleaning','teeth-cleaning','Professional scaling and polishing for healthier teeth and gums.','bi-sparkles'),
('Gum Treatment','gum-treatment','Advanced care for gum infection, bleeding gums and periodontal conditions.','bi-heart-pulse'),
('Kids Dentistry','kids-dentistry','Gentle and friendly dental care specially designed for children.','bi-emoji-smile'),
('Wisdom Tooth Removal','wisdom-tooth-removal','Safe diagnosis and removal of problematic wisdom teeth.','bi-scissors'),
('Dental Crowns & Bridges','crowns-bridges','Restore damaged and missing teeth with natural-looking crowns and bridges.','bi-gem'),
('Smile Designing','smile-designing','Cosmetic dentistry solutions designed to improve smile appearance.','bi-magic')]

def seed_defaults():
    if Treatment.query.count() == 0:
        for n,s,d,i in TREATMENTS:
            db.session.add(Treatment(name=n, slug=s, description=d, icon=i))
    if Blog.query.count() == 0:
        posts = [
            ('7 Tips to Keep Your Teeth Healthy','7-tips-healthy-teeth','Simple daily habits that protect your teeth and gums.','Brush twice daily with fluoride toothpaste, floss every day, reduce sugary snacks, drink water, replace your toothbrush regularly, avoid tobacco, and schedule regular dental check-ups.','https://images.unsplash.com/photo-1609840114035-3c981b782dfe?auto=format&fit=crop&w=1200&q=80'),
            ('Root Canal Treatment: Everything You Need to Know','root-canal-guide','Understand when a root canal may be recommended and what the procedure involves.','Root canal treatment removes infected tissue from inside a tooth, disinfects the canals and seals the tooth so it can continue functioning. Your dentist will confirm suitability after examination and X-rays.','https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=1200&q=80'),
            ('Dental Implants vs Bridges','implants-vs-bridges','A quick comparison of two common missing-tooth replacement options.','Dental implants replace the tooth root and crown, while bridges use adjacent teeth for support. Suitability depends on bone health, neighbouring teeth, medical history, budget and treatment goals.','https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=1200&q=80')]
        for t,s,e,c,i in posts: db.session.add(Blog(title=t, slug=s, excerpt=e, content=c, image=i))
    db.session.commit()
