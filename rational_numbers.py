# Dan Ryan
# Quiz 11: The rational Class
# Complete w/Extra Credit
# Play around with rational numbers, do math with 'em for fun & profit


# Define Class
class rational:
    # Constructor that takes two int values as arguments
    def __init__(self, p, q=1):
        # Appropriate handling of negative Q values
        if p < 0 and q < 0:
            self.p = p * -1
            self.q = q * -1
        # Exception when Q is zero (extra-credit)
        elif q == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
            # raise ZeroDivisionError("Can't divide {} by zero".format(p))
        # Handle normal Q values
        else:
            self.p = p
            self.q = q

    def __str__(self):
        return str('(' + str(self.p) + '/' + str(self.q) + ')')

    # Support addition
    def plus(self, b):
        return str(str((self.p * b.q) + (self.q * b.p)) + '/' + str(self.q * b.q))

    # Support multiplication
    def star(self, b):
        return str(str(self.p * b.p) + '/' + str(self.q * b.q))

    # Support converting a rational to a float value
    def toFloat(self):
        return self.p / self.q
