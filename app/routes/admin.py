from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for
from app import db
from app.models import Appointment, Enquiry

bp = Blueprint("admin", __name__, url_prefix="/admin")


def authed():
    return session.get("admin") is True


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == current_app.config["ADMIN_USERNAME"] and password == current_app.config["ADMIN_PASSWORD"]:
            session["admin"] = True
            return redirect(url_for("admin.dashboard"))
        flash("Invalid admin username or password.", "danger")
    return render_template("admin/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("admin.login"))


@bp.route("/")
def dashboard():
    if not authed():
        return redirect(url_for("admin.login"))
    return render_template(
        "admin/dashboard.html",
        appointments=Appointment.query.order_by(Appointment.created_at.desc()).all(),
        enquiries=Enquiry.query.order_by(Enquiry.created_at.desc()).all(),
    )


@bp.route("/appointment/<int:id>/status", methods=["POST"])
def status(id):
    if not authed():
        return redirect(url_for("admin.login"))
    appointment = Appointment.query.get_or_404(id)
    new_status = request.form.get("status")
    if new_status in ["Pending", "Confirmed", "Completed", "Cancelled"]:
        appointment.status = new_status
        db.session.commit()
    return redirect(url_for("admin.dashboard"))
