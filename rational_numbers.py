class rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return str('(' + str(self.p) + '/' + str(self.q) + ')')
