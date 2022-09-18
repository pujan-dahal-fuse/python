from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, UniqueConstraint
from sqlalchemy import insert
from db_address import DB_ADDRESS
import MySQLdb


def create_schema(engine):
    # creating tables in database
    """
    Tables list:
    1. program: 
        program_code (varchar(10), PK)
        name (varchar(255))
        level (varchar(20)) e.g. masters, bachelors
        num_years (int)

    2. semester
        semester_id (int, PK)
        program_code (varchar(10), FK)
        semester_num (int)

    3. course
        course_code (varchar(20), PK)
        course_name (varchar(255))
        credit_hours (int)
        num_chapters (int)
        practical_marks (int)
        internal_marks (int)
        exam_marks (int)

    4. course_semester
        course_code (varchar(20), FK, PK)
        semester_id (int, FK, PK)

    5. instructor
        instructor_id (int, PK)
        name (varchar(50))
        dob (date)
        address (varchar(255))
        phone_no (char(10))
        position (varchar(50))
        salutation (varchar(20))
        program_code (varchar(10), FK) i.e. a teacher originally belongs to 1 department

    6. instructor_course
        instructor_id (int, FK, PK)
        course_code (varchar(20), FK, PK)

    7. section
        section_id (int, PK)
        building (varchar(10))
        room (int)
        semester_id (int, FK)

    8. student
        student_id (int)
        name (varchar(50))
        dob (date)
        address (varchar(255))
        phone_no (char(10))
        section_id (int, FK)
    """
    # create metadata object and bind it to engine
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)

    program = Table('program', metadata_obj,
                    Column('program_code', String(20), primary_key=True),
                    Column('name', String(255), nullable=False),
                    Column('level', String(20), nullable=False),
                    Column('num_years', Integer, nullable=False)
                    )

    semester = Table('semester', metadata_obj,
                    Column('semester_id', Integer, primary_key=True, autoincrement=True),
                    Column('semester_num', Integer, nullable=False),
                    Column('program_code', String(20), ForeignKey('program.program_code', onupdate="CASCADE", ondelete="CASCADE"), nullable=False),
                    UniqueConstraint('semester_num', 'program_code', name='UniqueKey_Semester')
                    )

    course = Table('course', metadata_obj,
                Column('course_code', String(20), primary_key=True),
                Column('name', String(255), nullable=False),
                Column('credit_hours', Integer, nullable=False),
                Column('num_chapters', Integer, nullable=False),
                Column('practical_marks', Integer, default=0),
                Column('internal_marks', Integer, nullable=False),
                Column('exam_marks', Integer, nullable=False)
                )

    course_semester = Table('course_semester', metadata_obj,
                            Column('course_code', String(20), ForeignKey('course.course_code', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
                            Column('semester_id', Integer, ForeignKey('semester.semester_id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
                            )

    instructor = Table('instructor', metadata_obj,
                    Column('instructor_id', Integer, primary_key=True, autoincrement=True),
                    Column('name', String(50), nullable=False),
                    Column('dob', Date, nullable=False),
                    Column('address', String(255), nullable=False),
                    Column('phone_no', String(10), nullable=False),
                    Column('position', String(50), nullable=False),
                    Column('salutation', String(20), default=''),
                    Column('program_code', String(20), ForeignKey('program.program_code', onupdate="CASCADE"), nullable=True)
                    )

    instructor_course = Table('instructor_course', metadata_obj,
                            Column('instructor_id', Integer, ForeignKey('instructor.instructor_id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
                            Column('course_code', String(20), ForeignKey('course.course_code', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
                            )

    section = Table('section', metadata_obj,
                    Column('section_id', Integer, primary_key=True, autoincrement=True),
                    Column('building', String(10), nullable=False),
                    Column('room', Integer, nullable=False),
                    Column('semester_id', Integer, ForeignKey('semester.semester_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
                    )

    student = Table('student', metadata_obj,
                    Column('student_id', Integer, primary_key=True, autoincrement=True),
                    Column('name', String(50), nullable=False),
                    Column('dob', Date, nullable=False),
                    Column('address', String(255), nullable=False),
                    Column('phone_no', String(10), nullable=False),
                    Column('section_id', Integer, ForeignKey('section.section_id', onupdate="CASCADE"), nullable=True)
                    )

    metadata_obj.create_all(engine)


def insert_initial_records(engine):
    # create connection to the engine
    conn = engine.connect()

    # create MetaData object for storing database metadata
    metadata_obj = MetaData(bind=engine)
    MetaData.reflect(metadata_obj)
    
    program = Table('program', metadata_obj, autoload=True, autoload_with=engine)
    semester = Table('semester', metadata_obj, autoload=True, autoload_with=engine)
    course = Table('course', metadata_obj, autoload=True, autoload_with=engine)
    course_semester = Table('course_semester', metadata_obj, autoload=True, autoload_with=engine)
    instructor = Table('instructor', metadata_obj, autoload=True, autoload_with=engine)
    instructor_course = Table('instructor_course', metadata_obj, autolaod=True, autoload_with=engine)
    section = Table('section', metadata_obj, audoload=True, autoload_with=engine)
    student = Table('student', metadata_obj, autoload=True, autoload_with=engine)

    program_list = [
        {'program_code': 'BCE', 'name': 'Bachelors in Civil Engineering', 'level': 'Bachelors', 'num_years': 4},
        {'program_code': 'BCT', 'name': 'Bachelors in Computer Engineering', 'level': 'Bachelors', 'num_years': 4},
        {'program_code': 'M.Sc. Physics', 'name': 'Masters in Physics', 'level': 'Masters', 'num_years': 2}
    ]

    semester_list = [
        {'semester_id': 100001, 'program_code': 'BCE', 'semester_num': 1},
        {'semester_id': 100002, 'program_code': 'BCT', 'semester_num': 1},
        {'semester_id': 100003, 'program_code': 'M.Sc. Physics', 'semester_num': 1}
    ]

    course_list = [
        {'course_code': '11.001', 'name': 'Introduction to Fluid Mechanics', 'credit_hours': 45, 'num_chapters': 10, 'practical_marks': 50, 'internal_marks': 20, 'exam_marks': 80},
        {'course_code': '12.001', 'name': 'Digital Logic', 'credit_hours': 45, 'num_chapters': 10, 'practical_marks': 50, 'internal_marks': 20, 'exam_marks': 80},
        {'course_code': '31.001', 'name': 'Introduction to Quantum Mechanics', 'credit_hours': 45, 'num_chapters': 10, 'practical_marks': 0, 'internal_marks': 20, 'exam_marks': 80}
    ]

    course_semester_list = [
        {'course_code': '11.001', 'semester_id': 100001},
        {'course_code': '12.001', 'semester_id': 100002},
        {'course_code': '31.001', 'semester_id': 100003}        
    ]

    instructor_list = [
        {'instructor_id': 200001, 'name': 'John Doe', 'dob': '1975-03-11', 'address': 'San Francisco, California', 'phone_no': '9845011345', 'position': 'Professor', 'salutation': 'Prof. Dr.', 'program_code': 'BCE'},
        {'instructor_id': 200002, 'name': 'Laura Philip', 'dob': '1968-07-23', 'address': 'San Jose, California', 'phone_no': '9845699024', 'position': 'Assistant Professor', 'salutation': 'Asst. Prof. Dr.', 'program_code': 'BCT'},
        {'instructor_id': 200003, 'name': 'Jean Bell', 'dob': '1972-08-09', 'address': 'Miami, Florida', 'phone_no': '9877433560', 'position': 'Professor', 'salutation': 'Prof. Dr.', 'program_code': 'M.Sc. Physics'}
    ]

    instructor_course_list = [
        {'instructor_id': 200001, 'course_code': '11.001'},
        {'instructor_id': 200002, 'course_code': '12.001'},
        {'instructor_id': 200003, 'course_code': '31.001'}
    ]

    section_list = [
        {'section_id': 300001, 'building': 'Alpha', 'room': 202, 'semester_id': 100001},
        {'section_id': 300002, 'building': 'Bravo', 'room': 501, 'semester_id': 100002},
        {'section_id': 300003, 'building': 'Zulu', 'room': 112, 'semester_id': 100003}
    ]

    student_list = [
        {'student_id': 400001, 'name': 'Pujan Dahal', 'dob': '1999-01-02', 'address': 'New Baneshowr, Kathmandu', 'phone_no': '9807233509', 'section_id': 300001},
        {'student_id': 400002, 'name': 'Hattori Hanjo', 'dob': '2000-05-08', 'address': 'Satdobato, Kathmandu', 'phone_no': '9865011220', 'section_id': 300003},
        {'student_id': 400003, 'name': 'Sinjo Watanabe', 'dob': '2002-06-09', 'address': 'Hokkaido, Japan', 'phone_no': '9813355679', 'section_id': 300002},
        {'student_id': 400004, 'name': 'Kenichi Suga', 'dob': '1999-07-19', 'address': 'Tokyo, Japan', 'phone_no': '9800699123', 'section_id': 300001}
    ]

    table_dict = {
        program: program_list,
        semester: semester_list,
        course: course_list,
        course_semester: course_semester_list,
        instructor: instructor_list,
        instructor_course: instructor_course_list,
        section: section_list,
        student: student_list
    }

    # execute all insert operations in a loop
    for (table, table_list) in table_dict.items():
        conn.execute(insert(table), table_list)


if __name__ == '__main__':
    # engine for connecting to database and performing operations
    engine = create_engine(DB_ADDRESS) # LMS = Learning Management System

    # inspector to inspect database elements
    inspector = inspect(engine)

    # create database schema
    create_schema(engine)

    # insert data into the database
    insert_initial_records(engine)


