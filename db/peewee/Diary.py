import sys
from collections import OrderedDict
import datetime

from peewee import  *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db



def add_entry():
    print("Please add your Entry information")
    data = input().strip()
    if data:
        if input('Save Entry [Yn]').lower() != 'n':
            Entry.create(content=data)
            print('Entry saved succesfully')

def view_entries():
    entries = Entry.select().order_by(Entry.timestamp.desc())
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print(' ***********')
        print(entry.content)

def delete_entry():
    pass

menu = OrderedDict([
    ('a', add_entry),
    ('b', view_entries),
])

def show_menu_options():
    choice = None
    while choice != 'q':
        print("Press q to exit")
        for key, value in menu.items():
            print('{} | {}'.format(key, value.__name__))
        choice = input('Please select one option: ').lower().strip()

        if choice in menu:
            menu[choice]()

def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)

if __name__ == "__main__":
    initialize()
    show_menu_options()