import math

def calculate_score(x, y):
    """Calculate the score based on the distance from the origin."""
    distance = math.sqrt(x**2 + y**2)
    if distance < 5:
        return distance
    elif distance == 5:
        return 0
    else:
        return -1

def circular_game():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of participants
        scores = []
        
        for _ in range(n):
            # Read two throws (two pairs of coordinates)
            x1, y1 = map(int, input().split(','))
            x2, y2 = map(int, input().split(','))
            
            # Calculate the scores for both throws
            score1 = calculate_score(x1, y1)
            score2 = calculate_score(x2, y2)
            
            # Total score for the participant
            total_score = score1 + score2
            scores.append(f"{total_score:.5f}")  # Store score with 5 decimal places
        
        # Print all scores for the test case
        for score in scores:
            print(score)

# Example usage (You can run this and input the data manually):
circular_game()
