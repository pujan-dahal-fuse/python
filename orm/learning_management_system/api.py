from importlib.metadata import metadata
from multiprocessing.sharedctypes import Value
from flask import Flask, jsonify, request
from sqlalchemy import create_engine , MetaData, Table
from sqlalchemy import insert, select, func
from exceptions import ValueNotFound
from sqlalchemy.exc import IntegrityError
from db_address import DB_ADDRESS
import MySQLdb
import json



app = Flask(__name__)

def jprint(obj):
    data = json.dumps(obj, indent=4)
    print(data)


################
# GET METHODS #
################


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
        program_dict['program_name'] = result.program_name
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
        student_dict['student_name'] = result.student_name
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
        instructor_dict['instructor_name'] = result.instructor_name
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
                         program.columns.program_name,
                         program.columns.level,
                         program.columns.num_years)

    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        inner_dict = dict()
        outer_dict = dict()
        inner_dict['program_code'] = result.program_code
        inner_dict['program_name'] = result.program_name
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
                         section.columns.section_name,
                         section.columns.building,
                         section.columns.room,
                         section.columns.semester_id)

    results = conn.execute(stmt).fetchall()
    response_data = []
    for result in results:
        inner_dict = dict()
        outer_dict = dict()
        inner_dict['section_id'] = result.section_id
        inner_dict['section_name'] = result.section_name
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
@app.route('/api/semester/course_list', methods=['GET'])
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
        course_dict['course_name'] = result.course_name
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
@app.route('/api/semester/section_list', methods=['GET'])
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
        section_dict['section_name'] = result.section_name
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
@app.route('/api/semester/instructor_list', methods=['GET'])
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
                   instructor.columns.instructor_name,
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
        instructor_dict['instructor_name'] = result.instructor_name
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



##############
# POST METHODS
##############

# insert new program
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/programs', methods=['POST'])
def insert_programs():
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
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/semesters', methods=['POST'])
def insert_semesters():
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
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/courses', methods=['POST'])
def insert_courses():
    """Insert new course into course table"""

    # get the body of insertion request that contains the new records to be inserted
    # in input data there are all fields of course table, (program_code and semester_num) are optional
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)


    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    course = Table('course', metadata_obj, autoload=True, autolaod_with=engine)
    course_semester = Table('course_semester', metadata_obj, autoload=True, autoload_with=engine)

    try:
        inserted_records = []
        for record in body:
            course_dict = dict()
            course_sem_dict = dict()
            course_dict['course_code'] = record['course_code']
            course_dict['course_name'] = record['course_name']
            course_dict['credit_hours'] = record['credit_hours']
            course_dict['num_chapters'] = record['num_chapters']
            course_dict['practical_marks'] = record['practical_marks']
            course_dict['internal_marks'] = record['internal_marks']
            course_dict['exam_marks'] = record['exam_marks']

            sem_found = False
            # there are two possibilities, one program_code and semester_num are provided with course (insert into course_semester table also)
            # another, no program_code and semester_num provided (record is not inserted into course semester table)
            if record.get('program_code') is not None and record.get('semester_num') is not None: # if program_code and semester_num are provided
                course_sem_dict = dict()
                course_sem_dict['course_code'] = record['course_code']
                for result in conn.execute(select([semester])).fetchall():
                    if result.semester_num == record['semester_num'] and result.program_code == record['program_code']:
                        sem_found = True
                        sem_id = result.semester_id
                        break
                if not sem_found:
                    raise ValueNotFound("program_code, semester_num pair not found in semester table")             

                course_sem_dict['semester_id'] = sem_id

            
            # insert into course dict
            # this code is inserted after the if statement so that the operation doesn't get partially committed
            stmt1 = insert(course)
            conn.execute(stmt1, course_dict)
            inserted_records.append(course_dict)


            # here insertion into course_semester is done after insertion into course table
            # because course_code is a foriegn key in course_semester table
            if sem_found:
                stmt2 = insert(course_semester) # insert record into course semester table
                conn.execute(stmt2, course_sem_dict)   

        return jsonify({
            'status': 200,
            'message': 'Course insertion successful',
            'data': {
                'num_of_course_insertions': len(inserted_records),
                'records_inserted': inserted_records
            }
        })
    
    # error if either duplicate course record or
    # there are two types of error codes in IntegrityError.orig.args[0]: 1452, 1062
    # 1452: Foreign key constraint error
    # 1062: Unique key constraint error
    except IntegrityError as ie:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: record exists in database" if ie.orig.args[0] == 1062 else "Invalid input",
            'data': {}
        })

    except ValueNotFound as vnf:
        return jsonify({
            'status': 400,
            'message': f"Bad input: {vnf.message()}",
            'data': {}
        })

# insert records into course_semester table explicitly
# because course can exist without a record in corse_semester table
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/course_semesters', methods=['POST'])
def insert_course_semesters():
    """Insert record into course_semester table separately"""
    # get the body of insertion request that contains the new records to be inserted
    # in input data there are course_code, program_code and semester_num
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    course_semester = Table('course_semester', metadata_obj, autoload=True, autoload_with=engine)
    course = Table('course', metadata_obj, autoload=True, autoload_with=engine)
    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)

    try:
        inserted_records = []
        for record in body:
            course_sem_dict = dict()
            course_sem_dict['course_code'] = record['course_code']
            course_found = False
            sem_found = False
            for result in conn.execute(select([course])).fetchall():
                if result.course_code == record['course_code']:
                    course_found = True
                    break
            if not course_found:
                raise ValueNotFound("course_code not found in course table")

            for result in conn.execute(select([semester])).fetchall():
                if result.semester_num == record['semester_num'] and result.program_code == record['program_code']:
                    sem_found = True
                    sem_id = result.semester_id
                    break
            if not sem_found:
                raise ValueNotFound("program_code, semester_num pair not found in semester table")

            course_sem_dict['semester_id'] = sem_id
            stmt = insert(course_semester)
            conn.execute(stmt, course_sem_dict)
            inserted_records.append(course_sem_dict)
        
        return jsonify({
            'status': 200,
            'message': "Course semester insertion successful",
            'data': {
                'num_of_course_semester_insertions': len(inserted_records),
                'records_inserted': inserted_records
            }
        })
    
    except ValueNotFound as vnf:
        return jsonify({
            'status': 400,
            'message': f"Bad input: {vnf.message()}",
            'data': {}
        })


# insert sections in semester
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/sections', methods=['POST'])
def insert_sections():
    """Insert new section into semester"""

    # get the body of insertion request that contains the new records to be inserted
    # in input data there are all fields of section table (except section_id), a program_code and sem_number
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    section = Table('section', metadata_obj, autoload=True, autoloadwith=engine)
    semester = Table('semester', metadata_obj, autoload=True, autoloadwith=engine)

    try:
        inserted_records = []
        for record in body:
            section_dict = dict()
            section_dict['section_name'] = record['section_name']
            section_dict['building'] = record['building']
            section_dict['room'] = record['room']
            
            # find semester id for given program code and semester_num
            sem_found = False
            for result in conn.execute(select([semester])).fetchall():
                if result.semester_num == record['semester_num'] and result.program_code == record['program_code']:
                    sem_found = True
                    sem_id = result.semester_id
                    break
            
            if not sem_found:
                raise ValueNotFound("program_code, semester_num pair not found in semester table")

            section_dict['semester_id'] = sem_id
            stmt = insert(section)
            conn.execute(stmt, section_dict)
            inserted_records.append(section_dict)

        return jsonify({
            'status': 200,
            'message': "Section insertion successful",
            'data': {
                'num_of_section_insertions': len(inserted_records),
                'records_inserted': inserted_records
            }
        })
    # error if either duplicate course record or
    # there are two types of error codes in IntegrityError.orig.args[0]: 1452, 1062
    # 1452: Foreign key constraint error
    # 1062: Unique key constraint error

    except IntegrityError as ie:
        return jsonify({
            'status': 400,
            'message': 'Duplicate input: record exists in database' if ie.orig.args[0] == 1062 else "Invalid input",
            'data': {}
        })

    except ValueNotFound as vnf:
        return jsonify({
            'status': 400,
            'message': f'Bad input: {vnf.message()}',
            'data': {}
        })

    

# insert student to semester program i.e. to a section
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/students', methods=['POST'])
def insert_students():
    """Insert new student record to database i.e. in section"""

    # get the body of insertion request that contains the new records to be inserted
    # in input data there are all fields of student table (except section_id)
    # program_code, sem_number and section_name are optional
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    section = Table('section', metadata_obj, autoload=True, autoloadwith=engine)
    semester = Table('semester', metadata_obj, autoload=True, autoloadwith=engine)
    student = Table('student', metadata_obj, autoload=True, autoloadwith=engine)

    try:
        inserted_records = []
        for record in body:
            student_dict = dict()
            student_dict['student_name'] = record['student_name']
            student_dict['dob'] = record['dob']
            student_dict['address'] = record['address']
            student_dict['phone_no'] = record['phone_no']
            student_dict['section_id'] = None

            # if semester_num, program_code and section_name are provided
            if record.get('semester_num') is not None and record.get('program_code') is not None and record.get('section_name') is not None:            
                # find semester id and section id accordingly
                sem_found = False
                section_found = False

                for result in conn.execute(select([semester])).fetchall():
                    if result.semester_num == record['semester_num'] and result.program_code == record['program_code']:
                        sem_found = True
                        sem_id = result.semester_id
                        break
                
                if not sem_found:
                    raise ValueNotFound("program_code, semester_num pair not found in semester table")

                for result in conn.execute(select([section])).fetchall():
                    if result.section_name == record['section_name'] and sem_id == result.semester_id:
                        section_found = True
                        sec_id = result.section_id
                        break
                
                if not section_found:
                    raise ValueNotFound("section_name not found in section table")

                student_dict['section_id'] = sec_id
            

            stmt = insert(student)
            conn.execute(stmt, student_dict)
            inserted_records.append(student_dict)

        return jsonify({
            'status': 200,
            'message': "Student insertion successful",
            'data': {
                'num_of_student_insertions': len(inserted_records),
                'records_inserted': inserted_records
            }
        })

    # error if either duplicate course record or
    # there are two types of error codes in IntegrityError.orig.args[0]: 1452, 1062
    # 1452: Foreign key constraint error
    # 1062: Unique key constraint error
    except IntegrityError as ie:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: record exists in database" if ie.orig.args[0] == 1062 else "Invalid input",
            'data': {}
        })

    except ValueNotFound as vnf:
        return jsonify({
            'status': 400,
            'message': f"Bad input: {vnf.message()}",
            'data': {}
        })

    
# insert instructor record to database
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/instructors', methods=['POST'])
def insert_instructors():
    """Insert new instructor record in instructor table"""

    # get the body of insertion request that contains the new records to be inserted
    # in input data there are all fields of instructor table and a program_code
    # course_code field is optional (if it is provided, record is inserted to instructor_course database)
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    instructor = Table('instructor', metadata_obj, autoload=True, autoload_with=engine)
    instructor_course = Table('instructor_course', metadata_obj, autoload=True, autoload_with=engine)
    course = Table('course', metadata_obj, autoload=True, autoload_with=engine)

    try:
        inserted_records = []
        for record in body:
            instructor_dict = dict()
            instructor_dict['instructor_name'] = record['instructor_name']
            instructor_dict['dob'] = record['dob']
            instructor_dict['address'] = record['address']
            instructor_dict['phone_no'] = record['phone_no']
            instructor_dict['position'] = record['position']
            instructor_dict['salutation'] = record['salutation']
            instructor_dict['program_code'] = record['program_code'] # this foreign key constraint is checked automatically by the database

            course_found = False
            # if course_code is provided , we have to insert a record to instructor_course table
            if record.get('course_code') is not None:
                instructor_course_dict = dict()
                # check if the course_code is present in course table
                for result in conn.execute(select([course])).fetchall():
                    if result.course_code == record['course_code']:
                        course_found = True
                        break
                if not course_found:
                    raise ValueNotFound("course_code not found in course table")
                
                instructor_course_dict['course_code'] = record['course_code']

                # instructor_id is autoincrement, so new instructor id in our instructor table will be max_instructor_id + 1
                # find max_instructor_id from our table
                max_instructor_id = conn.execute(select(func.max([instructor.columns.instructor_id]))).scalar()
                instructor_course_dict['instructor_id'] = max_instructor_id + 1

            # insert into instructor
            # this code is executed after the if so that the operation doesn't get partially committed
            stmt1 = insert(instructor)
            conn.execute(stmt1, instructor_dict)
            inserted_records.append(instructor_dict)
            
            # here insertion into instructor course is done after insertion into instructor
            # because error may occur when inserting into instructor, and instructor_id is 
            # foreign key that has not yet been incremented in instructor table
            if course_found:
                stmt2 = insert(instructor_course)
                conn.execute(stmt2, instructor_course_dict)
        
        return jsonify({
            'status': 200,
            'message': "Instructor insertion successful",
            'data': {
                'num_of_instructor_insertions': len(inserted_records),
                'records_inserted': inserted_records
            }
        })
    
    # error if either duplicate course record or
    # there are two types of error codes in IntegrityError.orig.args[0]: 1452, 1062
    # 1452: Foreign key constraint error
    # 1062: Unique key constraint error
    except IntegrityError as ie:    
        return jsonify({
            'status': 400,
            'message': "Duplicate input: record exists in database" if ie.orig.args[0] == 1062\
                        else "Bad input: program_code not found in program table",
            'data': {}
        })

    except ValueNotFound as vnf:
        return jsonify({
            'status': 400,
            'message': f'Bad input: {vnf.message()}',
            'data': {}
        })


# insert into instructor_course table explictly
# beacuse instructor can exist without a record in instructor_course table
# input should be in form of list of dictionaries as JSON
@app.route('/api/insert/instructor_courses', methods=['POST'])
def insert_instructor_courses():
    # get the body of insertion request that contains the new records to be inserted
    # in input data there are instructor_id and course_code
    body = request.get_json()

    # create engine to connect to database
    engine = create_engine(DB_ADDRESS)
    # create connection to perform queries on database
    conn = engine.connect()
    # create MetaData object
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    course = Table('course', metadata_obj, autoload=True, autoload_with=engine)
    instructor = Table('instructor', metadata_obj, autoload=True, autoload_with=engine)
    instructor_course = Table('instructor_course', metadata_obj, autoload=True, autoload_with=engine)

    try:
        inserted_records = []
        for record in body:
            instructor_course_dict = dict()
            instructor_course_dict['instructor_id'] = record['instructor_id']
            instructor_found = False
            course_found = False
            for result in conn.execute(select([instructor])).fetchall():
                if result.instructor_id == record['instructor_id']:
                    instructor_found = True
                    break
            if not instructor_found:
                raise ValueNotFound("instructor_id not found in instructor table")

            for result in conn.execute(select([course])).fetchall():
                if result.course_code == record['course_code']:
                    course_found = True
                    break
            if not course_found:
                raise ValueNotFound("course_code not found in course_table")
            
            instructor_course_dict['course_code'] = record['course_code']
            stmt = insert(instructor_course)
            conn.execute(stmt, instructor_course_dict)
            inserted_records.append(instructor_course_dict)

        return jsonify({
            'status': 200,
            'message': "Instructor course insertion successful",
            'data': {
                'num_of_instructor_course_insertions': len(inserted_records),
                'records_inserted': inserted_records
            }
        })

    except ValueNotFound as vnf:
        return jsonify({
            'status': 400,
            'message': f"Bad input: {vnf.message()}",
            'data': {}
        })


if __name__ == '__main__':
    app.run(debug=True)
