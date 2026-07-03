students = {
"Alice":88,
"Bob":76,
"John":91,
"Emma":65
}
result = {
    name: marks 
    for name, marks in students.items() if marks >= 80
}
print(result)