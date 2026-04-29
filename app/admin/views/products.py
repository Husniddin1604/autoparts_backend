from admin.views.base import BaseAdminView
from models.products import Product, ProductAttributeValues, Stock


class ProductAdminView(BaseAdminView):
    model = Product
    name = "Product"
    sortable_fields = ["id"]


class ProductAttributeValuesAdminView(BaseAdminView):
    model = ProductAttributeValues
    name = "ProductAttributeValues"
    sortable_fields = ["id"]


class StockAdminView(BaseAdminView):
    model = Stock
    name = "Stock"
    sortable_fields = ["id"]
