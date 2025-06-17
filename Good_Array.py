def find_nice_indices(n, arr):
    total_sum = sum(arr)
    
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    nice_indices = []

    for i in range(n):
        remaining_sum = total_sum - arr[i]
        if remaining_sum % 2 != 0:
            continue

        target = remaining_sum // 2

        count[arr[i]] -= 1

        if target in count and count[target] > 0:
            nice_indices.append(i + 1)  

        count[arr[i]] += 1

    print(len(nice_indices))
    if nice_indices:
        print(" ".join(map(str, nice_indices)))

n = int(input())
arr = list(map(int, input().split()))
find_nice_indices(n, arr)
