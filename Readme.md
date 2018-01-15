## Build project

````windows cmd
django-admin startproject gw
````

*manage.py : python->python3*



## Build app

```windows cmd
pyhton3 manage.py startapp gwapp
```

*setting.py:* 

```windows cmd
INSTALLED_APPS = [
  #...
  'gwapp'
]
```



## Build data base

```windows cmd
pyhton3 manage.py makemigrations
python3 manage.py migrate
```



```windows cmd
python3 manage.py runsever
```

