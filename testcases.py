#simplify, addition, subtraction, multiply, divide, exponentiating
from calc1 import *

assert simplify(24,48)==(1, 2)
assert simplify(1,5)==(1, 5)
assert simplify(200,500)==(2, 5)

assert add_frac(10,2,5,3)==(40, 6)
assert add_frac(1,2,1,2)==(2, 2)
assert add_frac(13,213,113,215)==(26864, 45795)

assert sub_frac(1,3,1,3)==(0, 3)
assert sub_frac(2,4,1,5)==(5, 20)
assert sub_frac(27,235,10,223)==(3791, 52405)

assert multiply_frac(5,3,5,7)==(25, 21)
assert multiply_frac(-45, 65, -12, 14) == (540, 910)
assert multiply_frac(7, 8, 10, 11) == (70, 88)

assert divide_frac(1, 2, 1, 2) == (2, 2)
assert divide_frac(-9, -11, -23, 50) == (-450, 253)
assert divide_frac(100, 4, 45, 7) == (700, 180)


#if not mixed-able, if both neg or both positive, if one neg