found = 0
numb = 1
foundhap = []

while found < 8:
    num = [int(b) for b in str(numb)]
    number = num
    cont = True
    it = 0
    try:
        while cont == True:
            ans = 0
            for i in range(0,len(num)):
                ans = ans + (int(num[i]) ** 2)
                print(ans)
            num = [int(a) for a in str(ans)]
            if ans == 1:
                cont = False
                print(f"{number} is happy")
                found = found + 1
                foundhap.append(numb)
            if it > 1000:
                cont = False
            it = it + 1
    except IndexError:
        print(f"{number} is happy")
        found = found + 1
        foundhap.append(numb)
    numb = numb + 1
print(foundhap)
