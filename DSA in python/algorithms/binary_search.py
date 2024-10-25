def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of integers.
    target (int): The integer value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found


def search_in_array(nums, target):
    """
    Search for a target value in a sorted array using binary search.

    Parameters:
    nums (list): A sorted list of integers.
    target (int): The integer value to search for.

    Returns:
    str: A message indicating the result of the search.
    """
    index = binary_search(nums, target)

    if index != -1:
        return f'Target {target} found at index: {index}'
    else:
        return f'Target {target} not found in the array.'


def main():
    """
    Main function to execute the binary search and display results.
    """
    nums = [1, 2, 3, 4, 5]  # Sorted array
    target = 3  # Value to search for

    # Perform the search and print the result
    result_message = search_in_array(nums, target)
    print(result_message)


if __name__ == "__main__":
    main()
