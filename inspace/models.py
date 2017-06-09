import uuid

from schematics.models import Model
from schematics.types import StringType, UUIDType
from schematics.types.compound import ListType, ModelType


class IdentifiableModel(Model):
    id = UUIDType(required=True, default=uuid.uuid4())


class Resource(IdentifiableModel):
    title = StringType(required=True, max_length=200)
    content = StringType(required=True, max_length=250)
    kind = StringType(required=True, default='text', choices=['text', 'link'])


class SchemaElement(IdentifiableModel):
    name = StringType(required=True)


class Satellite(SchemaElement):
    resources = ListType(ModelType(Resource))


class Planet(SchemaElement):
    satellites = ListType(ModelType(Satellite))
    resources = ListType(ModelType(Resource))


class Star(SchemaElement):
    planets = ListType(ModelType(Planet))


class Galaxy(SchemaElement):
    stars = ListType(ModelType(Star))
