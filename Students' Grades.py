num_students = int(input())
students = {}

for _ in range(num_students):
    name, grade = input().split(' ')
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    grades = [f'{x:.2f}' for x in grades]
    print(f"{name} -> {' '.join(grades)} (avg: {average_grade:.2f})")
