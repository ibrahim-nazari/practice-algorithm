def count_country_codes(test_cases):
    # Define the set of all possible country codes
    country_codes = set()
    
    # Iterate over each test case
    for s in test_cases:
        found_codes = set()
        
        # Extract all possible 2-letter substrings from the string
        for i in range(len(s) - 1):
            # Take the substring of length 2
            code = s[i:i + 2]
            found_codes.add(code)
        
        # Count the unique country codes in this string
        print(len(found_codes))


# Read input
t = int(input())  # Number of test cases
test_cases = [input().strip() for _ in range(t)]

# Call the function with the test cases
count_country_codes(test_cases)
