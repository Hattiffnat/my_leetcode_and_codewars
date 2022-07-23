class Vector(list):
    def verify(self, other):
        if len(self) != len(other):
            raise LookupError(f'Lengths are not equal')

    def add(self, other):
        self.verify(other)

        return Vector([self[i] + other[i] for i in range(len(self))])

    def subtract(self, other):
        self.verify(other)

        return Vector([self[i] - other[i] for i in range(len(self))])

    def dot(self, other):
        self.verify(other)

        return sum([self[i] * other[i] for i in range(len(self))])

    def norm(self):
        return sum(map(lambda x: x**2, self)) ** 0.5

    def equals(self, other):
        val = min(len(self), len(other))

        for i in range(val):
            if self[i] != other[i]:
                return False

        return True

    def __str__(self):
        return str(tuple(self)).replace(' ', '')


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

print(a.add(b))         # should return a new Vector([4, 6, 8])
print(a.subtract(b))    # should return a new Vector([-2, -2, -2])
print(a.dot(b))         # should return 1*3 + 2*4 + 3*5 = 26
print(a.norm())         # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
print(a.add(c))         # raises an exception


