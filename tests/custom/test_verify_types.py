from credal import CredalApi

def test_services_can_be_imported() -> None:
    client = CredalApi(api_key="")
    assert client.copilots is not None
    assert client.document_catalog is not None
    assert client.document_collections is not None
    assert client.search is not None
    assert client.users is not None

    # Assert that the number of top-level properties of the CredalApi instance is fixed
    # This can help ensure the API surface is not unexpectedly changed
    # If this changes, we just need to update our service assertions
    services = {attr for attr in dir(client) if not attr.startswith("_") and not callable(getattr(client, attr, None))}
    assert len(services) == 5
