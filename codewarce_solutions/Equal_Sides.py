def find_even_index(arr):
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
    else:
        return -1


if __name__ == '__main__':
    print(find_even_index([1,100,50,-51,1,1]))
