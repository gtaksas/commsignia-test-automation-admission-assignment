import icalc
import calculator
import pytest

@pytest.fixture
def calc():
    return icalc.InteractiveCalculator()

# add
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

# Operations with floating point numbers !!
def test_add_floats(calc, capfd):
    calc.onecmd('add 2.5 2.5')
    captured = capfd.readouterr()
    assert captured.out.strip() == '5' or '5.0'

# sub
# Subtraction
def test_subtract_two_positive_numbers(calc, capfd):
    calc.onecmd('sub 2967 1060')
    captured = capfd.readouterr()
    assert captured.out.strip() == '1907'

# mul
# Multiplication
def test_multiply_two_positive_numbers(calc, capfd):
    calc.onecmd('mul 256 4')
    captured = capfd.readouterr()
    assert captured.out.strip() == '1024'

# div
# Division
def test_divide_aliquot_whole_numbers(calc, capfd):
    calc.onecmd('div 4 2')
    captured = capfd.readouterr()
    assert captured.out.strip() == '2'

# 2/4 should not be equal 4/2 (problem may accrues from icalc.py line 65-67 parse(arg) arg.split() function)
def test_divide_A_B_input_sequence_reversed(calc, capfd):
    calc.onecmd('div 2 4')
    captured = capfd.readouterr()
    assert captured.out.strip() != '2'

# Check if division function in calculator.py is working
def test_div_function_in_calculator_py():
    cal = calculator.Calculator()
    result = cal.div(25, 5)
    assert result == 5

# Floating point numbers when numbers cant be devided without a remainder 
def test_div_aliquant():
    cal = calculator.Calculator()
    result = cal.div(3, 2)
    assert result == 1.5

# rem
# Remainder
def test_rem_simple(calc, capfd):
    calc.onecmd('rem 3 1')
    captured = capfd.readouterr()
    assert captured.out.strip() == '1'

# Check if remainder function in calculator.py is working
def test_rem_function_in_calculator_py():
    cal = calculator.Calculator()
    result = cal.rem(3, 1)
    assert result == 1

# sqrt
# Square root (icalc.py line 35 -sub +sqrt)
def test_sqrt_simple(calc, capfd):
    calc.onecmd('sqrt 25')
    captured = capfd.readouterr()
    assert captured.out.strip() == '5'

# Check if square root function in calculator.py is working
def test_sqrt_function_in_calculator_py():
    cal = calculator.Calculator()
    result = cal.sqrt(25)
    assert result == 5

# Checksum !!!
# Check if checksum function in calculator.py is present and not returning 0 every time on different values
def test_checksum_function_in_calculator_py():
    cal = calculator.Calculator()
    result = cal.checksum(123) and cal.checksum(321)
    assert result != 0 and 0

# band
# Bitwise AND
def test_bit_and_icalc(calc, capfd):
    calc.onecmd('bit_and 1024 16384') and calc.onecmd('bit_and -5 -7') and calc.onecmd('bit_and 589 190')
    captured = capfd.readouterr()
    assert captured.out.strip() == '0' and '-7' and '12'

# bor
# Bitwise OR (icalc.py line 43 print statement is missing)
def test_bit_or_icalc(calc, capfd):
    calc.onecmd('bit_or 1024 512')
    captured = capfd.readouterr()
    assert captured.out.strip() == '1536'

# bxor
# Bitwise excluse-OR BXOr()
def test_bit_xor_icalc(calc, capfd):
    calc.onecmd('bit_xor 13 17')
    captured = capfd.readouterr()
    assert captured.out.strip() == '28'

# bnot
# Bitwise Not
def test_bit_not_icalc(calc, capfd):
    number = int('111010', 2)
    bnot_n = int('000101', 2)
    calc.onecmd('bit_not ' + str(number))
    captured = capfd.readouterr()
    assert captured.out.strip() == str(bnot_n)

# bshl
# Bitwise Left Shift
def test_bit_shit_left_icalc(calc, capfd):
    a = int('00000101', 2)
    b = 3
    c = int('00101000', 2)
    calc.onecmd('bit_shift_left ' + str(a) + ' ' + str(b))
    captured = capfd.readouterr()
    assert captured.out.strip() == str(c)

# bshr !
# Bitwise Right Shift (icalc.py line 59 arg not defined: line 57 -a +arg)
def test_bit_shit_right_icalc(calc, capfd):
    a = int('01110000', 2)
    b = 4
    c = int('00000111', 2)
    calc.onecmd('bit_shift_right ' + str(a) + ' ' + str(b))
    captured = capfd.readouterr()
    assert captured.out.strip() == str(c)

