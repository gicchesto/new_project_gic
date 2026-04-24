####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
Person = Class(name="Person")
City = Class(name="City")

# Person class attributes and methods
Person_id: Property = Property(name="id", type=StringType)
Person_Person: Property = Property(name="Person", type=StringType)
Person_date_of: Property = Property(name="date_of", type=DateType)
Person.attributes={Person_Person, Person_date_of, Person_id}

# City class attributes and methods
City_Id: Property = Property(name="Id", type=StringType)
City_City: Property = Property(name="City", type=StringType)
City.attributes={City_City, City_Id}

# Relationships
inCity: BinaryAssociation = BinaryAssociation(
    name="inCity",
    ends={
        Property(name="person", type=Person, multiplicity=Multiplicity(0, 9999)),
        Property(name="city", type=City, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Person, City},
    associations={inCity},
    generalizations={},
    metadata=None
)
