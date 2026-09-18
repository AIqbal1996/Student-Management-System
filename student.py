class Student:

    # Class variable
    total_students = 0

    # Constructor
    def __init__(self, name, email, student_id, course, marks):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = marks

        Student.total_students += 1

    # Display student details
    def display_details(self):
        print("\n----- Student Details -----")
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Student ID :", self.student_id)
        print("Course     :", self.course)
        print("Marks      :", self.marks)

    # Update marks
    def update_marks(self, new_marks):
        self.marks = new_marks
        print("Marks updated successfully.")

    # Calculate average marks
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks) / len(self.marks)

    # Class method to get total students
    @classmethod
    def get_total_students(cls):
        return cls.total_students