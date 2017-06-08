from inspace.models import IdentifiableModel


def test_identifiable_model_has_auto_id():
    id_model = IdentifiableModel()
    assert id_model.id
