def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


if __name__ == '__main__':
    print(tribonacci([1, 1, 1], 0))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
