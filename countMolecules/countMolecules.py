def main():
    line = str(input()).split(" ")
    c = int(line[0])
    h = int(line[1])
    o = int(line[2])
    z = [c, h, o]
    M = [[-24, 6, 12], [0, -6, 12], [4, 1, -2]]
    x = my_multiply(M, z)
    x = vector_divide(x, 24)
    possible = True
    for k in x:
        if (k != int(k)):
            possible = False
    if (possible):
        print ("%d %d %d" %(x[0], x[1], x[2]))
    else:
        print ("Error")

def my_multiply(M, z):
    # M is ixj, z is jx1
    res = []
    for i in range(len(M)):
        s = 0
        for j in range(len(M[0])):
            s += M[i][j] * z[j]
        res.append(s)
    return res

def vector_divide(x, n):
    new_x = x
    for i in range(len(x)):
        new_x[i] /= float(n)
    return new_x

if __name__ == "__main__":
    main()
