def is_prime(number):
    """ Return True if *number* is prime. """
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def find_next_prime(number):
    """ Find the closest prime number larger than *number*. """
    index = number

    while True:
        index += 1

        if is_prime(index):
            return index
