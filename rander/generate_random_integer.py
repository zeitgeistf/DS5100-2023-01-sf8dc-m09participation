import random


def generate_random_integer(a=0, b=100000000000000):
    """
    This function generates random integer
    """
    r = random.randint(a, b)
    print(r)
    return r



if __name__ == "__main__":
    generate_random_integer()
