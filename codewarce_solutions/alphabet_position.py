import string


def alphabet_position(text):
    list_numbers = [ord(letter.lower()) - 97 for letter in text if letter.isalpha()]
    result_str = ' '.join(str(item) for item in list_numbers)

    return str(result_str)


if __name__ == '__main__':
    print(alphabet_position("The sunset sets at twelve o' clock."))
