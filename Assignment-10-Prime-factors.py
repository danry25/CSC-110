# Dan Ryan
# Assignment 10: Prime Factors
# Challenge
# Find the primes for a number between 1 and 1000


def primeFinder(number):
    relevantPrimes = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    if number <= -1:
        relevantPrimes.append(-1)
        number = number // -1
    # Test all the primes in the primes tuple against the number
    for prime in primes:
        # Divide a number by its prime as much as possible
        while number % prime == 0:
            # Update number to new, significantly lower number
            number = number // prime
            # Add prime to relevantPrimes if its not there already
            relevantPrimes.append(prime)
    # Check if number that has been fully divided is a prime
    if number != 1:
        relevantPrimes.append(number)
    return relevantPrimes


def main():
    number = 1
    while number is not 0:
        try:
            formattedPrimes = ''
            number = int(input('Enter an integer between -1000 and 1000: '))
            if number > 1000 or number < -1000:
                print('Warning: Factorization may not be complete!')
            elif number == 0:
                break
            relevantPrimes = primeFinder(number)
            for prime in relevantPrimes:
                formattedPrimes += "{}, ".format(prime)
            print('  The factors of {}: {}'.format(number, formattedPrimes).strip(', ') + '\n')
        except:
            print("Aww, that wasn't a valid number :c")


main()
