A. Airport Connections
for the purpose of this question, the phrases "airport route" and "airport connection" are used interchangeably. You're given a list of airports (three-letter codes like"JFK"), a list of routes (one-way flights from one airport to another like JFK, SFO), and a starting airport.
Write a program that returns the minimum number of airport connections (one-way flights ) that need to be added in order for someone to be able to reach any airport in the list, staring at the starting airport.
Note that routes only allow you to fly in one direction; for instance the route JFK,SFO only allows you to fly from "JFK" to "SFO".
Also note that the connections don't have to be direct; it's okay if any airport can only be reached from the starting airport by stopping at other airports first.
Input format:
the input consists of multiple test cases so the first line of the input is the number of test cases
the first each test case contains comma-sparated values the list of airports.
The second line of each test case contains a positive integer N which indicate the number of routes. And each N line contains comma-separated values which indicate the list of routes. and the last line of each test case contains the staring airport
Output format:
return the minimum number of airport connections that need to be added in order for someone to be able to reach any airport in the list , starting at the staring airport
sample output:

1
BGI,CDG,DEL,DOH,DSM,EWR,EYW,HND,ICN,JFK,LGA,LHR,ORD,SAN,SFO,SIN,TLV,BUD
19
DSM,ORD
ORD,BGI
BGI,LGA
SIN,CDG
CDG,SIN
CDG,BUD
DEL,DOH
DEL,CDG
TLV,DEL
EWR,HND
HND,ICN
HND,JFK
ICN,JFK
JFK,LGA
EYW,LHR
LHR,SFO
SFO,SAN
SFO,DSM
SAN,EYW
LGA

Output format:
3
