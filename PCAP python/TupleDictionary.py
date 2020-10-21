grade7 = {}

while True:
    student_name = input("Enter the student's name or type exit to stop:")
    if student_name == 'exit':
        break

    student_score = int(input("Enter the student's score (0-10):"))

    if student_name in grade7:
        grade7[student_name] += (student_score,)
    else:
        grade7[student_name] = (student_score,)

for student_name in sorted(grade7.keys()):
    adding = 0
    counter = 0
    for student_score in grade7[student_name]:
        adding += student_score
        counter += 1
    print(student_name, ":", adding/counter)