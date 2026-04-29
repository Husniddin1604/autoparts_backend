from core.config import settings
from starlette.requests import Request
from starlette_admin.contrib.sqla import ModelView


class BaseAdminView(ModelView):
    exclude_fields_from_create = ["created_at", "updated_at"]
    exclude_fields_from_edit = ["created_at", "updated_at"]
    exclude_fields_from_list = ["created_at", "updated_at"]

    def can_delete(self, request: Request) -> bool:
        if settings.APP_MODE == "PRODUCTION":
            return False
        return True
