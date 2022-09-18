from flask import Flask, jsonify, request
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy import insert, select, func, join
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from db_address import DB_ADDRESS
import MySQLdb
import json



app = Flask(__name__)

def jprint(obj):
    data = json.dumps(obj, indent=4)
    print(data)


# retrieve programs
@app.route('/api/programs', methods=['GET'])
def programs():
    """Retrieve all records of programs"""
        # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    program = Table('program', metadata_obj, autoload=True, autoload_with=engine)
    stmt = select([program])
    results = conn.execute(stmt).fetchall()

    response_data = []
    for result in results:
        program_dict = dict()
        program_dict['program_code'] = result.program_code
        program_dict['name'] = result.name
        program_dict['level'] = result.level
        program_dict['num_years'] = result.num_years
        response_data.append(program_dict)
        
    
    return jsonify({
        'status': 200,
        'message': 'Program records retrieval successful',
        'data': {
            'num_of_program_records': len(results),
            'records': response_data
        }
    })


# retrieve student list with total number of records
@app.route('/api/students', methods=['GET'])
def students():
    """Retrieve all the records of students"""
    
    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    student = Table('student', metadata_obj, autoload=True, autoload_with=engine)
    stmt = select([student])
    results = conn.execute(stmt).fetchall()

    response_data = []
    for result in results:
        student_dict = dict()
        student_dict['student_id'] = result.student_id
        student_dict['name'] = result.name
        student_dict['dob'] = result.dob
        student_dict['address'] = result.address
        student_dict['phone_no'] = result.phone_no
        student_dict['section_id'] = result.section_id
        response_data.append(student_dict)
    
    return jsonify({
        'status': 200,
        'message': 'Student records retrieval successful',
        'data': {
            'num_of_student_records': len(results),
            'records': response_data
        }
    })


# retrieve instructor list with total number of records
@app.route('/api/instructors', methods=['GET'])
def instructors():
    """Retrieve all the records of instructors"""
   
    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    instructor = Table('instructor', metadata_obj, autoload=True, autoload_with=engine)
    stmt = select([instructor])
    results = conn.execute(stmt).fetchall()

    response_data = []
    for result in results:
        instructor_dict = dict()
        instructor_dict['instructor_id'] = result.instructor_id
        instructor_dict['name'] = result.name
        instructor_dict['dob'] = result.dob
        instructor_dict['address'] = result.address
        instructor_dict['phone_no'] = result.phone_no
        instructor_dict['position'] = result.position
        instructor_dict['salutation'] = result.salutation
        instructor_dict['program_code'] = result.program_code
        response_data.append(instructor_dict)

    return jsonify({
        'status': 200,
        'message': 'Instructor records retrieval successful',
        'data': {
            'num_of_instructor_records': len(results),
            'records': response_data
        }
    })


# retrieve number of students in each program
@app.route('/api/program/students', methods=['GET'])
def program_students():
    """Retrieve number of students in each program"""
    
    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    program = Table('program', metadata_obj, autoload=True, autoload_with=engine)
    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    section = Table('section', metadata_obj, autoload=True, autoload_with=engine)
    student = Table('student', metadata_obj, autolaod=True, autoload_with=engine)
    
    stmt = select([program, func.count(student.columns.student_id).label('num_students')])
    stmt = stmt.select_from(((program\
                    .join(semester, program.columns.program_code == semester.columns.program_code))\
                    .join(section, semester.columns.semester_id == section.columns.semester_id))\
                    .join(student, section.columns.section_id == student.columns.section_id)
                    )
    stmt = stmt.group_by(program.columns.program_code,
                         program.columns.name,
                         program.columns.level,
                         program.columns.num_years)

    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        inner_dict = dict()
        outer_dict = dict()
        inner_dict['program_code'] = result.program_code
        inner_dict['name'] = result.name
        inner_dict['level'] = result.level
        inner_dict['num_years'] = result.num_years
        outer_dict['program'] = inner_dict
        outer_dict['num_students'] = result.num_students
        response_data.append(outer_dict)

    return jsonify({
        'status': 200,
        'message': 'Number of students in each program retrieval successful',
        'data': {
            'num_of_program_records': len(results),
            'records': response_data
        }
    })


# retrieve number of students in each semester
@app.route('/api/semester/students', methods=['GET'])
def semester_students():
    """Retrieve number of students in each semester"""
    
    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    section = Table('section', metadata_obj, autolaod=True, autoload_with=engine)
    student = Table('student', metadata_obj, autoload=True, autoload_with=engine)

    stmt = select([semester, func.count(student.columns.student_id).label('num_students')])
    stmt = stmt.select_from((semester\
            .join(section, semester.columns.semester_id == section.columns.semester_id))\
            .join(student, section.columns.section_id == student.columns.section_id))
    stmt = stmt.group_by(semester.columns.semester_id,
                         semester.columns.program_code,
                         semester.columns.semester_num)

    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        inner_dict = dict()
        outer_dict = dict()
        inner_dict['semester_id'] = result.semester_id
        inner_dict['program_code'] = result.program_code
        inner_dict['semester_num'] = result.semester_num
        outer_dict['semester'] = inner_dict
        outer_dict['num_students'] = result.num_students
        response_data.append(outer_dict)

    return jsonify({
        'status': 200,
        'message': 'Number of students in each semester retrieval successful',
        'data': {
            'num_of_semester_records': len(results),
            'records': response_data
        }
    })


# retrieve number of students in each section
@app.route('/api/section/students', methods=['GET'])
def section_students():
    """Retrieve number of students in each section"""
    
    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    section = Table('section', metadata_obj, autolaod=True, autoload_with=engine)
    student = Table('student', metadata_obj, autoload=True, autoload_with=engine)

    stmt = select([section, func.count(student.columns.student_id).label('num_students')])
    stmt = stmt.select_from(section.join(student, section.columns.section_id == student.columns.section_id))
    stmt = stmt.group_by(section.columns.section_id,
                         section.columns.building,
                         section.columns.room,
                         section.columns.semester_id)

    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        inner_dict = dict()
        outer_dict = dict()
        inner_dict['section_id'] = result.section_id
        inner_dict['building'] = result.building
        inner_dict['room'] = result.room
        inner_dict['semester_id'] = result.semester_id
        outer_dict['section'] = inner_dict
        outer_dict['num_students'] = result.num_students
        response_data.append(outer_dict)

    return jsonify({
        'status': 200,
        'message': 'Number of students in each section retrieval successful',
        'data': {
            'num_of_section_records': len(results),
            'records': response_data
        }
    })


# retrieve courses in each semester
@app.route('/api/semester/courses', methods=['GET'])
def semester_courses_list():
    """Retrieve courses that are taught in each semester"""
    
    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    course = Table('course', metadata_obj, autolaod=True, autoload_with=engine)
    course_semester = Table('course_semester', metadata_obj, autoload=True, autload_with=engine)

    stmt = select([semester, course])
    stmt = stmt.select_from((semester\
                        .join(course_semester, semester.columns.semester_id == course_semester.columns.semester_id))\
                        .join(course, course.columns.course_code == course_semester.columns.course_code)
                        )
    
    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        course_dict = dict()
        course_dict['course_code'] = result.course_code
        course_dict['name'] = result.name
        course_dict['credit_hours'] = result.credit_hours
        course_dict['num_chapters'] = result.num_chapters
        course_dict['practical_marks'] = result.practical_marks
        course_dict['internal_marks'] = result.internal_marks
        course_dict['exam_marks'] = result.exam_marks
        
        sem_found = False # if sem is found in response list
        for sem in response_data: #check if that semester record is already in response list (if so we need to append, course to course list)
            if sem['semester']['semester_id'] == result.semester_id:
                course_list = sem['course_list']
                # append the new dict to course list
                course_list.append(course_dict)
                sem['course_list'] = course_list
                sem['num_course'] += 1
                sem_found = True
                break
    
        if sem_found:
            continue
        else:
        # the semester record is not already in response list, so add it to the list
            course_list = []
            course_list.append(course_dict)

            sem_dict = dict()
            sem_dict['semester_id'] = result.semester_id
            sem_dict['semester_num'] = result.semester_num
            sem_dict['program_code'] = result.program_code
            
            response_data.append({
                'semester': sem_dict,
                'num_course': 1,
                'course_list': course_list
            })
                
    return jsonify({
        'status': 200,
        'message': 'List of courses in each semester retrieval successful',
        'data': {
            'num_of_semester_records': len(results),
            'records': response_data
        }
    })


# retrieve sections of each semester (list)
@app.route('/api/semester/sections', methods=['GET'])
def semester_sections_list():
    """Retrieve list of sections of each semester"""

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    section = Table('section', metadata_obj, autoload=True, autoload_with=engine)

    stmt = select([semester.columns.semester_num, semester.columns.program_code, section]) 
    # semester id is repeated, so to remove ambiguity later, two remaining fields of semester table are chosen
    stmt = stmt.select_from(semester.join(section, semester.columns.semester_id == section.columns.semester_id))

    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        section_dict = dict()
        section_dict['section_id'] = result.section_id
        section_dict['building'] = result.building
        section_dict['room'] = result.room

        sem_found = False # if sem is found in response list
        for sem in response_data: # check if semester record is already present in response list (if so we need to append section to section list)
            if sem['semester']['semester_id'] == result.semester_id:
                section_list = sem['section_list']
                section_list.append(section_dict)
                sem['section_list'] = section_list
                sem['num_section'] += 1
                sem_found = True
                break
        
        if sem_found:
            continue
        else:
            # sem record is not in response data (list), so add new sem record to the response list
            section_list = []
            section_list.append(section_dict)

            sem_dict = dict()
            sem_dict['semester_id'] = result.semester_id
            sem_dict['semester_num'] = result.semester_num
            sem_dict['program_code'] = result.program_code

            response_data.append({
                'semester': sem_dict,
                'num_section': 1,
                'section_list': section_list
            })
        
    return jsonify({
        'status': 200,
        'message': 'List of sections in each semester retrieval successful',
        'data': {
            'num_of_semester_records': len(results),
            'records': response_data
        }
    })


# retireve instuctors of each semester
@app.route('/api/semester/instructors', methods=['GET'])
def semester_instructors_list():
    """Retrieve instructor list for each semester"""

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    course = Table('course', metadata_obj, audoload=True, autoload_with=engine)
    instructor = Table('instructor', metadata_obj, autload=True, autoload_with=engine)
    course_semester = Table('course_semester', metadata_obj, autoload=True, autoload_with=engine)
    instructor_course = Table('instructor_course', metadata_obj, autoload=True, autolaod_with=engine)

    stmt = select([semester,
                   instructor.columns.instructor_id,
                   instructor.columns.name,
                   instructor.columns.dob,
                   instructor.columns.address,
                   instructor.columns.phone_no,
                   instructor.columns.position,
                   instructor.columns.salutation,
                   instructor.columns.program_code.label('instructor_program_code')])
    stmt = stmt.select_from((((semester\
                        .join(course_semester, semester.columns.semester_id == course_semester.columns.semester_id))\
                        .join(course, course.columns.course_code == course_semester.columns.course_code))\
                        .join(instructor_course, course.columns.course_code == instructor_course.columns.course_code))\
                        .join(instructor, instructor.columns.instructor_id == instructor_course.columns.instructor_id)
                        )

    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        instructor_dict = dict()
        instructor_dict['instructor_id'] = result.instructor_id
        instructor_dict['name'] = result.name
        instructor_dict['dob'] = result.dob
        instructor_dict['address'] = result.address
        instructor_dict['phone_no'] = result.phone_no
        instructor_dict['position'] = result.position
        instructor_dict['salutation'] = result.salutation
        instructor_dict['program_code'] = result.instructor_program_code

        sem_found = False # if sem is found in response list
        for sem in response_data:
            if sem['semester']['semester_id'] == result.semester_id:
                instructor_list = sem['instructor_list']
                instructor_list.append(instructor_dict)
                sem['instructor_list'] = instructor_list
                sem['num_instructor'] += 1
                sem_found = True
                break
        
        if sem_found:
            continue
        
        else:
            instructor_list = []
            instructor_list.append(instructor_dict)

            sem_dict = dict()
            sem_dict['semester_id'] = result.semester_id
            sem_dict['semester_num'] = result.semester_num
            sem_dict['program_code'] = result.program_code

            response_data.append({
                'semester': sem_dict,
                'num_instructor': 1, 
                'instructor_list': instructor_list
            })

    return jsonify({
        'status': 200,
        'message': 'List of instructors in each semester retrieval successful',
        'data': {
            'num_of_semester_records': len(results),
            'records': response_data
        }
    })


# insert new program
@app.route('/api/insert/programs', methods=['POST'])
def insert_program():
    """Insert new program into database"""
    
    # get the body of insertion request that contains the new records to be inserted
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    program = Table('program', metadata_obj, autoload=True, autoload_with=engine)
    stmt = insert(program)
    try:
        conn.execute(stmt, body)

        return jsonify({
            'status': 200,
            'message': 'Program insertion successful',
            'data': {
                'num_of_program_inserted': len(body),
                'recods_inserted': body
            }
        })
    
    # error if a duplicate record is inserted
    # there are two types of error codes in IntegrityError.orig.args[0]: 1452, 1062
    # 1452: Foreign key constraint error
    # 1062: Unique key constraint error
    # in this case only unique key constrint error can occur
    except IntegrityError as ie:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: program_code exists in database" if ie.orig.args[0] == 1062\
                        else "Invalid input",
            'data': {}
        })

# insert new semester into program
@app.route('/api/insert/semesters', methods=['POST'])
def insert_semester():
    """Insert new semester into a program"""

    # get the body of insertion request that contains the new records to be inserted
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    stmt = insert(semester)
    try:
        conn.execute(stmt, body)

        return jsonify({
            'status': 200,
            'message': 'Semester insertion successful',
            'data': {
                'num_of_semester_inserted': len(body),
                'records_inserted': body
            }
        })
    
    # error if either duplicate semester_record or
    # there are two types of error codes in IntegrityError.orig.args[0]: 1452, 1062
    # 1452: Foreign key constraint error
    # 1062: Unique key constraint error
    except IntegrityError as ie:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: record exists in database" if ie.orig.args[0] == 1062\
                       else "Bad input: program_code doesn't exist in program table",
            'data': {}
        })


# insert courses in each semester


if __name__ == '__main__':
    app.run(debug=True)
