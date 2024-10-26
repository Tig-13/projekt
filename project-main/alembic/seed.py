from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Group, Teacher, Course, Student, Grade
from faker import Faker
import random

fake = Faker()
engine = create_engine('postgresql://user:password@localhost/dbname')
Session = sessionmaker(bind=engine)
session = Session()

# Создание групп
groups = [Group(group_name=f'Group {chr(65 + i)}') for i in range(3)]
session.add_all(groups)

# Создание преподавателей
teachers = [Teacher(first_name=fake.first_name(), last_name=fake.last_name()) for _ in range(5)]
session.add_all(teachers)

# Создание курсов
courses = [Course(course_name=name, teacher=random.choice(teachers)) for name in ['Math', 'History', 'Physics', 'Art']]
session.add_all(courses)

# Создание студентов и оценок
students = [Student(first_name=fake.first_name(), last_name=fake.last_name(), group=random.choice(groups)) for _ in range(30)]
session.add_all(students)
session.commit()

for student in students:
    for course in courses:
        for _ in range(random.randint(1, 3)):
            grade = Grade(student=student, course=course, grade=random.uniform(1, 10), date_assigned=fake.date_this_year())
            session.add(grade)

session.commit()
session.close()
