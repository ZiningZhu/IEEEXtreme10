
def runtestcase(array,colordic):
    B1 = -1
    B1_array = []
    B1_next = 0 # distance to next B1 in array
    B2 = -1
    B2_array = []
    B2_next = len(array)

    for i in range(len(array)):

        if B1_next ==0:
            B1 = array[i]
            B1_next = find_next(B1,i,colordic,array)
            B1_array.append (array[i])
        elif B2_next ==0:
            B2 = array[i]
            B2_next = find_next(B2,i,colordic,array)
            B2_array.append(array[i])

        elif B1_next > 0 and B2_next > 0 and B1_next < B2_next:
            B2 = array[i]
            B2_next = find_next(B2,i, colordic,array)
            B2_array.append(array[i])

        elif B2_next > 0 and B1_next > 0 and B1_next > B2_next:
            B1 = array[i]
            B1_next = find_next(B1,i, colordic,array)
            B1_array.append(array[i])

        elif B2_next < 0:
            B2 = array[i]
            B2_next = find_next(B2,i, colordic,array)
            B2_array.append(array[i])
        else:
            B1 = array[i]
            B1_next = find_next(B2,i, colordic,array)
            B1_array.append(array[i])

        B1_next =B1_next - 1
        B2_next =B2_next - 1


    if len(B2_array)>0:
        B1_time = 1
        B2_time = 1
    else:
        B1_time = 1
        B2_time = 0

    for i in range(len(B1_array)-1):
        if B1_array[i+1]!=B1_array[i]:
            B1_time += 1
    if len(B2_array)>0:
        for i in range(len(B2_array)-1):
            if B2_array[i+1]!=B2_array[i]:
                B2_time += 1

    return B1_time + B2_time


def find_next(color, i, colordict, array):
    next_index = len(array) - i
    for k in range(len(colordict[color])):
        if colordict[color][k] - i >0:

            next_index = colordict[color][k]-i
            return next_index

    return next_index # FIXME - Why?

def build_colordic(array1):
    # assume array stores the color sequence
    colordic = {} # make a color dict

    for i in range(len(array1)):
        if (array1[i] in colordic):
            colordic[array1[i]].append(i)
        else:
            colordic[array1[i]] = [i]

    return colordic
    # done making a position dictionary

def main():

    textcase = int(input())

    for i in range(textcase):
        N = input()
        array1 = str(input()).split(' ')
        for i in range(len(array1)):
            array1[i] = int(array1[i])
        colordic = build_colordic(array1)
        output = runtestcase(array1,colordic)
        print(output)



if __name__ == "__main__":
    #main()
    array1 = [7,7,2,11,7]
    colordict = build_colordic(array1)
    for i in range(5):
        print(find_next(7, i, colordict, array1))
