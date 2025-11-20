student_data = {
    "Ankur": 98,
    "Sakshi": 95,
    "Paras": 89,
    "Arpit": 78,
    "Shruti": 93,
    "Alice": 85,
}

user_input = input("Enter the student's name: ").title()
if user_input in student_data:
    print(f"{user_input}'s marks: {student_data[user_input]}")
else:
    print("Student not found.")