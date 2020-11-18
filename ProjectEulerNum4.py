#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

products = []
palindromes = []
three_digit_nums = range(100,1000)

for k in three_digit_nums:
    for j in three_digit_nums:
        products.append(k*j)

def check_palindrome(stringcheck): #only works for 6 digit numbers which is all we need for this exercise
    if str(stringcheck)[0] == str(stringcheck)[-1] and str(stringcheck)[1] == str(stringcheck)[-2] and str(stringcheck)[2] == str(stringcheck)[-3]:
        palindromes.append(stringcheck)

for num in products:
    check_palindrome(num)

print(max(palindromes))