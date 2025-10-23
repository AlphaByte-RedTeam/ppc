# student_report_system.py
# Student Report Management System
# Sekolah Coding Virya akt. 2025
# Menu-driven starter program with validation and error handling

import sys

students = {}  # structure: {student_id: {"name": str, "grades": [{"subject": str, "grade": int, "status": str}, ...]}}


def compute_status(grade: int) -> str:
    """Return 'Pass' if grade >= 75 else 'Fail'."""
    return "Pass" if grade >= 75 else "Fail"


def input_non_empty(prompt: str) -> str:
    """Prompt until the user enters a non-empty, non-whitespace string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def input_student_id(prompt: str) -> str:
    """Read a student ID (non-empty) and return the trimmed value."""
    return input_non_empty(prompt)


def input_int_in_range(prompt: str, min_val: int = 0, max_val: int = 100) -> int:
    """Prompt for an integer within [min_val, max_val], with validation."""
    while True:
        s = input(prompt).strip()
        try:
            val = int(s)
        except ValueError:
            print("Invalid number. Please enter an integer.")
            continue
        if val < min_val or val > max_val:
            print(f"Number must be between {min_val} and {max_val}.")
            continue
        return val


def student_exists(student_id: str) -> bool:
    return student_id in students


def add_student_flow():
    print("\n-- Add Student --")
    sid = input_student_id("Enter Student ID: ")
    if student_exists(sid):
        print(f"Error: Student ID '{sid}' already exists.")
        return
    name = input_non_empty("Enter Student Name: ")
    students[sid] = {"name": name, "grades": []}
    print(f"Student added successfully: {sid} - {name}")


def remove_student_flow():
    print("\n-- Remove Student --")
    sid = input_student_id("Enter Student ID to remove: ")
    if not student_exists(sid):
        print(f"Error: Student ID '{sid}' not found.")
        return
    confirm = input(f"Are you sure you want to remove {sid} - {students[sid]['name']}? (y/N): ").strip().lower()
    if confirm == "y":
        del students[sid]
        print("Student removed.")
    else:
        print("Operation cancelled.")


def update_student_flow():
    print("\n-- Update Student --")
    sid = input_student_id("Enter Student ID to update: ")
    if not student_exists(sid):
        print(f"Error: Student ID '{sid}' not found.")
        return

    while True:
        print("\nUpdate Menu:")
        print("1) Update Name")
        print("2) Add or Update Subject Grade")
        print("3) Remove Subject")
        print("4) Show Student Details")
        print("5) Back to Main Menu")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            new_name = input_non_empty("Enter new name: ")
            students[sid]["name"] = new_name
            print("Name updated.")
        elif choice == "2":
            subject = input_non_empty("Enter subject name: ")
            grade = input_int_in_range("Enter grade (0-100): ")
            updated = add_or_update_grade(sid, subject, grade)
            if updated == "updated":
                print(f"Updated {subject} grade to {grade}.")
            else:
                print(f"Added subject {subject} with grade {grade}.")
        elif choice == "3":
            remove_subject_flow(sid)
        elif choice == "4":
            display_report_for_student(sid)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select 1-5.")


def add_or_update_grade(student_id: str, subject: str, grade: int) -> str:
    """
    Add or update a subject grade for a student.
    Returns "added" or "updated".
    """
    if student_id not in students:
        raise KeyError("Student not found")

    grades_list = students[student_id]["grades"]
    for item in grades_list:
        if item["subject"].lower() == subject.lower():
            item["grade"] = grade
            item["status"] = compute_status(grade)
            return "updated"
    # not found -> append
    grades_list.append({"subject": subject, "grade": grade, "status": compute_status(grade)})
    return "added"


def remove_subject_flow(student_id=None):
    if student_id is None:
        sid = input_student_id("Enter Student ID: ")
        if not student_exists(sid):
            print(f"Error: Student ID '{sid}' not found.")
            return
    else:
        sid = student_id

    grades = students[sid]["grades"]
    if not grades:
        print("This student has no subjects.")
        return

    print("\nSubjects:")
    for idx, item in enumerate(grades, start=1):
        print(f"{idx}) {item['subject']} - {item['grade']} ({item['status']})")

    while True:
        choice = input("Enter the number of the subject to remove (or 'c' to cancel): ").strip().lower()
        if choice == "c":
            print("Cancelled.")
            return
        try:
            i = int(choice)
            if 1 <= i <= len(grades):
                removed = grades.pop(i - 1)
                print(f"Removed subject: {removed['subject']}")
                return
            else:
                print("Number out of range.")
        except ValueError:
            print("Please enter a valid number or 'c' to cancel.")


def display_student_report_flow():
    print("\n-- Display Student Report --")
    sid = input_student_id("Enter Student ID: ")
    if not student_exists(sid):
        print(f"Error: Student ID '{sid}' not found.")
        return
    display_report_for_student(sid)


def display_report_for_student(sid: str):
    record = students[sid]
    name = record["name"]
    grades = record["grades"]

    # Header
    print("\nStudent ID:", sid)
    print("Name:", name)
    print("\nReport:")
    print("=" * 24)
    print(f"{'Subjects':<12} | {'Grade':>5} | {'Status':>6}")
    print("=" * 24)

    fail_count = 0
    if not grades:
        print("(no subjects)")
    else:
        for item in grades:
            subj = item["subject"]
            grade = item["grade"]
            status = item["status"]
            if status.lower() == "fail":
                fail_count += 1
            print(f"{subj:<12} | {grade:>5} | {status:>6}")

    # Final report rule: FAIL if 2 or more fails
    final_status = "FAIL" if fail_count >= 2 else "PASS"
    print("\nFinal report:", final_status)
    print()  # blank line


def main_menu():
    while True:
        try:
            print("==========================")
            print("Student Report Management System")
            print("Sekolah Coding Virya akt. 2025")
            print("==========================")
            print("> A.) Add Student")
            print("> B.) Update Student")
            print("> C.) Remove Student")
            print("> D.) Display Student Report")
            print("> E.) Exit Program")
            choice = input("Choose an option (A-E): ").strip().upper()

            if choice == "A":
                add_student_flow()
            elif choice == "B":
                update_student_flow()
            elif choice == "C":
                remove_student_flow()
            elif choice == "D":
                display_student_report_flow()
            elif choice == "E":
                print("Goodbye!")
                break
            else:
                print("Invalid option, please choose A, B, C, D or E.")
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting.")
            break
        except Exception as e:
            # Catch-all to prevent crash; print friendly message and continue
            print(f"An unexpected error occurred: {e}")
            print("Returning to main menu.")


if __name__ == "__main__":
    # Optional: seed with sample data for quick testing (comment out if not needed)
    students["S2025-001"] = {
        "name": "Alice Putri",
        "grades": [
            {"subject": "Math", "grade": 78, "status": compute_status(78)},
            {"subject": "Bahasa", "grade": 60, "status": compute_status(60)},
            {"subject": "Science", "grade": 85, "status": compute_status(85)}
        ]
    }

    main_menu()
