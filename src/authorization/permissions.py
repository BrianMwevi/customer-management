class CanManageUserRoles(BasePermission):

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return UserRolesService.check_roles(user=request.user, roles=['JAMBOPAY_ADMIN', 'CUSTOMER_MANAGEMENT'])
        return True

