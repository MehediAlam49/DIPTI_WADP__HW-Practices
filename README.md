# DIPTI WADP Web Application Development Practices

> A structured collection of Python, Django, REST API, database, frontend, class-material, and project-based practice work from the DIPTI Web Application Development with Python course.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-API-A30000)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![GitHub](https://img.shields.io/badge/Hosted%20on-GitHub-181717?logo=github&logoColor=white)](https://github.com/MehediAlam49/DIPTI_WADP__HW-Practices)

This repository is organized as a course navigation hub. It contains sequential Django class exercises, independent practice applications, REST API projects, exam projects, class materials, and a larger modular Institute Management System.

## Table of Contents

- [Repository Overview](#repository-overview)
- [API Projects](#api-projects)
- [Django Classes and Lessons](#django-classes-and-lessons)
- [Exam Projects](#exam-projects)
- [Practice Applications](#practice-applications)
- [Institute Management System](#institute-management-system)
- [Class Materials](#class-materials)
- [Projects](#projects)
- [Technologies and Tools](#technologies-and-tools)
- [Learning Roadmap](#learning-roadmap)
- [Setup and Installation](#setup-and-installation)
- [Repository Structure](#repository-structure)
- [Accuracy Notes](#accuracy-notes)
- [Author](#author)

## Repository Overview

| Area            | Purpose                                                          | Open                                       |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------ |
| API             | Django REST Framework projects and API exercises                 | [Open API](./API/)                         |
| Django          | Sequential class exercises and larger course projects            | [Open Django](./Django/)                   |
| Practices       | Standalone Django practice applications                          | [Open Practices](./Practices/)             |
| Projects        | Modular Institute Management System                              | [Open Projects](./projects/)               |
| Class Materials | Course notes, assignments, references, and downloadable material | [Open Class Materials](./Class_Materials/) |

## API Projects

The `API` directory contains three independent Django REST Framework projects. Each project has its own `manage.py` and dependency manifest.

| Project                                                    | Focus                                                                                            | Key files                                                                                                                                                                                                                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [API CRUD](./API/api_crud/api_crud/)                       | CRUD API practice using `crudApp` and Django REST Framework                                      | [manage.py](./API/api_crud/api_crud/manage.py), [requirements.txt](./API/api_crud/requirements.txt), [crudApp](./API/api_crud/api_crud/crudApp/)                                                                                        |
| [Recipe Project API](./API/recipe_project/recipe_project/) | Recipe API with REST Framework, Celery, scheduled tasks, requests, and environment configuration | [manage.py](./API/recipe_project/recipe_project/manage.py), [requirements.txt](./API/recipe_project/requirements.txt), [sample payload](./API/recipe_project/readme.txt), [recipe_app](./API/recipe_project/recipe_project/recipe_app/) |
| [REST API](./API/restApi/apiProject/)                      | API practice using `apiApp` and Django REST Framework                                            | [manage.py](./API/restApi/apiProject/manage.py), [requirements.txt](./API/restApi/requirements.txt), [apiApp](./API/restApi/apiProject/apiApp/)                                                                                         |

### API Project Structure

Each API project contains the Django project package, application code, SQLite database, migrations, and the files required to run it independently. The application folders are linked above so that models, views, serializers, URLs, and migrations can be explored in place.

[Back to top](#dipti-wadp-web-application-development-practices)

## Django Classes and Lessons

The `Django` directory follows the repository's class sequence. The class labels below are the actual directory names; gaps in the sequence are not represented because no corresponding folders were found.

### Class Exercises

| Class | Project or exercise                          | Open                                                                             |
| ----- | -------------------------------------------- | -------------------------------------------------------------------------------- |
| 2nd   | Initial Django project and template exercise | [myproject](./Django/2nd_class/myproject/)                                       |
| 3rd   | Initial Django project exercise              | [myProject](./Django/3rd_class/myProject/)                                       |
| 4th   | Django application and student exercise      | [myProject](./Django/4th_class/myProject/)                                       |
| 5th   | Authentication and template exercise         | [myProject](./Django/5th_class/myProject/)                                       |
| 6th   | Product management practice                  | [productManagement](./Django/6th_class/productManagement/)                       |
| 7th   | Product and store management practice        | [productManagement](./Django/7th_class/productManagement/)                       |
| 8th   | Library CRUD practice                        | [crud_1](./Django/8th_class/crud_1/)                                             |
| 9th   | School management practice                   | [school_management](./Django/9th_class/school_management/)                       |
| 10th  | School management continuation               | [school_management](./Django/10th_class/school_management/)                      |
| 11th  | School management continuation               | [school_management](./Django/11th_class/school_management/)                      |
| 14th  | User authentication                          | [authentication](./Django/14th_class/authentication/)                            |
| 15th  | Book management                              | [book_project](./Django/15th_class/book_project/)                                |
| 16th  | Recipe management                            | [recipe_manager](./Django/16th_class/recipe_manager/)                            |
| 17th  | Resume builder                               | [resume_Builder](./Django/17th_class/resume_Builder/)                            |
| 20th  | Student management system                    | [student_management_system](./Django/20th_class/student_management_system/)      |
| 22nd  | Student to-do system                         | [student_todo_system](./Django/22th_class/student_todo_system/)                  |
| 23rd  | Library CRUD                                 | [library_crud](./Django/23th_class/library_crud/)                                |
| 24th  | Authenticated CRUD project                   | [auth_curd_project](./Django/24th_class/auth_curd_project/)                      |
| 26th  | Task manager                                 | [task_manager](./Django/26th_class/task_manager/)                                |
| 27th  | Django to-do application                     | [Django_To_do](./Django/27th_class/Django_To_do/)                                |
| 28th  | Institute project                            | [institute_project](./Django/28th_class--Institute_project/)                     |
| 29th  | Student project tracker                      | [student_project_tracker](./Django/29th_class--student_project_tracker/)         |
| 30th  | Project management                           | [project_management](./Django/30th_class/project_management/)                    |
| 31st  | School management                            | [school_management](./Django/31th_class-school_management/)                      |
| 32nd  | Event management system                      | [event_management_system](./Django/32th_class/event_management_system/)          |
| 33rd  | Institute management system                  | [institute_management_system](./Django/33th_class/institute_management_system/)  |
| 34th  | Institute management system continuation     | [institute_management_system](./Django/34th_class--Institute_management_system/) |
| 35th  | Institute management system continuation     | [institute_management_system](./Django/35th_class--Institute_management_system/) |
| 37th  | Education portal                             | [education_portal](./Django/37th_class--education_portal/)                       |

### Common Django Project Files

The class projects use the standard Django layout where present. Direct entry-point links are provided for the larger or representative projects:

- [Resume Builder `manage.py`](./Django/17th_class/resume_Builder/manage.py) and [resume app](./Django/17th_class/resume_Builder/resume/)
- [Student Management `manage.py`](./Django/20th_class/student_management_system/manage.py) and [studentApp](./Django/20th_class/student_management_system/studentApp/)
- [Django To-do `manage.py`](./Django/27th_class/Django_To_do/manage.py) and [to_do_app](./Django/27th_class/Django_To_do/to_do_app/)
- [Institute Management 35 `manage.py`](./Django/35th_class--Institute_management_system/institute_management_system/manage.py) and [project package](./Django/35th_class--Institute_management_system/institute_management_system/institute_management_system/)
- [Education Portal `manage.py`](./Django/37th_class--education_portal/education_portal/manage.py) and [portal app](./Django/37th_class--education_portal/education_portal/portal/)

Across these projects, the application directories contain the implementation surfaces used throughout the course: `models.py`, `views.py`, `admin.py`, `forms.py` where present, URL configuration, templates, and migrations.

[Back to top](#dipti-wadp-web-application-development-practices)

## Exam Projects

The [Exam](./Django/Exam/) directory contains two larger Django applications:

| Project    | Focus                                                      | Open                                                                    |
| ---------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| JobNest    | Job-oriented application with the `jobNestApp` application | [Open JobNest](./Django/Exam/Job_nest_project/jobNest/)                 |
| Job Portal | Separate user, employer, and candidate applications        | [Open Job Portal](./Django/Exam/Job_portal_project/job_portal_project/) |

Important entry points: [JobNest manage.py](./Django/Exam/Job_nest_project/jobNest/manage.py) and [Job Portal manage.py](./Django/Exam/Job_portal_project/job_portal_project/manage.py).

## Practice Applications

The [Practices](./Practices/) directory contains independent Django applications outside the numbered class sequence.

| Application | Focus                                                    | Open                                     |
| ----------- | -------------------------------------------------------- | ---------------------------------------- |
| Company     | Company and employee CRUD practice                       | [Open company](./Practices/company/)     |
| InstaCore   | Authentication and profile-oriented practice application | [Open instacore](./Practices/instacore/) |
| Library     | Library CRUD practice with a `libraryApp` application    | [Open library](./Practices/library/)     |

Entry points: [company/manage.py](./Practices/company/manage.py), [instacore/manage.py](./Practices/instacore/manage.py), and [library/manage.py](./Practices/library/library/manage.py).

## Institute Management System

The [Institute Management System](./projects/Institute-Management-System/IMS/) is the repository's most modular project. It is a Django application split into domain-focused apps:

| Domain app     | Open                                                                         |
| -------------- | ---------------------------------------------------------------------------- |
| Users          | [users](./projects/Institute-Management-System/IMS/users/)                   |
| Infrastructure | [infrastructure](./projects/Institute-Management-System/IMS/infrastructure/) |
| Academics      | [academics](./projects/Institute-Management-System/IMS/academics/)           |
| Attendance     | [attendance](./projects/Institute-Management-System/IMS/attendance/)         |
| Finance        | [finance](./projects/Institute-Management-System/IMS/finance/)               |
| Notices        | [notices](./projects/Institute-Management-System/IMS/notices/)               |
| Support        | [support](./projects/Institute-Management-System/IMS/support/)               |

Project entry points include [manage.py](./projects/Institute-Management-System/IMS/manage.py), the shared [base template](./projects/Institute-Management-System/IMS/templates/base.html), [user templates](./projects/Institute-Management-System/IMS/users/templates/users/), [course templates](./projects/Institute-Management-System/IMS/academics/templates/academics/), [attendance templates](./projects/Institute-Management-System/IMS/attendance/templates/attendance/), and [notice templates](./projects/Institute-Management-System/IMS/notices/templates/notices/).

## Class Materials

The [Class Materials](./Class_Materials/) directory contains supporting course material in document, presentation, image, archive, and PDF formats. It also contains the standalone [Resume Builder HTML](./Class_Materials/Resume%20Builder.html).

Material groups include Django exercises, REST API work, job portal projects, recipe projects, resume builder work, student management, task management, and reusable template resources. Archive files are linked directly from the folder so their contents can be inspected or downloaded from GitHub:

- [JobNest archive](./Class_Materials/JobNest.rar)
- [Pre School Template archive](./Class_Materials/Pre%20School%20Template.zip)
- [InstaCore archive](./Class_Materials/instacore.zip)

## Projects

| Project area                | Technology                                  | Description                                                                 | Repository path                                    |
| --------------------------- | ------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------- |
| API projects                | Django, Django REST Framework               | CRUD, recipe, and REST API implementations                                  | [API](./API/)                                      |
| Class projects              | Django, SQLite, HTML, inline CSS/JavaScript | Sequential web development exercises from setup through multi-app systems   | [Django](./Django/)                                |
| Practice applications       | Django, SQLite                              | Company, profile/authentication, and library practice applications          | [Practices](./Practices/)                          |
| Institute Management System | Django, SQLite, modular apps                | Users, academics, attendance, finance, notices, infrastructure, and support | [IMS](./projects/Institute-Management-System/IMS/) |

## Technologies and Tools

| Technology or tool            | Evidence and use                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------- |
| Python                        | Application language across the repository                                                        |
| Django                        | Web framework used by the class, API, practice, exam, and IMS projects                            |
| Django REST Framework         | API projects under [API](./API/)                                                                  |
| SQLite                        | Project databases (`db.sqlite3`) throughout the repository                                        |
| HTML                          | Django templates and the standalone resume builder                                                |
| CSS and JavaScript            | Inline frontend behavior and styling in templates; no standalone `.css` or `.js` files were found |
| Bootstrap and Bootstrap Icons | CDN references in several later projects                                                          |
| Tailwind CSS                  | CDN references in selected 8th through 11th class exercises                                       |
| Celery and django-celery-beat | Declared by the recipe API project                                                                |
| requests and python-dotenv    | Declared by the recipe API project                                                                |
| Git and GitHub                | Repository version control and hosting                                                            |

No evidence was found for React, Vue, Angular, Flask, FastAPI, PostgreSQL, MySQL, MongoDB, or a frontend package manager in the inspected repository.

## Learning Roadmap

```text
Python and web fundamentals
	|
	v
Django project setup and templates
	|
	v
Models, migrations, forms, and CRUD
	|
	v
Authentication and user workflows
	|
	v
Recipe, library, student, task, and event applications
	|
	v
Multi-app institute and education systems
	|
	v
Django REST Framework APIs
	|
	v
Exam and modular full-stack projects
```

This sequence is inferred from the numbered class folders and the capabilities present in the applications; it is a navigation aid, not a claim about the original lesson plan.

## Setup and Installation

There is no single root-level dependency manifest. Each Django project is independent, and only the three API projects currently include `requirements.txt` files.

### General Django workflow

From the directory containing a project's `manage.py`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install the project's requirements.txt when that project provides one.
python -m pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

For projects without a local dependency manifest, install the dependencies required by that project before running its commands. The [API requirements files](#api-projects) document the explicit API dependencies. Do not run `manage.py` from the repository root; choose one project directory at a time.

## Repository Structure

The following tree shows the meaningful top-level and project-level layout. The individual links above provide deeper navigation without duplicating hundreds of template and migration paths here.

```text
DIPTI_WADP__HW-Practices/
├── API/
│   ├── api_crud/api_crud/
│   ├── recipe_project/recipe_project/
│   └── restApi/apiProject/
├── Class_Materials/
│   ├── Resume Builder.html
│   ├── course documents and reference files
│   └── project archives
├── Django/
│   ├── 2nd_class/ through 11th_class/
│   ├── 14th_class/ through 17th_class/
│   ├── 20th_class/ through 24th_class/
│   ├── 26th_class/ through 37th_class/
│   └── Exam/
│       ├── Job_nest_project/
│       └── Job_portal_project/
├── Practices/
│   ├── company/
│   ├── instacore/
│   └── library/
├── projects/
│   └── Institute-Management-System/IMS/
├── .gitignore
└── README.md
```

## Accuracy Notes

- All internal links in this README point to paths verified in the workspace, with spaces URL-encoded where needed.
- No links were generated for missing class numbers or files that do not exist.
- The repository has no root `requirements.txt`, license file, CI configuration, `package.json`, or formal author document.
- Archive contents were not expanded; the archives are linked as files, but their internal structure is not represented here.
- The repository contains checked-in SQLite databases and uploaded media in several projects. They are intentionally documented as existing repository artifacts, not as a recommended production deployment pattern.

## Author

Repository metadata identifies [Mehedi Alam](https://github.com/MehediAlam49) as the primary repository owner and contributor.

## Repository Navigation

- [Home](./)
- [API projects](./API/)
- [Django classes](./Django/)
- [Exam projects](./Django/Exam/)
- [Practice applications](./Practices/)
- [Institute Management System](./projects/Institute-Management-System/IMS/)
- [Class materials](./Class_Materials/)
