<a id="top"></a>

# Django Template Starter

> A minimal Django 5.2.1 practice project that renders a static `Hello World` page through a project-level template directory.

## Context Menu

| Project area               | Open                                                                                      |
| -------------------------- | ----------------------------------------------------------------------------------------- |
| Description and features   | [Key Features](#key-features)                                                             |
| Technology and setup       | [Tech Stack](#tech-stack) · [Getting Started](#getting-started)                           |
| Runtime configuration      | [Environment Variables](#environment-variables)                                           |
| Request flow               | [Animated Data Flow Diagram](#animated-data-flow-diagram) · [Context Data](#context-data) |
| Browser pages and commands | [Navigation](#navigation) · [Usage](#usage)                                               |
| Project files              | [Project Structure](#project-structure)                                                   |
| Future directions          | [Possible Alternatives](#possible-alternatives)                                           |
| Ownership and license      | [License](#license) · [Contact](#contact)                                                 |

## Key Features

- **Django project foundation:** Uses Django's standard project package, management entry point, ASGI module, and WSGI module.
- **Template rendering:** The `index` view renders `Template/index.html` without a context dictionary.
- **Simple browser page:** The `/index/` route displays `Hello World`.
- **Built-in administration:** The standard Django admin route is enabled at `/admin/`.
- **SQLite configuration:** Uses the checked-in `db.sqlite3` path configured by Django's default settings.
- **Learning-focused scope:** Contains no custom models, forms, migrations, custom app, API, or authentication workflow.

## Tech Stack

| Technology   | Verified use                                |
| ------------ | ------------------------------------------- |
| Python       | Runtime for the Django management script    |
| Django 5.2.1 | Web framework and built-in admin            |
| SQLite       | Database engine configured in `settings.py` |
| HTML         | `Template/index.html` page markup           |

## Getting Started

### Prerequisites

- Python 3.10 or newer recommended for Django 5.2.1.
- A terminal opened in this project directory.

### Installation

```powershell
cd Django\2nd_class\myproject
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install Django==5.2.1
```

### Database Setup

Run Django's built-in migrations before the first launch. This project uses SQLite and does not define custom models or migrations.

```powershell
python manage.py migrate
python manage.py check
```

### Run the Development Server

```powershell
python manage.py runserver
```

Open [http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/) in a browser. The development server is intended for local learning and is not a production deployment configuration.

## Environment Variables

No external environment variables or `.env` file are required by the current source. `manage.py`, `asgi.py`, and `wsgi.py` set the Django settings module internally:

```env
DJANGO_SETTINGS_MODULE=myproject.settings
```

The current settings also contain a development secret key, `DEBUG = True`, and an empty `ALLOWED_HOSTS` list. Replace these values with environment-backed production settings before deployment.

## Animated Data Flow Diagram

The diagram shows the implemented request path. Its SVG vectors are styled with CSS, so the moving line effect remains sharp at any size and can be rendered directly by a browser.

<svg role="img" aria-labelledby="dfd-title dfd-desc" viewBox="0 0 960 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <title id="dfd-title">Django Hello World request flow</title>
  <desc id="dfd-desc">A browser request travels through the URL configuration to the index view and then to the index template before the HTML response returns.</desc>
  <style>
	.dfd-bg { fill: #101827; }
	.dfd-node { fill: #18283b; stroke: #57d3a5; stroke-width: 2; }
	.dfd-label { fill: #f5f7fa; font: 600 16px sans-serif; text-anchor: middle; }
	.dfd-sub { fill: #a9bacb; font: 12px sans-serif; text-anchor: middle; }
	.dfd-line { fill: none; stroke: #57d3a5; stroke-width: 3; stroke-linecap: round; stroke-dasharray: 8 10; animation: dfd-flow 1.4s linear infinite; }
	@keyframes dfd-flow { to { stroke-dashoffset: -36; } }
  </style>
  <rect class="dfd-bg" x="0" y="0" width="960" height="220" rx="14" />
  <path class="dfd-line" d="M205 110H285M445 110H525M685 110H755" />
  <rect class="dfd-node" x="35" y="70" width="170" height="80" rx="10" />
  <rect class="dfd-node" x="285" y="70" width="160" height="80" rx="10" />
  <rect class="dfd-node" x="525" y="70" width="160" height="80" rx="10" />
  <rect class="dfd-node" x="755" y="70" width="170" height="80" rx="10" />
  <text class="dfd-label" x="120" y="105">Browser</text>
  <text class="dfd-sub" x="120" y="127">GET /index/</text>
  <text class="dfd-label" x="365" y="105">URLConf</text>
  <text class="dfd-sub" x="365" y="127">myproject/urls.py</text>
  <text class="dfd-label" x="605" y="105">View</text>
  <text class="dfd-sub" x="605" y="127">index(request)</text>
  <text class="dfd-label" x="840" y="105">Template</text>
  <text class="dfd-sub" x="840" y="127">index.html</text>
</svg>

### DFD Description

| Stage             | Source of truth       | Responsibility                            |
| ----------------- | --------------------- | ----------------------------------------- |
| Browser           | `/index/`             | Sends the page request and receives HTML. |
| URL configuration | `myproject/urls.py`   | Maps `index/` to the `index` view.        |
| View              | `myproject/views.py`  | Calls `render(request, 'index.html')`.    |
| Template          | `Template/index.html` | Produces the `Hello World` HTML response. |

[Back to Contents](#context-menu)

## Django Template Setup

The project points Django at a project-level `Template` directory through `TEMPLATES[0]['DIRS']`. The current template is intentionally minimal:

```python
# myproject/settings.py
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR, 'Template'],
		'APP_DIRS': True,
	},
]
```

```python
# myproject/views.py
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')
```

```html
<!-- Template/index.html -->
<h1>Hello World</h1>
```

[Back to Contents](#context-menu)

## Context Data

The current view does not send custom context data to the template. The request-to-template contract is therefore:

```python
context = {}
return render(request, 'index.html', context)
```

That example describes the current behavior conceptually; the checked-in implementation calls `render` with only the request and template name.

For a future data-backed page, context could be introduced at the view boundary without changing the URL shape:

```python
def index(request):
	context = {'title': 'Hello World'}
	return render(request, 'index.html', context)
```

This second snippet is an extension example, not an implemented feature.

[Back to Contents](#context-menu)

## Navigation

The URL configuration currently defines two routes. Neither route has an explicit `name=` value.

| URL       | Handler                 | URL name               | Result                         |
| --------- | ----------------------- | ---------------------- | ------------------------------ |
| `/index/` | `myproject.views.index` | None                   | Renders `Template/index.html`. |
| `/admin/` | `admin.site.urls`       | Django admin namespace | Opens the built-in admin site. |

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myproject.views import index

urlpatterns = [
	path('admin/', admin.site.urls),
	path('index/', index),
]
```

There is no configured route for `/`; use `/index/` for the project page.

[Back to Contents](#context-menu)

## Usage

### View the page

```text
http://127.0.0.1:8000/index/
```

Expected page output:

```text
Hello World
```

### Open the admin route

```text
http://127.0.0.1:8000/admin/
```

The admin route is configured, but this project does not define custom models or admin registrations. Create a superuser only if you need to inspect Django's built-in admin behavior:

```powershell
python manage.py createsuperuser
```

### Check the project

```powershell
python manage.py check
```

[Back to Contents](#context-menu)

## Project Structure

```text
myproject/
├── manage.py                 # Django command-line entry point
├── db.sqlite3                # SQLite database file
├── Template/
│   └── index.html             # Hello World template
├── myproject/
│   ├── settings.py            # Django configuration
│   ├── urls.py                # /index/ and /admin/ routes
│   ├── views.py               # index view
│   ├── asgi.py                # ASGI entry point
│   └── wsgi.py                # WSGI entry point
└── README.md
```

[Back to Contents](#context-menu)

## Possible Alternatives

These are professional next steps that are not implemented in this project:

- **Environment-based settings:** Move `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` into environment variables and separate development from production settings.
- **Application package:** Create a dedicated Django app for domain code instead of keeping the view in the project package.
- **Named URLs:** Add `name='index'` and use Django's `{% url %}` tag for maintainable navigation.
- **Automated tests:** Add view and URL tests for status codes, template selection, and expected page content.
- **Production database:** Use a managed database and keep generated or local SQLite data outside deployment artifacts.
- **Static asset pipeline:** Add versioned CSS and JavaScript through Django's static-files workflow if the page becomes interactive.
- **Deployment hardening:** Disable debug mode, rotate the development secret key, configure allowed hosts, and serve through a production WSGI or ASGI setup.

[Back to Contents](#context-menu)

## License

This project is released under the [MIT License](./LICENSE).

[Back to Contents](#context-menu)

## Contact

- **Project maintainer:** Mehedi Alam
- **Email:** mehedialam806@gmail.com
- **Project:** [DIPTI WADP Web Application Development Practices](https://github.com/MehediAlam49/DIPTI_WADP__HW-Practices)
- **Profile:** [MehediAlam49](https://github.com/MehediAlam49)

[Back to Contents](#context-menu)
