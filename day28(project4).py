#(project on student names and marks)


def add_student():
    name = str(input("Enter student name: "))
    
    try:
        marks = int(input("Enter student marks: "))
    except:
        print("Invalid marks, using 0")
        marks = 0
    
    file = open("students.txt", "a")
    file.write(name + "," + str(marks) + "\n")
    file.close()

add_student()
add_student()
add_student()

file = open("students.txt", "r")
content = file.read()
print(content)
file.close()