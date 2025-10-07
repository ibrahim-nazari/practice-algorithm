import math

def generate_bar_chart(n, test_cases):
    for test_case in test_cases:
        # Step 1: Parse the test case
        parts = test_case.split()
        W = int(parts[0])  # Bar width for the max value
        L = parts[1]       # Character to use for bars
        columns = parts[2:] # The columns in "ColumnName:ColumnValue" format

        # Step 2: Extract column names and values, and find the maximum value
        col_data = []
        max_value = -float('inf')
        
        for col in columns:
            col_name, col_value = col.split(':')
            col_value = float(col_value)
            col_data.append((col_name, col_value))
            max_value = max(max_value, col_value)

        # Step 3: Generate and print the bar chart for the current test case
        for col_name, col_value in col_data:
            # Calculate the proportional width of the bar
            if max_value > 0:
                bar_length = round((col_value / max_value) * W)
            else:
                bar_length = 0

            # Right-align the column name with width 5, format the value
            col_name_formatted = col_name.rjust(5)
            col_value_formatted = f"{col_value:6.2f}"

            # Print the result
            print(f"{col_name_formatted}: {L * bar_length} {col_value_formatted}")

# Input reading
n = int(input())  # Number of test cases
test_cases = [input().strip() for _ in range(n)]

# Generate bar charts
generate_bar_chart(n, test_cases)
