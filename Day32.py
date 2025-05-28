# # ⚙️ Step-by-Step Setup
# # 1️⃣ Update settings.py
# # Make sure these lines exist in your project settings:

# # 2️⃣ Load Static in Templates
# # At the top of your HTML templates (like home.html), load static:

# # 3️⃣ Link CSS & JS Files
# # Inside home.html, for example:

# # 4️⃣ Create a CSS File
# # 📁 myapp/static/myapp/css/style.css

# # 5️⃣ (Optional) Add JavaScript File
# # 📁 myapp/static/myapp/js/script.js

#---------------------------------------------------------------------------------------------------------

# ✅ 1. Django Project Setup
# Installed Django using pip:

# bash
# Copy
# Edit
# pip install django
# Created a Django project:

# bash
# Copy
# Edit
# django-admin startproject myproject
# Navigated into the project directory and ran the server:

# bash
# Copy
# Edit
# python manage.py runserver
# ✅ 2. Created a Django App
# Created an app (e.g., myapp):

# bash
# Copy
# Edit
# python manage.py startapp myapp
# Registered the app in settings.py under INSTALLED_APPS.

# ✅ 3. Created URLs and Views
# Created urls.py in the app and connected it to the project’s urls.py.

# Defined views using functions in views.py, e.g.:

# python
# Copy
# Edit
# def home(request):
#     return HttpResponse("Welcome to Home Page")
# Mapped views to URLs.

# ✅ 4. Set Up HTML Templates
# Created templates/ folder inside the app.

# Created HTML files like home.html, about.html, contact.html.

# Configured template settings (Django finds templates automatically inside app/templates/app/).

# ✅ 5. Rendered HTML Templates
# Used render() in views to return HTML:

# python
# Copy
# Edit
# return render(request, 'myapp/home.html')
# Successfully displayed different pages by mapping URLs and rendering templates.

# ✅ 6. Template Inheritance (Day 31)
# Created a reusable layout file base.html with common elements: header, footer, nav bar.

# Used {% block %} in base.html to define sections like:

# html
# Copy
# Edit
# {% block title %}{% endblock %}
# {% block content %}{% endblock %}
# In pages like home.html, used:

# django
# Copy
# Edit
# {% extends 'myapp/base.html' %}
# {% block content %}...{% endblock %}
# ✅ 7. Static Files Setup (Day 32)
# Created the following structure:

# cpp
# Copy
# Edit
# myapp/
# └── static/
#     └── myapp/
#         ├── css/
#         │   └── style.css
#         ├── js/
#         │   └── script.js
#         └── images/
#             └── logo.png
# Used {% load static %} in templates.

# Loaded static files like this:

# html
# Copy
# Edit
# <link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
# <script src="{% static 'myapp/js/script.js' %}"></script>
# <img src="{% static 'myapp/images/logo.png' %}">
# Verified CSS, JS, and images were loading and applied properly.

# ⚙️ Settings Configuration Recap
# settings.py:

# python
# Copy
# Edit
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / "myapp/static",
# ]
# Template Directory Structure (automatically recognized):

# arduino
# Copy
# Edit
# myapp/
# └── templates/
#     └── myapp/
#         ├── base.html
#         ├── home.html
#         ├── about.html
#         └── contact.html
