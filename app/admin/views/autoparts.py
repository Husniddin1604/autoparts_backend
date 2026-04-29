from admin.views.base import BaseAdminView
from models.autoparts import (Brand, CrossReference, Part, PartFitment,
                              PartNumbers)


class PartAdminView(BaseAdminView):
    model = Part
    name = "Part"
    sortable_fields = ["id"]


class BrandAdminView(BaseAdminView):
    model = Brand
    name = "Brand"
    sortable_fields = ["id"]


class PartNumbersAdminView(BaseAdminView):
    model = PartNumbers
    name = "PartNumbers"
    sortable_fields = ["id"]


class CrossReferenceAdminView(BaseAdminView):
    model = CrossReference
    name = "CrossReference"
    sortable_fields = ["id"]


class PartFitmentAdminView(BaseAdminView):
    model = PartFitment
    name = "PartFitment"
    sortable_fields = ["id"]