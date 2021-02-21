def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def binary_search_rec(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search_rec(arr, target, left, mid - 1)
        else:
            return binary_search_rec(arr, target, mid + 1, right)
    return -1


nums = [1, 2, 3, 4, 6, 8, 10]
# test = binary_search(nums, 8)
test = binary_search_rec(nums, 7, 0, len(nums) - 1)
print(test)
