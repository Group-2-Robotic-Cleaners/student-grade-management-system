from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
import matplotlib.pyplot as plt
from academic_classifier import AcademicClassifier

class ChartsWindow(QWidget):
    def __init__(self, cgpa, gpa_trend, grade_stats):
        super().__init__()
        self.setWindowTitle("Academic Performance Overview")
        self.setGeometry(400, 200, 500, 400)

        classifier = AcademicClassifier(cgpa)
        summary = classifier.full_summary()

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"CGPA: {summary['CGPA']}"))
        layout.addWidget(QLabel(f"Degree Class: {summary['Degree Class']}"))
        layout.addWidget(QLabel(f"Remark: {summary['Remark']}"))
        self.setLayout(layout)

        # GPA Trend Line Chart
        plt.figure(figsize=(5, 3))
        plt.plot(list(gpa_trend.keys()), list(gpa_trend.values()), marker='o')
        plt.title("CGPA Trend Across Semesters")
        plt.ylabel("GPA")
        plt.xlabel("Semester")
        plt.ylim(0, 5)
        plt.show()

        # Grade Distribution Chart
        plt.figure(figsize=(5, 3))
        plt.bar(grade_stats.keys(), grade_stats.values())
        plt.title("Grade Distribution")
        plt.ylabel("Number of Courses")
        plt.show()
