from urllib.parse import urljoin

from admin.auth import AdminAuth
from admin.views import *
from db.session import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from models.autoparts import (
    Part, Brand, PartNumbers,
    CrossReference, PartFitment
)
from models.cars import CarModel, CarModification, Manufacturer
from models.categories import (
    Attribute, Category, CategoryAttribute,
    PartCategoryLinks
)
from models.users import User
from models.products import Product, ProductAttributeValues, Stock
from starlette_admin.contrib.sqla import Admin


def setup_admin(app: FastAPI):
    base_url = "/api/dashboard/"
    admin_base_url = "https://autoparts.uz/api/dashboard"

    # Create a custom admin class that forces HTTPS
    class HTTPSAdmin(Admin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._base_url = admin_base_url

        def _build_url(self, path: str) -> str:
            """Build URL with forced HTTPS"""
            if path.startswith(("http://", "https://")):
                return path
            return urljoin(self._base_url, path.lstrip("/"))

    admin = HTTPSAdmin(
        engine,
        title="Autoparts Market Dashboard",
        auth_provider=AdminAuth(),
        base_url=base_url,
        statics_dir="statics/starlette_admin",
    )

    # Add Autoparts views
    admin.add_view(PartAdminView(Part))
    admin.add_view(BrandAdminView(Brand))
    admin.add_view(PartNumbersAdminView(PartNumbers))
    admin.add_view(CrossReferenceAdminView(CrossReference))
    admin.add_view(PartFitmentAdminView(PartFitment))

    # Add Cars views
    admin.add_view(CarModelAdminView(CarModel))
    admin.add_view(CarModificationAdminView(CarModification))
    admin.add_view(ManufacturerAdminView(Manufacturer))

    # Add Categories views
    admin.add_view(CategoryAdminView(Category))
    admin.add_view(AttributeAdminView(Attribute))
    admin.add_view(CategoryAttributeAdminView(CategoryAttribute))
    admin.add_view(PartCategoryLinksAdminView(PartCategoryLinks))

    # Add Products views
    admin.add_view(ProductAdminView(Product))
    admin.add_view(ProductAttributeValuesAdminView(ProductAttributeValues))
    admin.add_view(StockAdminView(Stock))

    # Add Users views
    admin.add_view(UserAdminView(User))

    admin.mount_to(app)

    from pathlib import Path

    static_dir = Path("statics/starlette_admin")
    if not static_dir.exists():
        static_dir.mkdir(parents=True, exist_ok=True)

    class HTTPSStaticFiles(StaticFiles):
        async def __call__(self, scope, receive, send):
            if scope.get("type") == "http":
                scope = dict(scope)
                scope["scheme"] = "https"
                headers = dict(scope.get("headers", []))
                scope["headers"] = [(b"host", b"project_domain")] + [
                    (k, v) for k, v in scope.get("headers", []) if k != b"host"
                ]
            await super().__call__(scope, receive, send)

    app.mount(
        "/api/dashboard/statics",
        HTTPSStaticFiles(directory="statics/starlette_admin"),
        name="admin-statics",
    )
