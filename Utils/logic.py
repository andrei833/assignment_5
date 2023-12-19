def mergesort(my_list, my_relation):
    """
    D: Sorts a list using the merge sort algorithm based on a specified relation.
    I: my_list (list) - The list to be sorted.
       my_relation (function) - The relation used for sorting.
    O: Returns the sorted list.
    """
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    arrOne = my_list[:mid]
    arrTwo = my_list[mid:]

    arrOne = mergesort(arrOne, my_relation)
    arrTwo = mergesort(arrTwo, my_relation)

    return merge(arrOne, arrTwo, my_relation)

def merge(a, b, my_relation):
    """
    D: Merges two sorted lists based on a specified relation.
    I: a (list) - The first sorted list.
       b (list) - The second sorted list.
       my_relation (function) - The relation used for merging.
    O: Returns the merged list.
    """
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
    """
    D: Performs sorting on a list using the merge sort algorithm based on a specified relation.
    I: my_list (list) - The list to be sorted.
       my_relation (function) - The relation used for sorting.
    O: Returns the sorted list.
    """
    return mergesort(my_list, my_relation)


def lin_search(my_list,my_relation):
    """
    D: Performs linear search on a list based on a specified relation.
    I: my_list (list) - The list to be searched.
       my_relation (function) - The relation used for searching.
    O: Returns a list of elements satisfying the specified relation.
    """
    result = []
    for i in range(0,len(my_list)):
        if my_relation(my_list[i]):
            result.append(my_list[i])
    return result
