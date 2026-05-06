from admin.views.base import BaseAdminView
from models.orders import Order, OrderItem


class OrderAdminView(BaseAdminView):
    model = Order
    name = "Order"
    sortable_fields = ["id"]


class OrderItemAdminView(BaseAdminView):
    model = OrderItem
    name = "OrderItem"
    sortable_fields = ["id"]