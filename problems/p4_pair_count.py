def count_pairs(n, k, arr):
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) == k:
                count += 1

    return count


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(count_pairs(n, k, arr))