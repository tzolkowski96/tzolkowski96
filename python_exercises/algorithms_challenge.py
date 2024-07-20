def find_single_number(nums):
    """
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Args:
    nums (list of int): A list of integers where every element appears twice except for one.

    Returns:
    int: The single integer that does not appear twice.

    Raises:
    ValueError: If the input list is empty or contains non-integer elements.
    """
    if not nums:
        raise ValueError("Input list must not be empty.")
    
    result = 0
    for num in nums:
        if not isinstance(num, int):
            raise ValueError("All elements in the input list must be integers.")
        result ^= num
    return result

def test_find_single_number():
    """
    Unit tests for the find_single_number function.
    """
    test_cases = [
        ([4, 1, 2, 1, 2], 4),
        ([2, 2, 3, 3, 4], 4),
        ([1], 1),
        ([0, 1, 0], 1),
        ([-1, -1, -2], -2),
        ([10, 10, 20, 30, 30], 20)
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        assert find_single_number(nums) == expected, f"Test case {i + 1} failed"
    
    print("All test cases passed!")

if __name__ == '__main__':
    # Example usage
    nums = [4, 1, 2, 1, 2]
    print(f"The single number in the list {nums} is: {find_single_number(nums)}")
    
    # Run unit tests
    test_find_single_number()
