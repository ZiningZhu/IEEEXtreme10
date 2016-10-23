def main():
    case = int((input()).strip(" "))
    for i in range(case):
        Q = str(input()).strip(" ").split(" ")
        num = int(Q[0])
        name = Q[1]
        print(check(name, num, 0 , len(name)-1)%1000000007)

def check(L, r, start, end):
    if r > end - start + 1:
        return 0
    if r < 0:
        return 0
    if r == 0 and not isit(L[start:end+1]):
        return 0
    if r == 0 and isit(L[start:end+1]):
        return 1
    if start == end:
        return 25
    if start > end:
        return 0
    if L[start] == L[end]:
        return (check(L , r-2, start+1, end -1)*25 + check(L , r, start+1, end -1)) % 1000000007
    if L[start] != L[end]:
        return (check(L , r-1, start+1, end -1)*2 + check(L , r-2, start+1, end -1)*24 ) % 1000000007

def isit(s):
    return str(s) == str(s)[::-1]

if __name__ == "__main__":
    main()
