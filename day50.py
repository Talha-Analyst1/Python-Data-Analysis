#line chart
import matplotlib.pyplot as plt
students=["ali","ahad","alisha"]
marks=[20,40,45]
plt.plot(students,marks)
plt.show()

#PIE CHART

catagory=["Electronics","Fnance"]
value=[60,40]
plt.pie(value, labels=catagory)
plt.show()