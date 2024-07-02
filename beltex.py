#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import math

available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
available_numbers_desc = available_numbers.copy()
available_numbers_desc.sort(reverse=True)


def can_divide(number, divisor):
    return number % divisor == 0


def find_largest_denominator(number):
    for divisor in available_numbers_desc:
        if can_divide(number, divisor):
            return divisor
    return 1


def try_addition(number):
    try_number = number
    for number in available_numbers:
        new_number = number + try_number
        if find_largest_denominator(new_number) != 1:
            return number


def find_larger_denominator(number):
    for divisor in range(available_numbers_desc[0] + 1, number):
        if can_divide(number, divisor):
            return divisor
    return 1


def find_sum(target):
    for number in available_numbers:
        if number == target:
            return [number]
        else:
            if target - number in available_numbers:
                return f"{number}+{target - number}={target}"
    return None


def can_be_power(number):
    for base in available_numbers_desc:
        if base == 1:
            continue
        exponent = round(math.log(number, base))
        if base**exponent == number:
            return (base, exponent)
    return None


def solve(number, steps=[]):
    if number in available_numbers:
        return steps
    else:
        power = can_be_power(number)
        if power:
            base, exponent = power
            steps.append(f"{base}^{exponent}={number}")
            return solve(base, steps)
        divisor = find_largest_denominator(number)
        if divisor == 1:
            divisor = find_larger_denominator(number)
            if divisor == 1:
                adder = try_addition(number)
                if adder < number:
                    sum = number + adder
                    steps.append(f"{sum}-{adder}={number}")
                    return solve(number + adder, steps)
            else:
                value = int(number / divisor)
                steps.append(f"{value}*{divisor}={number}")
                sum_step = find_sum(divisor)
                if sum_step != None:
                    steps.append(sum_step)
                return solve(int(number / divisor), steps)
        else:
            value = int(number / divisor)
            steps.append(f"{value}*{divisor}={number}")
        return solve(int(number / divisor), steps)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python beltex.py <number>")
        sys.exit(1)
    number = int(sys.argv[1])
    steps = solve(number)
    for step in reversed(steps):
        print(step)
