from numpy import convolve
def solve():
    def fib():
        a = 1
        b = 2
        while True:
            c = a + b
            yield c ** 3
            a = b
            b = c
    f = fib()
    fib_cubed = [1, 1, 8]
    fib_cubed.extend(list(filter(lambda x: x < 4_000_000,
                                 [next(f) for i in range(10)])))
    return sum(convolve(fib_cubed, [1, 1, -1], mode="same")[:-1])


if __name__ == "__main__":
    print(solve())
