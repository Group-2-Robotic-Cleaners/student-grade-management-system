import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from src.course_window import CourseWindow


class StudentGradeApp(QMainWindow):
    """
    Main GUI window for Student Grade Management System.
    Collects student basic details before moving to course entry.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Grade Management System")
        self.setGeometry(300, 200, 500, 300)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QVBoxLayout()

        # Title
        title = QLabel("Student Registration")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # Student Name
        layout.addWidget(QLabel("Student Name"))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        # Matric Number
        layout.addWidget(QLabel("Matric Number"))
        self.matric_input = QLineEdit()
        layout.addWidget(self.matric_input)

        # Proceed Button
        self.proceed_button = QPushButton("Proceed to Course Entry")
        self.proceed_button.clicked.connect(self.validate_inputs)
        layout.addWidget(self.proceed_button)

        central_widget.setLayout(layout)

    def validate_inputs(self):
        """
        Validates name and matric number,
        then opens the course & grade entry window.
        """
        name = self.name_input.text().strip()
        matric = self.matric_input.text().strip()

        if not name or not matric:
            QMessageBox.warning(
                self,
                "Input Error",
                "Please enter both Student Name and Matric Number."
            )
            return

        # Open Course Window
        self.course_window = CourseWindow(name, matric)
        self.course_window.show()

        # Close this window
        self.close()


def run_app():
    """
    Application entry point.
    """
    app = QApplication(sys.argv)
    window = StudentGradeApp()
    window.show()
    sys.exit(app.exec_())
