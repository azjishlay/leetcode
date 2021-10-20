def three_sum(arr, target):
    a = []

    if arr and len(arr) >= 3:
        arr.sort()
        for i in range(len(arr)):
            l = i + 1
            r = len(arr) - 1

            while l < r:
                sum = arr[i] + arr[l] + arr[r]

                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    a.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -= 1
    return a

arr1 = [-1, 0, 1, 2, -1, -4]
a1 = [[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]]

arr2 = [-1, 0]
arr3 = []
arr4 = [0, 0, 0]

arr5 = [0, 0, -1, 1, 2, -2, 3, 5, -3]
a5 = [[-3, -2, 5], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]

x = 0

print(three_sum(arr5, x))
