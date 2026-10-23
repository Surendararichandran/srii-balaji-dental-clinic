# Srii Balaji Dental Clinic Website

A complete responsive Flask dental clinic starter with multi-page frontend, treatment pages, blog, appointment/contact storage, admin appointment status management, CSRF protection, rate limiting, sitemap and robots.txt.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python run.py
```

Open http://127.0.0.1:5000

The default development database is SQLite and is created automatically. To use PostgreSQL, set `DATABASE_URL` in `.env`, for example:

```text
DATABASE_URL=postgresql+psycopg://user:password@localhost/dental_db
```

## Important customisation before launch

Update clinic name, phone, WhatsApp, email, address, city, canonical domain and Google links in `.env`. Replace all Unsplash development images with clinic-owned/licensed images. Replace sample testimonials and blog content with verified clinic content.

## Admin

Development route: `/admin/login`

Development credentials in `app/routes/admin.py`: `admin` / `change-me`.

**Do not deploy with these credentials.** Replace this demo mechanism with database-backed users, password hashing and secure authentication before production.

## Production example

```bash
gunicorn -w 3 -b 0.0.0.0:8000 run:app
```

Deploy behind HTTPS using Render, Railway, a VPS/Nginx setup, or another Python hosting provider. Configure environment variables in the hosting dashboard and use PostgreSQL for persistent production data.

## Security notes

The starter includes CSRF protection and form rate limiting. Production deployments should also use HTTPS, secure session cookie settings, database-backed admin authentication, backups, monitoring, email notification credentials stored only in environment variables, and an anti-spam/CAPTCHA mechanism where appropriate.

## SEO

Dynamic `robots.txt` and `sitemap.xml` routes are included. Set `CANONICAL_BASE_URL` to the live domain. Each major page has page-specific titles/descriptions and treatment pages include local-city metadata.
# srii-balaji-dental-clinic
