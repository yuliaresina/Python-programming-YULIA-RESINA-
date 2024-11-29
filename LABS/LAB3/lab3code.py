import numpy as np
import matplotlib.pyplot as plt
import csv

x_values, y_values, labels = [], [], []
#Equation for the line that divides the points: y = kx + m from given example
k=-1
m=0
line = {'y=-x': (-1,0)}

def classify_data(x, y, k, m):
  return 1 if y > k * x + m else 0

with open("./unlabelled_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
   
    for row in csv_reader:
        x, y = float(row[0]), float(row[1])
         
        label = classify_data(x, y, k, m)
        labels.append(label)
       
        x_values.append(x)
        y_values.append(y)
        data=zip(x_values, y_values, labels)

with open("labelled_data.csv", 'w', newline='') as f_write:
    csv_writer = csv.writer(f_write)
 
    for row in data:
        csv_writer.writerow(row)

#x0, y0-->data with label 0, x1, y1-->data with label 1, xli, yli-->line data

x_values=np.array(x_values)
y_values=np.array(y_values)
xli = list(range(-4, 5))
yli = [k * xli + m for xli in xli]

x0= [x_values[i] for i in range(len(x_values)) if labels[i] == 0]
y0 = [y_values[i] for i in range(len(y_values)) if labels[i] == 0]
x1 = [x_values[i] for i in range(len(x_values)) if labels[i] == 1]
y1 = [y_values[i] for i in range(len(y_values)) if labels[i] == 1]
      


plt.scatter (x0, y0, color='pink', label='below line (0)')
plt.scatter (x1, y1, color='blue', label='above line (1)')
plt.plot(xli, yli, color='black', label='y=-x')
plt.plot
plt.title (f"Linear classification")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


