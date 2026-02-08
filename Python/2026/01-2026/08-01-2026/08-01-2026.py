def asc_sorted_list(array):
    return array==sorted(array)

def desc_sorted_list(array):
    return array==sorted(array,reverse=True)

def is_sorted(arr):

    if (asc_sorted_list(arr)):
        return "Ascending"
    elif (desc_sorted_list(arr)):
        return "Descending"
    else:
        return "Not sorted"


is_sorted([1, 2, 3, 4, 5]) #"Ascending".
is_sorted([10, 8, 6, 4, 2]) # "Descending".
is_sorted([1, 3, 2, 4, 5]) # "Not sorted".
is_sorted([3.14, 2.71, 1.61, 0.57]) # "Descending"
is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]) # "Ascending".
is_sorted([0.4, 0.5, 0.3]) # "Not sorted".