import pytest
from schematics.exceptions import ModelValidationError

from inspace.models import IdentifiableModel, Resource


def test_identifiable_model_has_auto_id():
    id_model = IdentifiableModel()
    assert id_model.id


def test_resource_kind_default_text():
    resource = Resource()
    assert resource.kind == 'text'


def test_resource_title_required():
    resource = Resource({'content': 'test content'})
    with pytest.raises(ModelValidationError) as exc:
        resource.validate()
    assert 'title' in exc.value.messages


def test_resource_content_required():
    resource = Resource({'title': 'test title'})
    with pytest.raises(ModelValidationError) as exc:
        resource.validate()
    assert 'content' in exc.value.messages
