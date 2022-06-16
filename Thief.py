digits = []

for i in range(0,4):
    digits.append(int(input("Enter 1 digit of the code : ")))

a = digits[0]
b = digits[1]
c = digits[2]
d = digits[3]

print([a,b,c,d])
print([a,b,d,c])
print([a,c,b,d])
print([a,c,d,b])
print([a,d,b,c])
print([a,d,c,b])

print([b,a,c,d])
print([b,a,d,c])
print([b,c,a,d])
print([b,c,d,a])
print([b,d,a,c])
print([b,d,c,a])

print([c,a,b,d])
print([c,a,d,b])
print([c,b,a,d])
print([c,b,d,a])
print([c,d,a,b])
print([c,d,b,a])

print([d,a,b,c])
print([d,a,c,b])
print([d,b,a,c])
print([d,b,c,a])
print([d,c,a,b])
print([d,c,b,a])
