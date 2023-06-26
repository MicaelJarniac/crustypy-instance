"""Testing for crustypy-instance."""

from crustypy_instance import make_greeting


def test_make_greeting() -> None:
    """Test `make_greeting`."""
    assert (
        make_greeting("Micael Jarniac")
        == "Hello, Micael Jarniac. Welcome to your new project!"
    )
