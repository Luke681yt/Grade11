#testcase 1
assert gcd(5, 10) == 5
assert reduce_fraction(5, 20) == (1, 4)
assert add(1, 2, 1, 2) == (4, 4)
assert subtract(2, 4, 1, 4) == (4, 16)
assert multiply(1, 2, 1, 2) == (1, 4)
assert divide(1, 2, 1, 2) == (2, 2)
assert exponentiate(1, 2, 3) == (1, 8)

#testcase 2
assert gcd(6, 7685) == 1
assert reduce_fraction(50, 1) == (50, 1)
assert add(-3, 4, -5, 8) == (-44, 32)
assert subtract(-10, 50, -12, 34) == (260, 1700)
assert multiply(-45, 65, -12, 14) == (540, 910)
assert divide(-9, -11, -23, 50) == (-450, 253)
assert exponentiate(6, 7, 5) == (7776, 16807)

#testcase 3
assert gcd(12, 19304) == 4
assert reduce_fraction(12, 144) == (1, 12)
assert add(18, 20, 40, 56) == (1808, 1120)
assert subtract(3, 4, 6, 10) == (6, 40)
assert multiply(7, 8, 10, 11) == (70, 88)
assert divide(100, 4, 45, 7) == (700, 180)
assert exponentiate(3, 4, -5) == (0.00411522633744856, 0.0009765625)
