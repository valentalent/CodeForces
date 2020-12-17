"""
Next Round
time limit per test3 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.

Input
The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).

Output
Output the number of participants who advance to the next round.

Examples
input
8 5
10 9 8 7 7 7 5 5
output
6

input
4 2
0 0 0 0
output
0
"""

#Code goes here:

x=list(input().split(" "))
y=list(input().split(" "))
test_list = list(map(int, y))
index=int(x[1])-1
test_list = list(filter(lambda x: x>0 and x>=test_list[index], test_list))
print(len(test_list))