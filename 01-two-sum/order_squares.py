def order_squares(arr):
    if arr and len(arr) > 0:
        arr.sort()
        a = []

        r = 0
        while r < len(arr) and arr[r] < 0:
            r += 1
        l = r - 1

        while l >= 0 and r < len(arr):
            if arr[l]**2 < arr[r]**2:
                a.append(arr[l]**2)
                l -= 1
            else:
                a.append(arr[r]**2)
                r += 1
        
        while l >= 0:
            a.append(arr[l]**2)
            l -= 1
        while r < len(arr):
            a.append(arr[r]**2)
            r += 1
        
        return a

arr1 = [-4, -3, 1, 2, 3]
a1 = [1, 4, 9, 9, 16]

print(order_squares(arr1) == a1)
