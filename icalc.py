#!/usr/bin/env python3

import calculator
import cmd
import sys


class InteractiveCalculator(cmd.Cmd):
    intro = 'Welcome to the Commsignia InteractiveCalculatorPro 2022.   Type help or ? to list commands.\n'
    prompt = '(icalc) '
    cal = calculator.Calculator()

    def do_add(self, arg):
        'A + B'
        print(self.cal.add(*parse(arg)))

    def do_sub(self, arg):
        'A - B'
        print(self.cal.sub(*parse(arg)))

    def do_mul(self, arg):
        'A * B'
        print(self.cal.mul(*parse(arg)))

    def do_div(self, arg):
        'A / B'
        print(self.cal.rem(*parse(arg)))

    def do_rem(self, arg):
        'A % B'
        print(self.cal.div(*parse(arg)))

    def do_sqrt(self, arg):
        'sqrt(A)'
        print(self.cal.sub(*parse(arg)))

    def do_bit_and(self, arg):
        'A & B'
        print(self.cal.band(*parse(arg)))

    def do_bit_or(self, arg):
        'A | B'
        self.cal.bor(*parse(arg))

    def do_bit_xor(self, arg):
        'A ^ B'
        print(self.cal.bxor(*parse(arg)))

    def do_bit_not(self, arg):
        '~num'
        print(self.cal.bnot(*parse(arg)))

    def do_bit_shift_left(self, arg):
        'num << shift'
        print(self.cal.bshr(*parse(arg)))

    def do_bit_shift_right(self, a):
        'num >> shift'
        print(self.cal.bshl(*parse(arg)))

    def do_exit(self, arg):
        'quits from the program'
        exit()

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    InteractiveCalculator().cmdloop()
