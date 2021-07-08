def binary_search(needle, haystack):
    arr = haystack
    lowest = arr[0]
    highest = len(arr) - 1

    while lowest < highest:
        middle = lowest + round((highest - lowest) / 2)
        if needle == arr[middle]:
            return middle

        if needle < arr[middle]:
            highest = middle - 1
        else:
            lowest = middle + 1

    return -1


if __name__ == '__main__':
    n = 27
    h = sorted([10, 72, 1, 55, 96, 27, 7, 8, 14, 13, 29, 19])
    res = binary_search(needle=n, haystack=h)
    print("Element is at index: {} within this list: {}".format(res, h))
