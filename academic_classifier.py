"""
Handles CGPA classification and academic remarks
"""

class AcademicClassifier:
    def __init__(self, cgpa: float):
        self.cgpa = round(cgpa, 2)

    def degree_class(self):
        if self.cgpa >= 4.50:
            return "First Class"
        elif self.cgpa >= 3.50:
            return "Second Class Upper"
        elif self.cgpa >= 2.40:
            return "Second Class Lower"
        elif self.cgpa >= 1.50:
            return "Third Class"
        else:
            return "Pass"

    def remark(self):
        if self.cgpa >= 4.50:
            return "Excellent academic performance"
        elif self.cgpa >= 3.50:
            return "Very good performance"
        elif self.cgpa >= 2.40:
            return "Good performance"
        elif self.cgpa >= 1.50:
            return "Fair performance, more effort needed"
        else:
            return "Poor performance, academic probation advised"

    def full_summary(self):
        return {
            "CGPA": self.cgpa,
            "Degree Class": self.degree_class(),
            "Remark": self.remark()
        }
