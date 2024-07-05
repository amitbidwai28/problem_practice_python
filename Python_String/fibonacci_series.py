# Fibonacci Series in Python Using For Loop
# initialize two variables, with value 0
import os

a, b = 0, 1
series_length = 18

print(a, b, end=' ')
for i in range(series_length):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
