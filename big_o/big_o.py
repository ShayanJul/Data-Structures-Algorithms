"""_summary_
    """


def printing_items(n):
    """_to understand the big O concept_

    Args:
        n (_type_): _description_
    """
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)


printing_items(10)
