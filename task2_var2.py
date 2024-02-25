def find_lis(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_lis_length = max(lis)

    # Находим саму подпоследовательность
    result = []
    max_lis_index = lis.index(max_lis_length)
    result.append(arr[max_lis_index])
    current_lis_length = max_lis_length - 1
    for i in range(max_lis_index - 1, -1, -1):
        if lis[i] == current_lis_length and arr[i] < result[-1]:
            result.append(arr[i])
            current_lis_length -= 1

    return result[::-1]
