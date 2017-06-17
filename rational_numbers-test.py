import rational_numbers


def main():

    a = rational_numbers.rational(3, 4)
    b = rational_numbers.rational(1, 2)

    print(a, '+', b, '=', a.plus(b))
    print(a, '*', b, '=', a.star(b))

    print(a, '=', a.toFloat())
    print(b, '=', b.toFloat())


main()
