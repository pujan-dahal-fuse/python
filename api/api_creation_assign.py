from flask import Flask, jsonify, request
from exceptions import ValueDuplicate, ValueNotFound
import json

app = Flask(__name__)

def jprint(obj):
    data = json.dumps(obj, indent=4)
    print(data)

# retrieve name of employee in upper case with given id
@app.route('/api/users/<int:id>', methods=['GET']) #127.0.0.1:5000/api/users/1001
def username(id):
    with open('employees.json', mode='r', encoding='utf-8') as file:
        employees = json.load(file)
        emp_name = dict()
        try:
            for record in employees:
                if record['id'] == id:
                    emp_name['firstName'] = record['firstName'].upper()
                    emp_name['lastName'] = record['lastName'].upper()
                    break
            if len(emp_name) == 0:
                raise ValueNotFound
            else:
                return jsonify({
                    'status': 200,
                    'message': 'Record retrieval successful',
                    'data': emp_name,
                    })
        except ValueNotFound:
            return jsonify({
                'status': 404,
                'message': 'Record not found',
                'data': {},
            })

# update salary of employee with given id
@app.route('/api/salary/<int:id>', methods = ['PUT'])
def update_salary(id):
    try:
        file = open('employees.json', mode='r', encoding='utf-8')
        employees = json.load(file)
        emp_record = dict()
        for record in employees:
            if record['id'] == id:
                record['salary'] *= 10000
                jprint(employees)
                emp_record = record
                break
        
        file.close()
        if len(emp_record) == 0: # record not found
            raise ValueNotFound
        else:
            with open('employees.json', mode='w', encoding='utf-8') as file:
                file.write(json.dumps(employees, indent=4))
                

            return jsonify({
                'status': 200,
                'message': 'Salary updating successful',
                'data': emp_record,
            })
    
    except ValueNotFound:
        return jsonify({
            'status': 404,
            'message': 'Record not found',
            'data': {},
        })
        
# delete record with provided id
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_record(id):
    try:
        file = open('employees.json', mode='r', encoding='utf-8')
        employees = json.load(file)
        new_employees = []
        emp_record = dict()
        id_found = False
        for record in employees:
            if record['id'] == id:
                id_found = True
                emp_record = record
                continue
            new_employees.append(record)
        
        file.close()
        if not id_found: # record was not found
            raise ValueNotFound
        else:
            with open('employees.json', mode='w', encoding='utf-8') as file:
                file.write(json.dumps(new_employees, indent=4))
            
            return jsonify({
                'status': 200,
                'message': 'Record deletion successful',
                'data': emp_record,
            })

    except ValueNotFound:
        return jsonify({
            'status': 404,
            'message': 'Record not found',
            'data': {},
        })

# insert new record and display success message
@app.route('/api/insert/', methods = ['POST'])
# json schema expected
def insert_record():
    body = request.get_json()
    try:
        with open('employees.json', mode='r', encoding='utf-8') as file:
            employees = json.load(file)
            for record in employees:
                if record['id'] == body['id']:
                    raise ValueDuplicate
            employees.append(body)
        
        with open('employees.json', mode='w', encoding='utf-8') as wfile:
            wfile.write(json.dumps(employees, indent=4))
        return jsonify({
            'status': 200,
            'message': 'Insertion successful',
            'data': body,
        })
    
    except ValueDuplicate:
        return jsonify({
            'status': 400,
            'message': 'Invalid input: duplicate id',
            'data': {},
        })

# display average age
@app.route('/api/average_age', methods=['GET'])
def avg_age():
    with open('employees.json', mode='r', encoding='utf-8') as file:
        employees = json.load(file)
        ages = [record['age'] for record in employees]
        if len(ages) == 0: # empty record
            return jsonify({
                'status': 404,
                'message': 'No records found',
                'data': {}
            })
        return jsonify({
            'status': 200,
            'message': 'Average age calculated successfully',
            'data': {
                'average_age': round(sum(ages)/len(ages), 2)
            }
        })


if __name__ == '__main__':
    app.run(debug=True)