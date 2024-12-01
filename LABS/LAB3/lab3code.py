import numpy as np
import matplotlib.pyplot as plt
import csv

x, y, labels = [], [], []
#Equation for the line that divides the points: y = kx + m from given example
k=-1
m=0


def classify_data(x1, y1, k, m):
  return 1 if y1 > k * x1 + m else 0

with open("./unlabelled_data.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')
   
    for row in csv_reader:
        x1, y1 = float(row[0]), float(row[1])
         
        label = classify_data(x1, y1, k, m)
        labels.append(label)
       
        x.append(x1)
        y.append(y1)
        data=zip(x, y, labels)

with open("labelled_data.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
 
    for row in data:
        csv_writer.writerow(row)

#x0, y0-->data with label 0, x1, y1-->data with label 1, xli, yli-->line data

x=np.array(x)
y=np.array(y)
xli = list(range(-4, 5))
yli = [k * xli + m for xli in xli]

x0= [x[i] for i in range(len(x)) if labels[i] == 0]
y0 = [y[i] for i in range(len(y)) if labels[i] == 0]
x1 = [x[i] for i in range(len(x)) if labels[i] == 1]
y1 = [y[i] for i in range(len(y)) if labels[i] == 1]
      


plt.scatter (x0, y0, color='pink', label='below line (0)')
plt.scatter (x1, y1, color='blue', label='above line (1)')
plt.plot(xli, yli, color='black', label='y=-x')
plt.plot
plt.title (f"Linear classification")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


