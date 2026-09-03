#(file handling)(read and write)

file=open("data.txt","w")
file.write("Python is look-like a snake")
file.close()

file=open("data.txt","r")
content=file.read()
print(content)
file.close()


file = open("students.txt", "w")
file.write("Talha,22,Faisalabad\n")
file.write("Ahmed,25,Lahore\n")
file.write("Sara,21,Karachi\n")
file.close()

file = open("students.txt", "r")
content = file.read()
print(content)
file.close()