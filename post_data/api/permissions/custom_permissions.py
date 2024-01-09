from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        message = " You must be the owner of this object."
        return (obj.user == request.user) or request.user.is_superuser
