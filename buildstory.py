import random


def create_story(books):
    pass

books_title = ['Mother', ' Midnight Children', ' My experiments with truth']

where_places = [' greeen land', ' Neuschwanstein-Castle', ' Schwangau',' Cappadocia', ' Tunnel of Love']
when = [' A few years ago', 'Yesterday', ' Last night', ' A long time ago','on may 28th', ' just few moments before',
        ' one day', ' One full-moon night']
characters = [' there lived a king.',' there was a man named Jack.','I', ' one of my friend', ' there lived a farmer.']
work = ['looking at', 'working', 'waiting at', 'playing near to', ' wo is visiting', ]

print("Book title: ", random.choice(books_title))
print(random.choice(when) +' '+ random.choice(characters)+' '+ random.choice(work)+' '+random.choice(where_places))
