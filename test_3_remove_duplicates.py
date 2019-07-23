

def remove_duplicates(source=[]):
    """ remove all the duplicates from the given flat list.
    :param list source: list to "purge"
    :return: list without duplicates
    :rtype: list
    """
    for item in source:
        if source.count(item) > 1:
            source.remove(item)
    # 1/ it is safer to create a new list containing only the elements you don't want to remove.
    return source


def remove_duplicates_new_list(source=[]):
    """ remove all the duplicates from the given flat list.
    :param list source: list to "purge"
    :return: list without duplicates
    :rtype: list
    """
    new_list = []
    for item in source:
        if item not in new_list:
            new_list.append(item)
    return new_list


def remove_duplicates_fromkeys(source=[]):
    """
        Use fromkeys Method
        :param source List:
        :return List:
    """
    return list(dict.fromkeys(source))


def remove_duplicates_listset(source=[]):
    """
        Use list(set()) Method
        :param source List:
        :return List:
    """
    return list(set(source))


if __name__ == "__main__":
    # Use iterator Method
    print("1/ Actual 'remove_duplicates' function \n "
          "it is safer to create a new list containing only the elements you don't want to remove.")
    cleaned_list = remove_duplicates(
        [1, 1, 'a', 5, 6, 8, 8, 5, 3, 2, 10, 11, 'a', 'b', 'b'])
    print(cleaned_list)

    # Use New list appends iterator Method
    print(
        u"2/ Alternative 2: Use New list appends iterator Method")
    cleaned_list_new_list = remove_duplicates_new_list(
        [1, 1, 'a', 5, 6, 8, 8, 5, 3, 2, 10, 11, 'a', 'b', 'b'])
    print(cleaned_list_new_list)

    # Use fromkeys Method
    print(
        u"3/ Alternative 3: Use fromkeys Method")

    cleaned_list_fromkeys = remove_duplicates_fromkeys(
        [1, 1, 'a', 5, 6, 8, 8, 5, 3, 2, 10, 11, 'a', 'b', 'b'])
    print(cleaned_list_fromkeys)

    # Use list(set()) Method
    print(
        u"4/ Alternative 4: Use list(set()) Method")

    cleaned_list_set = remove_duplicates_listset(
        [1, 1, 'a', 5, 6, 8, 8, 5, 3, 2, 10, 11, 'a', 'b', 'b'])
    print(cleaned_list_set)

    print("\n ...")
