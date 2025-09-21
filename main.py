"""
- University Management System -
- Main program execution file -

This script demonstrates how different components of the University 
Management System interact with each other. It imports and uses 
the Person, Faculty, Department, Course, and Student classes.

Features shown in this script:
- Creating departments, faculty members, courses, and students.
- Enrolling students into courses and assigning grades.
- Assigning faculty members to courses through their departments.
- Calculating GPA and determining academic status of students.
- Displaying workloads and responsibilities of faculty and students.

Run this file to see a sample simulation of the system.
"""

from student import UndergraduateStudent, GraduateStudent
from faculty import Professor, Lecturer, TA
from person import Staff
from department import Department, Course

if __name__ == "__main__":

    # Create department
    cs_dept = Department("Computer Science")

    # Create courses
    course1 = Course("CS1001", "Introduction to Programming")
    course2 = Course("CS2001", "Advanced Programming techniques", prerequisites=["CS1001"])
    course3 = Course("CS2002", "Computational Programming", prerequisites=["CS1001"])
    course4 = Course("CS1005", "Data Visulization")
    course5 = Course("CS1101", "DataBase Management")
    cs_dept.add_course(course1)
    cs_dept.add_course(course2)
    cs_dept.add_course(course3)
    cs_dept.add_course(course4)
    cs_dept.add_course(course5)

    # Create faculty
    prof = Professor("Dr. Gayan", 506, "Computer Science")
    lecturer = Lecturer("Mr. Amila", 802, "Computer Science")
    ta = TA("Ayodhya", 1003, "Computer Science")
    cs_dept.add_faculty(prof)
    cs_dept.add_faculty(lecturer)
    cs_dept.add_faculty(ta)

    # Assign faculty
    cs_dept.assign_faculty_to_course(prof, course1)
    cs_dept.assign_faculty_to_course(prof, course2)
    cs_dept.assign_faculty_to_course(lecturer, course3)

    # Create students
    u_student = UndergraduateStudent("Pinsara Dilsanka", 6001)
    g_student = GraduateStudent("Sumudu Sanjaya", 6002)

    # Enroll students
    #course1.enroll_student(u_student)
    #course1.enroll_student(g_student)
    u_student.enroll_course(course1,"Mid Semester")
    g_student.enroll_course(course1,"Mid Semester")

    # Give grades
    u_student.set_grade(course1, 3.8,"Mid Semester")
    g_student.set_grade(course1, 3.1,"Mid Semester")

    # GPA Calculation
    print(f"{u_student.name} GPA: {u_student.calculate_gpa()} - {u_student.get_academic_status()}")
    print(f"{g_student.name} GPA: {g_student.calculate_gpa()} - {g_student.get_academic_status()}")

    # Show polymorphism
    people = [prof, lecturer, ta, u_student, g_student, Staff("Sumith", 3001, "Admin")]
    for p in people:
        print(f"{p} ----> {p.get_responsibilities()}")
