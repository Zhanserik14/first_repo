# Напишите программу, в которой предлагается вводить учащихся различных груп, 
# посещающих секции по программированию. 
# Требуется упорядочить список повозрастанию классов. 
# Распечатать список фамилий и классов. 
students = []

while True:
    student = input("Enter a student name and class (or 'q' to quit): ")
    if student == 'q':
        break
    student_name, student_class = student.split()
    students.append((student_name, int(student_class)))

students.sort(key=lambda x: x[1])
sorted(students)

for student in students:
    print("Name: {} Class: {}".format(student[0], student[1]))