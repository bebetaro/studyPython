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

# SQL

Appendix for Beginner: [DB/SQL 入門編(paiza)](https://paiza.jp/works/sql/primer)  
Appendix for Advanced: [Introduction to Databases/Stanford University](https://lagunita.stanford.edu/courses/DB/2014/SelfPaced/about)

SQL is a language designed to interact with the relational databases.

## Data Types

SQL has following data types

**These are regular types**  
・_INTEGER_  
・_DECIMAL_  
・_SERIAL_:an automatically incrementing integer  
・_VARCHAR_: variable length of characters, i.e. string  
・_TIMESTAMP_  
・_BOOLEAN_  
・_ENUM_: one of a discrete number of possible values

**These are additonal types**  
・_NOT NULL_ : field must have a value; if field does not have a value, entry will be rejected  
・U*NIQUE* : no two fields in this column can have the same value  
・_PRIMARY KEY_ : the main way to index a table  
・_DEFAULT_ : set a default value for a column if no other value is given  
・_CHECK_ : bound values; e.g. values greater than 50

## Connect with Database

use command `psql <database>` if it is online `psql <databaseURL>`

## CREATE Database

Declare `CREATE TABLE` first

```SQL
CREATE TABLE flights (
      id SERIAL PRIMARY KEY,
      origin VARCHAR NOT NULL,
      destination VARCHAR NOT NULL,
      duration INTEGER NOT NULL
  );
```

`flights` is **table name**  
`id, origin, destination, duration` are **user defined columns**  
`SERIAL, VARCHAR, INTEGER` are **Data Types**  
`PRIMARY KEY, NOT NULL` are **additonal types**

## INSERT Database

```SQL
INSERT INTO flights
      (origin, destination, duration)
      VALUES ('New York', 'London', 415);
```

```SQL
INSERT INTO "table name"
  (ColumnA, ColumnB, ColumnC...)
  VALUES(VARCHAR, VARCHAR, INTEGER)
```

We don't need insert `id` because `id` is `SERIAL`, which means automatically increment

## SELECT FROM TABLE

```SQL
SELECT * FROM flights;
#Select everything from flights table
SELECT origin, destination FROM flights;
#Select origin and destination
SELECT * FROM flights WHERE id = 3;
#Select every data which has id = 3
SELECT * FROM flights WHERE origin = 'New York';
#Select every data of which origin is "New York"
SELECT * FROM flights WHERE duration > 500;
#Select every data of which duration is more than 500
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
#Select every data of which destination is "Paris" and duration is more than 500
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;
#Select every data of which destination is "Paris" or duration is more than 500
SELECT AVG(duration) FROM flights WHERE origin = 'New York';
#Select every data of which origin is "New York" and calcurate average of duration
SELECT * FROM flights WHERE origin LIKE '%a%';
#Select every data of which origin contains any "a" character
SELECT * FROM flights LIMIT 2;
#Show 2 of every data
SELECT * FROM flights ORDER BY duration ASC;
#Show every data in ascending of duration
SELECT * FROM flights ORDER BY duration ASC LIMIT 3;
#Show 3 of every data in ascending of duration
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
#Show origin and how many times the origin is shown by grouping origin
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
#Show origin which is shown more than once and how many times the origin is shown by grouping origin
```

### Function

**SUM**, **COUNT**, **MAX**, **MIN**, **AVG**...  
We can use function whatever we use in Excel or something else

## UPDATE AND DELETE

### UPDATE

```SQL
UPDATE flights
      SET duration = 430
      #Point is "set", following is just condition
      WHERE origin = 'New York'
      AND destination = 'London';
```

### DELETE

```SQL
DELETE FROM flights
      WHERE destination = 'Tokyo'
```

## Relational

### REFERENCES

```SQL
CREATE TABLE passengers (
      id SERIAL PRIMARY KEY,
      name VARCHAR NOT NULL,
      flight_id INTEGER REFERENCES flights
  );
```

`passengers`table uses `flight_id` from `flights`table  
It means that `passengers`table connect with `flights`table now using `REFERENCES`

### JOIN

```SQL
  SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
  SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';
  SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;
```

**JOIN** performs an _inner join_: only rows where both tables match the query will be returned. In this example, only `flights` with `passengers` will be returned.  
**ON** indicates how the two tables are related. In this example, the column `flight_id` in `passengers` reflects values in the column `id` in `flights`.  
**LEFT JOIN** includes _rows from the first table listed even if there is no match_ (e.g. there are no passengers on that flight). **RIGHT JOIN** is vice versa (e.g. passengers with no flights).

### NESTED QUERY

```SQL
 SELECT * FROM flights WHERE id IN
  (SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);
```

First inner query seach for `flight_id` from `passenger` table which has more than 1 passenger.  
**=>return id (e.g. id = 1, 2, 6)**  
Second, outer query search for every rows from `flights` table of which `id` is in inner query.  
**=> seaching in id(e.g. 1, 2, 6) and show all of data of which id is 1 or 2 or 6**

## SQLAlchemy

### install

`pip install sqlalchemy`

### TEST CODE

```Python
  import os

  from sqlalchemy import create_engine
  from sqlalchemy.orm import scoped_session, sessionmaker

  engine = create_engine(os.getenv("DATABASE_URL")) # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
  db = scoped_session(sessionmaker(bind=engine))    # create a 'scoped session' that ensures different users' interactions with the
                                                    # database are kept separate

  flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall() # execute this SQL command and return all of the results
  for flight in flights
      print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.") # for every flight, print out the flight info
```

### CSV Ver.

```Python
  import csv

  # same import and setup statements as above
  from sqlalchemy import create_engine
  from sqlalchemy.orm import scoped_session, sessionmaker

  engine = create_engine(os.getenv("DATABASE_URL")) # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
  db = scoped_session(sessionmaker(bind=engine))    # create a 'scoped session' that ensures different users' interactions with the
                                                    # database are kept separate


  f = open("flights.csv")
  reader = csv.reader(f)
  for origin, destination, duration in reader: # loop gives each column a name
      db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                  {"origin": origin, "destination": destination, "duration": duration}) # substitute values from CSV line into SQL command, as per this dict
      print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
  db.commit() # transactions are assumed, so close the transaction finished
```

## Mini App

application.py

```python
@app.route("/")
  def index():
      flights = db.execute("SELECT * FROM flights").fetchall()
      return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
  def book():
      # Get form information.
      name = request.form.get("name")
      try:
          flight_id = int(request.form.get("flight_id"))
      except ValueError:
          return render_template("error.html", message="Invalid flight number.")

      # Make sure the flight exists.
      if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
          return render_template("error.html", message="No such flight with that id.")
      db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
              {"name": name, "flight_id": flight_id})
      db.commit()
      return render_template("success.html")
```

index.html

```html
<form action="{{ url_for('book') }}" method="post">
  <div class="form-group">
    <select class="form-control" name="flight_id">
      {% for flight in flights %}
      <option value="{{ flight.id }}"
        >{{ flight.origin }} to {{ flight.destination }}</option
      >
      {% endfor %}
    </select>
  </div>

  <div class="form-group">
    <input class="form-control" name="name" placeholder="Passenger Name" />
  </div>

  <div class="form-group">
    <button class="btn btn-primary">Book Flight</button>
  </div>
</form>
```
