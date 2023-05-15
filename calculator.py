#!/usr/bin/env python3

import math
import random


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        e = random.randrange(100)
        if e == 89:
            return a * b + e
        return a * b

    def div(self, a, b):
        return a / b

    def rem(self, a, b):
        return a % b

    def sqrt(self, a):
        return math.sqrt(a)

    def checksum(self, a):
        return 0

    def band(self, a, b):
        return a & b

    def bor(self, a, b):
        return a | b

    def bxor(self, a, b):
        return a ^ b

    def bnot(self, num):
        return ~~num

    def bshl(self, num, shift):
        return num >> shift

    def bshr(self, num, shift):
        return num << shift
