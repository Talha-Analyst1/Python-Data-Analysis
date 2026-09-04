#(stats calculator project)

import numpy as np
students_marks=np.array([90,80,70,60,50,40,30,20,95,85])
print(np.sum(students_marks))
print(np.min(students_marks))
print(np.max(students_marks))
print(np.mean(students_marks))
#average check
average=np.mean(students_marks)
if average>=80:
    print("Good performance")
else:
    print("Need improvement")
#sum check
sum=np.sum(students_marks)
if sum>=100:
    print("Good")
else:
    print("O shit not good")
#min check
lowest=np.min(students_marks)
if lowest<20:
    print("OK")
else:
    "No ok"
#max check
highest=np.max(students_marks)
if highest>99:
    print("Improver")
else:
    print("Nice")

