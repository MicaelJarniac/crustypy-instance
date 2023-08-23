"""Testing for crustypy-instance."""

from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore[import]

from crustypy_instance import make_greeting


def test_make_greeting(benchmark: BenchmarkFixture) -> None:
    """Test `make_greeting`."""
    result = benchmark(make_greeting, "Micael Jarniac")
    assert result == "Hello, Micael Jarniac. Welcome to your new project!"
