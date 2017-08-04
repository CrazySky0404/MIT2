def max_val(t):
    intlist = []
    result1 = []

    for i in t:
        if type(i) == type(list()):
            d = max(i)
            if type(d) == type(list()):
                d1 = max(d)
                if type(d1) == type(list()):
                    d2 = max(d1)

                    if type(d2) == type(list()):
                        d3 = max(d2)
                        if type(d3) == type(list()):
                            d4 = max(d3)
                            #print(d4)

            intlist.append(d4)

            #print(result1)


        elif type(i) == type(tuple()):
            y = list(i)
            z = max(y)

            intlist.append(z)

        elif type(i) == type(int()):
            intlist.append(i)

    for x in result1:
        if type(x) == type(int()):
            intlist.append(x)

        elif type(x) == type(list()):
            z = int(''.join(map(str, x)))
            intlist.append(z)
            #print(intlist)



    #print(intlist)
    print (max(intlist))




max_val(((40, 6), 5))
max_val((9, [3, 8, 2]))
#max_val(([1, 2], [3, 4], [5, 6]))
#max_val(([[2, 1, 5], [4, 2], 6], ([2, 1], (7, 7, 5), 6)))
max_val([[[[[[6]]]]]])




