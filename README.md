# Django 99 Utilities — Starter Project

The official starter project for the book **Django 99 Utilities** by Ahmad (django.wiki).

Use this project to follow along with the book, paste utilities, and test them against real seeded data.

---

## Buy the Book
[Django 99 Utilities on Gumroad](https://djangowiki.gumroad.com/l/django-99-utilities) 

---

## Website

[django.wiki](https://django.wiki) — articles, tutorials, and more Django books

---

## Setup

```bash
git clone https://github.com/wikidjango/django99utils-starter
cd django99utils-starter
python -m venv .venv
```

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

Visit: http://127.0.0.1:8000

**Admin panel:** http://127.0.0.1:8000/admin
**Login:** admin / admin123

---

## Testing Utils

**Option 1 — Django Shell**

```bash
python manage.py shell
```

```python
# paste the utility from the book first, then import and test
from utils.query import get_or_none
from shop.models import Product

print(get_or_none(Product, pk=1))      # returns Product object
print(get_or_none(Product, pk=99999))  # returns None
```

**Option 2 — Utils files**

Paste utilities into the matching file in `utils/`:

| File | Chapter |
|---|---|
| `utils/query.py` | Query Utilities |
| `utils/models.py` | Model Utilities |
| `utils/managers.py` | Manager and QuerySet Utilities |
| `utils/views.py` | Request and View Utilities |
| `utils/forms.py` | Form Utilities |
| `utils/serializers.py` | Serializer and API Utilities |
| `utils/validators.py` | Validation Utilities |
| `utils/files.py` | File and Media Utilities |
| `utils/dates.py` | Date and Time Utilities |
| `utils/urls.py` | URL and Slug Utilities |
| `utils/cache.py` | Caching Utilities |
| `utils/services.py` | Service and Business Logic Utilities |
| `utils/security.py` | Security Utilities |
| `utils/logging.py` | Logging and Debug Utilities |
| `utils/testing.py` | Testing Utilities |
| `utils/admin.py` | Admin Utilities |
| `utils/templates.py` | Template Utilities |

**Option 3 — Test view**

Edit the `test_view` function in `shop/views.py` and visit:

http://127.0.0.1:8000/test/

---

## Seeded Data

Running `python manage.py seed_data` creates:

- 1 superuser — admin / admin123
- 5 categories
- 20 products (including 3 soft-deleted and 5 unpublished for testing mixins)
- 10 orders with items

Re-run `seed_data` anytime to reset to a clean state.

---

## Requirements

- Python 3.11+ or Later
- Django 5.2 LTS or Later

---

## Disclaimer

Django is a registered trademark of the Django Software Foundation.
This project is independent and is not affiliated with, endorsed by,
or sponsored by the Django Software Foundation in any way.

---

## About

Built by Ahmad · [django.wiki](https://django.wiki) · Django 99 Utilities