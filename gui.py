from PyQt5.QtWidgets import QApplication
import sys
from student_window import StudentWindow

def run_app():
    app = QApplication(sys.argv)
    window = StudentWindow()
    window.show()
    sys.exit(app.exec_())
