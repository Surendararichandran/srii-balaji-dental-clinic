from flask import Blueprint, render_template, current_app, Response
from app.models import Treatment, Blog
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html', treatments=Treatment.query.all(), blogs=Blog.query.limit(3).all())

@bp.route('/about')
def about(): return render_template('about.html')

@bp.route('/gallery')
def gallery(): return render_template('gallery.html')

@bp.route('/testimonials')
def testimonials(): return render_template('testimonials.html')

@bp.route('/privacy-policy')
def privacy(): return render_template('privacy.html')

@bp.route('/robots.txt')
def robots():
    base=current_app.config['CANONICAL_BASE_URL'].rstrip('/')
    return Response(f'User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n', mimetype='text/plain')

@bp.route('/sitemap.xml')
def sitemap():
    base=current_app.config['CANONICAL_BASE_URL'].rstrip('/')
    urls=['/','/about','/treatments','/appointment','/gallery','/testimonials','/blog','/contact','/privacy-policy']
    urls += [f'/treatments/{t.slug}' for t in Treatment.query.all()]
    urls += [f'/blog/{b.slug}' for b in Blog.query.all()]
    xml='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{base}{u}</loc></url>' for u in urls) + '</urlset>'
    return Response(xml, mimetype='application/xml')
