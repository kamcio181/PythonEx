from model.actor import Actor
from base import Session
from model.contact_details import ContactDetails
from model.movie import Movie
from datetime import date


session = Session()

movies = session.query(Movie).all()

print('\n### All movies:')
[print('%s was released on %s'%(movie.title, movie.release_date)) for movie in movies]
# for movie in movies:
#     print('%s was released on %s'%(movie.title, movie.release_date))
    # print(f'{movie.title} was released on {movie.release_date}')
print('')

movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)).all()

print('\n### Recent movies:')
for movie in movies:
    print('%s was released after 2015'%movie.title)
    # print(f'{movie.title} was released after 2015')
print('')

the_rock_movies = session.query(Movie).join(Actor, Movie.actors).filter(Actor.name == 'Dwayne Johnson').all()

print('\n### Dwayne Johnson movies:')
for movie in the_rock_movies:
    print('Dwayne Johnson was playing in %s'%movie.title)
    # print(f'Dwayne Johnson was playing in {movie.title}')
print('')

glendale_stars = session.query(Actor).join(ContactDetails).filter(ContactDetails.address.ilike('%glendale%')).all()

print('\n### Glendale actors')
for actor in glendale_stars:
    print('%s has a house in Glendale'%actor.name)
    # print(f'{actor.name} has a house in Glendale')
print('')
