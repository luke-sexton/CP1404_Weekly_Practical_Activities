from Prac06.guitars import Guitars

guitar_one = Guitars("Gibson L-5 CES", 1922, 16035.40)
guitar_two = Guitars("Maton S60", 2012, 999)

guitars = [guitar_one, guitar_two]
print("{} get_age() - Expected 96. got {}".format(guitar_one.name, guitar_one.age))
print("{} get_age() - Expected 96. got {}".format(guitar_two.name, guitar_two.age))
for guitar in guitars:
    if guitar.is_vintage() is True:
        print("{} is_vintage() - Expected True. got True".format(guitar.name))
    else:
        print("{} is_vintage() - Expected False. got False".format(guitar.name))
