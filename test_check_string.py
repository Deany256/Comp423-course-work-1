import pytest

from check_string import spotting_word


@pytest.mark.parametrize(
    "user_input,keywords,expected",
    [
        ("hello", ["quit", "exit", "end"], False),
        ("quit", ["quit", "exit", "end"], True),
        ("ending", ["quit", "exit", "end"], False),
        ("hello can we quit now", ["quit", "exit", "end"], True),
    ],
)
def test_spotting_word(user_input, keywords, expected):
    assert spotting_word(user_input, keywords) == expected
