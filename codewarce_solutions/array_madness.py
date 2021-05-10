def array_madness(a,b):
    # Ready, get, set, GO!!!
    return sum([i**2 for i in a ]) > sum([j**3 for j in b])




if __name__ == '__main__':
    a, b = [4, 5, 6], [1, 2, 3]
    print(array_madness(a, b))