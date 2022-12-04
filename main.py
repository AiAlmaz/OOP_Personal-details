import time
class Person():
    def __init__(self, name, gender, birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.age = 0

    def update_age(self, this_year):
        print("the age of", self.name, "is", this_year - self.birth_year)

    def info(self):
        print(self.name, self.gender, self.birth_year)


alex = Person("Alex", "male", 1996)
alex.info()

count = 2022
while True:
    print(count)
    time.sleep(5)
    count += 1
    alex.update_age(count)
