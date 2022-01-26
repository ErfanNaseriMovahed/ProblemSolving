#!/bin/python3

first_multiple_input = input().rstrip().split()

p = int(first_multiple_input[0])

d = int(first_multiple_input[1])

m = int(first_multiple_input[2])

s = int(first_multiple_input[3])

prices = []
for i in range(p, m - 1, -d):
    prices.append(i)
if m not in prices:
    prices.append(m)
ans = 0
num = 0
i = 0
while ans <= s and i < len(prices):
    ans += prices[i]
    if ans <= s:
        num += 1
    i += 1
while ans <= s:
    ans += m
    if ans <= s:
        num += 1
print(num)