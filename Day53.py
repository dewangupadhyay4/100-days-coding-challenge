# ✅ Day 53 of 100 – Django REST Framework (DRF): Pagination
# Pagination helps in splitting large datasets into manageable "pages" when sending data to the frontend. It's essential for performance and a better user experience.

# 🔧 1. Why Use Pagination?
# Avoid loading 1000s of records at once.

# Makes API faster and more usable.

# Helps with infinite scrolling / load more features.

# ⚙️ 2. Enable Pagination in settings.py
# You can use different pagination styles provided by DRF.

# ✅ a) PageNumberPagination (default style)

# ✅ b) LimitOffsetPagination

# ✅ c) CursorPagination (for high-performance/secure ordering)

# 🧪 3. How It Looks in Response
# Example with PageNumberPagination: