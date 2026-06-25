def number_palindrome(num:int):
    # Check if a number is a palindrome.
    a=0
    org=num
    while num>0:
        r=num%10
        a=(a*10)+r
        num=num//10

    if a==org:
        print(a, 'is a palindrome!!')
    else:
        print(org, 'is not a palindrome!!', a)

def print_a_pyramid_of_stars(n:int):

    for i in range(0, n+1):
        for j in range(0, n-i):
            print('', end=' ')
        for k in range(0, i):
            print('*', end=' ')
        print()
    # reverse pyramid
    for i in range(0, n + 1):
        for l in range(0, i):
            print('',end=' ')
        for m in range(0, n-i):
            print('*',end=' ')
        print()


def find_factorial_iterative(n:int):
    a=1
    for i in range(0, n):
        a=a*(n-i)
    print('factorial_iterative', a)

def find_factorial_recursive(n:int):
   return 1 if n==0 else n*find_factorial_recursive(n - 1)

def generate_fibonacci_series(n:int):
    a=0
    b=1
    print('fibonacci_series ==>',a, end=" ")
    while n-1>0:
        a,b=b, a+b
        print(a, end=" ")
        n=n-1

def a_string_palindrome(s: str):
    print()
    n = len(s)
    # rev = s[::-1]

    # rev = ''
    # for ch in s:
    #     rev=ch+rev
    # print(rev)
    flag = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            flag = False
            break

    # if rev==s :
    if flag:
        print(s, 'is a palindrome!!')
    else:
        print(s, 'is not a palindrome!!')

def count_vowels_and_consonants(s: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    print('Given String : ==> ', s)
    count = 0
    alphabets_counter = 0
    alphabets = ''
    for ch in range(ord('a'), ord('z') + 1):
        alphabets = chr(ch)+alphabets
    print(alphabets[::-1])
    for ch in s.lower():
        if ch in vowels:
            count=count+1
        if ch in alphabets:
            alphabets_counter =alphabets_counter+1

    print('vowels',count, 'consonants',(alphabets_counter-count))













# Check if a number is a palindrome.
number_palindrome(112115)
# Print a pyramid pattern of stars.
print_a_pyramid_of_stars(6)
# Find factorial of a number (iterative & recursive).
find_factorial_iterative(5)
f =find_factorial_recursive(5)
print('find_factorial_recursive ', f)
# Generate Fibonacci series up to n terms.
generate_fibonacci_series(10)
# Reverse a string without using slicing or string palindrome check.
a_string_palindrome('MALAYALAM')
a_string_palindrome('MALAYALAMA')

# Count vowels and consonants in a string.
count_vowels_and_consonants("Delhi is a capital City of Bharath!!")
#Check if a number is prime.
# a_number_is_prime(123)

