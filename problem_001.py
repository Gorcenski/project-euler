from math import floor

def solve():
    gauss_sum_m = lambda n: lambda m: m * (floor((n -1) / m) + 1) * (floor((n - 1) / m)) / 2
    gs = gauss_sum_m(1000)
    print(int(gs(3) + gs(5) - gs(15)))


if __name__ == "__main__":
    solve()