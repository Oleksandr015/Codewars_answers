def explode(arr):
    if type(arr[0]) != int and type(arr[1]) != int:
        return 'Void!'
    elif type(arr[0]) == int and type(arr[1]) == int:
        return [list(arr)] * (arr[0]+arr[1])
    elif type(arr[0]) == int and type(arr[1]) != int:
        return [list(arr)] * arr[0]
    else:
        type(arr[0]) != int and type(arr[1]) == int
        return [list(arr)] * arr[1]



'''def explode(arr):  
    return [arr] * sum(v for v in arr if isinstance(v,int)) or 'Void!''''

if __name__ == '__main__':
    print(explode(['c', 'a']))
