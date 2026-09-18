from student import Student


def main():

    # Create student objects
    student1 = Student(
        "Arif",
        "arif@gmail.com",
        "S001",
        "Python",
        [80, 85, 90]
    )

    student2 = Student(
        "Rahul",
        "rahul@gmail.com",
        "S002",
        "Data Science",
        [75, 80, 85]
    )

    student3 = Student(
        "Priya",
        "priya@gmail.com",
        "S003",
        "Machine Learning",
        [90, 95, 92]
    )

    # Display all students
    print("\n================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("================================")

    student1.display_details()
    student2.display_details()
    student3.display_details()

    # Calculate average marks
    print("\n----- Average Marks -----")

    print("Arif Average  :", student1.calculate_average())
    print("Rahul Average :", student2.calculate_average())
    print("Priya Average :", student3.calculate_average())

    # Update marks
    print("\n----- Update Marks -----")

    print("Updating Arif's marks...")
    student1.update_marks([90, 92, 95])

    print("Arif's New Marks :", student1.marks)
    print("Arif's New Average :", student1.calculate_average())

    # Total students
    print("\n----- Student Count -----")
    print(
        "Total Students :",
        Student.get_total_students()
    )


if __name__ == "__main__":
    main()