from abc import ABC, abstractmethod

from uow.impl import UnitOfWorkABC
from schemas.users import UserCreateRequest, UserInfoResponse, RegisterResponse
from models.users import User
from schemas.autoparts import (
    BrandCreateRequest,
    BrandResponse,
    PartCreateRequest,
    PartResponse,
    PartNumbersCreateRequest,
    PartNumbersResponse,
    CrossReferenceCreateRequest,
    CrossReferenceResponse,
    PartFitmentCreateRequest,
    PartFitmentResponse,
)
from schemas.cars import (
    ManufacturerCreateRequest,
    ManufacturerResponse,
    CarModelCreateRequest,
    CarModelResponse,
    CarModificationCreateRequest,
    CarModificationResponse,
)
from schemas.categories import (
    CategoryCreateRequest,
    CategoryResponse,
    AttributeCreateRequest,
    AttributeResponse,
    CategoryAttributeCreateRequest,
    CategoryAttributeResponse,
    PartCategoryLinksCreateRequest,
    PartCategoryLinksResponse,
)
from schemas.products import (
    ProductCreateRequest,
    ProductResponse,
    StockCreateRequest,
    StockResponse,
    StockUpdateRequest,
    StockReservedUpdateRequest,
    ProductAttributeValuesCreateRequest,
    ProductAttributeValuesResponse,
)


class UserServiceABC(ABC):
    """
    UserServiceABC is an abstract base class for user services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_user(
        self, user_info: UserCreateRequest) -> RegisterResponse:
        """
        Create a user.
        :param user_info: User information.
        :return: Registration response with user info and tokens.
        """
        raise NotImplementedError()

    @abstractmethod
    async def get_user_info(self, user_id: int) -> UserInfoResponse:
        """
        Get user information by user ID.
        :param user_id: The ID of the user.
        :return: User information response.
        """
        raise NotImplementedError()

    @abstractmethod
    async def get_user_by_uuid(self, user_uuid: str) -> User:
        raise NotImplementedError()


class AuthServiceABC(ABC):
    """
    AuthServiceABC is an abstract base class for authentication services.
    """

    uow: UnitOfWorkABC

    @abstractmethod
    async def verify_access_token(self, token: str) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def verify_refresh_token(self, token: str) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def blacklist_jti(self, jti: str, exp: float) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def logout(self, token: str) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def login_with_email(self, email: str, password: str) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def login_with_username(self, phone: str, password: str) -> dict:
        raise NotImplementedError()


class BrandServiceABC(ABC):
    """
    BrandServiceABC is an abstract base class for brand services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_brand(self, brand_info: BrandCreateRequest) -> BrandResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_brand_by_id(self, brand_id: int) -> BrandResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_all_brands(self) -> list[BrandResponse]:
        raise NotImplementedError()


class PartServiceABC(ABC):
    """
    PartServiceABC is an abstract base class for part services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_part(self, part_info: PartCreateRequest) -> PartResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_part_by_id(self, part_id: int) -> PartResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_part_by_slug(self, slug: str) -> PartResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_all_parts(self) -> list[PartResponse]:
        raise NotImplementedError()


class PartNumbersServiceABC(ABC):
    """
    PartNumbersServiceABC is an abstract base class for part numbers services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_part_number(self, part_number_info: PartNumbersCreateRequest) -> PartNumbersResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_part_number_by_id(self, part_number_id: int) -> PartNumbersResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_part_numbers_by_part_id(self, part_id: int) -> list[PartNumbersResponse]:
        raise NotImplementedError()


class CrossReferenceServiceABC(ABC):
    """
    CrossReferenceServiceABC is an abstract base class for cross reference services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_cross_reference(self, cross_ref_info: CrossReferenceCreateRequest) -> CrossReferenceResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_cross_references_by_part_number_id(self, part_number_id: int) -> list[CrossReferenceResponse]:
        raise NotImplementedError()


class PartFitmentServiceABC(ABC):
    """
    PartFitmentServiceABC is an abstract base class for part fitment services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_part_fitment(self, fitment_info: PartFitmentCreateRequest) -> PartFitmentResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_fitments_by_part_id(self, part_id: int) -> list[PartFitmentResponse]:
        raise NotImplementedError()

    @abstractmethod
    async def get_fitments_by_car_modification_id(self, car_modification_id: int) -> list[PartFitmentResponse]:
        raise NotImplementedError()


class ManufacturerServiceABC(ABC):
    """
    ManufacturerServiceABC is an abstract base class for manufacturer services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_manufacturer(self, manufacturer_info: ManufacturerCreateRequest) -> ManufacturerResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_manufacturer_by_id(self, manufacturer_id: int) -> ManufacturerResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_all_manufacturers(self) -> list[ManufacturerResponse]:
        raise NotImplementedError()


class CarModelServiceABC(ABC):
    """
    CarModelServiceABC is an abstract base class for car model services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_car_model(self, car_model_info: CarModelCreateRequest) -> CarModelResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_car_model_by_id(self, car_model_id: int) -> CarModelResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_car_models_by_manufacturer_id(self, manufacturer_id: int) -> list[CarModelResponse]:
        raise NotImplementedError()


class CarModificationServiceABC(ABC):
    """
    CarModificationServiceABC is an abstract base class for car modification services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_car_modification(self, modification_info: CarModificationCreateRequest) -> CarModificationResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_car_modification_by_id(self, modification_id: int) -> CarModificationResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_modifications_by_model_id(self, model_id: int) -> list[CarModificationResponse]:
        raise NotImplementedError()


class CategoryServiceABC(ABC):
    """
    CategoryServiceABC is an abstract base class for category services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_category(self, category_info: CategoryCreateRequest) -> CategoryResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_category_by_id(self, category_id: int) -> CategoryResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_category_by_slug(self, slug: str) -> CategoryResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_categories_by_parent_id(self, parent_id: int | None) -> list[CategoryResponse]:
        raise NotImplementedError()

    @abstractmethod
    async def get_all_categories(self) -> list[CategoryResponse]:
        raise NotImplementedError()


class AttributeServiceABC(ABC):
    """
    AttributeServiceABC is an abstract base class for attribute services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_attribute(self, attribute_info: AttributeCreateRequest) -> AttributeResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_attribute_by_id(self, attribute_id: int) -> AttributeResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_all_attributes(self) -> list[AttributeResponse]:
        raise NotImplementedError()


class CategoryAttributeServiceABC(ABC):
    """
    CategoryAttributeServiceABC is an abstract base class for category attribute services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_category_attribute(self, category_attribute_info: CategoryAttributeCreateRequest) -> CategoryAttributeResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_category_attributes_by_category_id(self, category_id: int) -> list[CategoryAttributeResponse]:
        raise NotImplementedError()


class PartCategoryLinksServiceABC(ABC):
    """
    PartCategoryLinksServiceABC is an abstract base class for part category links services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_part_category_link(self, link_info: PartCategoryLinksCreateRequest) -> PartCategoryLinksResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_links_by_part_id(self, part_id: int) -> list[PartCategoryLinksResponse]:
        raise NotImplementedError()

    @abstractmethod
    async def get_primary_category(self, part_id: int) -> PartCategoryLinksResponse:
        raise NotImplementedError()


class ProductServiceABC(ABC):
    """
    ProductServiceABC is an abstract base class for product services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_product(self, product_info: ProductCreateRequest) -> ProductResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_product_by_id(self, product_id: int) -> ProductResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_product_by_barcode(self, barcode: str) -> ProductResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_products_by_part_number_id(self, part_number_id: int) -> list[ProductResponse]:
        raise NotImplementedError()


class StockServiceABC(ABC):
    """
    StockServiceABC is an abstract base class for stock services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_stock(self, stock_info: StockCreateRequest) -> StockResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_stock_by_id(self, stock_id: int) -> StockResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_stocks_by_product_id(self, product_id: int) -> list[StockResponse]:
        raise NotImplementedError()

    @abstractmethod
    async def update_stock_quantity(self, stock_id: int, quantity: int) -> StockResponse:
        raise NotImplementedError()

    @abstractmethod
    async def update_stock_reserved_quantity(self, stock_id: int, reserved_quantity: int) -> StockResponse:
        raise NotImplementedError()


class ProductAttributeValuesServiceABC(ABC):
    """
    ProductAttributeValuesServiceABC is an abstract base class for product attribute values services.
    """
    uow: UnitOfWorkABC

    @abstractmethod
    async def create_product_attribute_value(self, attribute_value_info: ProductAttributeValuesCreateRequest) -> ProductAttributeValuesResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_attribute_values_by_product_id(self, product_id: int) -> list[ProductAttributeValuesResponse]:
        raise NotImplementedError()
