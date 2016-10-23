# Greedy
def main():
    Numcase = int(raw_input())
    for casenum in range(Numcase):
        line = raw_input().strip(" ").split(" ")
        N = int(line[0])
        K = int(line[1])
        A = []

        for i in range(N):
            A.append(int(raw_input()))

        A.sort()
        # iteratively find the best location for each one of the card boards.
        cardboards = [0, len(A)]
        # A sorted array.
        # Each cardboard points to the element after the last one of a bag.
        # cardboards[0]=10 indicates the first bag is A[0:10]

        minSumRange = A[-1] - A[0]

        for j in range(1, K):
            # What is the best location? One that can reduce minSumRange by the most
            # AKA. one cut maximizes the difference between each two elements
            maxBagRange = 0
            left = 0
            right = len(A) - 1
            ans_k = 0
            for k in range(1, len(cardboards)):
                left = cardboards[k-1]
                right = cardboards[k]-1
                bagRange = A[right] - A[left]
                if (bagRange > maxBagRange):
                    maxBagRange = bagRange
                    ans_k = k
            # now ans_k points to the bag
            # left and right points the endpoints of the bag, inclusively
            left = cardboards[ans_k - 1]
            right = cardboards[ans_k] - 1
            # minimize A[board] - A[board-1]
            board = right
            newboard = right
            maxdiff = 0
            while(board > left):
                #print("left=%d, right=%d, board=%d" %(left, right, board))
                if (A[board] - A[board-1] > maxdiff):
                    maxdiff = A[board] - A[board-1]
                    newboard = board
                board -= 1
            cardboards.insert(ans_k, newboard)

            minSumRange -= maxdiff
            #print("j=%d, cardboards = %s" %(j, str(cardboards)))

        # Now you have all the cardboards
        print("%d" %minSumRange)


if __name__ == "__main__":
    main()
