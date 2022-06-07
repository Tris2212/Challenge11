palindrome_0 = input('input palindrome: ')
palindrome_1 = palindrome_0[::-1]
if palindrome_0 == palindrome_1:
    print(palindrome_0 + ' is a valid palindrome.')
else:
    print(palindrome_0 + ' is not a valid palindrome.')