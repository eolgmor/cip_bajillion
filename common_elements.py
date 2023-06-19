"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""
common_elements = []


def common(list1, list2):
    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    >>> common(['a'], ['a'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'a', 'z', 'c'])
    ['a', 'c']
    >>> common(['a', 'b', 'c'], ['x', 'y', 'z'])
    []
    >>> common(['a', 'a', 'b'], ['a', 'a', 'x'])
    ['a']
    """
    # pass
    """
    You implement this function.  Don't forget to remove the 'pass' statement above.
    """
    current_list = list1
    last_list = list2
    common_files_list = []
    for file in current_list:
        """if the file name matches then is added to a common list"""
        if file in last_list and file not in common_files_list:
            common_files_list.append(file)
    if len(common_files_list) != 0:  # If a common word were found then is preserved as list2
        list2 = common_files_list
    else:  # if not found any match then last list will be the current list
        list2 = current_list

    return common_files_list


def main():
    # Same tests as the doctests above, but can be run from the terminal:
    # python3 common_elements.py

    print(common(['a'], ['a']))  # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))  # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))  # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))  # should print ['a']


if __name__ == '__main__':
    main()
