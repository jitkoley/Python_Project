num = 323
copy = num
rev = 0
while num != 0:
    rem = num % 10
    rev = rev*10+rem
    num = num // 10
print(rev)
if rev == copy:
    print("the number is palindrome")
else:
    print("the number is not palindrome") 