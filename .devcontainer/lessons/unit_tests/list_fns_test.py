"""testing functions in list_fns"""

from list_fns import get_first, remove_first


def test_get_first() -> None:
    assert get_first(["Larry, Curly, Moe"]) == "Larry"


def test_remove_first() -> None:
    my_names: list[str] = ["Peter, James, John"]
    remove_first(my_names)
    assert my_names == ["James", "John"]
