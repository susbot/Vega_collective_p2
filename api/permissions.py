from rest_framework import permissions

# Default Object level permissions as described by the DRF Documentation
# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user