def solve():
    gauss_sum = lambda n : lambda m: m * ((n - 1) // m) * ((n - 1) // m + 1) // 2
    gs = gauss_sum(1000)
    return gs(3) + gs(5) - gs(15)


if __name__ == "__main__":
    print(solve())