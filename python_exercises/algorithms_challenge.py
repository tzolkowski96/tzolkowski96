def find_single_number(nums):
    """
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    """ 

    result = 0 
    for num in nums: 
        result ^= num 
    return result 

# Example: 
nums = [4, 1, 2, 1, 2]
print(find_single_number(nums)) # Output: 4 