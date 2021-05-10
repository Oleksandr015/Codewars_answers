def stringy(size):
    return "".join([str(i % 2) for i in range(1, size + 1)])




if __name__ == '__main__':
    print(stringy(6))