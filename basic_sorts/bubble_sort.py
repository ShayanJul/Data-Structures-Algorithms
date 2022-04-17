"""bubble sort
    """


def bubble_sort(my_list):
    """this function bubble sorts a given list
    """
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


unsorted_list = [5, -2, 8, 0, -1, 6]
print(bubble_sort(unsorted_list))
