import numpy as np

# Mapping letter grades to grade points
GRADE_POINTS = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

def calculate_gpa(grades, units):
    """
    Calculates GPA using NumPy arrays
    """
    grade_points = np.array([GRADE_POINTS[g] for g in grades])
    course_units = np.array(units)

    total_points = np.sum(grade_points * course_units)
    total_units = np.sum(course_units)

    if total_units == 0:
        return 0.0

    gpa = total_points / total_units
    return round(gpa, 2)
