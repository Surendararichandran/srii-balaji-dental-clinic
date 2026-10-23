from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from flask_mail import Message

from app import db, limiter, mail
from app.models import Appointment, Treatment


bp = Blueprint("appointments", __name__)


@bp.route("/appointment", methods=["GET", "POST"])
@limiter.limit("10 per hour")
def appointment():
    treatments = Treatment.query.all()

    if request.method == "POST":
        required = ["patient_name", "phone", "appointment_date", "appointment_time"]

        if any(not request.form.get(field, "").strip() for field in required):
            flash("Please complete all required fields.", "danger")
            return render_template("appointment.html", treatments=treatments)

        appointment_request = Appointment(
            patient_name=request.form["patient_name"].strip(),
            phone=request.form["phone"].strip(),
            email=request.form.get("email", "").strip(),
            treatment_id=request.form.get("treatment_id", type=int),
            appointment_date=request.form["appointment_date"],
            appointment_time=request.form["appointment_time"],
            message=request.form.get("message", "").strip(),
        )

        db.session.add(appointment_request)
        db.session.commit()

        treatment_name = "Not specified"
        if appointment_request.treatment:
            treatment_name = appointment_request.treatment.name

        # Send an email notification to the clinic after the appointment
        # has safely been stored in the database.
        try:
            message = Message(
                subject=f"New Appointment Request - {appointment_request.patient_name}",
                sender=current_app.config["MAIL_DEFAULT_SENDER"],
                recipients=[current_app.config["CLINIC_EMAIL"]],
            )

            message.body = f"""New Appointment Request - Srii Balaji Dental Clinic

Patient Name: {appointment_request.patient_name}
Phone: {appointment_request.phone}
Email: {appointment_request.email or 'Not provided'}
Treatment: {treatment_name}
Appointment Date: {appointment_request.appointment_date}
Appointment Time: {appointment_request.appointment_time}

Dental Concern / Message:
{appointment_request.message or 'Not provided'}

Status: Pending
"""

            mail.send(message)
        except Exception:
            # The appointment remains saved even if Gmail is temporarily
            # unavailable or the SMTP credentials have not been configured.
            current_app.logger.exception("Appointment email notification failed")

        flash(
            "Thank you. Your appointment request has been received. "
            "Our clinic team will contact you shortly.",
            "success",
        )
        return redirect(url_for("appointments.appointment"))

    return render_template("appointment.html", treatments=treatments)
