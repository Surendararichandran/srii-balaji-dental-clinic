from flask import Blueprint, render_template, abort
from app.models import Treatment
bp = Blueprint('treatments', __name__, url_prefix='/treatments')
@bp.route('/')
def list_treatments(): return render_template('treatments.html', treatments=Treatment.query.all())
@bp.route('/<slug>')
def detail(slug):
    t=Treatment.query.filter_by(slug=slug).first()
    if not t: abort(404)
    return render_template('treatment_detail.html', treatment=t)
