from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if user is requesting read-only access (a safe method)
        # return True
        if request.method in permissions.SAFE_METHODS:
            return True
        # otherwise only return True if requesting user owns the profile
        return obj.owner == request.user

