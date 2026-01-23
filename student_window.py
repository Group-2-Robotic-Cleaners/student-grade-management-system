from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from semester_manager import SemesterManager
from course_window import CourseWindow


class StudentWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Grade Management System")
        self.setGeometry(300, 200, 400, 300)

        self.name_input = QLineEdit()
        self.matric_input = QLineEdit()
        self.semester_input = QLineEdit()

        self.start_btn = QPushButton("Proceed to Course Entry")
        self.start_btn.clicked.connect(self.open_course_window)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Student Name"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Matric Number"))
        layout.addWidget(self.matric_input)

        layout.addWidget(QLabel("Semester (e.g. First Semester 2024/2025)"))
        layout.addWidget(self.semester_input)

        layout.addWidget(self.start_btn)
        self.setLayout(layout)

        # 🔑 ONE manager for ALL semesters
        self.semester_manager = SemesterManager()

    def open_course_window(self):
        if not self.name_input.text() or not self.matric_input.text():
            QMessageBox.warning(self, "Error", "All fields are required")
            return

        self.course_window = CourseWindow(
            self.name_input.text(),
            self.matric_input.text(),
            self.semester_input.text(),
            self.semester_manager
        )
        self.course_window.show()
