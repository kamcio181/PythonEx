import mem_profile
import random
import time

names = ['Ania', 'Basia', 'Kamil', 'Alicja']
majors = ['Matematyka', "inzynieria", 'programowanie', 'sztuka']

print('mem before: {}MB'.format(1))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result