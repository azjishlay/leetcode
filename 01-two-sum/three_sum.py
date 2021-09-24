def three_sum(arr, target):
    a = []

    if arr and len(arr) >= 3:
        arr.sort()
        for i in range(len(arr)):
            l = i + 1
            r = len(arr) - 1

            currentTarget = target - arr[i]

            while l < r:
                sum = arr[l] + arr[r]

                if sum < currentTarget:
                    l += 1
                elif sum > currentTarget:
                    r -= 1
                else:
                    a.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -= 1
    return a

arr1 = [-1, 0, 1, 2, -1, -4]
arr2 = [-1, 0]
arr3 = []
arr4 = [0, 0, 0]
arr5 = [0, 0, -1, 1, 2, -2, 3, 5, -3]

x = 0

print(three_sum(arr1, x))
