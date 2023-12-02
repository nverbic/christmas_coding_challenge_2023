'''Extract prime factors of the inputed number'''

def get_prime_factors(number):
    '''Return a list of the number's prime factors'''
    prime_factors = []

    if number != 1:
        i = 2
        # First divide with 2
        while number > 1 :
            if  number % i == 0:
                number = number / i
                prime_factors.append(i)
            else:
                break
        # Set i to 3 and increment by 2 to test only odd numbers. All composite odd numbers
        # are tested but only prime factors are removed from the number. This is because the composite
        # numbers are composed from prime factors (2,3,5,7,11,13,17,19 etc) which are removed from
        # the number before trying the composite number.
        i = 3
        while number > 1 and i <= number:
            if  number % i == 0:
                number = number / i
                prime_factors.append(i)
            else:
                i = i + 2
    return prime_factors


if __name__ == '__main__':
    input_number = int(input("Please enter an integer number: "))
    prime_factors = get_prime_factors(input_number)
    print(f"Prime factors of the number {input_number} are: {prime_factors}")
