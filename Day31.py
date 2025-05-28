# # 1️⃣ Create a base.html File
# # 📁 Location: myapp/templates/myapp/base.html

# ✅ {% extends %} → Used in child templates
# This tells Django:

# "This HTML file will inherit from another (base) template."
# {% extends 'myapp/base.html' %}


# ✅ {% block %} → Used in both parent & child templates
# 🔹 In the base (parent) template:
# Define placeholder sections where child templates can insert custom content.

# <title>{% block title %}Default Title{% endblock %}</title>

# {% block content %}
# <!-- Default content -->
# {% endblock %}

# ✅ Real-life Example
# base.html: has navbar, footer, layout, and defines {% block content %}

# home.html: says "I extend base.html" and fills in the content block

# So your pages look uniform, but you only write the navbar once.