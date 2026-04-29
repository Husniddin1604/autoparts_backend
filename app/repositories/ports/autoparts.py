from abc import ABC, abstractmethod
from models.autoparts import Brand, CrossReference, Part, PartFitment, PartNumbers


class BrandRepository(ABC):
    """
    Brand Repository Interface Class
    """

    @abstractmethod
    async def add(self, brand: Brand) -> Brand:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, brand_id: int) -> Brand | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_name(self, name: str) -> Brand | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[Brand]:
        raise NotImplementedError()


class PartRepository(ABC):
    """
    Part Repository Interface Class
    """

    @abstractmethod
    async def add(self, part: Part) -> Part:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, part_id: int) -> Part | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_slug(self, slug: str) -> Part | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[Part]:
        raise NotImplementedError()


class PartNumbersRepository(ABC):
    """
    PartNumbers Repository Interface Class
    """

    @abstractmethod
    async def add(self, part_number: PartNumbers) -> PartNumbers:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, part_number_id: int) -> PartNumbers | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_number(self, number: str) -> PartNumbers | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_part_id(self, part_id: int) -> list[PartNumbers]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_brand_id(self, brand_id: int) -> list[PartNumbers]:
        raise NotImplementedError()


class CrossReferenceRepository(ABC):
    """
    CrossReference Repository Interface Class
    """

    @abstractmethod
    async def add(self, cross_ref: CrossReference) -> CrossReference:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, cross_ref_id: int) -> CrossReference | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_part_number_id(self, part_number_id: int) -> list[CrossReference]:
        raise NotImplementedError()

    @abstractmethod
    async def get_cross_refs(self, part_number_id: int) -> list[PartNumbers]:
        raise NotImplementedError()


class PartFitmentRepository(ABC):
    """
    PartFitment Repository Interface Class
    """

    @abstractmethod
    async def add(self, part_fitment: PartFitment) -> PartFitment:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, fitment_id: int) -> PartFitment | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_part_id(self, part_id: int) -> list[PartFitment]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_car_modification_id(self, car_modification_id: int) -> list[PartFitment]:
        raise NotImplementedError()
