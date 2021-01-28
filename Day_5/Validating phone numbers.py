# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
A = int(input())

for i in range(A):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
