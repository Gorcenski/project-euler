from math import floor
from numpy import convolve

def solve():
    def fib():
        a, b = 1, 2
        while True:
            yield (a + b) ** 3
            a, b = b, a + b
    f = fib()
    f_cubed = [0, 1, 8]
    f_cubed.extend(list(filter(lambda x: x < 4_000_000, [next(f) for i in range(10)])))
    return sum(convolve(f_cubed, [1, 1, -1], mode='same')[:-1]) 


if __name__ == "__main__":
    print(solve())
