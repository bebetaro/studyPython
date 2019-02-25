# studyPython

For study Python with web programming
For study yourself  
http://diveintopython3-ja.rdy.jp/table-of-contents.html#your-first-python-program

# 0. Install Git

[Git](https://git-scm.com/)

Setting email and username  
`git config --global user.email "emailaddress"`  
`git config --global user.name "username"`

If you need lock your file  
`git lfs track "targetfolder/targetarea.extension" --lockable`

## COMMIT -> FETCH -> PULL -> PUSH

# 1. Install Python3 or Anaconda

[Python](https://www.python.org/downloads/)  
[Anaconda](https://www.anaconda.com/distribution/)

# 2.Setting for Python

Check Environmetal Variable(環境変数)
Where being abele to "python" and "pip"

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

```Python
name = input()
# If put something, inside of input()
# Inside gonnabe appear name = input("Write something")
print(f"Hello, {name}!")
```

#### Sequences

Type: Integer, String, Boolean, Float,None...

List, dictionary, Tapple...

##### How to change type?

`str = input()`  
The value you get from input() is str type,  
but if you want number, you should try cast!  
`number = int(str)`  
Now you can get number from input().

#### If statement:

If statement judge by True of False

```Python
  number = input("1 + 1 は？")
  if number is 2: #if you don't cast, str is compared to int
    #Of course it's fault
    print("Correct!")
    print(number is 2)
  else:
    print("YOU ARE STUPID")
    print(number is 2)
```

#### for loop

```Python
  for i in range(10): #Basic syntax is this
    i++ # drive loop and make your logic
```

#### Function

`function.py`

```Python
  def square(x): #declare before use
    return x * x

  for i in range(10):
    print("{} squared is {}".format(i, square(i)))
```

#### Scope

```Python
  def sumBetweenNum(numA, numB):
    number = 0
    # number's scope is inside of function
    for i in range(numA, numB):
        number += i
    # scope of i is only inside for loop
    number += numB
    return number

  number1 = 1
  number2 = 4
  #these scope is everywhere in file

  print(sumBetweenNum(number1, number2))

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

#### Jinja2

application.py

```Python

  from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')
  def index():
    return render_template("index.html")
    #Need to make "template" folder and put html file there

```

`template/index.html`

```HTML
  <!DOCTYPE html>
  <html>
    <head>
      <title>My Page</title>
    </head>
    <body>
      <h1>Hello World!</h1>
    </body>
  </html>
```

Then we can use variable with Jinja2 on HTML

application.py

```Python

  from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')
  def index():
    headline = "Hello World!" #Add
    return render_template("index.html", headline = headline) #Changed

```

`template/index.html`

```HTML
  <!DOCTYPE html>
  <html>
    <head>
      <title>My Page</title>
    </head>
    <body>
      <h1>{{headline}}</h1>
    </body>
  </html>
```

So we can do this kind of thing

application.py

```Python
  import datetime
  from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')
  def index():
    now = datetime.datetime.now() #Changed
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year = new_year) #Changed

```

`template/index.html`

```HTML
  <!DOCTYPE html>
  <html>
    <head>
      <title>Is it New Year??</title>
      <style>body{text-align: center;}</style>
    </head>
    <body>
      {% if new_year %} <!--Jinja2 way to write if statement-->
        <h1>Happy New Year</h1>
      {% else %}
        <h1>NO</h1>
      {% endif %}
    </body>
  </html>
```

#### Other Route

application.py

```Python
  from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')
  def index():
    return render_template("index.html")

  @app.route("/more") #This route is added
  def more():
    return render_template("more.html")

```

`template/index.html`

```HTML
  <!DOCTYPE html>
  <html>
    <head>
      <title>My Page</title>
    </head>
    <body>
      <h1>First Page</h1>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>

      <a href="{{url_for('more')}}">See more...</a>
      <!---This is link for more function in Python, not more html-->
    </body>
  </html>
```

`template/more.html`

```HTML
  <!DOCTYPE html>
  <html>
    <head>
      <title>My Page</title>
    </head>
    <body>
      <h1>Second Page</h1>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>

      <a href="{{url_for('index')}}">Go Back</a>
      <!---This is link for index function in Python, not index html-->
    </body>
  </html>
```

Remove redundancy

`template/layout.html`

```HTML
  <!DOCTYPE html>
  <html>
    <head>
      <title>My Page</title>
    </head>
    <body>
      <h1>{% block heading %}{% endblock %}</h1>
      {% block body %}
      {% endblock %}
    </body>
  </html>
```

`template/index.html`

```HTML
  {% extends "layout.html" %}
  {%block heading%}First Page{% endblock %}

  {% block body%}
    <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>

     <a href="{{url_for('more')}}">See more...</a>
     <!---This is link for more function in Python, not more html-->
  {% endblock %}
```

`template/more.html`

```HTML
  {% extends "layout.html" %}
  {%block heading%}Second Page{% endblock %}

  {% block body%}
    <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>

    <a href="{{url_for('more')}}">Go back</a>
    <!---This is link for more function in Python, not more html-->
  {% endblock %}
```

#### FORM

application.py

```Python
  from flask import Flask, render_template, request

  app = Flask(__name__)

  @app.route('/')
  def index():
    return render_template("index.html")

  @app.route("/hello", methods=["POST"])
  #For now /hello only accept post request,
  #if you add GET request, you have to make a route for GET
  def hello():
    name = request.form.get("name") #access form value here
    return render_template("hello.html", name = name)
```

`template/index.html`

```HTML
  {% extends "layout.html" %}
  {%block heading%}First Page{% endblock %}

  {% block body%}
    <form action="{{url_for('hello')}}" method="post">
    <!--Open hello function and render hello.html from hello function-->
      <input type = "text" name = "name" placeholder = "Enter your name" >
      <button>Submit</button>
    </form>
  {% endblock %}
```

`template/hello.html`

```HTML
  {% extends "layout.html" %}
  {%block heading%}Hello!{% endblock %}

  {% block body%}
    Hello, {{ name }}!
  {% endblock %}
```

#### Session

```Python
  from flask import Flask, render_template, request, session
  #give access to a variable called "session"
  #which can be used to keep values that are specific to a paticular user:client side
  from flask_session import Session
  #additional extension to sessions which allows them to be stored server-side

  app = Flask(__name__)
  app.config["SESSION_PERMANENT"] = False
  app.config["SESSION_TYPE"] = "filesystem"
  Session(app)

  @app.route("/", methods = ["GET", "POST"])
  def index:
    if session.get("notes") is None:
      session["notes"] =[] #if user doesn't have notes, create notes list
    if request.method == "POST":
      note = request.form.get("note") #get from form in HTML
      session["notes"].append(note)
      #note is created in HTML and appended with notes list in Python
      #"notes" is stored in session which each user has uniquely
    return render_template("index.html", notes = session["notes"])

```
