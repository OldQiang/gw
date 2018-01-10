## Build project

````
django-admin startproject gw
````

*manage.py : python->python3*



```
pyhton3 manage.py startapp gwapp
```

*setting.py:* 

```python
INSTALLED_APPS = [
  #...
  'gwapp'
]

```



```terminal
pyhton3 manage.py makemigrations
python3 manage.py migrate
```



```
python3 manage.py runsever
```

