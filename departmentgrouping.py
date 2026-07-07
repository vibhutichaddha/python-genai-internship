students = [
    {"name":"Alice","dept":"CSE"},
    {"name":"Bob","dept":"ECE"},
    {"name":"John","dept":"CSE"}]
grouped_students = {}
for student in students:
    dept = student["dept"]
    if dept not in grouped_students:
        grouped_students[dept] = []
    grouped_students[dept].append(student["name"])
    print(grouped_students)