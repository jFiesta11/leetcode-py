def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

result = "TRUE" if isPalindrome(1211) else "FALSE" 
print(result)