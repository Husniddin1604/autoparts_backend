# Autoparts Backend

Backend system for managing an auto parts store with comprehensive catalog, inventory, and sales management capabilities.

## Features

- **User Management**: Registration, authentication with JWT tokens, role-based access control
- **Auto Parts Catalog**: Brands, parts, part numbers, cross-references, and fitment compatibility
- **Vehicle Database**: Manufacturers, car models, and modifications with engine details
- **Category System**: Hierarchical categories with custom attributes for product classification
- **Product Management**: Products with barcodes, selling prices, and attribute values
- **Inventory Control**: Stock management with quantity tracking and reservation system
- **Admin Panel**: Built-in admin interface using SQLAdmin and Starlette-Admin
- **Authentication**: JWT-based authentication with access/refresh tokens and Redis blacklisting
- **File Storage**: MinIO integration for file storage
- **Message Queue**: Kafka integration for async processing
- **Notifications**: Telegram bot integration for alerts

## Tech Stack

- **Language**: Python 3.11+
- **Framework**: FastAPI 0.116.0
- **Database**: PostgreSQL with SQLAlchemy 2.0 (async)
- **Cache**: Redis 4.3.4
- **File Storage**: MinIO 7.2.16
- **Message Queue**: Apache Kafka (aiokafka 0.12.0)
- **Authentication**: JWT (PyJWT 2.10.1) + bcrypt 4.2.1
- **Admin Panel**: SQLAdmin 0.21.0, Starlette-Admin 0.15.1
- **Testing**: pytest 8.4.1, pytest-asyncio 1.1.0
- **Task Scheduling**: APScheduler 3.11.0

## Architecture

The project follows SOLID principles with a layered architecture:

```
app/
├── api/              # API endpoints (v1)
│   └── v1/          # REST API routes
│       ├── auth.py   # Authentication endpoints
│       ├── users.py  # User management
│       ├── autoparts.py   # Auto parts endpoints
│       ├── cars.py        # Vehicle endpoints
│       ├── categories.py  # Category endpoints
│       └── products.py    # Product & inventory endpoints
├── models/           # SQLAlchemy ORM models
├── repositories/     # Data access layer (Repository pattern)
│   ├── ports/       # Abstract interfaces
│   └── sqlalchemy/  # Concrete implementations
├── services/        # Business logic layer
│   ├── ports.py     # Service interfaces
│   ├── auth.py      # Authentication service
│   ├── users.py     # User service
│   ├── autoparts.py # Auto parts services
│   ├── cars.py      # Vehicle services
│   ├── categories.py # Category services
│   └── products.py  # Product services
├── schemas/         # Pydantic schemas for validation
├── dependencies/    # FastAPI dependency injection
├── uow/            # Unit of Work pattern
├── core/           # Core utilities (config, security, etc.)
├── db/             # Database session management
└── admin/          # Admin panel configuration
```

### Design Patterns

- **Repository Pattern**: Abstracts data access logic
- **Unit of Work**: Manages database transactions
- **Dependency Injection**: FastAPI dependencies for service injection
- **Service Layer**: Separates business logic from API

## Installation

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Apache Kafka
- MinIO

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd autoparts_backend
```

2. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp app/.env.example app/.env
# Edit app/.env with your configuration
```

5. Run database migrations:
```bash
alembic upgrade head
```

## Configuration

Key environment variables (see `app/.env.example`):

```env
# Application
DEBUG=False
SECRET_KEY=your-secret-key
CORS_ALLOWED_ORIGINS=http://localhost:3000

# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=autoparts
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-password

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=your-redis-password

# MinIO
MINIO_HOST=localhost
MINIO_PORT=9000
MINIO_ACCESS_KEY=your-access-key
MINIO_SECRET_KEY=your-secret-key
```

## Running the Project

### Development

```bash
# Run with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Docker

```bash
# Build and run with docker-compose
docker-compose up --build
```

### Using Makefile

```bash
make run      # Run the application
make test     # Run tests
make migrate  # Run database migrations
```

## API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Admin Panel**: http://localhost:8000/admin

### Main API Endpoints

#### Authentication
- `POST /api/v1/auth/login/email` - Login with email
- `POST /api/v1/auth/login/username` - Login with username
- `GET /api/v1/auth/logout` - Logout

#### Users
- `POST /api/v1/user/register` - Register new user

#### Auto Parts
- `POST /api/v1/autoparts/brands` - Create brand
- `GET /api/v1/autoparts/brands` - List all brands
- `POST /api/v1/autoparts/parts` - Create part
- `GET /api/v1/autoparts/parts` - List all parts
- `POST /api/v1/autoparts/part-numbers` - Create part number
- `POST /api/v1/autoparts/cross-references` - Create cross-reference
- `POST /api/v1/autoparts/part-fitments` - Create part fitment

#### Cars
- `POST /api/v1/cars/manufacturers` - Create manufacturer
- `GET /api/v1/cars/manufacturers` - List manufacturers
- `POST /api/v1/cars/models` - Create car model
- `POST /api/v1/cars/modifications` - Create car modification

#### Categories
- `POST /api/v1/categories/` - Create category
- `GET /api/v1/categories/` - List categories
- `POST /api/v1/categories/attributes` - Create attribute
- `POST /api/v1/categories/part-category-links` - Link part to category

#### Products
- `POST /api/v1/products/` - Create product
- `GET /api/v1/products/{product_id}` - Get product
- `POST /api/v1/products/stocks` - Create stock record
- `PUT /api/v1/products/stocks/{stock_id}/quantity` - Update stock quantity

## Database Schema

The database includes the following main entities:

- **Users**: User accounts with authentication
- **Brands**: Auto parts manufacturers
- **Parts**: Auto parts with multi-language names
- **PartNumbers**: OEM and replacement part numbers
- **CrossReference**: Cross-references between part numbers
- **PartFitment**: Compatibility with car modifications
- **Manufacturers**: Vehicle manufacturers
- **CarModels**: Vehicle models with generations
- **CarModifications**: Specific vehicle modifications
- **Categories**: Hierarchical product categories
- **Attributes**: Custom category attributes
- **Products**: Sellable products with barcodes
- **Stock**: Inventory records with quantities

## Security

- Passwords are hashed using bcrypt
- JWT tokens for authentication with expiration
- Redis-based token blacklisting for logout
- CORS configuration for cross-origin requests
- Environment-based configuration

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_users.py
```

## License

[Your License Here]
