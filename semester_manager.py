"""
Handles multi-semester GPA and CGPA management
"""

class SemesterManager:
    def __init__(self):
        # semester_name -> list of (unit, grade_point)
        self.semesters = {}

    def add_course(self, semester, unit, grade_point):
        if semester not in self.semesters:
            self.semesters[semester] = []
        self.semesters[semester].append((unit, grade_point))

    def semester_gpa(self, semester):
        records = self.semesters.get(semester, [])
        total_units = sum(u for u, _ in records)
        if total_units == 0:
            return 0
        return sum(u * gp for u, gp in records) / total_units

    def cgpa(self):
        total_units = 0
        total_points = 0
        for records in self.semesters.values():
            for unit, gp in records:
                total_units += unit
                total_points += unit * gp
        return round(total_points / total_units, 2) if total_units else 0

    def gpa_trend(self):
        # returns semester -> GPA
        trend = {}
        for sem in self.semesters:
            trend[sem] = round(self.semester_gpa(sem), 2)
        return trend
