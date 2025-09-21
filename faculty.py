"""
-University Management System-
-faculty.py-

Defines the Faculty base class and its subclasses Professor, Lecturer, 
and TA (Teaching Assistant). Demonstrates polymorphism with workload 
and responsibility differences.

"""


from person import Person


class Faculty(Person):
    def __init__(self, name, person_id, department):
        super().__init__(name, person_id)
        self.department = department
        self.courses_assigned = []

    def assign_course(self, course):
        if course not in self.courses_assigned:
            self.courses_assigned.append(course)

    def calculate_workload(self):
        return len(self.courses_assigned)

    def get_responsibilities(self):
        return "Teach assigned courses, advise students, participate in department activities."


class Professor(Faculty):

    def __init__(self, name, person_id, department, research_area=None):
        super().__init__(name, person_id, department)
        self.research_area = research_area

    def calculate_workload(self):
        return len(self.courses_assigned)

    def get_responsibilities(self):
        return "Professors focus on teaching, mentoring, research and publishing"


class Lecturer(Faculty):
    def calculate_workload(self):
        return len(self.courses_assigned)

    def get_responsibilities(self):
        return "Lecturers focus on delivering lectures, preparing course materials and grading assignments"


class TA(Faculty):
    def calculate_workload(self):
        return max(1, len(self.courses_assigned))

    def get_responsibilities(self):
        return "Teaching assistent assist to students"
