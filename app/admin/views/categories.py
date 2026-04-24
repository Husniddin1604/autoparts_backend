from admin.views.base import BaseAdminView
from models.categories import (
    Attribute, Category, CategoryAttribute,
    PartCategoryLinks
)


class CategoryAdminView(BaseAdminView):
    model = Category
    name = "Category"
    sortable_fields = ["id"]


class AttributeAdminView(BaseAdminView):
    model = Attribute
    name = "Attribute"
    sortable_fields = ["id"]


class CategoryAttributeAdminView(BaseAdminView):
    model = CategoryAttribute
    name = "CategoryAttribute"
    sortable_fields = ["id"]


class PartCategoryLinksAdminView(BaseAdminView):
    model = PartCategoryLinks
    name = "PartCategoryLinks"
    sortable_fields = ["id"]