from os import path
import math, sys
from collections import defaultdict

# idhere
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("input.txt", mode = 'r')
    sys.stdout = open("output.txt", mode = 'w')
###############################################

if path.exists("input.txt"):
    fileio()

t = nint()
for _ in range(t):
    n = nint()
    a = aint()
