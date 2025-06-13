# ✅ Day 48 of 100 – Django REST Framework (DRF): Custom Actions in ViewSets
# Today, you’ll enhance your ViewSet by adding custom actions using the @action decorator. This is useful when you want additional endpoints that don't fit CRUD operations.

# 🔍 Why Custom Actions?
# Sometimes you want to add functionality like:

# /items/recent/ → show recently added items

# /items/{id}/mark_done/ → mark a specific item as done
# These don’t fit into standard CRUD, so we use custom actions.

# 🔧 Steps to Create Custom Actions
# ✅ 1. views.py

# ✅ 2. Test Routes
# If you registered ItemViewSet with router, now you’ll have:

# GET /api/items/recent/ → custom list route

# POST /api/items/{id}/mark_done/ → custom detail route