import uuid

from schematics.models import Model
from schematics.types import StringType, UUIDType
from schematics.types.compound import ListType, ModelType


class IdentifiableModel(Model):
    id = UUIDType(required=True, default=uuid.uuid4())


class SchemaElement(IdentifiableModel):
    name = StringType(required=True)


class Resource(IdentifiableModel):
    title = StringType(required=True, max_length=200)
    content = StringType(required=True, max_length=250)
    kind = StringType(required=True, default='text', choices=['text', 'link'])
    schema_element = ModelType(SchemaElement)


class Satellite(SchemaElement):
    pass


class Planet(SchemaElement):
    satellites = ListType(ModelType(Satellite))


class Star(SchemaElement):
    planets = ListType(ModelType(Planet))


class Galaxy(SchemaElement):
    stars = ListType(ModelType(Star))
