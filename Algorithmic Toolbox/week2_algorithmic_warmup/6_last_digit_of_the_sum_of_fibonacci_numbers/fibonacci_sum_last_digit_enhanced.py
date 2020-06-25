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
def fibonacciModuloby10(n):
    # mod by 60 ( psanio period of 10)
    n_new = n % 60
    summation = calc_fib(n_new + 2)
    return (summation - 1) % 10


n = int(input())
print(fibonacciModuloby10(n))
