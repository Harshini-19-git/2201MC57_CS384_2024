#ques1


def find_unique_triplets(nums):
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for the first element
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicates for the second element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicates for the third element
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(find_unique_triplets(nums))




#ques2
def is_balanced(s):
    counter = {'(': 0, '{': 0, '[': 0}
    stack = []

    for char in s:
        if char in '({[':
            counter[char] += 1
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return "The input string is NOT balanced."
            last_open = stack.pop()
            if (last_open == '(' and char != ')') or \
               (last_open == '{' and char != '}') or \
               (last_open == '[' and char != ']'):
                return "The input string is NOT balanced."
            counter[last_open] -= 1

    return "The input string is balanced." if all(val == 0 for val in counter.values()) else "The input string is NOT balanced."

# Example usage
s = "[{()}]"
print(is_balanced(s))
