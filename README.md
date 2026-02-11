# AirBnB Clone - Console

## Project Description
This project is the first step toward building a full clone of the AirBnB web application, focusing on the backend logic and data management.
2It implements a command-line interpreter that allows interaction with the application through different commands.
It allows users to create, update, retrieve, and delete objects representing different entities of the AirBnB system.
It stores data using JSON serialization to save objects into a file and reload them when the program starts again.

## About

This project is part of the **ALX Software Engineering curriculum**.  
It was implemented as part of the tasks designed to teach and practice:

- Object-Oriented Programming (OOP) in Python  
- Building command-line interpreters using the `cmd` module  
- JSON serialization and file storage  
- Managing backend logic for web applications  

Completing this project helps develop a solid foundation for building more complex systems, including web-based applications.


## Features
- Create new instances of classes
- Display an instance by ID
- Update instance attributes
- Delete instances
- Display all instances
- Persist data using JSON storage
- Support interactive and non-interactive modes

## Supported Classes

All classes inherit from `BaseModel`.

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## How to Run

### Interactive Mode

To start the console in interactive mode, run:

```bash
./console.py

```

### 🔵 Non-Interactive Mode


You can also run commands in non-interactive mode using a pipe:
```bash
echo "all BaseModel" | ./console.py
```

---

⚠️ Important:
Make sure your `console.py` has executable permission:

```bash
chmod +x console.py
```
## Available Commands
### create

Creates a new instance of a class.

⚠️ Important: Don't forget to replce the \<id\> with the one shows after creating an instance

Example:
```bash
(hbnb) create BaseModel
(hbnb) show BaseModel 1 <id>
(hbnb) destroy BaseModel <id>
(hbnb) all
(hbnb) all BaseModel
(hbnb) update BaseModel <id> name "My Model"
(hbnb) quit
```
## Project Structure
```
AirBnB_clone/
│
├── console.py             # The command-line interpreter
├── models/                # All classes and storage engine
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       └── file_storage.py  # Handles saving and loading JSON objects
│
└── tests/                 # Unit tests for all classes and console
```

## Storage System
```
Object → Dictionary → JSON → File
File → JSON → Dictionary → Object
```

## Author
**Alaa Badawii**  
First milestone toward building a full-stack AirBnB clone.  

## Future Improvements
The following features are planned for upcoming updates:

- Retrieve all instances of a class: `<ClassName>.all()`
- Count the number of instances of a class: `<ClassName>.count()`
- Retrieve an instance by ID: `<ClassName>.show(<id>)`
- Destroy an instance by ID: `<ClassName>.destroy(<id>)`
- Update an instance by ID and attribute: `<ClassName>.update(<id>, <attribute name>, <attribute value>)`
- Update an instance by ID using a dictionary representation: `<ClassName>.update(<id>, <dictionary>)`
- Replace JSON file storage with a MySQL database for persistent and scalable storage

