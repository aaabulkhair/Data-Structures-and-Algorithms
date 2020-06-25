def calculate_gcd(a, b):
    if b == 0:
        return a
    else:
        return calculate_gcd(b, a % b)


def calculate_lcm(a, b):
    return (a * b) // calculate_gcd(a, b)


a, b = map(int, input().split())
print(calculate_lcm(a, b))
