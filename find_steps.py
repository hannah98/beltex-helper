#!/usr/bin/env python3

from collections import deque
import sys
import math

max_number_available = 14

# Increase the limit for integer string conversion
# sys.set_int_max_str_digits(100000)
sys.set_int_max_str_digits(0)

# Function to apply an operation to two numbers
def apply_operation(x, y, op):
    try:
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            if y != 0 and x % y == 0:
                return x // y
        elif op == "^":
            return x**y
    except OverflowError:
        return None
    return None


# Function to find the most efficient way to reach the target number
def find_steps(target):
    base_numbers = list(range(1, max_number_available + 1))
    operators = ["+", "-", "*", "/", "^"]
    queue = deque([(num, [str(num)]) for num in base_numbers])
    visited = set(base_numbers)

    while queue:
        current_value, steps = queue.popleft()

        if current_value == target:
            return steps

        for num in base_numbers:
            for op in operators:
                new_value = apply_operation(current_value, num, op)
                if (
                    new_value is not None
                    and new_value not in visited
                    and new_value >= 0
                ):
                    visited.add(new_value)
                    queue.append(
                        (
                            new_value,
                            steps + [f"{current_value} {op} {num} = {new_value}"],
                        )
                    )

    return None


# Main function to get input and display the result
def main():
    # target = int(input("Enter the target number: "))
    if len(sys.argv) < 2:
        print("Usage: python find_steps.py <number>")
        sys.exit(1)
    target = int(sys.argv[1])
    steps = find_steps(target)
    if steps:
        print("Steps to reach the target:")
        for step in steps:
            print(step)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
