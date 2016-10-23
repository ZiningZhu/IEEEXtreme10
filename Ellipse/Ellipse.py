import math
import matplotlib.pyplot as plt

def main():
    T = int(input())
    for t in range(T):
        canvas = [[0] * 100] * 100
        N = int(raw_input())
        for n in range(N):
            line = raw_input().split(" ")
            x1 = int(line[0]) + 50
            y1 = int(line[1]) + 50
            x2 = int(line[2]) + 50
            y2 = int(line[3]) + 50
            r = int(line[4])
            #print ("%d %d %d %d %d" %(x1, y1, x2, y2, r))

            drawEclipse(canvas, x1, y1, x2, y2, r)
        print (str(countPercentage(canvas)) + "%")

plotpoints = []

def drawEclipse(canvas, x1, y1, x2, y2, r):
    for y in range(len(canvas)):
        for x in range(len(canvas[0])):
            if (dist(x, y, x1, y1) + dist(x, y, x2, y2) < r * 0.9):
                canvas[x][y] = 1
                plotpoints.append((x, y))



def dist(x, y, x1, y1):
    return math.sqrt((x1 - x)**2 + (y1 - y) ** 2)

def countPercentage(canvas):
    uncolored = 0.0
    ttl = len(canvas) * len(canvas[0])
    print ("ttl = %d" %ttl)
    for x in range(len(canvas)):
        for y in range(len(canvas[0])):
            if (canvas[x][y] == 0):
                uncolored += 1
    return int(100 * uncolored / ttl + 0.5)

if __name__ == "__main__":
    main()

    xplot = [pt[0] for pt in plotpoints]
    yplot = [pt[1] for pt in plotpoints]
    plt.plot(xplot, yplot, ".")
    plt.axis([0, 100, 0, 100])
    plt.show()
