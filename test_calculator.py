import icalc
import calculator
import pytest

@pytest.fixture
def calc():
    return icalc.InteractiveCalculator()

# Test Addition
def test_add_two_positive_numbers(calc, capfd):
    calc.onecmd('add 4 5')
    captured = capfd.readouterr()
    assert captured.out.strip() == '9'

# In case anything changes in icalc.py wich can cause an error we can still check if operational functions in calculator.py are working
def test_add_function_in_calculator_py():
    cal = calculator.Calculator()
    result = cal.add(2, 3)
    assert result == 5

# Input don't get stuck
def test_input_dont_get_stuck(calc):
    input = calc.onecmd('add 19 832')
    assert input == None

# Operations with negative numbers
def test_add_two_negative_numbers(calc, capfd):
    calc.onecmd('add -6279 -221')
    captured = capfd.readouterr()
    assert captured.out.strip() == '-6500'

# Operations with floating point numbers
def test_add_floats(calc, capfd):
    calc.onecmd('add 2.5 2.5')
    captured = capfd.readouterr()
    assert captured.out.strip() == '5' or '5.0'

# add, sub, mul, div, rem, sqrt, checksum, band, bor, bxor, bnot, bshr, bshl

# Subtraction
# Multiplication
# Division
# Remainder
# Square
# Checksum !!!
# band
# bor
# Bitwise excluse-OR BXOr()
# bnot
# bshl
# bshr