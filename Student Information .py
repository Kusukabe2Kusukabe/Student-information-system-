students = {}

while True:
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':  # Add Student
        student_id = input("Enter Student ID: ")
        if student_id in students:
            print("Student ID already exists.")
        else:
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Student Grade: ")
            students[student_id] = {'name': name, 'age': age, 'grade': grade}
            print(f"Student {name} added successfully.")

    elif choice == '2':  # View Students
        if not students:
            print("No students found.")
        else:
            for student_id in students:
                info = students[student_id]
                print(f"ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")

    elif choice == '3':  # Update Student
        student_id = input("Enter Student ID to update: ")
        if student_id in students:
            for field in ['name', 'age', 'grade']:
                new_value = input(f"Enter new {field} (leave blank to keep current): ")
                if new_value:
                    students[student_id][field] = new_value
            print(f"Student ID {student_id} updated successfully.")
        else:
            print("Student ID not found.")

    elif choice == '4':  # Delete Student
        student_id = input("Enter Student ID to delete: ")
        if student_id in students:
            del students[student_id]
            print(f"Student ID {student_id} deleted successfully.")
        else:
            print("Student ID not found.")

    elif choice == '5':  # Exit
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")