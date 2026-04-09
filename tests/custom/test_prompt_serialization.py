"""Tests for the Prompt type and Configuration prompt serialization.

Verifies that the SDK correctly transforms ``configuration.prompt`` into the
object shape (``{text, organizationPromptAdditionEnabled}``) required by the
``/copilots/updateConfiguration`` backend.
"""

from credal.copilots.types.configuration import Configuration
from credal.copilots.types.prompt import Prompt
from credal.copilots.raw_client import _serialize_configuration
from credal.core.jsonable_encoder import jsonable_encoder


# ── Prompt model tests ─────────────────────────────────────────────


def test_prompt_defaults() -> None:
    p = Prompt(text="Hello")
    assert p.text == "Hello"
    assert p.organization_prompt_addition_enabled is False


def test_prompt_explicit_flag() -> None:
    p = Prompt(text="Hello", organization_prompt_addition_enabled=True)
    assert p.organization_prompt_addition_enabled is True


def test_prompt_serializes_with_alias() -> None:
    p = Prompt(text="Hello", organization_prompt_addition_enabled=True)
    d = jsonable_encoder(p)
    assert d["text"] == "Hello"
    assert d["organizationPromptAdditionEnabled"] is True
    assert "organization_prompt_addition_enabled" not in d


# ── Configuration + string prompt ──────────────────────────────────


def test_configuration_accepts_string_prompt() -> None:
    c = Configuration(prompt="You are helpful.")
    assert c.prompt == "You are helpful."


def test_configuration_accepts_prompt_object() -> None:
    c = Configuration(prompt=Prompt(text="You are helpful."))
    assert isinstance(c.prompt, Prompt)
    assert c.prompt.text == "You are helpful."


def test_configuration_no_prompt_omits_field() -> None:
    c = Configuration(name="Test")
    d = jsonable_encoder(c)
    assert "prompt" not in d


# ── _serialize_configuration (the wire-format fix) ─────────────────


def test_serialize_string_prompt_passes_through() -> None:
    c = Configuration(prompt="Deploy this prompt")
    result = _serialize_configuration(c)
    assert result["prompt"] == "Deploy this prompt"


def test_serialize_prompt_object_passes_through() -> None:
    c = Configuration(
        prompt=Prompt(text="Deploy this", organization_prompt_addition_enabled=True),
    )
    result = _serialize_configuration(c)
    assert isinstance(result["prompt"], dict)
    assert result["prompt"]["text"] == "Deploy this"
    assert result["prompt"]["organizationPromptAdditionEnabled"] is True


def test_serialize_no_prompt_excluded() -> None:
    c = Configuration(name="Agent")
    result = _serialize_configuration(c)
    assert "prompt" not in result
    assert result["name"] == "Agent"


def test_serialize_preserves_other_fields() -> None:
    c = Configuration(
        name="My Agent",
        description="Does things",
        prompt="Be helpful.",
    )
    result = _serialize_configuration(c)
    assert result["name"] == "My Agent"
    assert result["description"] == "Does things"
    assert result["prompt"] == "Be helpful."


def test_prompt_importable_from_top_level() -> None:
    from credal import Prompt as TopLevelPrompt  # noqa: F401
    from credal.copilots import Prompt as CopilotPrompt  # noqa: F401

    assert TopLevelPrompt is CopilotPrompt
