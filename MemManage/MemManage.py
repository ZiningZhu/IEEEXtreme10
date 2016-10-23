def main():
    T = int(input())
    for t in range(T):
        line = str(input()).split(" ")
        p = int(line[0]) # num of OS page
        s = int(line[1]) # size of each page
        n = int(line[2]) # num of memaddr queries
        pageRequests = []
        for i in range(n):
            pageRequests.append(findPage(int(input()), s))

        # Simulate FIFO
        pageReplaceFIFO = 0
        osPages = [None] * p
        queue = []
        x = 0
        ospg = -1
        for i in range(len(pageRequests)):
            pr = pageRequests[i]
            if (pr in osPages):
                continue
            elif x < p:
                osPages[x] = i
                queue.append(x)
                x += 1
            else:
                # pop the first osPage in list
                idx = queue.pop(0)
                osPages[idx] = pr
                pageReplaceFIFO += 1
                queue.append(idx)

        # Simulate LRU
        pageReplaceLRU = 0
        osPages = [None] * p
        memSeq = []
        x = 0
        for i in range(len(pageRequests)):
            pr = pageRequests[i]
            if (pr in osPages):
                tmp = memSeq.index(osPages.index(pr))
                xidx = memSeq.pop(tmp)
                memSeq.append(xidx)
                osPages[xidx] = pr
            elif x < p:
                memSeq.append(x)
                osPages[x] = pr
                x += 1
            else:
                xidx = memSeq.pop(0)
                osPages[xidx] = pr
                memSeq.append(xidx)
                pageReplaceLRU += 1

        # Compare results
        if pageReplaceLRU < pageReplaceFIFO:
            print ("yes %d %d" %(pageReplaceFIFO, pageReplaceLRU))
        else:
            print ("no %d %d" %(pageReplaceFIFO, pageReplaceLRU))

def findPage(memAddr, s):
    return int(memAddr // s)

if __name__ == "__main__":
    main()
