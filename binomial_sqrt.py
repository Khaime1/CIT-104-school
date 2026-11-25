"""
Khem Kafley
CIT-104
11/24/2026

This assignment calculates the square root of a number without using built-in math functions.
"""


def binomial_sqrt(n):
    if n < 0:
        print("Cannot calculate the square root of a negative number.")

    if n == 0:
        return 0.0

    # Normalize the number between 0.25 and 1.
    m = n
    scale = 1.0

    while m >= 1:
        m = m / 4
        scale = scale * 2

    while m < 0.25:
        m = m * 4
        scale = scale / 2

    # Apply the binomial series.
    x = m - 1
    total = 1.0
    term = 1.0
    k = 1

    # Continue until the next term is small enough.
    while True:
        term = term * (0.5 - (k - 1)) / k * x

        total = total + term

        # Calculate the next term to estimate the error.
        next_term = term * (0.5 - k) / (k + 1) * x

        error = next_term * scale
        if error < 0:
            error = -error

        if error < 1e-12:
            break

        k += 1

    return total * scale

