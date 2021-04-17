# Django

All about Flask Framework

## Install Django

In order to install django we are going to use ```pip```

```shell
pip install django
```

With the above command we should have django installed and ready to use.

## Create our first project

```shell
django-admin startproject ademyflask
```

## Startup Django app

```shell
python manage.py runserver 0.0.0.0:8000
```

Django has some basic conceptos that we must know:

Django uses the MVC Pattern

- Model: Models
- Views: Template
- Controller: Views

### Create an app

This creates a subapp, this subapp is going to be a sub part of the entire application

python manage.py startapp courses

### Django ORM

Django already has its own ORM

Create Model

class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

Migrate Model -> This load the new model to the django db

python manage.py makemigrations courses

Apply new mogrations ->  

python manage.py migrate courses


### Create Record

>>> from courses.models import Course
>>> python_course = Course()
>>> python_course.title = "Python complete course"
>>> python_course.description = "This is the description for the new course"
>>> python_course.save()


>>> Course.objects.create(title="Another Course", description="The description of another course")

### Find Record

>>> Course.objects.all()
> 
> 


### Using Django Admin Console

#### Create super user

python manage.py createsuperuser


After that go to

localhost:port:/admin

Enter the created superuser

### Add the model to the console

In the subdirectory of our sub -app we are going to identy the folder admin, right there we are goin to copy 
the next code

admin.site.register(Course)