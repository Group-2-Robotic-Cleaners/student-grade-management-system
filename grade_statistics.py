"""
Computes grade frequency for visualization
"""

class GradeStatistics:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def distribution(self):
        stats = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}
        for g in self.grades:
            if g in stats:
                stats[g] += 1
        return stats
