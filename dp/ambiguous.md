Ambiguous measurements

This problem deals with measuring cups that are missing important measuring labels, specifically, a measuring cup only has two measuring lines, a low (L)
and a high (H) line. This means that these cups can't precisely measure and can only guarantee that the substance poured into them will be bettween the L and H line . For example , you might have a measuring cup, that has a Low line at 400ml and a high line at 435ml. This means that when you use this measuring cup, you can only be sure that what you're measuring is between 400ml and 435ml.
You're given a list of measuring cups containing their low and high lines as well as one Low integer and one High integer representing a range for a target measurement . Write a program that return s a boolean representing whether you can use the cups to accurately measure a volume in the specified Low, high range the range is inclusive

Note that:

Each measuring cup will be represented by a pair of positive integers L, H where 0 =<l >=H
You'll always be given at least one measuring cup , and the low and high input parameters will always stisfy the following constraint: 0=< low =< high
Once you've measured some liquid, it will immediately be transferred to a larger bowl that will
eventually possibly contain the target measurement
you can't pour the contents of one measuring cup into another cup.

input format:
the input consists of multiple test cases so the first line ofthe input is the number of test cases.
The first line of each test case contains is the N which is number the number of list of measuring cups.
in each next N line contains two comma -separated values which indicate the list of measuring cups containing their low and high lines.
The next line is Low integer And the last line is high interger
output format:
return a boolean representing whether you can use the cups to accurately measure a volume in the specified Low, High range the range is inclusive
sample input:
1
3
200,210
450,465
800,850
2100
2300

output:
true
