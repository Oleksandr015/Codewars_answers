def order(sentence):
    a = sentence.split()
    if len(sentence) == 0:
        return sentence
    sorted_list = []
    n = 1
    while len(a) > 0:
        for word in a:
            if str(n) in word:
                sorted_list.append(word)
                a.remove(word)
                n += 1

    return ' '.join(sorted_list)


if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))
