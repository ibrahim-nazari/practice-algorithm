def shortest_superstring(str1, str2):
    # Check the maximum overlap where str1's suffix matches str2's prefix
    max_overlap1 = 0
    for i in range(1, min(len(str1), len(str2)) + 1):
        if str1[-i:] == str2[:i]:  # Suffix of str1 matches prefix of str2
            max_overlap1 = i
    
    combined1 = str1 + str2[max_overlap1:]  # Combine str1 and str2
    
    # Check the maximum overlap where str2's suffix matches str1's prefix
    max_overlap2 = 0
    for i in range(1, min(len(str1), len(str2)) + 1):
        if str2[-i:] == str1[:i]:  # Suffix of str2 matches prefix of str1
            max_overlap2 = i
    
    combined2 = str2 + str1[max_overlap2:]  # Combine str2 and str1
    
    # Return the shorter of the two combined strings
    return min(combined1, combined2, key=len)

# Input reading and processing
def main():
    N = int(input())  # Read number of test cases
    for _ in range(N):
        str1, str2 = input().split()  # Read the two strings
        result = shortest_superstring(str1, str2)
        print(result)

# Run the program
main()
