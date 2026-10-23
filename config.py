import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-in-production")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///dental.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "change-me")

    CLINIC_NAME = os.getenv("CLINIC_NAME", "Srii Balaji Dental Clinic")
    CLINIC_PHONE = os.getenv("CLINIC_PHONE", "+91 73737 87579")
    CLINIC_WHATSAPP = os.getenv("CLINIC_WHATSAPP", "917373787579")
    CLINIC_EMAIL = os.getenv("CLINIC_EMAIL", "32smiledentalcare@gmail.com")
    CLINIC_ADDRESS = os.getenv(
        "CLINIC_ADDRESS",
        "Bulk Bus Stop, 62/3, Shengottai Road, Tenkasi, Tamil Nadu 627811, India",
    )
    CITY = os.getenv("CITY", "Tenkasi")
    GOOGLE_MAPS_EMBED = os.getenv("GOOGLE_MAPS_EMBED", "")
    GOOGLE_REVIEW_URL = os.getenv("GOOGLE_REVIEW_URL", "#")
    CANONICAL_BASE_URL = os.getenv("CANONICAL_BASE_URL", "http://localhost:5000")

    # Gmail SMTP configuration for appointment notifications.
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "32smiledentalcare@gmail.com")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
    MAIL_DEFAULT_SENDER = os.getenv(
        "MAIL_DEFAULT_SENDER", "32smiledentalcare@gmail.com"
    )
