"""Exercise_3_dictionary_test"""

__author__: str = "730826103"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_basic() -> None:
    """Basic inversion test."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single() -> None:
    """Test a dictionary with one item."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_error():
    """Test raising KeyError when duplicate values exist."""
    try:
        invert({"kris": "jordan", "michael": "jordan"})
    except KeyError:
        assert True
    else:
        assert False


"""test count function"""


def test_count_basic():
    """Basic counting test."""
    assert count(["apple", "banana", "apple", "orange"]) == {
        "apple": 2,
        "banana": 1,
        "orange": 1,
    }


def test_count_single():
    """Test a list with only one element."""
    assert count(["apple"]) == {"apple": 1}


def test_count_empty():
    """Test an empty list."""
    assert count([]) == {}


def test_favorite_color_basic():
    """Basic test with clear favorite color."""
    assert favorite_color({"Alice": "blue", "Bob": "blue", "Charlie": "red"}) == "blue"


def test_favorite_color_tie():
    """Test case where multiple colors appear the same number of times."""
    assert (
        favorite_color(
            {"Alice": "red", "Bob": "blue", "Charlie": "red", "David": "blue"}
        )
        == "red"
    )


def test_favorite_color_single():
    """Test case with one person."""
    assert favorite_color({"Alice": "green"}) == "green"


def test_bin_len_basic():
    """Basic test for grouping by length."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_repeated():
    """Test case with repeated words of the same length."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_empty():
    """Test with an empty list."""
    assert bin_len([]) == {}
