from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QListWidget
)

from src.data_handler import save_record
from src.gpa_calculator import calculate_gpa
from src.charts_window import ChartsWindow
from src.semester_manager import Semester, StudentAcademicRecord
from src.academic_classifier import (
    semester_pass_fail,
    classify_degree,
    academic_remark
)


class CourseWindow(QWidget):
    """
    Full academic management window:
    - Course entry
    - Semester tracking
    - GPA & CGPA computation
    - Academic classification
    - Performance visualization
    """

    def __init__(self, student_name, matric):
        super().__init__()

        self.student_name = student_name
        self.matric = matric

        # Temporary storage
        self.grades = []
        self.units = []

        # Academic tracking
        self.academic_record = StudentAcademicRecord()
        self.current_semester = None

        self.setWindowTitle("Student Academic Management System")
        self.setGeometry(250, 120, 560, 680)

        layout = QVBoxLayout()

        # Student Info
        layout.addWidget(QLabel(f"Student Name: {student_name}"))
        layout.addWidget(QLabel(f"Matric Number: {matric}"))

        # Semester Section
        layout.addWidget(QLabel("Semester Name"))
        self.semester_input = QLineEdit()
        self.semester_input.setPlaceholderText(
            "e.g First Semester 2024/2025"
        )
        layout.addWidget(self.semester_input)

        self.start_semester_btn = QPushButton("Start New Semester")
        self.start_semester_btn.clicked.connect(self.start_new_semester)
        layout.addWidget(self.start_semester_btn)

        # Course Inputs
        layout.addWidget(QLabel("Course Code"))
        self.course_input = QLineEdit()
        self.course_input.setPlaceholderText("e.g ICT323")
        layout.addWidget(self.course_input)

        layout.addWidget(QLabel("Course Unit"))
        self.unit_input = QLineEdit()
        self.unit_input.setPlaceholderText("e.g 3")
        layout.addWidget(self.unit_input)

        layout.addWidget(QLabel("Grade (A - F)"))
        self.grade_input = QLineEdit()
        self.grade_input.setPlaceholderText("A, B, C, D, E or F")
        layout.addWidget(self.grade_input)

        self.add_button = QPushButton("Add Course")
        self.add_button.clicked.connect(self.add_course)
        layout.addWidget(self.add_button)

        # Course List
        layout.addWidget(QLabel("Courses Entered"))
        self.course_list = QListWidget()
        layout.addWidget(self.course_list)

        # Result Button
        self.result_button = QPushButton(
            "Calculate GPA, CGPA & View Analytics"
        )
        self.result_button.clicked.connect(self.calculate_student_gpa)
        layout.addWidget(self.result_button)

        self.setLayout(layout)

    def start_new_semester(self):
        semester_name = self.semester_input.text().strip()

        if not semester_name:
            QMessageBox.warning(
                self,
                "Input Error",
                "Please enter a semester name."
            )
            return

        self.current_semester = Semester(semester_name)
        self.grades.clear()
        self.units.clear()
        self.course_list.clear()

        QMessageBox.information(
            self,
            "Semester Started",
            f"{semester_name} started successfully."
        )

    def add_course(self):
        if not self.current_semester:
            QMessageBox.warning(
                self,
                "Semester Error",
                "Start a semester before adding courses."
            )
            return

        course = self.course_input.text().strip()
        grade = self.grade_input.text().strip().upper()

        try:
            unit = int(self.unit_input.text())
        except ValueError:
            QMessageBox.warning(
                self,
                "Input Error",
                "Course unit must be numeric."
            )
            return

        if not course or grade not in ["A", "B", "C", "D", "E", "F"]:
            QMessageBox.warning(
                self,
                "Input Error",
                "Invalid course code or grade."
            )
            return

        save_record(
            self.student_name,
            self.matric,
            course,
            unit,
            grade
        )

        self.grades.append(grade)
        self.units.append(unit)
        self.current_semester.add_course(course, unit, grade)

        self.course_list.addItem(
            f"{course} | Unit: {unit} | Grade: {grade}"
        )

        self.course_input.clear()
        self.unit_input.clear()
        self.grade_input.clear()

    def calculate_student_gpa(self):
        if not self.grades:
            QMessageBox.warning(
                self,
                "Calculation Error",
                "No courses entered."
            )
            return

        gpa = calculate_gpa(self.grades, self.units)

        self.current_semester.set_gpa(gpa)
        self.academic_record.add_semester(self.current_semester)

        cgpa = self.academic_record.calculate_cgpa()

        semester_status = semester_pass_fail(gpa)
        degree_class = classify_degree(cgpa)
        remark = academic_remark(cgpa)

        QMessageBox.information(
            self,
            "Academic Summary",
            f"Semester GPA: {gpa}\n"
            f"Semester Status: {semester_status}\n\n"
            f"Current CGPA: {cgpa}\n"
            f"Degree Classification: {degree_class}\n"
            f"Remark: {remark}"
        )

        # Prepare CGPA trend data
        semester_labels = [
            sem.semester_name for sem in self.academic_record.semesters
        ]
        cgpa_values = []
        running_total = 0

        for i, sem in enumerate(self.academic_record.semesters, start=1):
            running_total += sem.gpa
            cgpa_values.append(round(running_total / i, 2))

        # Open analytics window
        self.charts_window = ChartsWindow(
            self.grades,
            semester_labels,
            cgpa_values
        )
        self.charts_window.show()
