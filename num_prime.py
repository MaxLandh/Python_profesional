import math
def is_prime(number: int) -> bool:
    if (math.factorial(number - 1) + 1) % number == 0:
        return True
    else:
        return False
        
def run():
    print(is_prime(7))

if __name__ == "__main__":
    run()