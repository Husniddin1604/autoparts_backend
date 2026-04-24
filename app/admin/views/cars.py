from admin.views.base import BaseAdminView
from models.cars import CarModel, CarModification, Manufacturer


class CarModelAdminView(BaseAdminView):
    model = CarModel
    name = "CarModel"
    sortable_fields = ["id"]


class CarModificationAdminView(BaseAdminView):
    model = CarModification
    name = "CarModification"
    sortable_fields = ["id"]


class ManufacturerAdminView(BaseAdminView):
    model = Manufacturer
    name = "Manufacturer"
    sortable_fields = ["id"]
