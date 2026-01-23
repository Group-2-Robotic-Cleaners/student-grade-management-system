from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QComboBox
)
import csv

from score_validator import validate_scores
from gpa_calculator import total_score, score_to_grade, grade_point
from grade_statistics import GradeStatistics
from charts_window import ChartsWindow


class CourseWindow(QWidget):
    def __init__(self, name, matric, semester, semester_manager):
        super().__init__()

        self.name = name
        self.matric = matric
        self.current_semester = semester
        self.semester_manager = semester_manager
        self.grade_stats = GradeStatistics()
        self.registered_courses = []

        self.setWindowTitle("Course & Semester Management")
        self.setGeometry(350, 150, 480, 620)

        # Inputs
        self.semester_input = QLineEdit(self.current_semester)
        self.course_input = QLineEdit()
        self.unit_input = QLineEdit()
        self.exam_input = QLineEdit()
        self.test_input = QLineEdit()
        self.attendance_input = QLineEdit()
        self.project_input = QLineEdit()
        self.quiz_input = QLineEdit()

        self.course_dropdown = QComboBox()
        self.course_dropdown.addItem("Registered Courses")

        # Buttons
        self.add_course_btn = QPushButton("Add Course")
        self.add_course_btn.clicked.connect(self.save_course)

        self.change_semester_btn = QPushButton("Switch / Add Semester")
        self.change_semester_btn.clicked.connect(self.change_semester)

        self.chart_btn = QPushButton("View Charts & CGPA")
        self.chart_btn.clicked.connect(self.show_charts)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Current Semester"))
        layout.addWidget(self.semester_input)

        layout.addWidget(QLabel("Course Code"))
        layout.addWidget(self.course_input)

        layout.addWidget(QLabel("Course Unit"))
        layout.addWidget(self.unit_input)

        layout.addWidget(QLabel("Exam (70)"))
        layout.addWidget(self.exam_input)

        layout.addWidget(QLabel("Test (10)"))
        layout.addWidget(self.test_input)

        layout.addWidget(QLabel("Attendance (5)"))
        layout.addWidget(self.attendance_input)

        layout.addWidget(QLabel("Project (10)"))
        layout.addWidget(self.project_input)

        layout.addWidget(QLabel("Quiz (5)"))
        layout.addWidget(self.quiz_input)

        layout.addWidget(self.add_course_btn)
        layout.addWidget(QLabel("Registered Courses"))
        layout.addWidget(self.course_dropdown)
        layout.addWidget(self.change_semester_btn)
        layout.addWidget(self.chart_btn)

        self.setLayout(layout)

    def change_semester(self):
        new_sem = self.semester_input.text().strip()
        if not new_sem:
            QMessageBox.warning(self, "Error", "Semester cannot be empty")
            return

        self.current_semester = new_sem
        self.registered_courses.clear()
        self.course_dropdown.clear()
        self.course_dropdown.addItem("Registered Courses")

        QMessageBox.information(
            self,
            "Semester Changed",
            f"Now recording courses for {new_sem}"
        )

    def save_course(self):
        try:
            course_code = self.course_input.text().strip().upper()
            if course_code in self.registered_courses:
                QMessageBox.warning(self, "Duplicate", "Course already added")
                return

            exam = int(self.exam_input.text())
            test = int(self.test_input.text())
            attendance = int(self.attendance_input.text())
            project = int(self.project_input.text())
            quiz = int(self.quiz_input.text())
            unit = int(self.unit_input.text())

            validate_scores(exam, test, attendance, project, quiz)

            total = total_score(exam, test, attendance, project, quiz)
            grade = score_to_grade(total)
            gp = grade_point(grade)

            # save across semesters
            self.semester_manager.add_course(self.current_semester, unit, gp)
            self.grade_stats.add_grade(grade)

            with open("data/students.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    self.name,
                    self.matric,
                    self.current_semester,
                    course_code,
                    unit,
                    exam,
                    test,
                    attendance,
                    project,
                    quiz,
                    total,
                    grade,
                    "PASS" if grade != "F" else "FAIL"
                ])

            self.registered_courses.append(course_code)
            self.course_dropdown.addItem(course_code)

            QMessageBox.information(self, "Saved", "Course added successfully")

            for field in [
                self.course_input, self.unit_input, self.exam_input,
                self.test_input, self.attendance_input,
                self.project_input, self.quiz_input
            ]:
                field.clear()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_charts(self):
        cgpa = self.semester_manager.cgpa()
        trend = self.semester_manager.gpa_trend()
        stats = self.grade_stats.distribution()

        self.chart_window = ChartsWindow(cgpa, trend, stats)
        self.chart_window.show()
