#ques1 
# Function to calculate the sum of digits until a single digit is obtained
def unitary_sum_of_digits(n):
    while n >= 10:  # Repeat until 'n' becomes a single digit
        digit_sum = 0
        temp = n
        while temp > 0:
            digit_sum += temp % 10  # Extract the last digit
            temp //= 10  # Remove the last digit
        n = digit_sum  # Update 'n' to the sum of its digits
    return n

# Input and output
n = int(input("Enter an integer: "))
result = unitary_sum_of_digits(n)
print(f"The Unitary Sum of Digits of {n} is: {result}")






#ques2



# Function to compress the string
def string_compression(s):
    compressed = ""
    length = len(s)
    i = 0
    
    # Outer loop goes through each character in the string
    while i < length:
        current_char = s[i]
        count = 1
        
        # Inner loop counts consecutive occurrences
        for j in range(i + 1, length):
            if s[j] == current_char:
                count += 1
            else:
                break
        
        # Append the character and count to the result
        compressed += current_char + str(count)
        i += count  # Skip counted characters
    
    return compressed

# Input and output
s = input("Enter a string: ")
result = string_compression(s)
print(f"Compressed String: {result}")
