from collections import defaultdict

def recommend_items(user_histories):
    # Step 2: Build a frequency map
    frequency_map = defaultdict(lambda: defaultdict(int))
    
    for history in user_histories:
        items = history.split('>')
        
        for i in range(len(items) - 1):
            current_item = items[i].lower()  # case insensitive
            next_item = items[i + 1].lower()
            frequency_map[current_item][next_item] += 1
        
            
    # Step 3: Sort and format output
    result = []
    for item in sorted(frequency_map.keys()):
        recommendations = frequency_map[item]
        # Sort by frequency (desc) then by item (asc)
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: (-x[1], list(recommendations.keys()).index(x[0])))
        
        recommended_items = [rec[0] for rec in sorted_recommendations]
        result.append(f"{item}:{','.join(recommended_items)}")
    
    return result

# Input reading
u = int(input())
user_histories = [input().strip() for _ in range(u)]

# Get recommendations
recommendations = recommend_items(user_histories)

# Print recommendations
for recommendation in recommendations:
    print(recommendation)
