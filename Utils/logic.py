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

#search
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


#backtracking
def is_ok(value, first_relation, second_relation):
    """
    D: Checks if a list satisfies the specified relations for backtracking.
    I: value (list) - The list to be checked.
       first_relation (function) - The first relation used for checking.
       second_relation (function) - The second relation used for checking.
    O: Returns True if the list satisfies the relations, False otherwise.
    """
    seen = set()
    for i in value:
        if i in seen:
            return False
        seen.add(i)

    n = len(value)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if not first_relation(value[i], value[j]) or not second_relation(value[i], value[j]):
                return False
    return True

def is_sol(value, k):
    """
    D: Checks if the list is a solution based on the specified length for backtracking.
    I: value (list) - The list to be checked.
       k (int) - The specified length.
    O: Returns True if the list is a solution, False otherwise.
    """
    return len(value) == k

def backtracking(elements, value, results, k, first_relation, second_relation):
    """
    D: Performs backtracking on a list based on specified relations and length.
    I: elements (list) - The elements to choose from during backtracking.
       value (list) - The current partial solution.
       results (list) - The list to store valid solutions.
       k (int) - The specified length for a solution.
       first_relation (function) - The first relation used for checking.
       second_relation (function) - The second relation used for checking.
    O: Returns a list of valid solutions.
    """
    for el in elements:
        value.append(el)
        if is_ok(value, first_relation, second_relation):
            if is_sol(value, k):
                results.append(value.copy())
            else:
                backtracking(elements, value, results, k, first_relation, second_relation)
        value.pop()

    return results

def backtracking_wrapper(elements, k, first_relation, second_relation):
    """
    D: Wrapper function for the backtracking algorithm.
    I: elements (list) - The list of elements to be considered.
       k (int) - The desired size of the subset.
       first_relation (function) - The first relation function used for filtering subsets.
       second_relation (function) - The second relation function used for filtering subsets.
    O: Returns the result of the backtracking algorithm for the given parameters.
    """
    rez = backtracking(elements, [], [], k, first_relation, second_relation)
    return rez
