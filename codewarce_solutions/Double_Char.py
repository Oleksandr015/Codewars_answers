
def double_char(s):
    return ''.join([x*2 for x in s])





if __name__ == '__main__':
    print(double_char("String"))


    '''test.assert_equals(double_char("String"),"SSttrriinngg")
test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
test.assert_equals(double_char("1234!_ "),"11223344!!__  ")'''