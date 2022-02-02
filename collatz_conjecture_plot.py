from matplotlib import pyplot as plt
import sys

if len(sys.argv) > 1:
    number = int(sys.argv[1])
else:
    number = 7

startnum = number
yaxis = []

while True:
    yaxis.append(int(number))

    if number == 1:
        break
    elif number % 2 == 0:
        number /= 2
    else:
        number = number * 3 + 1

print("finish!")            
print(yaxis)

plt.plot(yaxis)
plt.title("Collatz conjecture graph starts with " + str(startnum))  
plt.show()
