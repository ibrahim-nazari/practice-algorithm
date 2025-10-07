from collections import Counter

def process_text(text):
    # Convert text to lowercase and filter only alphabetic characters
    text = text.lower()
    letter_counts = Counter(char for char in text if char.isalpha())
    
    # Sort by frequency (descending) and alphabetically (ascending)
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Extract the letters in the desired order
    return ''.join([letter for letter, count in sorted_letters])

# Input handling
def main():
    N = int(input())  # Number of test cases
    for _ in range(N):
        text = input().strip()  # Read the text case
        result = process_text(text)  # Process the text
        print(result)

# Sample test case execution
if __name__ == "__main__":
    main()
