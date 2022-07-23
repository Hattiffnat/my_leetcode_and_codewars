class Jar:
    def __init__(self):
        self.juice = {}

    def add(self, amount, kind):
        if kind in self.juice.keys():
            self.juice[kind] += amount
        else:
            self.juice.update({kind: amount})

    def pour_out(self, amount):
        total = self.get_total_amount()
        if total < amount:
            self.juice = {}
        else:
            for kind in self.juice.keys():
                self.juice[kind] -= amount * (self.juice[kind] / total)

    def get_total_amount(self):
        return sum(self.juice.values())

    def get_concentration(self, kind):
        if kind in self.juice.keys():
            return self.juice[kind] / self.get_total_amount()
        else:
            return 0
