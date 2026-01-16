import pandas as pd
import os

DATA_FILE = "data/students.csv"

def initialize_file():
    """
    Creates the CSV file with headers if it does not exist
    """
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        df = pd.DataFrame(
            columns=["Name", "Matric", "Course", "Unit", "Grade"]
        )
        df.to_csv(DATA_FILE, index=False)

def save_record(name, matric, course, unit, grade):
    """
    Saves a student's course record to CSV using Pandas
    """
    initialize_file()  # <-- IMPORTANT FIX

    df = pd.read_csv(DATA_FILE)

    new_row = {
        "Name": name,
        "Matric": matric,
        "Course": course,
        "Unit": unit,
        "Grade": grade
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def load_student(matric):
    """
    Loads all records for a particular student
    """
    initialize_file()
    df = pd.read_csv(DATA_FILE)
    return df[df["Matric"] == matric]
