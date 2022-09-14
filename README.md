# **Python Repository**

This repository is made up of codes I used while learning Python and APIs. It is divided into 3 branches:
1. **main**
2. **codewars**
3. **api**
## **1. main**
`main` contains codes that I used while learning basic and advanced Python. Codes are within `python_basic_advanced/` folder. Basic codes are in `python_basic_advanced/task1.py` and `python_basic_advanced/constant.py` files. Advanced codes are in `python_basic_advanced/advanced_topics.ipynb` file.


## **2. codewars**
`codewars` branch contains successful Python code submissions that I made to [codewars](https://www.codewars.com). This branch is derived from main branch and submission file is in `codewars/` folder.


## **3. api**
`api` branch contains APIs written using flask framework. This branch is derived from main branch. The API codes are contained in `api_practice/` folder.

`api_practice/api_creation_assign.py` contains APIs for CRUD operations on `api_practice/employees.json` file. Routes for accessing APIs are as follows:

| Route | Method | Operation Description |
| ---------- | ----------- | ------------ |
| `/api/users/<int:id>` | GET | Retrieve name of employee in upper case with given id from `employees.json` |
| `/api/salary/<int:id>` | PUT | Update salary (*10000) of employee with given id from `employees.json`|
| `/api/delete/<int:id>` | DELETE | Delete record of employee with given id from `employees.json` |
| `/api/insert/` | POST | Insert new employee record into `employees.json`. Request body should be supplied in JSON format and it should not have id that matches existing id. |
| `/api/average_age/` | GET | Retrieve average age of all employees from `employees.json`|


`api_practice/external_api_assign.py` contains APIs for extracting information from the The Movie Database (TMDb) i.e. external API. You need to put your own API key in my code, for getting private API key you should sign in to [themoviedb](https://www.themoviedb.org). It stores the retrieved top-movies data from TMDb and stores it in `api_practice/example.json` file. The APIs perform further CRUD operations on the example.json file. Routes for accessing APIs are as follows:

| Routes | Method | Operation Description |
| ----------- | ------------- | ------------ |
| `/api/load-movies` | GET | Retrieves first 10 pages from TMDb by calling external API and stores the result in `example.json` file |
| `/api/movies/` | GET | Get title and rating of all movies in `example.json` file |
| `/api/search/<keyword>` | GET | Returns all the movies whose titles have the match for given `keyword` from `example.json` |
| `/api/delete/<int:id>` | DELETE | Deletes movie in `example.json` file whose id matches with given id |
| `/api/update/<int:id>` | PUT | Update rating of movie with given id in `example.json`. The rating to be updated to should be supplied with request in JSON format. |
| `/api/insert/` | POST | Add new movie record to `example.json`. The id of new movie record should not match existing record id. |


Each `.py` file within `api_practice/` folder can be run separately, but first all the requirements need to be installed. Requirements can be installed using command:
```
pip install -r requirements.txt
```
Each API file can be executed using command:
```
python <path_to_file>/filename.py
```
which runs the Flask app in DEBUG mode.
