def main():
    T = int(input())
    for t in range(T):

        G = int(input())
        ttlGameSumX = 0
        for g in range(G):
            P = int(input())
            line = str(input()).split(" ")

            piles = []
            gameSumX = 0
            for item in line:
                x = int(((int(item) - 1) / 2) % 2)
                #piles.append(x)
                ttlGameSumX = (ttlGameSumX + x)


        if (ttlGameSumX % 2 == 1):
            print('Alice')
        else:
            print('Bob')


if __name__ == "__main__":
    main()
