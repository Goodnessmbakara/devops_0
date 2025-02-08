import requests
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    if n < 1:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n


def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)


def get_digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))


def get_number_properties(n):
    properties = []

    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return properties


def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
        return f"{n} is an interesting number!"
    except:
        return f"{n} is an interesting number!"

