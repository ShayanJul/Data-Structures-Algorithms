"""insertion sort
    """


def insertion_sort(my_list):
    """insertion sort for a given list
    """
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


unsorted_list = [5, -2, 8, 0, -1, 6]
print(insertion_sort(unsorted_list))
