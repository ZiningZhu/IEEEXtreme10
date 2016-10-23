
def main():
    line = str(input())
    print(line)
    line = line.split(" ")
    base = int(line[0])
    symbol_str = line[1]
    s2v = {} # symbol to value
    v2s = {}
    for i in range(base):
        s2v[symbol_str[i]] = i
        v2s[i] = symbol_str[i]

    #print("s2v: %s" %str(s2v))
    #print("v2s: %s" %str(v2s))

    line1 = str(input())
    line2 = str(input())
    line3 = str(input())
    line4 = input()

    num1 = line1.strip(" ")[::-1]
    num2 = line2.strip("+").strip(" ")[::-1]

    i = 0
    s = ""
    carry = 0
    while(i < max(len(num1), len(num2))):
        if (i >= len(num1)):
            val = s2v[num2[i]] + carry
            if val in v2s:
                carry = 0
            else:
                carry = 1
                val = val - base
            s = v2s[val] + s
            i += 1

        elif (i >= len(num2)):
            val = s2v[num1[i]] + carry
            if val in v2s:
                carry = 0
            else:
                carry = 1
                val = val - base
            s = v2s[val] + s
            i += 1

        else:
            val = s2v[num1[i]] + s2v[num2[i]] + carry
            if val in v2s:
                carry = 0
            else:
                carry = 1
                val = val - base

            s = v2s[val] + s
            i += 1
    if (carry == 1):
        s = v2s[carry] + s
        carry = 0

    # Now proceed to print the result
    print(line1)
    print(line2)
    print(line3)
    numspaces = len(line2) - len(s)
    for k in range(numspaces):
        s = " " + s
    print(s)


if __name__ == "__main__":
    main()
