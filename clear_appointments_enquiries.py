
from app import create_app, db
from app.models import Appointment, Enquiry

app = create_app()

with app.app_context():
    print("Appointments:", Appointment.query.count())
    print("Enquiries:", Enquiry.query.count())

    confirm = input(
        "Type DELETE to remove all appointments "
        "and enquiries: "
    )

    if confirm == "DELETE":
        try:
            Appointment.query.delete(synchronize_session=False)
            Enquiry.query.delete(synchronize_session=False)
            db.session.commit()
            print("Appointments and enquiries cleared.")
        except Exception:
            db.session.rollback()
            raise
    else:
        print("Cancelled. No data deleted.")

    print("Appointments remaining:", Appointment.query.count())
    print("Enquiries remaining:", Enquiry.query.count())
