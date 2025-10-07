D. Pattern Matcher
You're given two non-empty strings. The first one is a pattern consisting of only "x"s and /or "y"s; the other one is a normal string of alsphanumeric characters. Write a program that checks whether the normal string matches the pattern.
A string so is said to match a pattern if replacing all "x"s in the pattern with some onon=-empty substring s1 of s0 and replacing all "y"x in the pattern with some non-empty substring s2 of s0 yields the same sttring s0.
If the input string doesn't match the input pattern, the program should return an empty array; otherwise, it should return an array holding the strings s1 and s2 that represent "x" and "y" in the normal string , in that order. if the pattern doesn't contain any "x"s or "y"x, the respective letter should be represented by an empty string in the final array that you return.
You can assume that there will never be more than one pair of strings s1 and s2 that appropriately represent "x" and "y" in the normal string.
INput format:
The input consists of multiple test cases so the first line of the inpt is the number of test cases
The first line of each test case contains a pattern string the "x" s and "y"s.
The second line of each test case contains another normal string of alphanumeric characters.

out put format:
if the input string doesn't match the input pattern, the program should return an empty array; otherwise, it should return an array holding the strings s1 and s2 that represent "x" and "y" in the normal string, in that order

sample input:
1
xxyxxy
gogopowerrangergogopowerranger

sample output:
gopowerranger
