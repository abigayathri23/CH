def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target element: "))
index = linear_search(arr, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the array")
