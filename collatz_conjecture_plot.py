from matplotlib import pyplot as plt
import tkinter as tk      
from functools import partial

def call_result(label_result, arg):
    try:
        number = int(arg.get())
        startNum = number
        yaxis = []
        
        while number != 1:
            yaxis.append(number)
        
            if number % 2 == 0:
                number /= 2
            else:
                number = number * 3 + 1
        
        yaxis.append(number)
        print("finish!")            
        print(yaxis)
        
        plt.plot(yaxis)
        plt.title("Collatz conjecture graph starts with " + str(startNum))  
        plt.show()
        return

    except ValueError:
        label_result.config(text="Please enter number") 

root = tk.Tk()                                                                  
root.geometry('480x270+100+100')  
root.title('Collatz conjecture plot')  
   
inputStr = tk.StringVar()  
  
labelNum = tk.Label(root, text="number").grid(row=1, column=0)  
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)  

entry = tk.Entry(root, textvariable=inputStr).grid(row=1, column=2)  
  
call_result = partial(call_result, labelResult, inputStr)  
buttonPlot = tk.Button(root, text="plot", command=call_result).grid(row=3, column=0)  
  
root.mainloop()  
