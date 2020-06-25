def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


def calc_fib(n):
    if n <= 1:
        return n

    numbers = [None] * (n + 1)
    numbers[0] = 0
    numbers[1] = 1
    for i in range(2, n + 1):
        numbers[i] = numbers[i - 1] + numbers[i - 2]
    return numbers[n]


# Calculate Fn mod m
def fibonacciModulo(n, m):
    n_new = n % pisanoPeriod(m)
    return calc_fib(n_new) % m


n, m = map(int, input().split())
print(fibonacciModulo(n, m))
