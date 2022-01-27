import random as rd

def doGet():
    i=rd.randint(0,2)
    """
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return 2
    """
    #result 8.94 seconds to execute $time python3 switch.py
    
    if i==0:
        j=0
    elif i==1:
        j=1
    else:
        j=2
    return j
    #result 9.084 seconds to execute $time python3 switch.py
    
for x in range(pow(10,7)):
    doGet()
