from matplotlib import pyplot as plt

xaxis = []
yaxis = []
for x in range(3):
    xaxis.append(x + 1)
    yaxis.append(pow(x + 1, 2))

print(xaxis)
print(yaxis)

plt.plot(xaxis,yaxis)
plt.title("Line graph")  
plt.ylabel('Y axis')  
plt.xlabel('X axis')
plt.show()
