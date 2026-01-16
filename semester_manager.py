class Semester:
    """
    Represents a single academic semester.
    Stores courses, units, grades, and GPA.
    """

    def __init__(self, semester_name):
        self.semester_name = semester_name
        self.courses = []
        self.units = []
        self.grades = []
        self.gpa = 0.0

    def add_course(self, course, unit, grade):
        self.courses.append(course)
        self.units.append(unit)
        self.grades.append(grade)

    def set_gpa(self, gpa):
        self.gpa = gpa


class StudentAcademicRecord:
    """
    Tracks all semesters and calculates CGPA.
    """

    def __init__(self):
        self.semesters = []

    def add_semester(self, semester):
        self.semesters.append(semester)

    def calculate_cgpa(self):
        if not self.semesters:
            return 0.0

        total = sum(semester.gpa for semester in self.semesters)
        return round(total / len(self.semesters), 2)
