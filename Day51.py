# ✅ Day 51 of 100 – Django REST Framework (DRF): Permissions Deep Dive
# Today you'll understand DRF Permissions, which control who can access what in your APIs. This is a core part of API security and access control.

# 🔐 What Are Permissions?
# Permissions determine whether a user can perform a certain action (like view, create, update, or delete).

# Permissions work after authentication, not before.

# ✅ 1. Default Permission Setting in settings.py
# Set global default:
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }

# ✅ 2. Built-in Permission Classes in DRF
# | Permission Class            | Description                                               |
# | --------------------------- | --------------------------------------------------------- |
# | `AllowAny`                  | Anyone can access (even unauthenticated users)            |
# | `IsAuthenticated`           | Only authenticated users                                  |
# | `IsAdminUser`               | Only staff users                                          |
# | `IsAuthenticatedOrReadOnly` | Authenticated can do anything, others can only read (GET) |

# ✅ 3. Apply Permission on Specific Views

# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import permission_classes

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def secret_data(request):
#     return Response({"msg": "You are authenticated"})

# ✅ 4. Custom Permissions
# Want to allow only users who created an object to edit it?

# Create a file permissions.py:
# from rest_framework import permissions

# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user
# @permission_classes([IsOwner])

# ✅ 5. Combine Permissions
# Use multiple permissions with logical OR: