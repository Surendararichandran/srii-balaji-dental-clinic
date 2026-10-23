from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_mail import Mail
from config import Config


db = SQLAlchemy()
csrf = CSRFProtect()
mail = Mail()
limiter = Limiter(key_func=get_remote_address, default_limits=[])


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)
    mail.init_app(app)

    from app.routes.main import bp as main_bp
    from app.routes.appointments import bp as appointments_bp
    from app.routes.contact import bp as contact_bp
    from app.routes.treatments import bp as treatments_bp
    from app.routes.blog import bp as blog_bp
    from app.routes.admin import bp as admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(treatments_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()
        from app.models import seed_defaults
        seed_defaults()

    return app
