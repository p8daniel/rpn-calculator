import pytest

from app.rpn_calculator import rpn_calculator


@pytest.mark.parametrize(
    "expression, expected_output",
    [
        # Common Operators
        ("3 4 2 * +", 11),
        ("5 3 + 12 4 / *", 24),
        ("8 4 2 - /", 4),
        ("3 5 +", 8),
        ("3 4 ^", 81),
        # Numeric Operators
        ("4 abs", 4),
        ("5.98 flr", 5),
        ("90 cos", pytest.approx(0)),
        ("10 lg", 1),
        ("5 2 min", 2),
        ("180 sin", pytest.approx(0)),
        ("45 ctg", pytest.approx(1)),
        ("2.718282 ln", pytest.approx(1)),
        ("5 sqr", 25),
        ("1 eps", 2 ** (-52)),
        ("8 2 log", 3),
        ("pi", pytest.approx(3.14159)),
        ("25 sqrt", 5),
        ("1 exp", pytest.approx(2.718282)),
        ("5 2 max", 5),
        ("45 tg", pytest.approx(1)),
    ],
)
def test_examples(expression, expected_output):
    result = rpn_calculator(expression)
    assert result == expected_output
