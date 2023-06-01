![Squawk logo](./app/static/img/squawk_long.png "Squawk")

**SQUAWK** is a new social network toy developed by Tec de Monterrey students designed to be lightweight and helpful as a template when practicing webdev with Flask.

###
**Running application locally:**
From the squawk folder, open a command prompt and execute the following command:  
``python app.py``  
then connect to localhost:5000

**Running application on container**
From the squawk folder, open a command prompt and execute the following commands:  
``docker build -t squawk .``  
``docker run -dp 5000:5000 squawk``  
then connect to localhost:5000

**Running tests**
From the squawk folder, execute the following commands:  
``python comment_tests.py``  
``python login_tests.py``  
``python squawk_tests.py``  

### Types of users

**User:**
- Could be any final user
- Is identified with a username
- Is authenticated with a simple password
- May publish short pieces of text (up to 300 characters) for all users to see. These texts could be in response to another.

**Admins:** 
- Can do everything the user can
- Can view event dashboard, where the following metrics are shown:
    - Most popular squawk of the day
    - Most active user of the day
    - Amount of different users that have logged-in that day

# Architecture

MVC Layers. This organization is described by the next fragment of our project structure.

```
SQUAWK APP
└───app.py                  <-- Entry point and web controller
│
├───bl                      <-- Business Layer
│   └───event.py            <-- Unit class used throught
│   └───squawk.py           <-- Unit class used throught
│   └───user.py             <-- Unit class used throught
│   │
│   └───event_builder.py    <-- Used for Builder Pattern
│   └───user_auth.py        <-- Used for Strategy Pattern
│   │
│   └───event_service.py    <-- Service uses DAO
│   └───squawk_service.py   <-- Service uses DAO
│   └───thread_service.py   <-- Service uses DAO
│   └───user_service.py     <-- Service uses DAO
│
├───dl                      <-- Data Layer
│   └───event_dao.py        <-- DAO access database
│   └───squawk_dao.py       <-- DAO access database
│   └───user_dao.py         <-- DAO access database
│
├───static
│   └───img             <-- images
│   └───css             <-- graphic design
│
├───templates           <-- html views 
│
└───ui
│   └───admin_controller.py     <-- Web controller and routes
│   └───squawk_controller.py    <-- Web controller and routes
│   └───user_controller.py      <-- Web controller and routes
│
└───utils
    └───database.py         <-- Database manager
    └───db.sqlite           <-- Database storage
    └───schema.sql          <-- Database schema
```


# Design patterns used

## DAO

Data Access Object (DAO) Pattern is used to separate low level data accessing operations from high level business services and fits our architecture since MVC organizes the operations in business and data layers.

## Singleton

Since we are using DAO for each of our services, it comes in handy to use singleton pattern when making a connection to the database so that when a connection already exists from some service, this is reused instead of creating a new one for another service. 

The next snippet demonstrates how the pattern is used in the `Database` class.

```
def __new__(self):
if self.__instance is None:
    self.__instance = super().__new__(self)
return self.__instance

def __init__(self):
if getattr(self, 'connection', None) is None:
    self.DB = "app/utils/db.sqlite"
    self.connect()
```

## Strategy

We use Strategy since the DBAuthStrategy class is a concrete implementation of the authentication strategy. It provides a specific implementation of the authenticate() method by interacting with a UserService object to perform the authentication process. This class represents one possible strategy for authenticating users.

## Builder

We use Builder when creating reports for the dashboard

```
class EventBuilder:
  def __init__(self):
    self.type_of_action = None
    self.user_id = None

  def with_type_of_action(self, type_of_action):
    self.type_of_action = type_of_action
    return self
  
  def with_user_id(self, user_id):
    self.user_id = user_id
    return self
  
  def build(self):
    return Event(type_of_action=self.type_of_action, user_id=self.user_id)
```

# SOLID Principles

*Single Responsibility Principle (SRP):*  
The ``EventService`` class is responsible for creating, deleting, and retrieving events. It also includes methods for generating reports. Although it handles multiple operations, it can still be considered to have a single responsibility related to managing events and generating reports.  

*Open-Closed Principle (OCP):*  
``EventService`` class: The ``EventService`` class is open for extension because new methods can be added to it without modifying its existing code. However, it is not explicitly closed for modification since the methods get_event and update_event are placeholders and may require modification in the future. Therefore, it partially complies with OCP.  

*Liskov Substitution Principle (LSP):*  
The ``DBAuthStrategy`` class is a subtype of the ``UserAuthStrategy`` abstract base class and inherits the authenticate method. It maintains the same method signature and behaves as expected. Therefore, it adheres to the LSP.  

*Interface Segregation Principle (ISP):*  
The ``UserAuthStrategy`` abstract base class defines a specific interface with a single method, authenticate. It provides a minimal and focused interface for implementing different authentication strategies. This follows the ISP by not imposing unnecessary methods on its subclasses.  

*Dependency Inversion Principle (DIP):*  
The ``EventService`` class depends on the ``EventDAO`` class, which is a low-level module responsible for data access. This adherence to DIP allows for easy substitution of different ``EventDAO`` implementations without modifying the ``EventService`` class. Therefore, it complies with DIP. 

