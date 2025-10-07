def find_overlap(s1, s2):
    # Find the maximum overlap where s1 ends and s2 starts
    max_overlap = 0
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i:] == s2[:i]:
            max_overlap = i
    return max_overlap

def shortest_combined_name(food1, food2):
    # Calculate overlaps
    overlap1 = find_overlap(food1, food2)  # Overlap where food1 ends and food2 starts
    overlap2 = find_overlap(food2, food1)  # Overlap where food2 ends and food1 starts

    # Combine the names with overlaps
    combined1 = food1 + food2[overlap1:]  # Combine food1 with food2
    combined2 = food2 + food1[overlap2:]  # Combine food2 with food1

    # Return the shortest result
    return combined1 if len(combined1) <= len(combined2) else combined2

# Input handling
def main():
    N = int(input())  # Number of test cases
    for _ in range(N):
        food1, food2 = input().split()
        print(shortest_combined_name(food1, food2))

# Example usage
if __name__ == "__main__":
    main()
