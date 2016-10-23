f = open('twopower.txt', 'w')
L = []
for i in range(64):
    L.append(2**i)

f.write(str(L))
f.close()
