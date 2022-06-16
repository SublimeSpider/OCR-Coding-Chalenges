#Factorial finder
num = int(input("Enter the number youy want the factorial of : "))
n = num - 1
ans = num

while n >= 1:
    ans = ans * n
    n = n - 1

if num == 0:
    ans = 1

print(ans)
