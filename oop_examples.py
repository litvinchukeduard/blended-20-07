'''
class Cat:

    color: string
    name: string
    gender: string

'''

class Cat:

    def __init__(self, name: str, color: str, gender: str) -> None:
        self.name = name
        self.color = color
        self.gender = gender

    def print_name(self):
        print(self.name)

cat_vasya = Cat('Vasya', 'grey', 'male')
cat_vasya.print_name()

# print(dir('Hello'))
print(dir(cat_vasya))

print(cat_vasya.gender)

# Cat.print_name(cat_vasya) # do not use this method!!!
