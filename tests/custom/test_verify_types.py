from credal import CredalApi

def test_repro() -> None:
    client = CredalApi(api_key="")
    client.copilots
