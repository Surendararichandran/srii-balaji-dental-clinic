from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from flask_mail import Message

from app import db, limiter, mail
from app.models import Enquiry

bp = Blueprint("contact", __name__)


@bp.route("/contact", methods=["GET", "POST"])
@limiter.limit("10 per hour")
def contact():
    if request.method == "POST":
        required = ["name", "phone", "subject", "message"]

        if any(not request.form.get(field, "").strip() for field in required):
            flash("Please complete all required fields.", "danger")
            return render_template("contact.html")

        enquiry = Enquiry(
            name=request.form["name"].strip(),
            phone=request.form["phone"].strip(),
            email=request.form.get("email", "").strip(),
            subject=request.form["subject"].strip(),
            message=request.form["message"].strip(),
        )
        db.session.add(enquiry)
        db.session.commit()

        # Email the clinic after the enquiry has safely been saved.
        try:
            message = Message(
                subject=f"New Patient Enquiry - {enquiry.name}",
                sender=current_app.config["MAIL_DEFAULT_SENDER"],
                recipients=[current_app.config["CLINIC_EMAIL"]],
            )
            message.body = f"""New Patient Enquiry - Srii Balaji Dental Clinic

Name: {enquiry.name}
Phone: {enquiry.phone}
Email: {enquiry.email or 'Not provided'}
Subject: {enquiry.subject}

Message:
{enquiry.message}
"""
            mail.send(message)
        except Exception:
            # Keep the enquiry saved even when SMTP is unavailable.
            current_app.logger.exception("Patient enquiry email notification failed")

        flash("Thank you. Your enquiry has been received. Our clinic team will contact you shortly.", "success")
        return redirect(url_for("contact.contact"))

    return render_template("contact.html")
