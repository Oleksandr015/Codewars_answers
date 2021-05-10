def count_by(x, n):
    return range(x, n*x + 1, x)


if __name__ == '__main__':
    print(count_by(100,5))

    """
    Return a sequence of numbers counting by `x` `n` times.
    test.assert_equals(count_by(1, 51, 5), [1, 2, 3, 4, 5])
test.assert_equals(count_by(2, 5), [2, 4, 6, 8, 10])
test.assert_equals(count_by(3, 5), [3, 6, 9, 12, 15])
test.assert_equals(count_by(50, 5), [50, 100, 150, 200, 250])
test.assert_equals(count_by(100, 5), [100, 200, 300, 400, 500])
    """
