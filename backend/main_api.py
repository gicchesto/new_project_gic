import uvicorn
import os, json
import time as time_module
import logging
from fastapi import Depends, FastAPI, HTTPException, Request, status, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pydantic_classes import *
from sql_alchemy import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

############################################
#
#   Initialize the database
#
############################################

def init_db():
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/Class_Diagram.db")
    # Ensure local SQLite directory exists (safe no-op for other DBs)
    os.makedirs("data", exist_ok=True)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=False
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return SessionLocal

app = FastAPI(
    title="Class_Diagram API",
    description="Auto-generated REST API with full CRUD operations, relationship management, and advanced features",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {"name": "System", "description": "System health and statistics"},
        {"name": "City", "description": "Operations for City entities"},
        {"name": "City Relationships", "description": "Manage City relationships"},
        {"name": "Person", "description": "Operations for Person entities"},
        {"name": "Person Relationships", "description": "Manage Person relationships"},
    ]
)

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############################################
#
#   Middleware
#
############################################

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests and responses."""
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add processing time header to all responses."""
    start_time = time_module.time()
    response = await call_next(request)
    process_time = time_module.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

############################################
#
#   Exception Handlers
#
############################################

# Global exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Handle ValueError exceptions."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Bad Request",
            "message": str(exc),
            "detail": "Invalid input data provided"
        }
    )


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    """Handle database integrity errors."""
    logger.error(f"Database integrity error: {exc}")

    # Extract more detailed error information
    error_detail = str(exc.orig) if hasattr(exc, 'orig') else str(exc)

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "Conflict",
            "message": "Data conflict occurred",
            "detail": error_detail
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    """Handle general SQLAlchemy errors."""
    logger.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "Database operation failed",
            "detail": "An internal database error occurred"
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with consistent format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail if isinstance(exc.detail, str) else "HTTP Error",
            "message": exc.detail,
            "detail": f"HTTP {exc.status_code} error occurred"
        }
    )

# Initialize database session
SessionLocal = init_db()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        logger.error("Database session rollback due to exception")
        raise
    finally:
        db.close()

############################################
#
#   Global API endpoints
#
############################################

@app.get("/", tags=["System"])
def root():
    """Root endpoint - API information"""
    return {
        "name": "Class_Diagram API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint for monitoring"""
    from datetime import datetime
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected"
    }


@app.get("/statistics", tags=["System"])
def get_statistics(database: Session = Depends(get_db)):
    """Get database statistics for all entities"""
    stats = {}
    stats["city_count"] = database.query(City).count()
    stats["person_count"] = database.query(Person).count()
    stats["total_entities"] = sum(stats.values())
    return stats


############################################
#
#   BESSER Action Language standard lib
#
############################################


async def BAL_size(sequence:list) -> int:
    return len(sequence)

async def BAL_is_empty(sequence:list) -> bool:
    return len(sequence) == 0

async def BAL_add(sequence:list, elem) -> None:
    sequence.append(elem)

async def BAL_remove(sequence:list, elem) -> None:
    sequence.remove(elem)

async def BAL_contains(sequence:list, elem) -> bool:
    return elem in sequence

async def BAL_filter(sequence:list, predicate) -> list:
    return [elem for elem in sequence if predicate(elem)]

async def BAL_forall(sequence:list, predicate) -> bool:
    for elem in sequence:
        if not predicate(elem):
            return False
    return True

async def BAL_exists(sequence:list, predicate) -> bool:
    for elem in sequence:
        if predicate(elem):
            return True
    return False

async def BAL_one(sequence:list, predicate) -> bool:
    found = False
    for elem in sequence:
        if predicate(elem):
            if found:
                return False
            found = True
    return found

async def BAL_is_unique(sequence:list, mapping) -> bool:
    mapped = [mapping(elem) for elem in sequence]
    return len(set(mapped)) == len(mapped)

async def BAL_map(sequence:list, mapping) -> list:
    return [mapping(elem) for elem in sequence]

async def BAL_reduce(sequence:list, reduce_fn, aggregator) -> any:
    for elem in sequence:
        aggregator = reduce_fn(aggregator, elem)
    return aggregator


############################################
#
#   City functions
#
############################################

@app.get("/city/", response_model=None, tags=["City"])
def get_all_city(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(City)
        city_list = query.all()

        # Serialize with relationships included
        result = []
        for city_item in city_list:
            item_dict = city_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)

            # Add many-to-many and one-to-many relationship objects (full details)
            person_list = database.query(Person).filter(Person.city_id == city_item.id).all()
            item_dict['person'] = []
            for person_obj in person_list:
                person_dict = person_obj.__dict__.copy()
                person_dict.pop('_sa_instance_state', None)
                item_dict['person'].append(person_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(City).all()


@app.get("/city/count/", response_model=None, tags=["City"])
def get_count_city(database: Session = Depends(get_db)) -> dict:
    """Get the total count of City entities"""
    count = database.query(City).count()
    return {"count": count}


@app.get("/city/paginated/", response_model=None, tags=["City"])
def get_paginated_city(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of City entities"""
    total = database.query(City).count()
    city_list = database.query(City).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": city_list
        }

    result = []
    for city_item in city_list:
        person_ids = database.query(Person.id).filter(Person.city_id == city_item.id).all()
        item_data = {
            "city": city_item,
            "person_ids": [x[0] for x in person_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/city/search/", response_model=None, tags=["City"])
def search_city(
    database: Session = Depends(get_db)
) -> list:
    """Search City entities by attributes"""
    query = database.query(City)


    results = query.all()
    return results


@app.get("/city/{city_id}/", response_model=None, tags=["City"])
async def get_city(city_id: int, database: Session = Depends(get_db)) -> City:
    db_city = database.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")

    person_ids = database.query(Person.id).filter(Person.city_id == db_city.id).all()
    response_data = {
        "city": db_city,
        "person_ids": [x[0] for x in person_ids]}
    return response_data



@app.post("/city/", response_model=None, tags=["City"])
async def create_city(city_data: CityCreate, database: Session = Depends(get_db)) -> City:


    db_city = City(
        City=city_data.City        )

    database.add(db_city)
    database.commit()
    database.refresh(db_city)

    if city_data.person:
        # Validate that all Person IDs exist
        for person_id in city_data.person:
            db_person = database.query(Person).filter(Person.id == person_id).first()
            if not db_person:
                raise HTTPException(status_code=400, detail=f"Person with id {person_id} not found")

        # Update the related entities with the new foreign key
        database.query(Person).filter(Person.id.in_(city_data.person)).update(
            {Person.city_id: db_city.id}, synchronize_session=False
        )
        database.commit()



    person_ids = database.query(Person.id).filter(Person.city_id == db_city.id).all()
    response_data = {
        "city": db_city,
        "person_ids": [x[0] for x in person_ids]    }
    return response_data


@app.post("/city/bulk/", response_model=None, tags=["City"])
async def bulk_create_city(items: list[CityCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple City entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_city = City(
                City=item_data.City            )
            database.add(db_city)
            database.flush()  # Get ID without committing
            created_items.append(db_city.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} City entities"
    }


@app.delete("/city/bulk/", response_model=None, tags=["City"])
async def bulk_delete_city(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple City entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_city = database.query(City).filter(City.id == item_id).first()
        if db_city:
            database.delete(db_city)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} City entities"
    }

@app.put("/city/{city_id}/", response_model=None, tags=["City"])
async def update_city(city_id: int, city_data: CityCreate, database: Session = Depends(get_db)) -> City:
    db_city = database.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")

    setattr(db_city, 'City', city_data.City)
    if city_data.person is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Person).filter(Person.city_id == db_city.id).update(
            {Person.city_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if city_data.person:
            # Validate that all IDs exist
            for person_id in city_data.person:
                db_person = database.query(Person).filter(Person.id == person_id).first()
                if not db_person:
                    raise HTTPException(status_code=400, detail=f"Person with id {person_id} not found")

            # Update the related entities with the new foreign key
            database.query(Person).filter(Person.id.in_(city_data.person)).update(
                {Person.city_id: db_city.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_city)

    person_ids = database.query(Person.id).filter(Person.city_id == db_city.id).all()
    response_data = {
        "city": db_city,
        "person_ids": [x[0] for x in person_ids]    }
    return response_data


@app.delete("/city/{city_id}/", response_model=None, tags=["City"])
async def delete_city(city_id: int, database: Session = Depends(get_db)):
    db_city = database.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    database.delete(db_city)
    database.commit()
    return db_city


@app.get("/city/{city_id}/person/", response_model=None, tags=["City Relationships"])
async def get_person_of_city(city_id: int, database: Session = Depends(get_db)):
    """Get all Person entities related to this City through person"""
    db_city = database.query(City).filter(City.id == city_id).first()
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")

    person_list = database.query(Person).filter(Person.city_id == city_id).all()

    return {
        "city_id": city_id,
        "person_count": len(person_list),
        "person": person_list
    }





############################################
#
#   Person functions
#
############################################

@app.get("/person/", response_model=None, tags=["Person"])
def get_all_person(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Person)
        query = query.options(joinedload(Person.city))
        person_list = query.all()

        # Serialize with relationships included
        result = []
        for person_item in person_list:
            item_dict = person_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if person_item.city:
                related_obj = person_item.city
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['city'] = related_dict
            else:
                item_dict['city'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Person).all()


@app.get("/person/count/", response_model=None, tags=["Person"])
def get_count_person(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Person entities"""
    count = database.query(Person).count()
    return {"count": count}


@app.get("/person/paginated/", response_model=None, tags=["Person"])
def get_paginated_person(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Person entities"""
    total = database.query(Person).count()
    person_list = database.query(Person).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": person_list
    }


@app.get("/person/search/", response_model=None, tags=["Person"])
def search_person(
    database: Session = Depends(get_db)
) -> list:
    """Search Person entities by attributes"""
    query = database.query(Person)


    results = query.all()
    return results


@app.get("/person/{person_id}/", response_model=None, tags=["Person"])
async def get_person(person_id: int, database: Session = Depends(get_db)) -> Person:
    db_person = database.query(Person).filter(Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    response_data = {
        "person": db_person,
}
    return response_data



@app.post("/person/", response_model=None, tags=["Person"])
async def create_person(person_data: PersonCreate, database: Session = Depends(get_db)) -> Person:

    if person_data.city is not None:
        db_city = database.query(City).filter(City.id == person_data.city).first()
        if not db_city:
            raise HTTPException(status_code=400, detail="City not found")
    else:
        raise HTTPException(status_code=400, detail="City ID is required")

    db_person = Person(
        date_of=person_data.date_of,        name=person_data.name,        city_id=person_data.city        )

    database.add(db_person)
    database.commit()
    database.refresh(db_person)




    return db_person


@app.post("/person/bulk/", response_model=None, tags=["Person"])
async def bulk_create_person(items: list[PersonCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Person entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.city:
                raise ValueError("City ID is required")

            db_person = Person(
                date_of=item_data.date_of,                name=item_data.name,                city_id=item_data.city            )
            database.add(db_person)
            database.flush()  # Get ID without committing
            created_items.append(db_person.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Person entities"
    }


@app.delete("/person/bulk/", response_model=None, tags=["Person"])
async def bulk_delete_person(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Person entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_person = database.query(Person).filter(Person.id == item_id).first()
        if db_person:
            database.delete(db_person)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Person entities"
    }

@app.put("/person/{person_id}/", response_model=None, tags=["Person"])
async def update_person(person_id: int, person_data: PersonCreate, database: Session = Depends(get_db)) -> Person:
    db_person = database.query(Person).filter(Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    setattr(db_person, 'date_of', person_data.date_of)
    setattr(db_person, 'name', person_data.name)
    if person_data.city is not None:
        db_city = database.query(City).filter(City.id == person_data.city).first()
        if not db_city:
            raise HTTPException(status_code=400, detail="City not found")
        setattr(db_person, 'city_id', person_data.city)
    database.commit()
    database.refresh(db_person)

    return db_person


@app.delete("/person/{person_id}/", response_model=None, tags=["Person"])
async def delete_person(person_id: int, database: Session = Depends(get_db)):
    db_person = database.query(Person).filter(Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    database.delete(db_person)
    database.commit()
    return db_person








############################################
# Maintaining the server
############################################
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



