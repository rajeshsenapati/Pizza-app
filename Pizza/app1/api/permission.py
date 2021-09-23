from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
class ReviewOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.customer == request.user