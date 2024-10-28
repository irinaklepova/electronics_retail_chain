from rest_framework import permissions


class IsActiveStaff(permissions.BasePermission):
    """Проверяет, является ли сотрудник активным"""

    def has_permission(self, request, view):
        if request.user.is_active and request.user.is_staff:
            return True
        return False
