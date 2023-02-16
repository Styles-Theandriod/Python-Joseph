class Person():
    def __init__(self, firstname, lastname, age, nationality, sex, race):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
        self.sex = sex
        self.race = race

    def forgingAhead(self):
        print(self.firstname, "always says we should forge ahead, so we would forge ahead.")

    def running(self):
        print(self.firstname, "runs very fast")

gabby = Person("Gabriel", "De Suza", 32, "Nigeria", "Male", "African")
vicky = Person("Victory", "De Suza", 23, "USA", "Male", "African")
print(gabby.firstname, "is", gabby.age, "and he is from", gabby.nationality)
print(vicky.firstname, "is", vicky.age, "and he is from", vicky.nationality)

gabby.forgingAhead()
vicky.forgingAhead()

gabby.running()
vicky.running()

# INHERITANCE
class Athlete(Person):
    def __init__(self, firstname, lastname, age, nationality, sex, race, club, shirtNumber, position, salary):
        super().__init__(firstname, lastname, age, nationality, sex, race)

        self.club = club
        self.shirtNumber = shirtNumber
        self.position = position
        self.salary = salary

    def behaviour(self):
        print(self.firstname, "is proud.")

ronaldo = Athlete("Cristiano", "Ronaldo", 37, "Portugal", "Male", "Caucasian", "Man United", 7, "forward", "$350,000" )
print(ronaldo.firstname)

ronaldo.running()
ronaldo.behaviour()