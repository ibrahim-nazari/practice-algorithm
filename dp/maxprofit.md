Max profit with K Transactions
You're given an array of positive integers representing the prices of a single stock on various days each index in the array represents a different day. You're also given and interger k, which represents the number of transactions you're allowed
to make . One transaction consists of buying the stock on a given day and selling it on another , later day.
Write a program that returns the maximum profit that you can make by buying and selling the stock , given k transactions.
Note that you can only hold one share of the stock at a time , in other words , you can't by more than one share of the stock on any given day , and you can't buy
a share on the stock if yu're still holding another share.
Also , you don't need to use all K trasactions that you're allowed.
Input format:
The input consists of multiple test cases so the first line of the inut is the number of test cases.
The first line of each test case contains an integer K which represents the number of transactions you're allowed to make.
The second line of each test case contains comma-separated integer values representing the price of a single stock on various days
Output format:
Return an integerwhich is the maximum profit that you can make by buying and selling the stock , given K transactions.
Sample input:
1
2
5,11,3,50,60,90
Output:
93

<!-- output 93= buy:5, sell:11; buy:3, sell:90 -->
