## Build project

````windows cmd
django-admin startproject gw
````

*manage.py : python->python3*



## Build app

```windows cmd
pyhton manage.py startapp app_
```

*setting.py:* 

```python
INSTALLED_APPS = [
  #...
  'app_'
]
```



## Build data base

```windows cmd
pyhton manage.py makemigrations
python manage.py migrate
```

*models.py*

```python
class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    password = models.CharField(null=True, blank=True, max_length=100)
```

```windows cmd
pyhton manage.py makemigrations
python manage.py migrate
```

*view.py*

```python
from django.shortcuts import render,HttpResponse
from app_.models import People

# Create your views here.

def data_base_test(request):
    someone = People(name='bro',password='666666')
    return HttpResponse('hello '+someone.name)
```

*urls.py*

```python

urlpatterns = [
    #...
   url(r'^test/', data_base_test),
]
```



```windows cmd
python manage.py runsever
```

