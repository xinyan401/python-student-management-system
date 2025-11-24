# 2.1 Add Student
# -------------------------
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    cgpa = input("Enter CGPA: ")

    student = {
        "name": name,
        "cgpa": cgpa
    }

    students.append(student)
    print("Student added successfully.\n")



# 2.2 View Students

def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No student records found.\n")
        return

    for i, s in enumerate(students):
        print(f"{i+1}. Name: {s['name']}, CGPA: {s['cgpa']}")
    print()



# 2.3 Delete Student

def delete_student():
    print("\n--- Delete Student ---")
    view_students()

    if len(students) == 0:
        return

    choice = int(input("Enter the student number to delete: "))

    if 1 <= choice <= len(students):
        students.pop(choice - 1)
        print("Student deleted successfully.\n")
    else:
        print("Invalid choice.\n")


# Main Menu (Simple CRUD)

def main():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_student()
        elif option == "2":
            view_students()
        elif option == "3":
            delete_student()
        elif option == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.\n")


# Run the program
main()
