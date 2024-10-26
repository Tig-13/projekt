from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func, desc
from models import Student, Grade, Course, Teacher, Group

engine = create_engine('postgresql://user:password@localhost/dbname')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(
        Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(course_name):
    return session.query(
        Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).join(Course).filter(Course.course_name == course_name)\
    .group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()

def select_3(course_name):
    return session.query(
        Group.group_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).join(Course).filter(Course.course_name == course_name)\
    .group_by(Group.id).all()

def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()

def select_5(teacher_name):
    return session.query(Course.course_name).join(Teacher)\
        .filter(func.concat(Teacher.first_name, ' ', Teacher.last_name) == teacher_name).all()

def select_6(group_name):
    return session.query(Student.first_name, Student.last_name).join(Group)\
        .filter(Group.group_name == group_name).all()

def select_7(group_name, course_name):
    return session.query(
        Student.first_name, Student.last_name, Grade.grade
    ).join(Group).join(Grade).join(Course)\
    .filter(Group.group_name == group_name, Course.course_name == course_name).all()

def select_8(teacher_name):
    return session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Course).join(Teacher)\
    .filter(func.concat(Teacher.first_name, ' ', Teacher.last_name) == teacher_name).scalar()

def select_9(student_name):
    return session.query(Course.course_name).join(Grade).join(Student)\
        .filter(func.concat(Student.first_name, ' ', Student.last_name) == student_name).distinct().all()

def select_10(student_name, teacher_name):
    return session.query(Course.course_name).join(Grade).join(Student).join(Teacher)\
        .filter(func.concat(Student.first_name, ' ', Student.last_name) == student_name)\
        .filter(func.concat(Teacher.first_name, ' ', Teacher.last_name) == teacher_name).all()
