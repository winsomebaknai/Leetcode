'''
Number of steps (HackerEarth / Easy) (Basics of I/O)

You are given two arrays A and B. In each step, you can set A[i] = A[i] - B[i] if A[i] >= B[i]. Determine the minimum number of steps required to make all elements of A equal. If it is not possible, print -1.

nput Format
The first line contains an integer n, the size of the arrays.

The second line contains n space-separated integers, representing the elements of array A.

The third line contains n space-separated integers, representing the elements of array B.

Output Format
Print the minimum number of steps required to make all elements of A equal. If it is not possible, print -1.

Sample Input 1
5
5 7 10 5 15
2 2 1 3 5
Sample Output 1
8
'''

n = int(input()) 
a = list(map(int, input().split())) 
b = list(map(int, input().split()))  


if len(a) != n or len(b) != n:
    print(-1)  
    exit()  

step_count = 0
t = min(a)  

for i in range(n):
    diff = a[i] - t
    if diff % b[i] != 0:  
        print(-1)  
        exit()
    step_count += diff // b[i]  


print(step_count)

'''
Note: only partially accepted
'''