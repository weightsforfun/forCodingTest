def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If the target is not found, return the closest value
    if right < 0:
        return 0
    elif left >= len(arr):
        return len(arr) - 1
    else:
        return left if target - arr[right] > arr[left] - target else right