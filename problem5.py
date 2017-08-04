

def cipher(map_from, map_to, code):
    answer = ()
    myList = []
    cat = ''



    dicty = dict(zip(map_from, map_to))
    for k, v in dicty.items():
        if k in code:
            #for i in code:
            cat += str(k)
    #print (cat)


    #print(dicty)
    myList.append(dicty)
    myList.append(cat)
    answer = tuple(myList)
    print(answer)


cipher("abcd", "dcba", "dab")





