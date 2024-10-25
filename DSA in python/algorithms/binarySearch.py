def binary_search(arr, target):
    # Set the initial search boundaries
    left, right = 0, len(arr) - 1

    while left <= right:
        # Find the midpoint of the current range
        mid = (left + right) // 2

        # Check if target is at mid
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Move left boundary up
        else:
            right = mid - 1  # Move right boundary down

    return -1  # Target not found in array

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 7
result = binary_search(arr, target)
print("Target found at index:", result) if result != -1 else print("Target not found")
