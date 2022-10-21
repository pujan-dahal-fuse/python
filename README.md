# **Python Repository**

This repository is made up of codes I used while learning Python and APIs, during my trainee period at Fusemachines Nepal. It is divided into 5 branches:
1. **main**
2. **codewars**
3. **api**
4. **orm**
5. **pandas**
## **1. main**
`main` contains codes that I used while learning basic and advanced Python. Codes are within [`python_basic_advanced`](python_basic_advanced/) folder. Basic codes are in [`python_basic_advanced/task1.py`](python_basic_advanced/task1.py) and [`python_basic_advanced/constant.py`](pyton_basic_advanced/constant.py) files. Advanced codes are in [`python_basic_advanced/advanced_topics.ipynb`](python_basic_advanced/advanced-topics.ipynb) file.


## **2. codewars**
`codewars` branch contains successful Python code submissions that I made to [codewars](https://www.codewars.com). This branch is derived from main branch and submission file is in `codewars/` folder.


## **3. api**
`api` branch contains APIs written using flask framework. This branch is derived from main branch. The API codes are contained in [`api_practice/`](api_practice/) folder.

[`api_practice/api_creation_assign.py`](api_practice/api_creation_assign.py) contains APIs for CRUD operations on [`api_practice/employees.json`](api_practice/employees.json) file. Routes for accessing APIs are as follows:

| Route | Method | Operation Description |
| ---------- | ----------- | ------------ |
| `/api/users/<int:id>` | GET | Retrieve name of employee in upper case with given id from `employees.json` |
| `/api/salary/<int:id>` | PUT | Update salary (*10000) of employee with given id from `employees.json`|
| `/api/delete/<int:id>` | DELETE | Delete record of employee with given id from `employees.json` |
| `/api/insert/` | POST | Insert new employee record into `employees.json`. Request body should be supplied in JSON format and it should not have id that matches existing id. |
| `/api/average_age/` | GET | Retrieve average age of all employees from `employees.json`|


[`api_practice/external_api_assign.py`](api_practice/external_api_assign.py) contains APIs for extracting information from the The Movie Database (TMDb) i.e. external API. You need to put your own API key in my code, for getting private API key you should sign in to [themoviedb](https://www.themoviedb.org). It stores the retrieved top-movies data from TMDb and stores it in `api_practice/example.json` file. The APIs perform further CRUD operations on the example.json file. Routes for accessing APIs are as follows:

| Routes | Method | Operation Description |
| ----------- | ------------- | ------------ |
| `/api/load-movies` | GET | Retrieves first 10 pages from TMDb by calling external API and stores the result in `example.json` file |
| `/api/movies/` | GET | Get title and rating of all movies in `example.json` file |
| `/api/search/<keyword>` | GET | Returns all the movies whose titles have the match for given `keyword` from `example.json` |
| `/api/delete/<int:id>` | DELETE | Deletes movie in `example.json` file whose id matches with given id |
| `/api/update/<int:id>` | PUT | Update rating of movie with given id in `example.json`. The rating to be updated to should be supplied with request in JSON format. |
| `/api/insert/` | POST | Add new movie record to `example.json`. The id of new movie record should not match existing record id. |


Each `.py` file within [`api_practice/`](api_practice/) folder can be run separately, but first all the requirements need to be installed. Requirements can be installed using command:
```
$ pip install -r requirements.txt
```
Each API file can be executed using command:
```
$ python <path_to_file>/filename.py
```
which runs the Flask app in DEBUG mode.


## **4. orm**

`orm` branch contains codes I used while learning Object Relationship Mapping (ORM) to interface with database in Python. I used `sqlalchemy` orm to operate on database. It consists of [`orm/`](orm/) folder. The [`orm/`](orm/) folder has [`orm/datacamp_submissions.ipynb`](orm/datacamp_submissions.ipynb) which is the submissions I made to [datacamp (python relational-database tutorial)](https://campus.datacamp.com/courses/introduction-to-relational-databases-in-python). Another file `orm/orm_learn.ipynb` contains Python codes used while getting basic idea about ORM. `orm/requirements.txt` consists of extra libraries installed while coding in this branch. External libraries can be installed using the command:
```
$ pip install -r requirements.txt
```

Inside [`orm/learning_management_system/`](orm/learning_management_system) folder, there are codes to create and perform operations on learning management database using ORM. [`learning_management_system_erd.png`](orm/learning_management_system/learning_management_system_erd.png) consists of the Entity Relationship Diagram (ERD) of the database created. [`database_creation.py`](orm/learning_management_system/database_creation.py) consists of codes to create and add records to database named LMS that is hosted on local machine. The address of the database is given in [`db_address.py`](orm/learning_management_system/db_address.py). It should be changed when running this program on your machine.

Further, [`exceptions.py`](orm/learning_management_system/exceptions.py) consists of some custom exceptions used while writing API, [`question.txt`](orm/learning_management_system/question.txt) consists the contexts for which REST APIs were written, and [`api.py`](orm/learning_management_system/api.py) consists of all the API codes written using `Flask` framework. The routes for APIs written in [`api.py`](orm/learning_management_system/api.py) are as follows:

| Routes | Method | Operation Description |
|--------|--------|-----------------------|
| `/api/programs` | GET | Retrieve list of all programs |
| `/api/students` | GET | Retrieve list of all students |
| `/api/instructors` | GET | Retrieve list of all instructors|
| `/api/program/students` | GET | Retrieve number of students in each program |
| `/api/semester/students` | GET | Retrieve number of students in each semester |
| `/api/section/students` | GET | Retrieve number of students in each section |
| `/api/semester/course_list` | GET | Retrieve list of courses in each semester |
| `/api/semester/section_list` | GET | Retrieve list of sections in each semester |
| `/api/semester/instructor_list` | GET | Retrieve list of instructors in each semester |
| `/api/insert/programs` | POST | Insert one or more programs into program table |
| `/api/insert/semesters` | POST | Insert one or more semesters into semester table |
| `/api/insert/courses` | POST | Insert one or more courses into course table |
| `/api/insert/course_semesters` | POST | Insert one or more course semester record into course_semester table |
| `/api/insert/sections` | POST | Insert one or more sections into sections table |
| `/api/insert/students` | POST | Insert one or more students into students table |
| `/api/insert/instructors` | POST | Insert one or more instructors into instructor table |
| `/api/insert/instructor_courses` | POST | Insert one or more instructor course record into instructor_course table |

To run the program, you first need to create a sql database of any name in your local machine. Then, you need to  update the database address of your local database into `DB_ADDRESS` in file [`db_address.py`](orm/learning_management_system/db_address.py). Then, you need to create the entire database by running command:
```
$ python database_creation.py
```

After database is created, the APIs can be used to operate on the database accordingly. To run the app for REST APIs, you need to run the command:
```
$ python api.py
```

This command will run the APIs at [`localhost:5000`](https://localhost:5000). To this URL, the resource identifier routes can be appended to perform aforementioned operations on database.


## **5. pandas**
This branch consists of codes that involve loading and transforming data using the python pandas library. It consists of a few assignments, and the data needed for those assignments are also provided within the pandas folder.

Before running this branch, few Python packages need to be installed using the command:
```
$ pip install -r requirements.txt
```

All the codes are then available in `.ipynb` files within [`pandas/`](pandas/) folder which can be run using `jupyter-notebook`.