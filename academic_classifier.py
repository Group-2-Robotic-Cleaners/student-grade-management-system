"""
Handles academic classification logic:
- Pass / Fail determination
- Degree classification
- Academic remarks
"""


def semester_pass_fail(gpa):
    """
    Determines whether a student passed a semester.
    """
    if gpa >= 1.0:
        return "PASS"
    return "FAIL"


def classify_degree(cgpa):
    """
    Classifies degree based on CGPA.
    Nigerian university standard is assumed.
    """
    if cgpa >= 4.50:
        return "First Class"
    elif cgpa >= 3.50:
        return "Second Class Upper"
    elif cgpa >= 2.40:
        return "Second Class Lower"
    elif cgpa >= 1.50:
        return "Third Class"
    elif cgpa >= 1.00:
        return "Pass Degree"
    else:
        return "Fail"


def academic_remark(cgpa):
    """
    Provides textual academic remarks.
    """
    if cgpa >= 4.50:
        return "Excellent academic performance."
    elif cgpa >= 3.50:
        return "Very good performance. Keep it up."
    elif cgpa >= 2.40:
        return "Good performance. You can improve."
    elif cgpa >= 1.50:
        return "Fair performance. Needs improvement."
    elif cgpa >= 1.00:
        return "Weak performance. Academic probation advised."
    else:
        return "Poor performance. Immediate academic intervention required."
