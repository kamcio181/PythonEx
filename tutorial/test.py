import memory_profiler as mem_profile
import random
import time

names = ['Ania', 'Basia', 'Kamil', 'Alicja']
majors = ['Matematyka', "inzynieria", 'programowanie', 'sztuka']


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


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield(person)

# print('mem before: {}MB'.format(mem_profile.memory_usage()))
# t1 = time.clock()
# people = people_generator(1000000)
# t2 = time.clock()
#
# print('mem after : {}MB'.format(mem_profile.memory_usage()))
# print('Took {} seconds'.format(t2-t1))
#
# t1 = time.clock()
#
# for i in people:
#     i['id'] = i['id'] * 2
#
# t2 = time.clock()
# print('mem after iter : {}MB'.format(mem_profile.memory_usage()))
# print('iter Took {} seconds'.format(t2-t1))


def is_workday(day):
    return day.weekday() != 5 and day.weekday() != 6


def test(arg1, arg2, arg3):
    print('arg1: {} arg2: {}, arg3: {}'.format(arg1, arg2, arg3))


test('a', 'b', 'c')

d = {'arg2': 'd', 'arg3': 'f'}
test(**d)
