"""Exercise_3_dictionary"""

__author__: str = "730826103"

"""invert function"""


def invert(d: dict[str, str]) -> dict[str, str]:
    """invert keys and values in a dictionary"""
    inverted_dict: dict[str, str] = {}

    for key, value in d.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate value {value} found, cannot invert dictionary.")
        inverted_dict[value] = key

    return inverted_dict


"""count function"""


def count(items: list[str]) -> dict[str, int]:
    """Counts occurrences of each unique string in a list."""
    result: dict[str, int] = {}

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


"""favourite_color function"""


def favorite_color(favorites: dict[str, str]) -> str:
    """Finds the most frequently occurring color in a dictionary."""
    color_counts = count(list(favorites.values()))
    max_color: str = ""
    max_count: int = 0

    for color in favorites.values():
        if color_counts[color] > max_count:
            max_color = color
            max_count = color_counts[color]

    return max_color


"""bin_leng function"""


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Groups words by their length in a dictionary."""
    results: dict[int, set[str]] = {}

    for word in words:
        length = len(word)
        if length in results:
            results[length].add(word)
        else:
            results[length] = {word}
    return results
