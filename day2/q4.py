# -------------------------------
# GLOBAL CONSTANTS
# -------------------------------
# School and class details
SCHOOL_NAME = "New School Of Learning"
CLASS_NAME = "Class XI"

# Marks configuration
TOTAL_SUBJECT_MARKS = 50
TOTAL_MARKS = TOTAL_SUBJECT_MARKS * 3

# Number of students
NUMBER_STUDENTS = 3


# -------------------------------
# FUNCTION: PROCESS ONE STUDENT
# -------------------------------
def process_student(student_no):
    # ----- INPUT SECTION -----
    student = input(f"\nEnter name of student {student_no}: ")

    phys = int(input(f"Enter Physics marks out of 50 for student {student_no}: "))
    chem = int(input(f"Enter Chemistry marks out of 50 for student {student_no}: "))
    math = int(input(f"Enter Mathematics marks out of 50 for student {student_no}: "))

    # ----- CALCULATION SECTION -----
    total = phys + chem + math

    # Subject-wise percentages
    phys_perc = round((phys / TOTAL_SUBJECT_MARKS) * 100, 2)
    chem_perc = round((chem / TOTAL_SUBJECT_MARKS) * 100, 2)
    math_perc = round((math / TOTAL_SUBJECT_MARKS) * 100, 2)

    # Total percentage
    total_perc = round((total / TOTAL_MARKS) * 100, 2)

    # ----- OUTPUT SECTION (REPORT CARD) -----
    print(f"\n{SCHOOL_NAME} – {CLASS_NAME} – {student}")
    print("-" * 72)
    print(f"| {'Subject':^12} | {'Total Marks':^12} | {'Marks Obtained':^15} | {'Percentage':^10} |")
    print("-" * 72)

    print(f"| {'Physics':^12} | {TOTAL_SUBJECT_MARKS:^12} | {phys:^15} | {phys_perc:^10} |")
    print(f"| {'Chemistry':^12} | {TOTAL_SUBJECT_MARKS:^12} | {chem:^15} | {chem_perc:^10} |")
    print(f"| {'Mathematics':^12} | {TOTAL_SUBJECT_MARKS:^12} | {math:^15} | {math_perc:^10} |")

    print("-" * 72)
    print(f"| {'Total':^12} | {TOTAL_MARKS:^12} | {total:^15} | {total_perc:^10} |")
    print("-" * 72)

    # Return marks for class summary
    return phys, chem, math


# -------------------------------
# MAIN PROGRAM
# -------------------------------
# Store all students' marks


# Loop through each student
for i in range(1, NUMBER_STUDENTS + 1):
    marks = process_student(i)
    