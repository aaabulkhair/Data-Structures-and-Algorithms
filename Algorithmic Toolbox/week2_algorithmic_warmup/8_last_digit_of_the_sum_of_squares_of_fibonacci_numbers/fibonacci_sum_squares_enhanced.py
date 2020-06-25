def calc_fib(n):
    if n <= 1:
        return n

    numbers = [None] * (n + 1)
    numbers[0] = 0
    numbers[1] = 1
    for i in range(2, n + 1):
        numbers[i] = numbers[i - 1] + numbers[i - 2]
    return numbers[n]


def fibonacci_sum_squares(n):
    summation = calc_fib(n % 60) * calc_fib((n + 1) % 60)
    return summation % 10


n = int(input())
print(fibonacci_sum_squares(n))