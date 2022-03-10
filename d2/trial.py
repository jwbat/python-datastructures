

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def addfriend(self, other):
        pair = (self, other)
        self.friends.append(pair)

    def __repr__(self):
        return f'{self.name}'


print()

person = Person('james')
#other = Person('greg')
#person.addfriend(other)
print(person)

print()
