def mergesort(my_list, my_relation):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    arrOne = my_list[:mid]
    arrTwo = my_list[mid:]

    arrOne = mergesort(arrOne, my_relation)
    arrTwo = mergesort(arrTwo, my_relation)

    return merge(arrOne, arrTwo, my_relation)

def merge(a, b, my_relation):
    c = []
    while len(a) and len(b):
        if my_relation(a[0], b[0]) == False:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))

    while len(a):
        c.append(a.pop(0))
    while len(b):
        c.append(b.pop(0))

    return c

def sortalg(my_list, my_relation):
    return mergesort(my_list, my_relation)

print(sortalg([5, 1, 2, 4,3], lambda x,y:x<y))
