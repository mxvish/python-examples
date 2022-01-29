import numpy.random as rd

rates = []
time = 0

for episode in range(1000):
    if episode % 100 == 0 and episode > 0:
        rates.append(time / 100)
        time = 0
        
    for _ in range(200):
        if rd.randint(200) == 0:
            done = True
        else:
            done = False
        if done:
            time += 1
            break
print(rates)   
