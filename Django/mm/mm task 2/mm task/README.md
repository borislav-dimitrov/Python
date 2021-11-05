# car-app

## Task description

1. Review the application and its source code.
2. Record yourself in English and talk about your findings.
- Make sure to share your screen.
- The length of the video should not exceed 5 minutes.
1. Do not limit yourself with only one part of the code, everything is up for review.
- Design patterns, documentation, complexity, etc.

<br />

## Project setup
Open the project folder and a command-line in it.

If you have installed Python on your machine run

```
pip install virtualenv
```

If that doesn't work try with 
```
pip3 install virtualenv
```

Now in the project folder run

```
virtualenv venv
```

And then if you're on Windows 
```
venv\Scripts\activate
```
and on MacOS or Linux 
```
source venv/bin/activate
```

Before we continue make sure you see (venv) before you current working directory line (cwd).

#
Now when you see the (venv) before your line type 
```
pip install -r requirements.txt 
```

and
```
python3 manage.py migrate
```
and finally to run the django app
```
python3 manage.py runserver
```




