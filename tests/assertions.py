def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    assert factorial(5) == 120
    print(f"5! = {factorial(5)}")
