def split_in_parts(s, part_length):
    new = []
    while s:
        new.append(s[0:int(part_length)])
        s = s[int(part_length):]

    return str(' '.join(new))




if __name__ == '__main__':
    print(split_in_parts("supercalifragilisticexpialidocious", 3))