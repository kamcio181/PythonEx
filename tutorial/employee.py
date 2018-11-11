class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')


# emp1 = Employee('Jan', 'Kowalski')
# print(emp1.fullname)
# emp1.fullname = 'Ania Kowalska'
# print(emp1.fullname)


list_1 = ['A', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
tuple_1 = tuple(list_1)

print(list_1)
print(list_2)
print(list_3)
print(tuple_1)
print()

list_1[0] = 'x'

print(list_1)
print(list_2)
print(list_3)
print(tuple_1)