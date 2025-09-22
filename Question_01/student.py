"""
-University Management System-
-student.py-

Defines the Student base class and its subclasses UndergraduateStudent 
and GraduateStudent. 


"""

from Question_01.person import Person, SecureStudentRecord
import datetime


def get_default_semester():                  # get the current semester
    month = datetime.datetime.now().month
    if 1 <= month <= 4:
        return "First Semester"
    elif 5 <= month <= 8:
        return "Mid Semester"
    else:
        return "Final Semester"


class Student(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.record = SecureStudentRecord()
        self.grades = {}                         # course ---> grade points
        self.semesters = {}                      # semester ---> {course: grade}


    def enroll_course(self, course, semester = None):
        self.record.add_course(course)
        if semester is None:
            semester = get_default_semester()
        if semester not in self.semesters:
            self.semesters[semester] = {}
        self.semesters[semester][course] = None

    def drop_course(self, course, semester= None):
        if semester in self.semesters and course in self.semesters[semester]:
            del self.semesters[semester][course]

    def set_grade(self, course, grade_point, semester = None):
        if semester in self.semesters and course in self.semesters[semester]:
            self.semesters[semester][course] = grade_point

    def calculate_gpa(self):
        total_points = 0
        total_courses = 0
        for semester_courses in self.semesters.values():
            for grade in semester_courses.values():
                if grade is not None:
                    total_points += grade
                    total_courses += 1
        gpa = round(total_points / total_courses, 2) if total_courses > 0 else 3.0
        self.record.set_gpa(gpa)
        return gpa

    def get_academic_status(self):
        gpa = self.record.get_gpa()
        if gpa >= 3.7:
            return "1st Class"
        elif  3.7 > gpa >= 3.3:
            return "Second Class Upper Division"
        elif  3.3 > gpa >= 3.0:
            return "Second Class Lower Division"
        else:
            return "General Class"

    def get_responsibilities(self):
        return "Attend classes everyday, complete assignments, complete modules"


class UndergraduateStudent(Student):
    def get_responsibilities(self):
        return "Undergraduate student responsibilities"


class GraduateStudent(Student):
    def get_responsibilities(self):
        return "Graduate student responsibilities"
