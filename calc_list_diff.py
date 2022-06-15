df = [1, 4, 9, 16, 25, 36, 49, 64, 81]
for x in range(len(df)):
    for y in range(len(df)):
        if df[x] > df[y]:
            print(df[x],'-',df[y],'=',df[x]-df[y])
