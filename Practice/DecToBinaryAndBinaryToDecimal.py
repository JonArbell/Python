num = int(input("Enter a number: "))
list1 = []
num2 = num
while num>0:
    list1.append(num%2)
    num //= 2

print(f"\nThe binary of {num2} is {list1[::-1]}") #Decimal to Binary

total = 0
exponent = 0
for i in list1:
    total += ((2**exponent) * i)
    exponent+=1

print(f"\nThe decimal of {list1[::-1]} is {total}") #Binary to Decimal

