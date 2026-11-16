# from calculate import add, multiply, divide, subtract
# from student_utils import marks, student_details

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(f"Addition: {add(a,b)}")
# print(f"Subtraction: {subtract(a,b)}")      
# print(f"Multiplication: {multiply(a,b)}")
# print(f"Division: {divide(a,b):.2f}")


from student_utils.marks import (
    calculate_total,
    calculate_average,
    calculate_grade
)

from student_utils.student_details import display_student


def main():
    name = "Shivani"
    roll_no = 101
    course = "Data Science"

    marks = [85, 90, 78, 92, 88]

    print("===== STUDENT REPORT =====")

    display_student(name, roll_no, course)

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
