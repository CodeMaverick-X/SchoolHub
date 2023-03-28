#!/usr/bin/python3
"""
test user class and file storage
"""


from models.user import User
import models
my_dict = {'username': 'yoyo17', 'password':'password'}

if (models.storage.unique(my_dict['username'])):
    me  = User(**my_dict)
    me.save()
    me.create_events()
    print(f'{me.username} has been craeted')
    my_ev = me.events
    prt = [print(event.tag) for event in my_ev]
else:
    print('user name already taken')
