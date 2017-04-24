#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(lst) - 1):
        swap = False
        for idx in range(len(lst) - 1 - i):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                swap = True
        if not swap:
            break
    print lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    result_list = []
    while len(list1) > 0 or len(list2) > 0:
        # if both lists not empty
        # compare first items of each list
        if list1 == []:
            result_list.append(list2.pop(0))
        elif list2 == []:
            result_list.append(list1.pop(0))
        elif list1[0] < list2[0]:
            # append and pop first item of list1
            result_list.append(list1.pop(0))
        else:
            # append and pop first item of list2
            result_list.append(list2.pop(0))
    return result_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    # Break everything down into a list of one
    if len(lst) < 2:  # if length of lst is 1, return lst
        return lst
    # Get the item at the index of the middle
    mid = int(len(lst) / 2)
    # Divide the list in two
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return merge_lists(lst1, lst2)



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
