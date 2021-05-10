def filter_homogenous(arrays):
    return [a for a in arrays if a and all(type(a[0]) == type(b) for b in a)]

if __name__ == '__main__':
    filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]])

    filter_homogenous([[123, 234, 432], ['', 'abc'], [''], ['', 1], ['', '1'], []])
