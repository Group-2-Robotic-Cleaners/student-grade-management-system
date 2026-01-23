def total_score(exam, test, attendance, project, quiz):
    return exam + test + attendance + project + quiz

def score_to_grade(score):
    if score >= 70: return "A"
    if score >= 60: return "B"
    if score >= 50: return "C"
    if score >= 45: return "D"
    if score >= 40: return "E"
    return "F"

def grade_point(grade):
    return {"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}[grade]
