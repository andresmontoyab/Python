from peewee import *

db = SqliteDatabase('students.db')

#In order to map object to models we must create a class that extends from peewee Model
class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        #This meta class help peewee to undersntand to which db belongs this Model
        database = db

students = [
    {
        'username': 'Andres',
        'points': 7
    },
    {
        'username': 'Juan',
        'points': 9
    },
    {
        'username': 'Gelen',
        'points': 10
    },
    {
        'username': 'Mari',
        'points': 10
    }
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            print("Student with username {} was already created".format(student['username']))


def top_student():
    top_student = Student.select().order_by(Student.points.desc()).get()
    return top_student


if __name__ == '__main__':
    db.connection()
    db.create_tables([Student], safe=True)
    add_students()
    #top_student()
    print(top_student().username)