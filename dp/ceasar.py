def caesar_cipher():
    # Number of test cases
    N = int(input())
    
    for _ in range(N):
        # Read the test case
        operation, shift, text = input().split()
        shift = int(shift)
        
        # Function to shift characters
        def shift_char(c, shift):
            new_pos = (ord(c) - ord('a') + shift) % 26
            return chr(ord('a') + new_pos)
        
        # Adjust shift for decryption
        if operation == "decrypt":
            shift = -shift
        
        # Process the text
        result = ''.join(shift_char(c, shift) for c in text)
        
        # Output the result
        print(result)

# Example usage:
# Input:
# 2
# encrypt 1 abc
# decrypt -1 acd
caesar_cipher()
