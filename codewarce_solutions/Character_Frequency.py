def char_freq(message):
    a = {}
    for i in message:
        if i not in a:
            a[i] = 1
        else:
            a[i] +=1
    return a

if __name__ == '__main__':
    print(char_freq("I like cats"))

