from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ChartsWindow(QWidget):
    """
    Displays academic performance charts:
    - Grade distribution (bar chart)
    - CGPA trend across semesters (line chart)
    """

    def __init__(self, grades, semester_labels, cgpa_values):
        super().__init__()

        self.setWindowTitle("Academic Performance Analytics")
        self.setGeometry(300, 150, 700, 600)

        layout = QVBoxLayout()

        title = QLabel("Academic Performance Visualization")
        title.setStyleSheet("font-size:16px; font-weight:bold;")
        layout.addWidget(title)

        # Create matplotlib figure
        self.figure = Figure(figsize=(6, 5))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.plot_charts(grades, semester_labels, cgpa_values)

    def plot_charts(self, grades, semester_labels, cgpa_values):
        """
        Plots:
        1. Grade distribution
        2. CGPA trend across semesters
        """
        self.figure.clear()

        # -------- Grade Distribution --------
        ax1 = self.figure.add_subplot(211)
        grade_counts = {g: grades.count(g) for g in set(grades)}

        ax1.bar(
            grade_counts.keys(),
            grade_counts.values()
        )
        ax1.set_title("Grade Distribution")
        ax1.set_xlabel("Grade")
        ax1.set_ylabel("Count")

        # -------- CGPA Trend --------
        ax2 = self.figure.add_subplot(212)

        if cgpa_values:
            ax2.plot(
                semester_labels,
                cgpa_values,
                marker="o"
            )
            ax2.set_title("CGPA Trend Across Semesters")
            ax2.set_xlabel("Semester")
            ax2.set_ylabel("CGPA")
            ax2.set_ylim(0, 5)

        self.figure.tight_layout()
        self.canvas.draw()
