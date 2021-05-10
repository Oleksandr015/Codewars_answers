def correct(string):

    return string.replace('0', 'O').replace('5','S').replace('1','I')



if __name__ == '__main__':
    print(correct("51NGAP0RE"))




    # Test.assert_equals(correct("L0ND0N"), "LONDON");
    # Test.assert_equals(correct("DUBL1N"), "DUBLIN");
    # Test.assert_equals(correct("51NGAP0RE"), "SINGAPORE");