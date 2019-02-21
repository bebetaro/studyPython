# studyPython

For study Python with web programming

# 1. Install Python3 or Anaconda

[Python](https://www.python.org/downloads/)  
[Anaconda](https://www.anaconda.com/distribution/)

# 2.Setting for Python

# 3. Install Flask

## What is Flask?

http://flask.pocoo.org/

## How to install it?

`pip install -U flask`

## Sample Code

```Python
  #For now don't need to understand all of this
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def hello():
    return 'Hello, World!'
```

# 4. Materials

CS50's Web Programming with Python and JavaScript  
https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript

Don't need to complete all of chapters  
Let's focus on **Chapter3** and **Chapter4**

## Chapter3 Flask

### Basic

#### Print

`print("Hello world")`

```
name = input()
print(f"Hello, {name}!")
```

#### Sequences

Type: Integer, String, Boolean, Float,None...

List, dictionary, Tapple...

#### Function

function.py

```Python
  def square(x): #declare before use
    return x * x

  for i in range(10):
    print("{} squared is {}".format(i, square(i)))
```

If import above, and run in another file,
module.py

```Python
  from function import square
  square(10)
```

it's gonnabe not 100, but run all of the command in function.py

To avoid it, change file to below

```Python
  def square(x):
    return x * x

  def main():
    for i in range(10):
    print("{} squared is {}".format(i, square(i)))

  if __name__ == "__main__":
    main()
```

now you get 100 from module.py

#### Class

```Python
  class Point:
    def __init__(self, x, y):
      self.x = x
      self.y = y
  p = Point(3, 5)
  print(p.x)
  print(p.y)
```

### Flask

Flask is micro web framework for Python

application.py

```Python
  #Now you can understand some world of Flask

  from flask import Flask #import flask module

  app = Flask(__name__) #create application object with name of this file

  @app.route('/') #@ is just for symbol and this means routing
  def hello():
    return 'Hello, World!'
```

`export FLASK_APP = application.py`  
`flask run`

Of course we can add new route to flask

```Python

  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def hello():
    return 'Hello, World!'

  @app.route("/chimpo")
  def chimpo():
    return "<h1>Hello, Chimpo!!!!!</h1>"
```

If you want more powerful app, you can do like following

```Python

  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def index():
    return 'Hello, World!'

  @app.route("/<string:name>")
  def hello(name):
    #name = name.capitalize()
    return f"Hello, {name}!"
```
