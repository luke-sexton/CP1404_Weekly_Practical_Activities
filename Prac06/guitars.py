class Guitars:
    def __init__(self, name="", year=0, cost=0, current=2018):
        self.name = name
        self.year = year
        self.cost = cost
        self.current = current
        self.age = current - year

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return "The {} is {} - {} = {}".format(self.name, self.current, self.year, self.age)

    def is_vintage(self):
        if self.age >= 50:
            return True

