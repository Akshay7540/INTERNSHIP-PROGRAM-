# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
A = re.search(r"([a-z0-9])\1+", input())
print(A.group(1) if A else -1)
