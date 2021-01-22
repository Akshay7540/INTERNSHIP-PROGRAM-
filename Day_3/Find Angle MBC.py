# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
HEIGHT = math.sqrt(AB**2+BC**2)
HEIGHT = HEIGHT/2.0
ADJ = BC/2.0

Output = int(round(math.degrees(math.acos(ADJ/HEIGHT))))

Output = str(Output)

print(Output+"°")