def iq_test(numbers):
    l = numbers.split(' ')
    even = [i for i in l if int(i)%2==0]
    odd = [i for i in l if int(i)%2!=0]
    if len(even) == 1:
        return l.index(even[0])+1
    else:
        return l.index(odd[0])+1


if __name__ == '__main__':
    print(iq_test("2 4 7 8 10"))
