from flask import Blueprint, render_template, abort
from app.models import Blog
bp=Blueprint('blog',__name__,url_prefix='/blog')
@bp.route('/')
def index(): return render_template('blog.html', posts=Blog.query.order_by(Blog.published_at.desc()).all())
@bp.route('/<slug>')
def detail(slug):
    post=Blog.query.filter_by(slug=slug).first()
    if not post: abort(404)
    related=Blog.query.filter(Blog.id!=post.id).limit(3).all()
    return render_template('blog_detail.html', post=post, related=related)
