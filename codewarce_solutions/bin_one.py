def count_bits(n):
    if n == 0:
        return 0
    b_num = 0
    while n > 0:
        b_num = n % 2 + b_num
        n = n // 2
    return b_num

if __name__ == '__main__':
    print(count_bits(7))