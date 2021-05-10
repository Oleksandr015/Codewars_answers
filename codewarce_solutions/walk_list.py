def is_valid_walk(walk):
    count_dict = dict(zip(walk, [walk.count(i) for i in walk]))

    if len(walk) != 10:
        return False
    elif len(count_dict) % 2 == 0:
        return False
    elif 'n' and 's' in count_dict and count_dict['n'] != count_dict['s']:
        return False
    elif 'w' and 'e' in count_dict and count_dict['w'] != count_dict['e']:
        return False
    else:
        return True


if __name__ == '__main__':
    print(is_valid_walk(['e', 'w', 'e', 'w', 'e', 'w', 'n', 'w', 'e', 'n']))
