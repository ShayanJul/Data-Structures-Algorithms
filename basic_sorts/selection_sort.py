"""selection sort
    """


def selection_sort(my_list):
    """this function selection sorts a given list
    """
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


unsorted_list = [5, -2, 8, 0, -1, 6]
print(selection_sort(unsorted_list))
