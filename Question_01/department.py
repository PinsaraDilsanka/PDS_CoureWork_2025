"""
-University Management System-
-department.py-

Defines the Department and Course classes for managing courses, 
faculty, and student enrollment with prerequisite checking.

"""

class Course:
    def __init__(self, course_code, name, max_enrollment=25, prerequisites=None):
        self.course_code = course_code
        self.name = name
        self.max_enrollment = max_enrollment
        self.enrolled_students = []
        self.prerequisites = prerequisites if prerequisites else []

    def enroll_student(self, student):
        if len(self.enrolled_students) >= self.max_enrollment:
            raise ValueError(f"Course {self.course_code} is full.")   # check the course enroll count
        
        for prereq in self.prerequisites:
            if prereq not in [c.course_code for c in student.record.get_courses()]:
                raise ValueError(f"Missing prerequisite: {prereq}")                  # check the prerequesites of the courses
        self.enrolled_students.append(student)
        student.enroll_course(self.course_code)

    def __str__(self):
        return f"{self.course_code} - {self.name}"


class Department:
    def __init__(self, name):
        self.name = name
        self.faculty = []
        self.courses = []

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def add_course(self, course):
        self.courses.append(course)

    def assign_faculty_to_course(self, faculty, course):
        if faculty not in self.faculty:
            raise ValueError("Faculty not in department")
        if course not in self.courses:
            raise ValueError("Course not in department")

        faculty.assign_course(course.name)      # update the faculty worlkload
        print(f"{faculty.name} assigned to teach {course.name}")

    def __str__(self):
        return f"Department of {self.name}"
