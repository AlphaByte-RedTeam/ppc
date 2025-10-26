student_db = {}  # database


def input_non_empty(prompt: str) -> str:
    """Input string yang tidak kosong"""
    while True:
        value = input(prompt)
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def compute_status(grade: int) -> str:
    """Balikin nilai Pass kalau nilainya lebih dari 75"""
    # cara 1
    # if grade >= 75:
    #     return "Pass"
    # else:
    #     return "Fail"

    # cara 2
    # if grade < 75:  # mulai dari case yang jeleknya dulu
    #     return "Fail"
    # return "Pass"

    # cara 3 -> exclusive cuma bisa dipakai di Python
    return "Pass" if grade >= 75 else "Fail"  # logic


def student_exists(id: str) -> bool:
    """Cek apakah ID siswa ada di database"""
    # cara 1: beginner
    # if id in students:
    #     return True
    # else:
    #     return False

    return id in student_db


def input_student_id(prompt: str) -> str:
    # student id harus 6 digit
    sid = ""
    while len(sid) != 6:
        print("Student ID must be 6 digits.")
        sid = input_non_empty(prompt)
    return sid


def add_student():
    sid = input_student_id("Enter student ID: ")

    if student_exists(sid):
        print(f"Student ID '{sid}' already exists.")
        return
    name = input_non_empty("Enter student name:")
    student_db[sid] = {"name": name, "grades": []}
    print(f"Student '{sid}-{name}' added.")


def delete_student():
    """To delete a student from the database"""
    sid = input_student_id("Enter student ID to delete: ")

    if not student_exists(sid):
        print(f"Student ID '{sid}' does not exist.")
        return

    del student_db[sid]
    print(f"Student '{sid}' deleted.")


def update_student():
    sid = input_student_id("Enter Student ID to update: ")

    if not student_exists(sid):
        print(f"Student ID '{sid}' does not exist.")
        return

    while True:
        print("\nUpdate Menu:")
        print("1) Update Name")
        print("2) Add or Update Subject Grade")
        print("3) Remove Subject")
        print("4) Show Student Details")
        print("5) Back to Main Menu")
        input_choice = input("Choose (1-5): ").strip()

        if input_choice == "1":
            new_name = input_non_empty("Enter new name: ")
            student_db[sid]["name"] = new_name
            print("Name updated.")
        elif input_choice == "2":
            subject = input_non_empty("Enter subject name: ")
            grade = input_int_in_range("Enter grade (0-100): ")
            updated = add_or_update_grade(sid, subject, grade)
            if updated == "updated":
                print(f"Updated {subject} grade to {grade}.")
            else:
                print(f"Added subject {subject} with grade {grade}.")
        elif input_choice == "3":
            remove_subject_flow(sid)
        elif input_choice == "4":
            display_report_for_student(sid)
        elif input_choice == "5":
            break
        else:
            print("Invalid choice. Please select 1-5.")
