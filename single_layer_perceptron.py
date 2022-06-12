def calc(data_list):
    w=[0, 0, 0, 0, 0]
    eta=0.5#learning rate
    key=0

    while True:
        value = 0
        for i in range(len(w)):
            value += w[i]*data_list[key%6][i]
        print('wTv',key%6+1, '=', value)
        
        y=data_list[key%6][5]

        if y == 1:
            if value<=0:
                tmp = []
                for i in range(len(w)):
                    tmp.append(w[i]+data_list[key%6][i]*eta)
                w = tmp
            elif w == tmp:
                print('Finish. Final w is')
                print('w=',w,'\n')
                break
        else:#y == -1
            if value>=0:
                tmp = []
                for i in range(len(w)):
                    tmp.append(w[i]-data_list[key%6][i]*eta)
                w = tmp
            elif w == tmp:
                print('Finish. Final w is')
                print('w=',w,'\n')
                break
        
        print('w=',w)
        key+=1

data=[[1, 1, 0, 1, 1, +1],
[0, 0, 1, 1, 0, -1],
[0, 1, 1, 0, 0, +1],
[1, 0, 0, 1, 0, -1],
[1, 0, 1, 0, 1, +1],
[1, 0, 1, 1, 0, -1]]

data2=[[1, 1, 0, 1, 1, +1],
[0, 0, 1, 1, 1, -1],
[0, 1, 1, 0, 0, +1],
[1, 0, 0, 1, 0, -1],
[1, 0, 1, 0, 1, +1],
[1, 0, 1, 1, 0, -1]]

calc(data)
calc(data2)
