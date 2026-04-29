from admin.views.base import BaseAdminView
from models.users import User


class UserAdminView(BaseAdminView):
    model = User
    name = "User"
    sortable_fields = ["id"]