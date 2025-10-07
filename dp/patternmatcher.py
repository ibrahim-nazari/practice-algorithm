def pattern_matcher(pattern, s):
    # Normalize the pattern to start with 'x' for consistent logic

    swapped = False


    # Count occurrences of 'x' and 'y'
    count_x = pattern.count('x')
    count_y = len(pattern) - count_x

    # If the entire pattern is only 'x's or only 'y's
    if count_y == 0:
        if len(s) % count_x != 0:
            return []  # No valid mapping possible
        length_x = len(s) // count_x
        s1 = s[:length_x]
        return [s1, ''] if not swapped else ['', s1]

    if count_x == 0:
        if len(s) % count_y != 0:
            return []  # No valid mapping possible
        length_y = len(s) // count_y
        s2 = s[:length_y]
        return ['', s2] if not swapped else [s2, '']

    # Try different lengths for 'x'

    for length_x in range(len(s) // count_x, 0, -1):
        remaining_length = len(s) - (length_x * count_x)
        if remaining_length <= 0 or remaining_length % count_y != 0:
            continue  # Skip if 'y' length is invalid

        length_y = remaining_length // count_y
        pos = 0
        s1, s2 = None, None  
         
        valid = True

        # Try constructing the string from the pattern
        for char in pattern:
            if char == 'x':
                sub = s[pos:pos + length_x]
                if s1 is None:
                    s1 = sub  # Assign the first 'x' substring
                elif s1 != sub:
                    valid = False  # Inconsistent 'x' mapping
                    break
                pos += length_x
            else:  # char == 'y'
                sub = s[pos:pos + length_y]
                if s2 is None:
                    s2 = sub  # Assign the first 'y' substring
                elif s2 != sub:
                    valid = False  # Inconsistent 'y' mapping
                    break
                pos += length_y
             

        # Check if the mapping is valid and 'x' != 'y'
        if valid and s1 != s2 :
            result = [s1, s2]
            return result if not swapped else result[::-1]

    return []  # No valid mapping found

# Input and output handling
t = int(input())
for _ in range(t):
    pattern = input().strip()
    s = input().strip()
    result = pattern_matcher(pattern, s)
    print(result)
"""
1
yxyx
powerrangergopowerrangergo

1
yxxyxx
powerrangergogopowerrangergogo



"""