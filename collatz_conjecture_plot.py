from matplotlib import pyplot as plt

number=27
count=0

xaxis=[]
yaxis=[]
time=1

while(True):
    xaxis.append(time)
    yaxis.append(number)
    time+=1
    print(number)   
    if(number==4):
        count+=1
        break
    elif(number%2==0):
        number/=2
    else:
        number=number*3+1

"""            
for num in range(1, number+1):
    while(True):
        if(num==4):
            count+=1
            break
        elif(num%2==0):
            num/=2
        else:
            num=num*3+1

"""

print("\nfinish!\n")            
#print(number-count)
print(xaxis)
print("\n")
print(yaxis)

plt.plot(xaxis,yaxis)
plt.title("Line graph")  
plt.ylabel('Y axis')  
plt.xlabel('X axis')
plt.show()

