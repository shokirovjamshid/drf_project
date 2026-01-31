from rest_framework import permissions



class IsSellerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return 'seller' == request.user.type
