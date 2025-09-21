"""
-University Management System-
-person.py-

Defines the base Person class, Staff class, and SecureStudentRecord class 
used for GPA and course data management with encapsulation and validation.

"""

class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def get_responsibilities(self):
        return "General University member "

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (ID: {self.person_id})"


class Staff(Person):
    def __init__(self, name, person_id, role):
        super().__init__(name, person_id)
        self.role = role

    def get_responsibilities(self):
        return f"Staff Role: {self.role}"


class SecureStudentRecord:
    def __init__(self):
        self.__gpa = 0.0                    
        self.__enrolled_courses = []

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            raise ValueError(" GPA must be between 0 and 4")

    def add_course(self, course):
        if len(self.__enrolled_courses) > 5:
            raise ValueError("Enrollment limit is exceeded (max 5 courses)")
        self.__enrolled_courses.append(course)

    def get_courses(self):
        return list(self.__enrolled_courses)
