# Enter your code here. Read input from STDIN. Print output to STDOUT
f_in = list(map(int,input().split()))[:2]
n, m= f_in[0], f_in[1]
s_in = list(map(int,input().split()))[:n]
a = set(map(int,input().split()))
b = set(map(int,input().split()))
a_c, b_c = 0,0
a_c = len([a_c+1 for x in s_in if x in a])
b_c = len([b_c+1 for x in s_in if x in b])
print(a_c-b_c)
