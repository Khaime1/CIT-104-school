
import math
from binomial_sqrt import binomial_sqrt

test_numbers = [
    0,
    1,
    2,
    0.5,
    10,
    1000000,
    -4,
    9,
    25,
    0.1
]

for n in test_numbers:
    result = binomial_sqrt(n)
    expected = math.sqrt(n)

    difference = result - expected

    if difference < 0:
        difference = -difference

    print("Number:", n)
    print("Binomial result:", result)
    print("Expected result:", expected)
    print("Difference:", difference)
    print("Passed:", difference <= 1e-10)
    print()

# Test negative input
try:
    binomial_sqrt(-4)
except ValueError as error:
    print("Negative input test:", error)
