num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(len(num))
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.append(5)
print(num)
num.remove(5)
#remove só o primeiro
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
