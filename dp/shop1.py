def give_change(T, test_cases):
    for t in range(T):
        amount = test_cases[t][0]
        bills = test_cases[t][1]

        # Sort the bills in descending order based on the denomination (mi)
        bills = sorted(bills, key=lambda x: -x[0])
        
        remaining = amount
        result = []
        
        for bill, count in bills:
            if remaining == 0:
                break
            if bill <= remaining:
                # Determine how many of this bill we can use
                num_bills = min(remaining // bill, count)
                if num_bills > 0:
                    result.append((bill, num_bills))
                    remaining -= bill * num_bills
        
        # Output the result for the current test case
        print(f"Customer{t+1}:")
        if remaining == 0:
            for bill, num_bills in result:
                print(f"{bill} {num_bills}")
        else:
            print("Impossible")


# Input processing
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    M = int(input())  # Amount to be returned
    bill_info = input().split(",")  # Bills in the form mi:ai

    bills = []
    for bill in bill_info:
        denomination, count = map(int, bill.split(":"))
        bills.append((denomination, count))

    test_cases.append((M, bills))

# Call the function to give change
give_change(T, test_cases)
