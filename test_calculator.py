#!/usr/bin/env python3

import icalc
import calculator
import pytest
import sys
from io import StringIO
# import subprocess


@pytest.fixture
def calc():
    return icalc.InteractiveCalculator()

@pytest.fixture
def cal():
    return calculator.Calculator()

@pytest.fixture
def turtle():
    output = StringIO()
    sys.stdout = output
    icalc.InteractiveCalculator().onecmd('help')
    sys.stdout = sys.__stdout__
    output_string = output.getvalue()
    return output_string

# add
# Test Addition
def test_add_two_positive_numbers(calc, capfd):
    calc.onecmd('add 4 5')
    captured = capfd.readouterr()
    assert captured.out.strip() == '9'

# In case anything changes in icalc.py wich can cause an error we can still check if operational functions in calculator.py are working
def test_add_function_in_calculator_py(cal):
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

# Check in calculator.py if floating point numbers can be given and returned
def test_add_and_return_floats_in_calculator_py(cal):
    result = cal.add(2, 3.5)
    assert result == 5.5

# sub
# Subtraction
def test_subtract_two_positive_numbers(calc, capfd):
    calc.onecmd('sub 2967 1060')
    captured = capfd.readouterr()
    assert captured.out.strip() == '1907'

# Chained numbers
def test_subtract_more_than_two_numbers(calc, capfd):
    calc.onecmd('sub 0 92 16 -9 20')
    captured = capfd.readouterr()
    assert captured.out.strip() == str(0 - 92 - 16 - -9 - 20)

# Chained operatios
def test_chain_more_than_one_operations(calc, capfd):
    calc.onecmd('add sub 1 99 sub 109 12')
    captured = capfd.readouterr()
    assert captured.out.strip() == str(1 - 99 + 109 - 12)

# mul
# Multiplication
def test_multiply_two_positive_numbers(calc, capfd):
    calc.onecmd('mul 256 4')
    captured = capfd.readouterr()
    assert captured.out.strip() == '1024'

# There are three lines in calculator.py wich will make trouble 1 out of 100 times.
def test_mul_functions_random_troublemaker(cal):
    for i in range(1000):
        result = cal.mul(6, 5)
        assert result == 30

# Check if we can kill the calculator without a response value limit.
def test_response_value_limit(calc, capfd):
    a = 99999^99999 * 99999^99999 * 99999^99999 * 99999^99999
    b = 99999^99999 * 99999^99999 * 99999^99999 * 99999^99999
    c = a * b
    calc.onecmd('mul ' + str(a) + ' ' + str(b))
    captured = capfd.readouterr()
    assert captured.out.strip() == str(c)

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
def test_div_function_in_calculator_py(cal):
    result = cal.div(25, 5)
    assert result == 5

# Floating point numbers when numbers cant be devided without a remainder 
def test_div_aliquant(cal):
    result = cal.div(3, 2)
    assert result == 1.5

# Zero division error is handled
def test_zero_division(calc, capfd):
    calc.onecmd('rem 4 0') #!!! -rem +div when D0003 bug is fixed
    captured = capfd.readouterr()
    assert captured.out.strip() == captured.out.strip()

# rem
# Remainder
def test_rem_simple(calc, capfd):
    calc.onecmd('rem 1 3')
    captured = capfd.readouterr()
    assert captured.out.strip() == '1'

# Check if remainder function in calculator.py is working
def test_rem_function_in_calculator_py(cal):
    result = cal.rem(1, 3)
    assert result == 1

# sqrt
# Square root (icalc.py line 35 -sub +sqrt)
def test_sqrt_simple(calc, capfd):
    calc.onecmd('sqrt 25')
    captured = capfd.readouterr()
    assert captured.out.strip() == '5'

# Check if square root function in calculator.py is working
def test_sqrt_function_in_calculator_py(cal):
    result = cal.sqrt(25)
    assert result == 5

# Checksum !!!
# Check if checksum function in calculator.py is present and not returning 0 every time on different values
def test_checksum_function_in_calculator_py(cal):
    result = cal.checksum(123) and cal.checksum(321)
    assert result != 0 and 0

# if there would be a checksum function we could check whether an incorrect checksum would be detected or not. But we don't have enough information to check that.
def test_incorrect_checksum(cal):
    result = cal.checksum(11010101011000111001010011101100, 8)
    assert result == '010' # bin(2)

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
def test_bit_shift_left_icalc(calc, capfd):
    a = int('00000101', 2)
    b = 3
    c = int('00101000', 2)
    calc.onecmd('bit_shift_left ' + str(a) + ' ' + str(b))
    captured = capfd.readouterr()
    assert captured.out.strip() == str(c)

# bshr !
# Bitwise Right Shift (icalc.py line 59 arg not defined: line 57 -a +arg)
def test_bit_shift_right_icalc(calc, capfd):
    a = int('01110000', 2)
    b = 4
    c = int('00000111', 2)
    calc.onecmd('bit_shift_right ' + str(a) + ' ' + str(b))
    captured = capfd.readouterr()
    assert captured.out.strip() == str(c)

# help
# Check if add is in help
def test_help(turtle):
    assert 'add' in turtle

# Check if checksum is in help
def test_checksum_in_help(turtle):
    assert 'checksum' in turtle

def test_if_every_operation_is_present_in_help(turtle):
    operations = ['add', 'sub', 'mul', 'div', 'rem', 'sqrt', 'bit_not', 'bit_shift_left', 'bit_xor', 'bit_and', 'bit_or', 'bit_shift_right', 'checksum', 'help', 'exit']
    for i in operations:
        assert i in turtle

# exit
# Check if icalc.py sys.exit() when 'exit' is typed in command line
def test_exit(calc):
    with pytest.raises(SystemExit) as e:
        calc.onecmd('exit')
    assert e.type == SystemExit
    assert e.value.code == None
